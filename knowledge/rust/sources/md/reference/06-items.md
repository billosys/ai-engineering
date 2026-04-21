r[items]
# Items

r[items.syntax]
```grammar,items
Item ->
    OuterAttribute* ( VisItem | MacroItem )

VisItem ->
    Visibility?
    (
        Module
      | ExternCrate
      | UseDeclaration
      | Function
      | TypeAlias
      | Struct
      | Enumeration
      | Union
      | ConstantItem
      | StaticItem
      | Trait
      | Implementation
      | ExternBlock
    )

MacroItem ->
      MacroInvocationSemi
    | MacroRulesDefinition
```

r[items.intro]
An _item_ is a component of a crate. Items are organized within a crate by a nested set of [modules]. Every crate has a single "outermost" anonymous module; all further items within the crate have [paths] within the module tree of the crate.

r[items.static-def]
Items are entirely determined at compile-time, generally remain fixed during execution, and may reside in read-only memory.

r[items.kinds]
There are several kinds of items:

* [modules]
* [`extern crate` declarations]
* [`use` declarations]
* [function definitions]
* [type alias definitions]
* [struct definitions]
* [enumeration definitions]
* [union definitions]
* [constant items]
* [static items]
* [trait definitions]
* [implementations]
* [`extern` blocks]

r[items.locations]
Items may be declared in the [root of the crate], a [module][modules], or a [block expression].

r[items.associated-locations]
A subset of items, called [associated items], may be declared in [traits] and [implementations].

r[items.extern-locations]
A subset of items, called external items, may be declared in [`extern` blocks].

r[items.decl-order]
Items may be defined in any order, with the exception of [`macro_rules`] which has its own scoping behavior.

r[items.name-resolution]
[Name resolution] of item names allows items to be defined before or after where the item is referred to in the module or block.

See [item scopes] for information on the scoping rules of items.

[`extern crate` declarations]: items/extern-crates.md
[`extern` blocks]: items/external-blocks.md
[`macro_rules`]: macros-by-example.md
[`use` declarations]: items/use-declarations.md
[associated items]: items/associated-items.md
[block expression]: expressions/block-expr.md
[constant items]: items/constant-items.md
[enumeration definitions]: items/enumerations.md
[function definitions]: items/functions.md
[implementations]: items/implementations.md
[item scopes]: names/scopes.md#item-scopes
[modules]: items/modules.md
[name resolution]: names/name-resolution.md
[paths]: paths.md
[root of the crate]: crates-and-source-files.md
[statement]: statements.md
[static items]: items/static-items.md
[struct definitions]: items/structs.md
[trait definitions]: items/traits.md
[traits]: items/traits.md
[type alias definitions]: items/type-aliases.md
[union definitions]: items/unions.md


---

r[items.mod]
# Modules

r[items.mod.syntax]
```grammar,items
Module ->
      `unsafe`? `mod` IDENTIFIER `;`
    | `unsafe`? `mod` IDENTIFIER `{`
        InnerAttribute*
        Item*
      `}`
```

r[items.mod.intro]
A module is a container for zero or more [items].

r[items.mod.def]
A _module item_ is a module, surrounded in braces, named, and prefixed with the keyword `mod`. A module item introduces a new, named module into the tree of modules making up a crate.

r[items.mod.nesting]
Modules can nest arbitrarily.

An example of a module:

```rust
mod math {
    type Complex = (f64, f64);
    fn sin(f: f64) -> f64 {
        /* ... */
#       unimplemented!();
    }
    fn cos(f: f64) -> f64 {
        /* ... */
#       unimplemented!();
    }
    fn tan(f: f64) -> f64 {
        /* ... */
#       unimplemented!();
    }
}
```

r[items.mod.namespace]
Modules are defined in the [type namespace] of the module or block where they are located.

r[items.mod.multiple-items]
It is an error to define multiple items with the same name in the same namespace within a module. See the [scopes chapter] for more details on restrictions and shadowing behavior.

r[items.mod.unsafe]
The `unsafe` keyword is syntactically allowed to appear before the `mod` keyword, but it is rejected at a semantic level. This allows macros to consume the syntax and make use of the `unsafe` keyword, before removing it from the token stream.

r[items.mod.outlined]
## Module source filenames

r[items.mod.outlined.intro]
A module without a body is loaded from an external file. When the module does not have a `path` attribute, the path to the file mirrors the logical [module path].

r[items.mod.outlined.search]
Ancestor module path components are directories, and the module's contents are in a file with the name of the module plus the `.rs` extension. For example, the following module structure can have this corresponding filesystem structure:

Module Path               | Filesystem Path  | File Contents
------------------------- | ---------------  | -------------
`crate`                   | `lib.rs`         | `mod util;`
`crate::util`             | `util.rs`        | `mod config;`
`crate::util::config`     | `util/config.rs` |

r[items.mod.outlined.search-mod]
Module filenames may also be the name of the module as a directory with the contents in a file named `mod.rs` within that directory. The above example can alternately be expressed with `crate::util`'s contents in a file named `util/mod.rs`. It is not allowed to have both `util.rs` and `util/mod.rs`.

> [!NOTE]
> Prior to `rustc` 1.30, using `mod.rs` files was the way to load a module with nested children. It is encouraged to use the new naming convention as it is more consistent, and avoids having many files named `mod.rs` within a project.

r[items.mod.outlined.path]
### The `path` attribute

r[items.mod.outlined.path.intro]
The directories and files used for loading external file modules can be influenced with the `path` attribute.

r[items.mod.outlined.path.search]
For `path` attributes on modules not inside inline module blocks, the file path is relative to the directory the source file is located. For example, the following code snippet would use the paths shown based on where it is located:

<!-- ignore: requires external files -->
```rust,ignore
#[path = "foo.rs"]
mod c;
```

Source File    | `c`'s File Location | `c`'s Module Path
-------------- | ------------------- | ----------------------
`src/a/b.rs`   | `src/a/foo.rs`      | `crate::a::b::c`
`src/a/mod.rs` | `src/a/foo.rs`      | `crate::a::c`

r[items.mod.outlined.path.search-nested]
For `path` attributes inside inline module blocks, the relative location of the file path depends on the kind of source file the `path` attribute is located in. "mod-rs" source files are root modules (such as `lib.rs` or `main.rs`) and modules with files named `mod.rs`. "non-mod-rs" source files are all other module files. Paths for `path` attributes inside inline module blocks in a mod-rs file are relative to the directory of the mod-rs file including the inline module components as directories. For non-mod-rs files, it is the same except the path starts with a directory with the name of the non-mod-rs module. For example, the following code snippet would use the paths shown based on where it is located:

<!-- ignore: requires external files -->
```rust,ignore
mod inline {
    #[path = "other.rs"]
    mod inner;
}
```

Source File    | `inner`'s File Location   | `inner`'s Module Path
-------------- | --------------------------| ----------------------------
`src/a/b.rs`   | `src/a/b/inline/other.rs` | `crate::a::b::inline::inner`
`src/a/mod.rs` | `src/a/inline/other.rs`   | `crate::a::inline::inner`

An example of combining the above rules of `path` attributes on inline modules and nested modules within (applies to both mod-rs and non-mod-rs files):

<!-- ignore: requires external files -->
```rust,ignore
#[path = "thread_files"]
mod thread {
    // Load the `local_data` module from `thread_files/tls.rs` relative to
    // this source file's directory.
    #[path = "tls.rs"]
    mod local_data;
}
```

r[items.mod.attributes]
## Attributes on modules

r[items.mod.attributes.intro]
Modules, like all items, accept outer attributes. They also accept inner attributes: either after `{` for a module with a body, or at the beginning of the source file, after the optional BOM and shebang.

r[items.mod.attributes.supported]
The built-in attributes that have meaning on a module are [`cfg`], [`deprecated`], [`doc`], [the lint check attributes], [`path`], and [`no_implicit_prelude`]. Modules also accept macro attributes.

[`cfg`]: ../conditional-compilation.md
[`deprecated`]: ../attributes/diagnostics.md#the-deprecated-attribute
[`doc`]: ../../rustdoc/the-doc-attribute.html
[`no_implicit_prelude`]: ../names/preludes.md#the-no_implicit_prelude-attribute
[`path`]: #the-path-attribute
[attribute]: ../attributes.md
[items]: ../items.md
[module path]: ../paths.md
[scopes chapter]: ../names/scopes.md
[the lint check attributes]: ../attributes/diagnostics.md#lint-check-attributes
[type namespace]: ../names/namespaces.md


---

r[items.extern-crate]
# Extern crate declarations

r[items.extern-crate.syntax]
```grammar,items
ExternCrate -> `extern` `crate` CrateRef AsClause? `;`

CrateRef -> IDENTIFIER | `self`

AsClause -> `as` ( IDENTIFIER | `_` )
```

r[items.extern-crate.intro]
An _`extern crate` declaration_ specifies a dependency on an external crate.

r[items.extern-crate.namespace]
The external crate is then bound into the declaring scope as the given [identifier] in the [type namespace].

r[items.extern-crate.extern-prelude]
Additionally, if the `extern crate` appears in the crate root, then the crate name is also added to the [extern prelude], making it automatically in scope in all modules.

r[items.extern-crate.as]
The `as` clause can be used to bind the imported crate to a different name.

r[items.extern-crate.lookup]
The external crate is resolved to a specific `soname` at compile time, and a runtime linkage requirement to that `soname` is passed to the linker for loading at runtime. The `soname` is resolved at compile time by scanning the compiler's library path and matching the optional `crate_name` provided against the [`crate_name` attributes] that were declared on the external crate when it was compiled. If no `crate_name` is provided, a default `name` attribute is assumed, equal to the [identifier] given in the `extern crate` declaration.

r[items.extern-crate.self]
The `self` crate may be imported which creates a binding to the current crate. In this case the `as` clause must be used to specify the name to bind it to.

Three examples of `extern crate` declarations:

<!-- ignore: requires external crates -->
```rust,ignore
extern crate pcre;

extern crate std; // equivalent to: extern crate std as std;

extern crate std as ruststd; // linking to 'std' under another name
```

r[items.extern-crate.name-restrictions]
When naming Rust crates, hyphens are disallowed. However, Cargo packages may make use of them. In such case, when `Cargo.toml` doesn't specify a crate name, Cargo will transparently replace `-` with `_` (Refer to [RFC 940] for more details).

Here is an example:

<!-- ignore: requires external crates -->
```rust,ignore
// Importing the Cargo package hello-world
extern crate hello_world; // hyphen replaced with an underscore
```

r[items.extern-crate.underscore]
## Underscore imports

r[items.extern-crate.underscore.intro]
An external crate dependency can be declared without binding its name in scope by using an underscore with the form `extern crate foo as _`. This may be useful for crates that only need to be linked, but are never referenced, and will avoid being reported as unused.

r[items.extern-crate.underscore.macro_use]
The [`macro_use` attribute] works as usual and imports the macro names into the [`macro_use` prelude].

<!-- template:attributes -->
r[items.extern-crate.no_link]
## The `no_link` attribute

r[items.extern-crate.no_link.intro]
The *`no_link` [attribute][attributes]* may be applied to an `extern crate` item to prevent linking the crate.

> [!NOTE]
> This is helpful, e.g., when only the macros of a crate are needed.

> [!EXAMPLE]
> <!-- ignore: requires external crates -->
> ```rust,ignore
> #[no_link]
> extern crate other_crate;
>
> other_crate::some_macro!();
> ```

r[items.extern-crate.no_link.syntax]
The `no_link` attribute uses the [MetaWord] syntax.

r[items.extern-crate.no_link.allowed-positions]
The `no_link` attribute may only be applied to an `extern crate` declaration.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[items.extern-crate.no_link.duplicates]
Only the first use of `no_link` on an `extern crate` declaration has effect.

> [!NOTE]
> `rustc` lints against any use following the first. This may become an error in the future.

[identifier]: ../identifiers.md
[RFC 940]: https://github.com/rust-lang/rfcs/blob/master/text/0940-hyphens-considered-harmful.md
[`macro_use` attribute]: ../macros-by-example.md#the-macro_use-attribute
[extern prelude]: ../names/preludes.md#extern-prelude
[`macro_use` prelude]: ../names/preludes.md#macro_use-prelude
[`crate_name` attributes]: ../crates-and-source-files.md#the-crate_name-attribute
[type namespace]: ../names/namespaces.md


---

r[items.use]
# Use declarations

r[items.use.syntax]
```grammar,items
UseDeclaration -> `use` UseTree `;`

UseTree ->
      (SimplePath? `::`)? `*`
    | (SimplePath? `::`)? `{` (UseTree ( `,`  UseTree )* `,`?)? `}`
    | SimplePath ( `as` ( IDENTIFIER | `_` ) )?
```

r[items.use.intro]
A _use declaration_ creates one or more local name bindings synonymous with some other [path]. Usually a `use` declaration is used to shorten the path required to refer to a module item. These declarations may appear in [modules] and [blocks], usually at the top. A `use` declaration is also sometimes called an _import_, or, if it is public, a _re-export_.

[path]: ../paths.md
[modules]: modules.md
[blocks]: ../expressions/block-expr.md

r[items.use.forms]
Use declarations support a number of convenient shortcuts:

r[items.use.forms.multiple]
* Simultaneously binding a list of paths with a common prefix, using the brace syntax `use a::b::{c, d, e::f, g::h::i};`

r[items.use.forms.self]
* Simultaneously binding a list of paths with a common prefix and their common parent module, using the `self` keyword, such as `use a::b::{self, c, d::e};`

r[items.use.forms.as]
* Rebinding the target name as a new local name, using the syntax `use p::q::r as x;`. This can also be used with the last two features: `use a::b::{self as ab, c as abc}`.

r[items.use.forms.glob]
* Binding all paths matching a given prefix, using the asterisk wildcard syntax `use a::b::*;`.

r[items.use.forms.nesting]
* Nesting groups of the previous features multiple times, such as `use a::b::{self as ab, c, d::{*, e::f}};`

An example of `use` declarations:

```rust
use std::collections::hash_map::{self, HashMap};

fn foo<T>(_: T){}
fn bar(map1: HashMap<String, usize>, map2: hash_map::HashMap<String, usize>){}

fn main() {
    // use declarations can also exist inside of functions
    use std::option::Option::{Some, None};

    // Equivalent to 'foo(vec![std::option::Option::Some(1.0f64),
    // std::option::Option::None]);'
    foo(vec![Some(1.0f64), None]);

    // Both `hash_map` and `HashMap` are in scope.
    let map1 = HashMap::new();
    let map2 = hash_map::HashMap::new();
    bar(map1, map2);
}
```

r[items.use.visibility]
## `use` Visibility

r[items.use.visibility.intro]
Like items, `use` declarations are private to the containing module, by default. Also like items, a `use` declaration can be public, if qualified by the `pub` keyword. Such a `use` declaration serves to _re-export_ a name. A public `use` declaration can therefore _redirect_ some public name to a different target definition: even a definition with a private canonical path, inside a different module.

r[items.use.visibility.unambiguous]
If a sequence of such redirections form a cycle or cannot be resolved unambiguously, they represent a compile-time error.

An example of re-exporting:

```rust
mod quux {
    pub use self::foo::{bar, baz};
    pub mod foo {
        pub fn bar() {}
        pub fn baz() {}
    }
}

fn main() {
    quux::bar();
    quux::baz();
}
```

In this example, the module `quux` re-exports two public names defined in `foo`.

r[items.use.path]
## `use` Paths

r[items.use.path.intro]
The [paths] that are allowed in a `use` item follow the [SimplePath] grammar and are similar to the paths that may be used in an expression. They may create bindings for:

* Nameable [items]
* [Enum variants]
* [Built-in types]
* [Attributes]
* [Derive macros]
* [`macro_rules`]

r[items.use.path.disallowed]
They cannot import [associated items], [generic parameters], [local variables], paths with [`Self`], or [tool attributes]. More restrictions are described below.

r[items.use.path.namespace]
`use` will create bindings for all [namespaces] from the imported entities, with the exception that a `self` import will only import from the type namespace (as described below). For example, the following illustrates creating bindings for the same name in two namespaces:

```rust
mod stuff {
    pub struct Foo(pub i32);
}

// Imports the `Foo` type and the `Foo` constructor.
use stuff::Foo;

fn example() {
    let ctor = Foo; // Uses `Foo` from the value namespace.
    let x: Foo = ctor(123); // Uses `Foo` From the type namespace.
}
```

r[items.use.path.edition2018]
> [!EDITION-2018]
> In the 2015 edition, `use` paths are relative to the crate root. For example:
>
> ```rust,edition2015
> mod foo {
>     pub mod example { pub mod iter {} }
>     pub mod baz { pub fn foobaz() {} }
> }
> mod bar {
>     // Resolves `foo` from the crate root.
>     use foo::example::iter;
>     // The `::` prefix explicitly resolves `foo`
>     // from the crate root.
>     use ::foo::baz::foobaz;
> }
>
> # fn main() {}
> ```
>
> The 2015 edition does not allow use declarations to reference the [extern prelude]. Thus, [`extern crate`] declarations are still required in 2015 to reference an external crate in a `use` declaration. Beginning with the 2018 edition, `use` declarations can specify an external crate dependency the same way `extern crate` can.

r[items.use.as]
## `as` renames

The `as` keyword can be used to change the name of an imported entity. For example:

```rust
// Creates a non-public alias `bar` for the function `foo`.
use inner::foo as bar;

mod inner {
    pub fn foo() {}
}
```

r[items.use.multiple-syntax]
## Brace syntax

r[items.use.multiple-syntax.intro]
Braces can be used in the last segment of the path to import multiple entities from the previous segment, or, if there are no previous segments, from the current scope. Braces can be nested, creating a tree of paths, where each grouping of segments is logically combined with its parent to create a full path.

```rust
// Creates bindings to:
// - `std::collections::BTreeSet`
// - `std::collections::hash_map`
// - `std::collections::hash_map::HashMap`
use std::collections::{BTreeSet, hash_map::{self, HashMap}};
```

r[items.use.multiple-syntax.empty]
An empty brace does not import anything, though the leading path is validated that it is accessible.
<!-- This is slightly wrong, see: https://github.com/rust-lang/rust/issues/61826 -->

r[items.use.multiple-syntax.edition2018]
> [!EDITION-2018]
> In the 2015 edition, paths are relative to the crate root, so an import such as `use {foo, bar};` will import the names `foo` and `bar` from the crate root, whereas starting in 2018, those names are relative to the current scope.

r[items.use.self]
## `self` imports

r[items.use.self.intro]
The keyword `self` may be used within [brace syntax] to create a binding of the parent entity under its own name.

```rust
mod stuff {
    pub fn foo() {}
    pub fn bar() {}
}
mod example {
    // Creates a binding for `stuff` and `foo`.
    use crate::stuff::{self, foo};
    pub fn baz() {
        foo();
        stuff::bar();
    }
}
# fn main() {}
```

> [!NOTE]
> `self` may also be used as the first segment of a path. The use of `self` as the first segment and inside a `use` brace is logically the same; it means the current module of the parent segment, or the current module if there is no parent segment. See [`self`] in the paths chapter for more information on the meaning of a leading `self`.

r[items.use.self.module]
When `self` is used within [brace syntax], the path preceding the brace group must resolve to a [module], [enumeration], or [trait].

```rust
mod m {
    pub enum E { V1, V2 }
    pub trait Tr { fn f(&self); }
}
use m::{self as _}; // OK: Modules can be parents of `self`.
use m::E::{self, V1}; // OK: Enums can be parents of `self`.
use m::Tr::{self}; // OK: Traits can be parents of `self`.
# fn main() {}
```

```rust,compile_fail,E0432
struct S {}
use S::{self as _}; // ERROR: Structs cannot be parents of `self`.
# fn main() {}
```

r[items.use.self.namespace]
`self` only creates a binding from the [type namespace] of the parent entity. For example, in the following, only the `foo` mod is imported:

```rust,compile_fail
mod bar {
    pub mod foo {}
    pub fn foo() {}
}

// This only imports the module `foo`. The function `foo` lives in
// the value namespace and is not imported.
use bar::foo::{self};

fn main() {
    foo(); //~ ERROR `foo` is a module
}
```

r[items.use.glob]
## Glob imports

r[items.use.glob.intro]
The `*` character may be used as the last segment of a `use` path to import all importable entities from the entity of the preceding segment. For example:

```rust
// Creates a non-public alias to `bar`.
use foo::*;

mod foo {
    fn i_am_private() {}
    enum Example {
        V1,
        V2,
    }
    pub fn bar() {
        // Creates local aliases to `V1` and `V2`
        // of the `Example` enum.
        use Example::*;
        let x = V1;
    }
}
```

r[items.use.glob.shadowing]
Items and named imports are allowed to shadow names from glob imports in the same [namespace]. That is, if there is a name already defined by another item in the same namespace, the glob import will be shadowed. For example:

```rust
// This creates a binding to the `clashing::Foo` tuple struct
// constructor, but does not import its type because that would
// conflict with the `Foo` struct defined here.
//
// Note that the order of definition here is unimportant.
use clashing::*;
struct Foo {
    field: f32,
}

fn do_stuff() {
    // Uses the constructor from `clashing::Foo`.
    let f1 = Foo(123);
    // The struct expression uses the type from
    // the `Foo` struct defined above.
    let f2 = Foo { field: 1.0 };
    // `Bar` is also in scope due to the glob import.
    let z = Bar {};
}

mod clashing {
    pub struct Foo(pub i32);
    pub struct Bar {}
}
```

> [!NOTE]
> For areas where shadowing is not allowed, see [name resolution ambiguities].

r[items.use.glob.last-segment-only]
`*` cannot be used as the first or intermediate segments.

r[items.use.glob.self-import]
`*` cannot be used to import a module's contents into itself (such as `use self::*;`).

r[items.use.glob.edition2018]
> [!EDITION-2018]
> In the 2015 edition, paths are relative to the crate root, so an import such as `use *;` is valid, and it means to import everything from the crate root. This cannot be used in the crate root itself.

r[items.use.as-underscore]
## Underscore imports

r[items.use.as-underscore.intro]
Items can be imported without binding to a name by using an underscore with the form `use path as _`. This is particularly useful to import a trait so that its methods may be used without importing the trait's symbol, for example if the trait's symbol may conflict with another symbol. Another example is to link an external crate without importing its name.

r[items.use.as-underscore.glob]
Asterisk glob imports will import items imported with `_` in their unnameable form.

```rust
mod foo {
    pub trait Zoo {
        fn zoo(&self) {}
    }

    impl<T> Zoo for T {}
}

use self::foo::Zoo as _;
struct Zoo;  // Underscore import avoids name conflict with this item.

fn main() {
    let z = Zoo;
    z.zoo();
}
```

r[items.use.as-underscore.macro]
The unique, unnameable symbols are created after macro expansion so that macros may safely emit multiple references to `_` imports. For example, the following should not produce an error:

```rust
macro_rules! m {
    ($item: item) => { $item $item }
}

m!(use std as _;);
// This expands to:
// use std as _;
// use std as _;
```

r[items.use.restrictions]
## Restrictions

The following rules are restrictions for valid `use` declarations.

r[items.use.restrictions.crate-alias]
When using `crate` to import the current crate, you must use `as` to define the binding name.

> [!EXAMPLE]
> ```rust
> use crate as root;
> use crate::{self as root2};
>
> // Not allowed:
> // use crate;
> // use crate::{self};
> ```

r[items.use.restrictions.macro-crate-alias]
When using [`$crate`] in a macro transcriber to import the current crate, you must use `as` to define the binding name.

> [!EXAMPLE]
> ```rust
> macro_rules! import_crate_root {
>     () => {
>         use $crate as my_crate;
>         use $crate::{self as my_crate2};
>     };
> }
> ```

r[items.use.restrictions.self-alias]
When using `self` to import the current module, you must use `as` to define the binding name.

> [!EXAMPLE]
> ```rust
> use {self as this_module};
> use self as this_module2;
> use self::{self as this_module3};
>
> // Not allowed:
> // use {self};
> // use self;
> // use self::{self};
> ```

r[items.use.restrictions.super-alias]
When using `super` to import a parent module, you must use `as` to define the binding name.

> [!EXAMPLE]
> ```rust
> mod a {
>     mod b {
>         use super as parent;
>         use super::{self as parent2};
>         use self::super as parent3;
>         use super::super as grandparent;
>         use super::super::{self as grandparent2};
>
>         // Not allowed:
>         // use super;
>         // use super::{self};
>         // use self::super;
>         // use super::super;
>         // use super::super::{self};
>     }
> }
> ```

r[items.use.restrictions.extern-prelude]
`::` as the [extern prelude] cannot be imported.

> [!EXAMPLE]
> ```rust,edition2018,compile_fail
> use ::{self as root}; //~ Error
> ```

> [!EDITION-2018]
> In the 2015 edition, the prefix `::` refers to the crate root, so `use ::{self as root};` is allowed because it is same as `use crate::{self as root};`. Starting with the 2018 edition the `::` prefix refers to the extern prelude, which cannot be directly imported.
>
> ```rust,edition2015
> use ::{self as root}; //~ Ok
> ```

r[items.use.restrictions.duplicate-name]
As with any item definition, `use` imports cannot create duplicate bindings of the same name in the same namespace in a module or block.

r[items.use.restrictions.variant]
`use` paths cannot refer to enum variants through a [type alias].

> [!EXAMPLE]
> ```rust,compile_fail
> enum MyEnum {
>   MyVariant
> }
> type TypeAlias = MyEnum;
>
> use MyEnum::MyVariant; //~ OK
> use TypeAlias::MyVariant; //~ ERROR
> ```

[`$crate`]: paths.qualifiers.macro-crate
[Attributes]: ../attributes.md
[brace syntax]: items.use.multiple-syntax
[Built-in types]: ../types.md
[Derive macros]: macro.proc.derive
[Enum variants]: enumerations.md
[enumeration]: items.enum
[`extern crate`]: extern-crates.md
[`macro_rules`]: ../macros-by-example.md
[`self`]: ../paths.md#self
[associated items]: associated-items.md
[extern prelude]: ../names/preludes.md#extern-prelude
[generic parameters]: generics.md
[items]: ../items.md
[local variables]: ../variables.md
[module]: items.mod
[name resolution ambiguities]: names.resolution.expansion.imports.ambiguity
[namespace]: ../names/namespaces.md
[namespaces]: ../names/namespaces.md
[paths]: ../paths.md
[tool attributes]: ../attributes.md#tool-attributes
[trait]: items.traits
[type alias]: type-aliases.md
[type namespace]: ../names/namespaces.md


---

r[items.fn]
# Functions

r[items.fn.syntax]
```grammar,items
Function ->
    FunctionQualifiers `fn` IDENTIFIER GenericParams?
        `(` FunctionParameters? `)`
        FunctionReturnType? WhereClause?
        ( BlockExpression | `;` )

FunctionQualifiers -> `const`? `async`?[^async-edition] ItemSafety?[^extern-qualifiers] (`extern` Abi?)?

ItemSafety -> `safe`[^extern-safe] | `unsafe`

Abi -> STRING_LITERAL | RAW_STRING_LITERAL

FunctionParameters ->
      SelfParam `,`?
    | (SelfParam `,`)? FunctionParam (`,` FunctionParam)* `,`?

SelfParam -> OuterAttribute* ( ShorthandSelf | TypedSelf )

ShorthandSelf -> (`&` | `&` Lifetime)? `mut`? `self`

TypedSelf -> `mut`? `self` `:` Type

FunctionParam -> OuterAttribute* ( FunctionParamPattern | `...` | Type[^fn-param-2015] )

FunctionParamPattern -> PatternNoTopAlt `:` ( Type | `...` )

FunctionReturnType -> `->` Type
```

[^async-edition]: The `async` qualifier is not allowed in the 2015 edition.

[^extern-safe]: The `safe` function qualifier is only allowed semantically within `extern` blocks.

[^extern-qualifiers]: *Relevant to editions earlier than Rust 2024*: Within `extern` blocks, the `safe` or `unsafe` function qualifier is only allowed when the `extern` is qualified as `unsafe`.

[^fn-param-2015]: Function parameters with only a type are only allowed in an associated function of a [trait item] in the 2015 edition.

r[items.fn.intro]
A _function_ consists of a [block] (that's the _body_ of the function), along with a name, a set of parameters, and an output type. Other than a name, all these are optional.

r[items.fn.namespace]
Functions are declared with the keyword `fn` which defines the given name in the [value namespace] of the module or block where it is located.

r[items.fn.signature]
Functions may declare a set of *input* [*variables*][variables] as parameters, through which the caller passes arguments into the function, and the *output* [*type*][type] of the value the function will return to its caller on completion.

r[items.fn.implicit-return]
If the output type is not explicitly stated, it is the [unit type].

r[items.fn.fn-item-type]
When referred to, a _function_ yields a first-class *value* of the corresponding zero-sized [*function item type*], which when called evaluates to a direct call to the function.

For example, this is a simple function:

```rust
fn answer_to_life_the_universe_and_everything() -> i32 {
    return 42;
}
```

r[items.fn.safety-qualifiers]
The `safe` function is semantically only allowed when used in an [`extern` block].

r[items.fn.params]
## Function parameters

r[items.fn.params.intro]
Function parameters are irrefutable [patterns], so any pattern that is valid in an else-less `let` binding is also valid as a parameter:

```rust
fn first((value, _): (i32, i32)) -> i32 { value }
```

r[items.fn.params.self-pat]
If the first parameter is a [SelfParam], this indicates that the function is a [method].

r[items.fn.params.self-restriction]
Functions with a self parameter may only appear as an [associated function] in a [trait] or [implementation].

r[items.fn.params.varargs]
A parameter with the `...` token indicates a [variadic function], and may only be used as the last parameter of an [external block] function. The variadic parameter may have an optional identifier, such as `args: ...`.

r[items.fn.body]
## Function body

r[items.fn.body.intro]
The body block of a function is conceptually wrapped in another block that first binds the argument patterns and then `return`s the value of the function's body. This means that the tail expression of the block, if evaluated, ends up being returned to the caller. As usual, an explicit return expression within the body of the function will short-cut that implicit return, if reached.

For example, the function above behaves as if it was written as:

<!-- ignore: example expansion -->
```rust,ignore
// argument_0 is the actual first argument passed from the caller
let (value, _) = argument_0;
return {
    value
};
```

r[items.fn.body.bodyless]
Functions without a body block are terminated with a semicolon. This form may only appear in a [trait] or [external block].

r[items.fn.generics]
## Generic functions

r[items.fn.generics.intro]
A _generic function_ allows one or more _parameterized types_ to appear in its signature. Each type parameter must be explicitly declared in an angle-bracket-enclosed and comma-separated list, following the function name.

```rust
// foo is generic over A and B

fn foo<A, B>(x: A, y: B) {
# }
```

r[items.fn.generics.param-names]
Inside the function signature and body, the name of the type parameter can be used as a type name.

r[items.fn.generics.param-bounds]
[Trait] bounds can be specified for type parameters to allow methods from that trait to be called on values of that type. This is specified using the `where` syntax:

```rust
# use std::fmt::Debug;
fn foo<T>(x: T) where T: Debug {
# }
```

r[items.fn.generics.mono]
When a generic function is referenced, its type is instantiated based on the context of the reference. For example, calling the `foo` function here:

```rust
use std::fmt::Debug;

fn foo<T>(x: &[T]) where T: Debug {
    // details elided
}

foo(&[1, 2]);
```

will instantiate type parameter `T` with `i32`.

r[items.fn.generics.explicit-arguments]
The type parameters can also be explicitly supplied in a trailing [path] component after the function name. This might be necessary if there is not sufficient context to determine the type parameters. For example, `mem::size_of::<u32>() == 4`.

r[items.fn.extern]
## Extern function qualifier

r[items.fn.extern.intro]
The `extern` function qualifier allows providing function _definitions_ that can be called with a particular ABI:

<!-- ignore: fake ABI -->
```rust,ignore
extern "ABI" fn foo() { /* ... */ }
```

r[items.fn.extern.def]
These are often used in combination with [external block] items which provide function _declarations_ that can be used to call functions without providing their _definition_:

<!-- ignore: fake ABI -->
```rust,ignore
unsafe extern "ABI" {
  unsafe fn foo(); /* no body */
  safe fn bar(); /* no body */
}
unsafe { foo() };
bar();
```

r[items.fn.extern.default-abi]
When `"extern" Abi?*` is omitted from `FunctionQualifiers` in function items, the ABI `"Rust"` is assigned. For example:

```rust
fn foo() {}
```

is equivalent to:

```rust
extern "Rust" fn foo() {}
```

r[items.fn.extern.foreign-call]
Functions can be called by foreign code, and using an ABI that differs from Rust allows, for example, to provide functions that can be called from other programming languages like C:

```rust
// Declares a function with the "C" ABI
extern "C" fn new_i32() -> i32 { 0 }

// Declares a function with the "stdcall" ABI
# #[cfg(any(windows, target_arch = "x86"))]
extern "stdcall" fn new_i32_stdcall() -> i32 { 0 }
```

r[items.fn.extern.default-extern]
Just as with [external block], when the `extern` keyword is used and the `"ABI"` is omitted, the ABI used defaults to `"C"`. That is, this:

```rust
extern fn new_i32() -> i32 { 0 }
let fptr: extern fn() -> i32 = new_i32;
```

is equivalent to:

```rust
extern "C" fn new_i32() -> i32 { 0 }
let fptr: extern "C" fn() -> i32 = new_i32;
```

r[items.fn.extern.unwind]
### Unwinding

r[items.fn.extern.unwind.intro]
Most ABI strings come in two variants, one with an `-unwind` suffix and one without. The `Rust` ABI always permits unwinding, so there is no `Rust-unwind` ABI. The choice of ABI, together with the runtime [panic handler], determines the behavior when unwinding out of a function.

r[items.fn.extern.unwind.behavior]
The table below indicates the behavior of an unwinding operation reaching each type of ABI boundary (function declaration or definition using the corresponding ABI string). Note that the Rust runtime is not affected by, and cannot have an effect on, any unwinding that occurs entirely within another language's runtime, that is, unwinds that are thrown and caught without reaching a Rust ABI boundary.

The `panic`-unwind column refers to [panicking] via the `panic!` macro and similar standard library mechanisms, as well as to any other Rust operations that cause a panic, such as out-of-bounds array indexing or integer overflow.

The "unwinding" ABI category refers to `"Rust"` (the implicit ABI of Rust functions not marked `extern`), `"C-unwind"`, and any other ABI with `-unwind` in its name. The "non-unwinding" ABI category refers to all other ABI strings, including `"C"` and `"stdcall"`.

Native unwinding is defined per-target. On targets that support throwing and catching C++ exceptions, it refers to the mechanism used to implement this feature. Some platforms implement a form of unwinding referred to as ["forced unwinding"][forced-unwinding]; `longjmp` on Windows and `pthread_exit` in `glibc` are implemented this way. Forced unwinding is explicitly excluded from the "Native unwind" column in the table.

| panic runtime  | ABI           | `panic`-unwind                        | Native unwind (unforced) |
| -------------- | ------------  | ------------------------------------- | -----------------------  |
| `panic=unwind` | unwinding     | unwind                                | unwind                   |
| `panic=unwind` | non-unwinding | abort (see notes below)               | [undefined behavior]     |
| `panic=abort`  | unwinding     | `panic` aborts without unwinding      | abort                    |
| `panic=abort`  | non-unwinding | `panic` aborts without unwinding      | [undefined behavior]     |

r[items.fn.extern.abort]
With `panic=unwind`, when a `panic` is turned into an abort by a non-unwinding ABI boundary, either no destructors (`Drop` calls) will run, or all destructors up until the ABI boundary will run. It is unspecified which of those two behaviors will happen.

For other considerations and limitations regarding unwinding across FFI boundaries, see the [relevant section in the Panic documentation][panic-ffi].

[forced-unwinding]: https://rust-lang.github.io/rfcs/2945-c-unwind-abi.html#forced-unwinding
[panic handler]: ../panic.md#the-panic_handler-attribute
[panic-ffi]: ../panic.md#unwinding-across-ffi-boundaries
[panicking]: ../panic.md
[undefined behavior]: ../behavior-considered-undefined.md

r[items.fn.const]
## Const functions

See [const functions] for the definition of const functions.

r[items.fn.async]
## Async functions

r[items.fn.async.intro]
Functions may be qualified as async, and this can also be combined with the `unsafe` qualifier:

```rust
async fn regular_example() { }
async unsafe fn unsafe_example() { }
```

r[items.fn.async.future]
Async functions do no work when called: instead, they capture their arguments into a future. When polled, that future will execute the function's body.

r[items.fn.async.desugar-brief]
An async function is roughly equivalent to a function that returns [`impl Future`] and with an [`async move` block][async-blocks] as its body:

```rust
// Source
async fn example(x: &str) -> usize {
    x.len()
}
```

is roughly equivalent to:

```rust
# use std::future::Future;
// Desugared
fn example<'a>(x: &'a str) -> impl Future<Output = usize> + 'a {
    async move { x.len() }
}
```

r[items.fn.async.desugar]
The actual desugaring is more complex:

r[items.fn.async.lifetime-capture]
- The return type in the desugaring is assumed to capture all lifetime parameters from the `async fn` declaration. This can be seen in the desugared example above, which explicitly outlives, and hence captures, `'a`.

r[items.fn.async.param-capture]
- The [`async move` block][async-blocks] in the body captures all function parameters, including those that are unused or bound to a `_` pattern. This ensures that function parameters are dropped in the same order as they would be if the function were not async, except that the drop occurs when the returned future has been fully awaited.

For more information on the effect of async, see [`async` blocks][async-blocks].

[async-blocks]: ../expressions/block-expr.md#async-blocks
[`impl Future`]: ../types/impl-trait.md

r[items.fn.async.edition2018]
> [!EDITION-2018]
> Async functions are only available beginning with Rust 2018.

r[items.fn.async.safety]
### Combining `async` and `unsafe`

r[items.fn.async.safety.intro]
It is legal to declare a function that is both async and unsafe. The resulting function is unsafe to call and (like any async function) returns a future. This future is just an ordinary future and thus an `unsafe` context is not required to "await" it:

```rust
// Returns a future that, when awaited, dereferences `x`.
//
// Soundness condition: `x` must be safe to dereference until
// the resulting future is complete.
async unsafe fn unsafe_example(x: *const i32) -> i32 {
  *x
}

async fn safe_example() {
    // An `unsafe` block is required to invoke the function initially:
    let p = 22;
    let future = unsafe { unsafe_example(&p) };

    // But no `unsafe` block required here. This will
    // read the value of `p`:
    let q = future.await;
}
```

Note that this behavior is a consequence of the desugaring to a function that returns an `impl Future` -- in this case, the function we desugar to is an `unsafe` function, but the return value remains the same.

Unsafe is used on an async function in precisely the same way that it is used on other functions: it indicates that the function imposes some additional obligations on its caller to ensure soundness. As in any other unsafe function, these conditions may extend beyond the initial call itself -- in the snippet above, for example, the `unsafe_example` function took a pointer `x` as argument, and then (when awaited) dereferenced that pointer. This implies that `x` would have to be valid until the future is finished executing, and it is the caller's responsibility to ensure that.

r[items.fn.attributes]
## Attributes on functions

r[items.fn.attributes.intro]
[Outer attributes][attributes] are allowed on functions. [Inner attributes][attributes] are allowed directly after the `{` inside its body [block].

This example shows an inner attribute on a function. The function is documented with just the word "Example".

```rust
fn documented() {
    #![doc = "Example"]
}
```

> [!NOTE]
> Except for lints, it is idiomatic to only use outer attributes on function items.

r[items.fn.attributes.builtin-attributes]
The attributes that have meaning on a function are:

- [`cfg_attr`]
- [`cfg`]
- [`cold`]
- [`deprecated`]
- [`doc`]
- [`export_name`]
- [`inline`]
- [`link_section`]
- [`must_use`]
- [`no_mangle`]
- [Lint check attributes]
- [Procedural macro attributes]
- [Testing attributes]

r[items.fn.param-attributes]
## Attributes on function parameters

r[items.fn.param-attributes.intro]
[Outer attributes][attributes] are allowed on function parameters and the permitted [built-in attributes] are restricted to `cfg`, `cfg_attr`, `allow`, `warn`, `deny`, and `forbid`.

```rust
fn len(
    #[cfg(windows)] slice: &[u16],
    #[cfg(not(windows))] slice: &[u8],
) -> usize {
    slice.len()
}
```

r[items.fn.param-attributes.parsed-attributes]
Inert helper attributes used by procedural macro attributes applied to items are also allowed but be careful to not include these inert attributes in your final `TokenStream`.

For example, the following code defines an inert `some_inert_attribute` attribute that is not formally defined anywhere and the `some_proc_macro_attribute` procedural macro is responsible for detecting its presence and removing it from the output token stream.

<!-- ignore: requires proc macro -->
```rust,ignore
#[some_proc_macro_attribute]
fn foo_oof(#[some_inert_attribute] arg: u8) {
}
```

[const contexts]: ../const_eval.md#const-context
[const functions]: ../const_eval.md#const-functions
[external block]: external-blocks.md
[path]: ../paths.md
[block]: ../expressions/block-expr.md
[variables]: ../variables.md
[type]: ../types.md#type-expressions
[unit type]: ../types/tuple.md
[*function item type*]: ../types/function-item.md
[Trait]: traits.md
[attributes]: ../attributes.md
[`cfg`]: ../conditional-compilation.md#the-cfg-attribute
[`cfg_attr`]: ../conditional-compilation.md#the-cfg_attr-attribute
[lint check attributes]: ../attributes/diagnostics.md#lint-check-attributes
[procedural macro attributes]: macro.proc.attribute
[testing attributes]: ../attributes/testing.md
[`cold`]: ../attributes/codegen.md#the-cold-attribute
[`inline`]: ../attributes/codegen.md#the-inline-attribute
[`deprecated`]: ../attributes/diagnostics.md#the-deprecated-attribute
[`doc`]: ../../rustdoc/the-doc-attribute.html
[`must_use`]: ../attributes/diagnostics.md#the-must_use-attribute
[patterns]: ../patterns.md
[`export_name`]: ../abi.md#the-export_name-attribute
[`link_section`]: ../abi.md#the-link_section-attribute
[`no_mangle`]: ../abi.md#the-no_mangle-attribute
[built-in attributes]: ../attributes.md#built-in-attributes-index
[trait item]: traits.md
[method]: associated-items.md#methods
[associated function]: associated-items.md#associated-functions-and-methods
[implementation]: implementations.md
[value namespace]: ../names/namespaces.md
[variadic function]: external-blocks.md#variadic-functions
[`extern` block]: external-blocks.md


---

r[items.type]
# Type aliases

r[items.type.syntax]
```grammar,items
TypeAlias ->
    `type` IDENTIFIER GenericParams? ( `:` TypeParamBounds )?
        WhereClause?
        ( `=` Type WhereClause?)? `;`
```

r[items.type.intro]
A _type alias_ defines a new name for an existing [type] in the [type namespace] of the module or block where it is located. Type aliases are declared with the keyword `type`. Every value has a single, specific type, but may implement several different traits, and may be compatible with several different type constraints.

For example, the following defines the type `Point` as a synonym for the type `(u8, u8)`, the type of pairs of unsigned 8 bit integers:

```rust
type Point = (u8, u8);
let p: Point = (41, 68);
```

r[items.type.constructor-alias]
A type alias to a tuple-struct or unit-struct cannot be used to qualify that type's constructor:

```rust,compile_fail
struct MyStruct(u32);

use MyStruct as UseAlias;
type TypeAlias = MyStruct;

let _ = UseAlias(5); // OK
let _ = TypeAlias(5); // Doesn't work
```

r[items.type.associated-type]
A type alias, when not used as an [associated type], must include a [Type][grammar-Type] and may not include [TypeParamBounds].

r[items.type.associated-trait]
A type alias, when used as an [associated type] in a [trait], must not include a [Type][grammar-Type] specification but may include [TypeParamBounds].

r[items.type.associated-impl]
A type alias, when used as an [associated type] in a [trait impl], must include a [Type][grammar-Type] specification and may not include [TypeParamBounds].

r[items.type.deprecated]
Where clauses before the equals sign on a type alias in a [trait impl] (like `type TypeAlias<T> where T: Foo = Bar<T>`) are deprecated. Where clauses after the equals sign (like `type TypeAlias<T> = Bar<T> where T: Foo`) are preferred.

[associated type]: associated-items.md#associated-types
[trait impl]: implementations.md#trait-implementations
[trait]: traits.md
[type namespace]: ../names/namespaces.md
[type]: ../types.md


---

r[items.struct]
# Structs

r[items.struct.syntax]
```grammar,items
Struct ->
      StructStruct
    | TupleStruct

StructStruct ->
    `struct` IDENTIFIER GenericParams? WhereClause? ( `{` StructFields? `}` | `;` )

TupleStruct ->
    `struct` IDENTIFIER GenericParams? `(` TupleFields? `)` WhereClause? `;`

StructFields -> StructField (`,` StructField)* `,`?

StructField -> OuterAttribute* Visibility? IDENTIFIER `:` Type

TupleFields -> TupleField (`,` TupleField)* `,`?

TupleField -> OuterAttribute* Visibility? Type
```

r[items.struct.intro]
A _struct_ is a nominal [struct type] defined with the keyword `struct`.

r[items.struct.namespace]
A struct declaration defines the given name in the [type namespace] of the module or block where it is located.

An example of a `struct` item and its use:

```rust
struct Point {x: i32, y: i32}
let p = Point {x: 10, y: 11};
let px: i32 = p.x;
```

r[items.struct.tuple]
A _tuple struct_ is a nominal [tuple type], and is also defined with the keyword `struct`. In addition to defining a type, it also defines a constructor of the same name in the [value namespace]. The constructor is a function which can be called to create a new instance of the struct. For example:

```rust
struct Point(i32, i32);
let p = Point(10, 11);
let px: i32 = match p { Point(x, _) => x };
```

r[items.struct.unit]
A _unit-like struct_ is a struct without any fields, defined by leaving off the list of fields entirely. Such a struct implicitly defines a [constant] of its type with the same name. For example:

```rust
struct Cookie;
let c = [Cookie, Cookie {}, Cookie, Cookie {}];
```

is equivalent to

```rust
struct Cookie {}
const Cookie: Cookie = Cookie {};
let c = [Cookie, Cookie {}, Cookie, Cookie {}];
```

r[items.struct.layout]
The precise memory layout of a struct is not specified. One can specify a particular layout using the [`repr` attribute].

[`repr` attribute]: ../type-layout.md#representations
[constant]: constant-items.md
[struct type]: ../types/struct.md
[tuple type]: ../types/tuple.md
[type namespace]: ../names/namespaces.md
[value namespace]: ../names/namespaces.md


---

r[items.enum]
# Enumerations

r[items.enum.syntax]
```grammar,items
Enumeration ->
    `enum` IDENTIFIER GenericParams? WhereClause? `{` EnumVariants? `}`

EnumVariants -> EnumVariant ( `,` EnumVariant )* `,`?

EnumVariant ->
    OuterAttribute* Visibility?
    IDENTIFIER ( EnumVariantTuple | EnumVariantStruct )? EnumVariantDiscriminant?

EnumVariantTuple -> `(` TupleFields? `)`

EnumVariantStruct -> `{` StructFields? `}`

EnumVariantDiscriminant -> `=` Expression
```

r[items.enum.intro]
An *enumeration*, also referred to as an *enum*, is a simultaneous definition of a nominal [enumerated type] as well as a set of *constructors*, that can be used to create or pattern-match values of the corresponding enumerated type.

r[items.enum.decl]
Enumerations are declared with the keyword `enum`.

r[items.enum.namespace]
The `enum` declaration defines the enumeration type in the [type namespace] of the module or block where it is located.

An example of an `enum` item and its use:

```rust
enum Animal {
    Dog,
    Cat,
}

let mut a: Animal = Animal::Dog;
a = Animal::Cat;
```

r[items.enum.constructor]
Enum constructors can have either named or unnamed fields:

```rust
enum Animal {
    Dog(String, f64),
    Cat { name: String, weight: f64 },
}

let mut a: Animal = Animal::Dog("Cocoa".to_string(), 37.2);
a = Animal::Cat { name: "Spotty".to_string(), weight: 2.7 };
```

In this example, `Cat` is a _struct-like enum variant_, whereas `Dog` is simply called an enum variant.

r[items.enum.fieldless]
An enum where no constructors contain fields is called a *<span id="field-less-enum">field-less enum</span>*. For example, this is a fieldless enum:

```rust
enum Fieldless {
    Tuple(),
    Struct{},
    Unit,
}
```

r[items.enum.unit-only]
If a field-less enum only contains unit variants, the enum is called an *<span id="unit-only-enum">unit-only enum</span>*. For example:

```rust
enum Enum {
    Foo = 3,
    Bar = 2,
    Baz = 1,
}
```

r[items.enum.constructor-names]
Variant constructors are similar to [struct] definitions, and can be referenced by a path from the enumeration name, including in [use declarations].

r[items.enum.constructor-namespace]
Each variant defines its type in the [type namespace], though that type cannot be used as a type specifier. Tuple-like and unit-like variants also define a constructor in the [value namespace].

r[items.enum.struct-expr]
A struct-like variant can be instantiated with a [struct expression].

r[items.enum.tuple-expr]
A tuple-like variant can be instantiated with a [call expression] or a [struct expression].

r[items.enum.path-expr]
A unit-like variant can be instantiated with a [path expression] or a [struct expression]. For example:

```rust
enum Examples {
    UnitLike,
    TupleLike(i32),
    StructLike { value: i32 },
}

use Examples::*; // Creates aliases to all variants.
let x = UnitLike; // Path expression of the const item.
let x = UnitLike {}; // Struct expression.
let y = TupleLike(123); // Call expression.
let y = TupleLike { 0: 123 }; // Struct expression using integer field names.
let z = StructLike { value: 123 }; // Struct expression.
```

<span id="custom-discriminant-values-for-fieldless-enumerations"></span>
r[items.enum.discriminant]
## Discriminants

r[items.enum.discriminant.intro]
Each enum instance has a _discriminant_: an integer logically associated to it that is used to determine which variant it holds.

r[items.enum.discriminant.repr-rust]
Under the [`Rust` representation], the discriminant is interpreted as an `isize` value. However, the compiler is allowed to use a smaller type (or another means of distinguishing variants) in its actual memory layout.

### Assigning discriminant values

r[items.enum.discriminant.explicit]
#### Explicit discriminants

r[items.enum.discriminant.explicit.intro]
In two circumstances, the discriminant of a variant may be explicitly set by following the variant name with `=` and a [constant expression]:

r[items.enum.discriminant.explicit.unit-only]
1. if the enumeration is "[unit-only]".

r[items.enum.discriminant.explicit.primitive-repr]
2. if a [primitive representation] is used. For example:

   ```rust
   #[repr(u8)]
   enum Enum {
       Unit = 3,
       Tuple(u16),
       Struct {
           a: u8,
           b: u16,
       } = 1,
   }
   ```

r[items.enum.discriminant.implicit]
#### Implicit discriminants

If a discriminant for a variant is not specified, then it is set to one higher than the discriminant of the previous variant in the declaration. If the discriminant of the first variant in the declaration is unspecified, then it is set to zero.

```rust
enum Foo {
    Bar,            // 0
    Baz = 123,      // 123
    Quux,           // 124
}

let baz_discriminant = Foo::Baz as u32;
assert_eq!(baz_discriminant, 123);
```

r[items.enum.discriminant.restrictions]
#### Restrictions

r[items.enum.discriminant.restrictions.same-discriminant]
It is an error when two variants share the same discriminant.

```rust,compile_fail
enum SharedDiscriminantError {
    SharedA = 1,
    SharedB = 1
}

enum SharedDiscriminantError2 {
    Zero,       // 0
    One,        // 1
    OneToo = 1  // 1 (collision with previous!)
}
```

r[items.enum.discriminant.restrictions.above-max-discriminant]
It is also an error to have an unspecified discriminant where the previous discriminant is the maximum value for the size of the discriminant.

```rust,compile_fail
#[repr(u8)]
enum OverflowingDiscriminantError {
    Max = 255,
    MaxPlusOne // Would be 256, but that overflows the enum.
}

#[repr(u8)]
enum OverflowingDiscriminantError2 {
    MaxMinusOne = 254, // 254
    Max,               // 255
    MaxPlusOne         // Would be 256, but that overflows the enum.
}
```

r[items.enum.discriminant.restrictions.generics]
Explicit enum discriminant initializers may not use generic parameters from the enclosing enum.

```rust,compile_fail
#[repr(u32)]
enum E<'a, T, const N: u32> {
    Lifetime(&'a T) = {
        let a: &'a (); // ERROR.
        1
    },
    Type(T) = {
        let x: T; // ERROR.
        2
    },
    Const = N, // ERROR.
}
```

### Accessing discriminant

#### Via `mem::discriminant`

r[items.enum.discriminant.access-opaque]

[`std::mem::discriminant`] returns an opaque reference to the discriminant of an enum value which can be compared. This cannot be used to get the value of the discriminant.

r[items.enum.discriminant.coercion]
#### Casting

r[items.enum.discriminant.coercion.intro]
If an enumeration is [unit-only] (with no tuple and struct variants), then its discriminant can be directly accessed with a [numeric cast]; e.g.:

```rust
enum Enum {
    Foo,
    Bar,
    Baz,
}

assert_eq!(0, Enum::Foo as isize);
assert_eq!(1, Enum::Bar as isize);
assert_eq!(2, Enum::Baz as isize);
```

r[items.enum.discriminant.coercion.fieldless]
[Field-less enums] can be cast if they do not have explicit discriminants, or where only unit variants are explicit.

```rust
enum Fieldless {
    Tuple(),
    Struct{},
    Unit,
}

assert_eq!(0, Fieldless::Tuple() as isize);
assert_eq!(1, Fieldless::Struct{} as isize);
assert_eq!(2, Fieldless::Unit as isize);

#[repr(u8)]
enum FieldlessWithDiscriminants {
    First = 10,
    Tuple(),
    Second = 20,
    Struct{},
    Unit,
}

assert_eq!(10, FieldlessWithDiscriminants::First as u8);
assert_eq!(11, FieldlessWithDiscriminants::Tuple() as u8);
assert_eq!(20, FieldlessWithDiscriminants::Second as u8);
assert_eq!(21, FieldlessWithDiscriminants::Struct{} as u8);
assert_eq!(22, FieldlessWithDiscriminants::Unit as u8);
```

#### Pointer casting

r[items.enum.discriminant.access-memory]

If the enumeration specifies a [primitive representation], then the discriminant may be reliably accessed via unsafe pointer casting:

```rust
#[repr(u8)]
enum Enum {
    Unit,
    Tuple(bool),
    Struct{a: bool},
}

impl Enum {
    fn discriminant(&self) -> u8 {
        unsafe { *(self as *const Self as *const u8) }
    }
}

let unit_like = Enum::Unit;
let tuple_like = Enum::Tuple(true);
let struct_like = Enum::Struct{a: false};

assert_eq!(0, unit_like.discriminant());
assert_eq!(1, tuple_like.discriminant());
assert_eq!(2, struct_like.discriminant());
```

r[items.enum.empty]
## Zero-variant enums

r[items.enum.empty.intro]
Enums with zero variants are known as *zero-variant enums*. As they have no valid values, they cannot be instantiated.

```rust
enum ZeroVariants {}
```

r[items.enum.empty.uninhabited]
Zero-variant enums are equivalent to the [never type], but they cannot be coerced into other types.

```rust,compile_fail
# enum ZeroVariants {}
let x: ZeroVariants = panic!();
let y: u32 = x; // mismatched type error
```

r[items.enum.variant-visibility]
## Variant visibility

Enum variants syntactically allow a [Visibility] annotation, but this is rejected when the enum is validated. This allows items to be parsed with a unified syntax across different contexts where they are used.

```rust
macro_rules! mac_variant {
    ($vis:vis $name:ident) => {
        enum $name {
            $vis Unit,

            $vis Tuple(u8, u16),

            $vis Struct { f: u8 },
        }
    }
}

// Empty `vis` is allowed.
mac_variant! { E }

// This is allowed, since it is removed before being validated.
#[cfg(false)]
enum E {
    pub U,
    pub(crate) T(u8),
    pub(super) T { f: String }
}
```

[`C` representation]: ../type-layout.md#the-c-representation
[call expression]: ../expressions/call-expr.md
[constant expression]: ../const_eval.md#constant-expressions
[enumerated type]: ../types/enum.md
[Field-less enums]: #field-less-enum
[never type]: ../types/never.md
[numeric cast]: ../expressions/operator-expr.md#semantics
[path expression]: ../expressions/path-expr.md
[primitive representation]: ../type-layout.md#primitive-representations
[`Rust` representation]: ../type-layout.md#the-rust-representation
[struct expression]: ../expressions/struct-expr.md
[struct]: structs.md
[type namespace]: ../names/namespaces.md
[unit-only]: #unit-only-enum
[use declarations]: use-declarations.md
[value namespace]: ../names/namespaces.md


---

r[items.union]
# Unions

r[items.union.syntax]
```grammar,items
Union ->
    `union` IDENTIFIER GenericParams? WhereClause? `{` StructFields? `}`
```

r[items.union.intro]
A union declaration uses the same syntax as a struct declaration, except with `union` in place of `struct`.

r[items.union.namespace]
A union declaration defines the given name in the [type namespace] of the module or block where it is located.

```rust
#[repr(C)]
union MyUnion {
    f1: u32,
    f2: f32,
}
```

r[items.union.common-storage]
The key property of unions is that all fields of a union share common storage. As a result, writes to one field of a union can overwrite its other fields, and size of a union is determined by the size of its largest field.

r[items.union.field-restrictions]
Union field types are restricted to the following subset of types:

r[items.union.field-copy]
- `Copy` types

r[items.union.field-references]
- References (`&T` and `&mut T` for arbitrary `T`)

r[items.union.field-manually-drop]
- `ManuallyDrop<T>` (for arbitrary `T`)

r[items.union.field-tuple]
- Tuples and arrays containing only allowed union field types

r[items.union.drop]
This restriction ensures, in particular, that union fields never need to be dropped. Like for structs and enums, it is possible to `impl Drop` for a union to manually define what happens when it gets dropped.

r[items.union.fieldless]
Unions without any fields are not accepted by the compiler, but can be accepted by macros.

r[items.union.init]
## Initialization of a union

r[items.union.init.intro]
A value of a union type can be created using the same syntax that is used for struct types, except that it must specify exactly one field:

```rust
# union MyUnion { f1: u32, f2: f32 }
#
let u = MyUnion { f1: 1 };
```

r[items.union.init.result]
The expression above creates a value of type `MyUnion` and initializes the storage using field `f1`. The union can be accessed using the same syntax as struct fields:

```rust
# union MyUnion { f1: u32, f2: f32 }
#
# let u = MyUnion { f1: 1 };
let f = unsafe { u.f1 };
```

r[items.union.fields]
## Reading and writing union fields

r[items.union.fields.intro]
Unions have no notion of an "active field". Instead, every union access just interprets the storage as the type of the field used for the access.

r[items.union.fields.read]
Reading a union field reads the bits of the union at the field's type.

r[items.union.fields.offset]
Fields might have a non-zero offset (except when [the C representation] is used); in that case the bits starting at the offset of the fields are read

r[items.union.fields.validity]
It is the programmer's responsibility to make sure that the data is valid at the field's type. Failing to do so results in [undefined behavior]. For example, reading the value `3` from a field of the [boolean type] is undefined behavior. Effectively, writing to and then reading from a union with [the C representation] is analogous to a [`transmute`] from the type used for writing to the type used for reading.

r[items.union.fields.read-safety]
Consequently, all reads of union fields have to be placed in `unsafe` blocks:

```rust
# union MyUnion { f1: u32, f2: f32 }
# let u = MyUnion { f1: 1 };
#
unsafe {
    let f = u.f1;
}
```

Commonly, code using unions will provide safe wrappers around unsafe union field accesses.

r[items.union.fields.write-safety]
In contrast, writes to union fields are safe, since they just overwrite arbitrary data, but cannot cause undefined behavior. (Note that union field types can never have drop glue, so a union field write will never implicitly drop anything.)

r[items.union.pattern]
## Pattern matching on unions

r[items.union.pattern.intro]
Another way to access union fields is to use pattern matching.

r[items.union.pattern.one-field]
Pattern matching on union fields uses the same syntax as struct patterns, except that the pattern must specify exactly one field.

r[items.union.pattern.safety]
Since pattern matching is like reading the union with a particular field, it has to be placed in `unsafe` blocks as well.

```rust
# union MyUnion { f1: u32, f2: f32 }
#
fn f(u: MyUnion) {
    unsafe {
        match u {
            MyUnion { f1: 10 } => { println!("ten"); }
            MyUnion { f2 } => { println!("{}", f2); }
        }
    }
}
```

r[items.union.pattern.subpattern]
Pattern matching may match a union as a field of a larger structure. In particular, when using a Rust union to implement a C tagged union via FFI, this allows matching on the tag and the corresponding field simultaneously:

```rust
#[repr(u32)]
enum Tag { I, F }

#[repr(C)]
union U {
    i: i32,
    f: f32,
}

#[repr(C)]
struct Value {
    tag: Tag,
    u: U,
}

fn is_zero(v: Value) -> bool {
    unsafe {
        match v {
            Value { tag: Tag::I, u: U { i: 0 } } => true,
            Value { tag: Tag::F, u: U { f: num } } if num == 0.0 => true,
            _ => false,
        }
    }
}
```

r[items.union.ref]
## References to union fields

r[items.union.ref.intro]
Since union fields share common storage, gaining write access to one field of a union can give write access to all its remaining fields.

r[items.union.ref.borrow]
Borrow checking rules have to be adjusted to account for this fact. As a result, if one field of a union is borrowed, all its remaining fields are borrowed as well for the same lifetime.

```rust,compile_fail
# union MyUnion { f1: u32, f2: f32 }
// ERROR: cannot borrow `u` (via `u.f2`) as mutable more than once at a time
fn test() {
    let mut u = MyUnion { f1: 1 };
    unsafe {
        let b1 = &mut u.f1;
//                    ---- first mutable borrow occurs here (via `u.f1`)
        let b2 = &mut u.f2;
//                    ^^^^ second mutable borrow occurs here (via `u.f2`)
        *b1 = 5;
    }
//  - first borrow ends here
    assert_eq!(unsafe { u.f1 }, 5);
}
```

r[items.union.ref.use]
As you could see, in many aspects (except for layouts, safety, and ownership) unions behave exactly like structs, largely as a consequence of inheriting their syntactic shape from structs. This is also true for many unmentioned aspects of Rust language (such as privacy, name resolution, type inference, generics, trait implementations, inherent implementations, coherence, pattern checking, etc etc etc).

[`transmute`]: std::mem::transmute
[boolean type]: ../types/boolean.md
[the C representation]: ../type-layout.md#reprc-unions
[type namespace]: ../names/namespaces.md
[undefined behavior]: ../behavior-considered-undefined.md


---

r[items.const]
# Constant items

r[items.const.syntax]
```grammar,items
ConstantItem ->
    `const` ( IDENTIFIER | `_` ) `:` Type ( `=` Expression )? `;`
```

r[items.const.intro]
A *constant item* is an optionally named _[constant value]_ which is not associated with a specific memory location in the program.

r[items.const.behavior]
Constants are essentially inlined wherever they are used, meaning that they are copied directly into the relevant context when used. This includes use of constants from external crates, and non-[`Copy`] types. References to the same constant are not necessarily guaranteed to refer to the same memory address.

r[items.const.namespace]
The constant declaration defines the constant value in the [value namespace] of the module or block where it is located.

r[items.const.static]
Constants must be explicitly typed. The type must have a `'static` lifetime: any references in the initializer must have `'static` lifetimes. References in the type of a constant default to `'static` lifetime; see [static lifetime elision].

r[items.const.static-temporary]
A reference to a constant will have `'static` lifetime if the constant value is eligible for [promotion]; otherwise, a temporary will be created.

```rust
const BIT1: u32 = 1 << 0;
const BIT2: u32 = 1 << 1;

const BITS: [u32; 2] = [BIT1, BIT2];
const STRING: &'static str = "bitstring";

struct BitsNStrings<'a> {
    mybits: [u32; 2],
    mystring: &'a str,
}

const BITS_N_STRINGS: BitsNStrings<'static> = BitsNStrings {
    mybits: BITS,
    mystring: STRING,
};
```

r[items.const.expr-omission]
The constant expression may only be omitted in a [trait definition].

r[items.const.destructor]
## Constants with destructors

Constants can contain destructors. Destructors are run when the value goes out of scope.

```rust
struct TypeWithDestructor(i32);

impl Drop for TypeWithDestructor {
    fn drop(&mut self) {
        println!("Dropped. Held {}.", self.0);
    }
}

const ZERO_WITH_DESTRUCTOR: TypeWithDestructor = TypeWithDestructor(0);

fn create_and_drop_zero_with_destructor() {
    let x = ZERO_WITH_DESTRUCTOR;
    // x gets dropped at end of function, calling drop.
    // prints "Dropped. Held 0.".
}
```

r[items.const.unnamed]
## Unnamed constant

r[items.const.unnamed.intro]
Unlike an [associated constant], a [free] constant may be unnamed by using an underscore instead of the name. For example:

```rust
const _: () =  { struct _SameNameTwice; };

// OK although it is the same name as above:
const _: () =  { struct _SameNameTwice; };
```

r[items.const.unnamed.repetition]
As with [underscore imports], macros may safely emit the same unnamed constant in the same scope more than once. For example, the following should not produce an error:

```rust
macro_rules! m {
    ($item: item) => { $item $item }
}

m!(const _: () = (););
// This expands to:
// const _: () = ();
// const _: () = ();
```

r[items.const.eval]
## Evaluation

[Free][free] constants are always [evaluated][const_eval] at compile-time to surface panics. This happens even within an unused function:

```rust,compile_fail
// Compile-time panic
const PANIC: () = std::unimplemented!();

fn unused_generic_function<T>() {
    // A failing compile-time assertion
    const _: () = assert!(usize::BITS == 0);
}
```

[const_eval]: ../const_eval.md
[associated constant]: ../items/associated-items.md#associated-constants
[constant value]: ../const_eval.md#constant-expressions
[free]: ../glossary.md#free-item
[static lifetime elision]: ../lifetime-elision.md#const-and-static-elision
[trait definition]: traits.md
[underscore imports]: use-declarations.md#underscore-imports
[`Copy`]: ../special-types-and-traits.md#copy
[value namespace]: ../names/namespaces.md
[promotion]: destructors.scope.const-promotion


---

r[items.static]
# Static items

r[items.static.syntax]
```grammar,items
StaticItem ->
    ItemSafety?[^extern-safety] `static` `mut`? IDENTIFIER `:` Type ( `=` Expression )? `;`
```

[^extern-safety]: The `safe` and `unsafe` function qualifiers are only allowed semantically within `extern` blocks.

r[items.static.intro]
A *static item* is similar to a [constant], except that it represents an allocation in the program that is initialized with the initializer expression. All references and raw pointers to the static refer to the same allocation.

r[items.static.lifetime]
Static items have the `static` lifetime, which outlives all other lifetimes in a Rust program. Static items do not call [`drop`] at the end of the program.

r[items.static.storage-disjointness]
If the `static` has a size of at least 1 byte, this allocation is disjoint from all other such `static` allocations as well as heap allocations and stack-allocated variables. However, the storage of immutable `static` items can overlap with allocations that do not themselves have a unique address, such as [promoteds] and [`const` items][constant].

r[items.static.namespace]
The static declaration defines a static value in the [value namespace] of the module or block where it is located.

r[items.static.init]
The static initializer is a [constant expression] evaluated at compile time. Static initializers may refer to and read from other statics. When reading from mutable statics, they read the initial value of that static.

r[items.static.read-only]
Non-`mut` static items that contain a type that is not [interior mutable] may be placed in read-only memory.

r[items.static.safety]
All access to a static is safe, but there are a number of restrictions on statics:

r[items.static.sync]
* The type must have the [`Sync`](std::marker::Sync) trait bound to allow thread-safe access.

r[items.static.init.omission]
The initializer expression must be omitted in an [external block], and must be provided for free static items.

r[items.static.safety-qualifiers]
The `safe` and `unsafe` qualifiers are semantically only allowed when used in an [external block].

r[items.static.generics]
## Statics & generics

A static item defined in a generic scope (for example in a blanket or default implementation) will result in exactly one static item being defined, as if the static definition was pulled out of the current scope into the module. There will *not* be one item per monomorphization.

This code:

```rust
use std::sync::atomic::{AtomicUsize, Ordering};

trait Tr {
    fn default_impl() {
        static COUNTER: AtomicUsize = AtomicUsize::new(0);
        println!("default_impl: counter was {}", COUNTER.fetch_add(1, Ordering::Relaxed));
    }

    fn blanket_impl();
}

struct Ty1 {}
struct Ty2 {}

impl<T> Tr for T {
    fn blanket_impl() {
        static COUNTER: AtomicUsize = AtomicUsize::new(0);
        println!("blanket_impl: counter was {}", COUNTER.fetch_add(1, Ordering::Relaxed));
    }
}

fn main() {
    <Ty1 as Tr>::default_impl();
    <Ty2 as Tr>::default_impl();
    <Ty1 as Tr>::blanket_impl();
    <Ty2 as Tr>::blanket_impl();
}
```

prints

```text
default_impl: counter was 0
default_impl: counter was 1
blanket_impl: counter was 0
blanket_impl: counter was 1
```

r[items.static.mut]
## Mutable statics

r[items.static.mut.intro]
If a static item is declared with the `mut` keyword, then it is allowed to be modified by the program. One of Rust's goals is to make concurrency bugs hard to run into, and this is obviously a very large source of race conditions or other bugs.

r[items.static.mut.safety]
For this reason, an `unsafe` block is required when either reading or writing a mutable static variable. Care should be taken to ensure that modifications to a mutable static are safe with respect to other threads running in the same process.

r[items.static.mut.extern]
Mutable statics are still very useful, however. They can be used with C libraries and can also be bound from C libraries in an `extern` block.

```rust
# fn atomic_add(_: *mut u32, _: u32) -> u32 { 2 }

static mut LEVELS: u32 = 0;

// This violates the idea of no shared state, and this doesn't internally
// protect against races, so this function is `unsafe`
unsafe fn bump_levels_unsafe() -> u32 {
    unsafe {
        let ret = LEVELS;
        LEVELS += 1;
        return ret;
    }
}

// As an alternative to `bump_levels_unsafe`, this function is safe, assuming
// that we have an atomic_add function which returns the old value. This
// function is safe only if no other code accesses the static in a non-atomic
// fashion. If such accesses are possible (such as in `bump_levels_unsafe`),
// then this would need to be `unsafe` to indicate to the caller that they
// must still guard against concurrent access.
fn bump_levels_safe() -> u32 {
    unsafe {
        return atomic_add(&raw mut LEVELS, 1);
    }
}
```

r[items.static.mut.sync]
Mutable statics have the same restrictions as normal statics, except that the type does not have to implement the `Sync` trait.

r[items.static.alternate]
## Using statics or consts

It can be confusing whether or not you should use a constant item or a static item. Constants should, in general, be preferred over statics unless one of the following are true:

* Large amounts of data are being stored.
* The single-address property of statics is required.
* Interior mutability is required.

[constant]: constant-items.md
[`drop`]: ../destructors.md
[constant expression]: ../const_eval.md#constant-expressions
[external block]: external-blocks.md
[interior mutable]: ../interior-mutability.md
[value namespace]: ../names/namespaces.md
[promoteds]: ../destructors.md#constant-promotion


---

r[items.traits]
# Traits

r[items.traits.syntax]
```grammar,items
Trait ->
    `unsafe`? `trait` IDENTIFIER GenericParams? ( `:` TypeParamBounds? )? WhereClause?
    `{`
        InnerAttribute*
        AssociatedItem*
    `}`
```

r[items.traits.intro]
A _trait_ describes an abstract interface that types can implement. This interface consists of [associated items], which come in three varieties:

- [functions](associated-items.md#associated-functions-and-methods)
- [types](associated-items.md#associated-types)
- [constants](associated-items.md#associated-constants)

r[items.traits.namespace]
The trait declaration defines a trait in the [type namespace] of the module or block where it is located.

r[items.traits.associated-item-namespaces]
Associated items are defined as members of the trait within their respective namespaces. Associated types are defined in the type namespace. Associated constants and associated functions are defined in the value namespace.

r[items.traits.self-param]
All traits define an implicit type parameter `Self` that refers to "the type that is implementing this interface". Traits may also contain additional type parameters. These type parameters, including `Self`, may be constrained by other traits and so forth [as usual][generics].

r[items.traits.impls]
Traits are implemented for specific types through separate [implementations].

r[items.traits.associated-item-decls]
Trait functions may omit the function body by replacing it with a semicolon. This indicates that the implementation must define the function. If the trait function defines a body, this definition acts as a default for any implementation which does not override it. Similarly, associated constants may omit the equal sign and expression to indicate implementations must define the constant value. Associated types must never define the type, the type may only be specified in an implementation.

```rust
// Examples of associated trait items with and without definitions.
trait Example {
    const CONST_NO_DEFAULT: i32;
    const CONST_WITH_DEFAULT: i32 = 99;
    type TypeNoDefault;
    fn method_without_default(&self);
    fn method_with_default(&self) {}
}
```

r[items.traits.const-fn]
Trait functions are not allowed to be [`const`].

r[items.traits.bounds]
## Trait bounds

Generic items may use traits as [bounds] on their type parameters.

r[items.traits.generic]
## Generic traits

Type parameters can be specified for a trait to make it generic. These appear after the trait name, using the same syntax used in [generic functions].

```rust
trait Seq<T> {
    fn len(&self) -> u32;
    fn elt_at(&self, n: u32) -> T;
    fn iter<F>(&self, f: F) where F: Fn(T);
}
```

<a id="object-safety"></a>
r[items.traits.dyn-compatible]
## Dyn compatibility

r[items.traits.dyn-compatible.intro]
A dyn-compatible trait can be the base trait of a [trait object]. A trait is *dyn compatible* if it has the following qualities:

r[items.traits.dyn-compatible.supertraits]
* All [supertraits] must also be dyn compatible.

r[items.traits.dyn-compatible.sized]
* `Sized` must not be a [supertrait][supertraits]. In other words, it must not require `Self: Sized`.

r[items.traits.dyn-compatible.associated-consts]
* It must not have any associated constants.

r[items.traits.dyn-compatible.associated-types]
* It must not have any associated types with generics.

r[items.traits.dyn-compatible.associated-functions]
* All associated functions must either be dispatchable from a trait object or be explicitly non-dispatchable:
    * Dispatchable functions must:
        * Not have any type parameters (although lifetime parameters are allowed).
        * Be a [method] that does not use `Self` except in the type of the receiver.
        * Have a receiver with one of the following types:
            * `&Self` (i.e. `&self`)
            * `&mut Self` (i.e `&mut self`)
            * [`Box<Self>`]
            * [`Rc<Self>`]
            * [`Arc<Self>`]
            * [`Pin<P>`] where `P` is one of the types above
        * Not have an opaque return type; that is,
            * Not be an `async fn` (which has a hidden `Future` type).
            * Not have a return position `impl Trait` type (`fn example(&self) -> impl Trait`).
        * Not have a `where Self: Sized` bound (receiver type of `Self` (i.e. `self`) implies this).
    * Explicitly non-dispatchable functions require:
        * Have a `where Self: Sized` bound (receiver type of `Self` (i.e. `self`) implies this).

r[items.traits.dyn-compatible.async-traits]
* The [`AsyncFn`], [`AsyncFnMut`], and [`AsyncFnOnce`] traits are not dyn-compatible.

> [!NOTE]
> This concept was formerly known as *object safety*.

```rust
# use std::rc::Rc;
# use std::sync::Arc;
# use std::pin::Pin;
// Examples of dyn compatible methods.
trait TraitMethods {
    fn by_ref(self: &Self) {}
    fn by_ref_mut(self: &mut Self) {}
    fn by_box(self: Box<Self>) {}
    fn by_rc(self: Rc<Self>) {}
    fn by_arc(self: Arc<Self>) {}
    fn by_pin(self: Pin<&Self>) {}
    fn with_lifetime<'a>(self: &'a Self) {}
    fn nested_pin(self: Pin<Arc<Self>>) {}
}
# struct S;
# impl TraitMethods for S {}
# let t: Box<dyn TraitMethods> = Box::new(S);
```

```rust,compile_fail
// This trait is dyn compatible, but these methods cannot be dispatched on a trait object.
trait NonDispatchable {
    // Non-methods cannot be dispatched.
    fn foo() where Self: Sized {}
    // Self type isn't known until runtime.
    fn returns(&self) -> Self where Self: Sized;
    // `other` may be a different concrete type of the receiver.
    fn param(&self, other: Self) where Self: Sized {}
    // Generics are not compatible with vtables.
    fn typed<T>(&self, x: T) where Self: Sized {}
}

struct S;
impl NonDispatchable for S {
    fn returns(&self) -> Self where Self: Sized { S }
}
let obj: Box<dyn NonDispatchable> = Box::new(S);
obj.returns(); // ERROR: cannot call with Self return
obj.param(S);  // ERROR: cannot call with Self parameter
obj.typed(1);  // ERROR: cannot call with generic type
```

```rust,compile_fail
# use std::rc::Rc;
// Examples of dyn-incompatible traits.
trait DynIncompatible {
    const CONST: i32 = 1;  // ERROR: cannot have associated const

    fn foo() {}  // ERROR: associated function without Sized
    fn returns(&self) -> Self; // ERROR: Self in return type
    fn typed<T>(&self, x: T) {} // ERROR: has generic type parameters
    fn nested(self: Rc<Box<Self>>) {} // ERROR: nested receiver cannot be dispatched on
}

struct S;
impl DynIncompatible for S {
    fn returns(&self) -> Self { S }
}
let obj: Box<dyn DynIncompatible> = Box::new(S); // ERROR
```

```rust,compile_fail
// `Self: Sized` traits are dyn-incompatible.
trait TraitWithSize where Self: Sized {}

struct S;
impl TraitWithSize for S {}
let obj: Box<dyn TraitWithSize> = Box::new(S); // ERROR
```

```rust,compile_fail
// Dyn-incompatible if `Self` is a type argument.
trait Super<A> {}
trait WithSelf: Super<Self> where Self: Sized {}

struct S;
impl<A> Super<A> for S {}
impl WithSelf for S {}
let obj: Box<dyn WithSelf> = Box::new(S); // ERROR: cannot use `Self` type parameter
```

r[items.traits.supertraits]
## Supertraits

r[items.traits.supertraits.intro]
**Supertraits** are traits that are required to be implemented for a type to implement a specific trait. Furthermore, anywhere a [generic][generics] or [trait object] is bounded by a trait, it has access to the associated items of its supertraits.

r[items.traits.supertraits.decl]
Supertraits are declared by trait bounds on the `Self` type of a trait and transitively the supertraits of the traits declared in those trait bounds. It is an error for a trait to be its own supertrait.

r[items.traits.supertraits.subtrait]
The trait with a supertrait is called a **subtrait** of its supertrait.

The following is an example of declaring `Shape` to be a supertrait of `Circle`.

```rust
trait Shape { fn area(&self) -> f64; }
trait Circle: Shape { fn radius(&self) -> f64; }
```

And the following is the same example, except using [where clauses].

```rust
trait Shape { fn area(&self) -> f64; }
trait Circle where Self: Shape { fn radius(&self) -> f64; }
```

This next example gives `radius` a default implementation using the `area` function from `Shape`.

```rust
# trait Shape { fn area(&self) -> f64; }
trait Circle where Self: Shape {
    fn radius(&self) -> f64 {
        // A = pi * r^2
        // so algebraically,
        // r = sqrt(A / pi)
        (self.area() / std::f64::consts::PI).sqrt()
    }
}
```

This next example calls a supertrait method on a generic parameter.

```rust
# trait Shape { fn area(&self) -> f64; }
# trait Circle: Shape { fn radius(&self) -> f64; }
fn print_area_and_radius<C: Circle>(c: C) {
    // Here we call the area method from the supertrait `Shape` of `Circle`.
    println!("Area: {}", c.area());
    println!("Radius: {}", c.radius());
}
```

Similarly, here is an example of calling supertrait methods on trait objects.

```rust
# trait Shape { fn area(&self) -> f64; }
# trait Circle: Shape { fn radius(&self) -> f64; }
# struct UnitCircle;
# impl Shape for UnitCircle { fn area(&self) -> f64 { std::f64::consts::PI } }
# impl Circle for UnitCircle { fn radius(&self) -> f64 { 1.0 } }
# let circle = UnitCircle;
let circle = Box::new(circle) as Box<dyn Circle>;
let nonsense = circle.radius() * circle.area();
```

r[items.traits.safety]
## Unsafe traits

r[items.traits.safety.intro]
Traits items that begin with the `unsafe` keyword indicate that *implementing* the trait may be [unsafe]. It is safe to use a correctly implemented unsafe trait. The [trait implementation] must also begin with the `unsafe` keyword.

[`Sync`] and [`Send`] are examples of unsafe traits.

r[items.traits.params]
## Parameter patterns

r[items.traits.params.patterns-no-body]
Parameters in associated functions without a body only allow [IDENTIFIER] or `_` [wild card][WildcardPattern] patterns, as well as the form allowed by [SelfParam]. `mut` [IDENTIFIER] is currently allowed, but it is deprecated and will become a hard error in the future.
<!-- https://github.com/rust-lang/rust/issues/35203 -->

```rust
trait T {
    fn f1(&self);
    fn f2(x: Self, _: i32);
}
```

```rust,compile_fail,E0642
trait T {
    fn f2(&x: &i32); // ERROR: patterns aren't allowed in functions without bodies
}
```

r[items.traits.params.patterns-with-body]
Parameters in associated functions with a body only allow irrefutable patterns.

```rust
trait T {
    fn f1((a, b): (i32, i32)) {} // OK: is irrefutable
}
```

```rust,compile_fail,E0005
trait T {
    fn f1(123: i32) {} // ERROR: pattern is refutable
    fn f2(Some(x): Option<i32>) {} // ERROR: pattern is refutable
}
```

r[items.traits.params.pattern-required.edition2018]
> [!EDITION-2018]
> Prior to the 2018 edition, the pattern for an associated function parameter is optional:
>
> ```rust,edition2015
> // 2015 Edition
> trait T {
>     fn f(i32); // OK: parameter identifiers are not required
> }
> ```
>
> Beginning in the 2018 edition, patterns are no longer optional.

r[items.traits.params.restriction-patterns.edition2018]
> [!EDITION-2018]
> Prior to the 2018 edition, parameters in associated functions with a body are limited to the following kinds of patterns:
>
> * [IDENTIFIER]
> * `mut` [IDENTIFIER]
> * [`_`][WildcardPattern]
> * `&` [IDENTIFIER]
> * `&&` [IDENTIFIER]
>
> ```rust,edition2015,compile_fail,E0642
> // 2015 Edition
> trait T {
>     fn f1((a, b): (i32, i32)) {} // ERROR: pattern not allowed
> }
> ```
>
> Beginning in 2018, all irrefutable patterns are allowed as described in [items.traits.params.patterns-with-body].

r[items.traits.associated-visibility]
## Item visibility

r[items.traits.associated-visibility.intro]
Trait items syntactically allow a [Visibility] annotation, but this is rejected when the trait is validated. This allows items to be parsed with a unified syntax across different contexts where they are used. As an example, an empty `vis` macro fragment specifier can be used for trait items, where the macro rule may be used in other situations where visibility is allowed.

```rust
macro_rules! create_method {
    ($vis:vis $name:ident) => {
        $vis fn $name(&self) {}
    };
}

trait T1 {
    // Empty `vis` is allowed.
    create_method! { method_of_t1 }
}

struct S;

impl S {
    // Visibility is allowed here.
    create_method! { pub method_of_s }
}

impl T1 for S {}

fn main() {
    let s = S;
    s.method_of_t1();
    s.method_of_s();
}
```

[WildcardPattern]: ../patterns.md#wildcard-pattern
[bounds]: ../trait-bounds.md
[trait object]: ../types/trait-object.md
[associated items]: associated-items.md
[method]: associated-items.md#methods
[supertraits]: #supertraits
[implementations]: implementations.md
[generics]: generics.md
[where clauses]: generics.md#where-clauses
[generic functions]: functions.md#generic-functions
[unsafe]: ../unsafety.md
[trait implementation]: implementations.md#trait-implementations
[`Send`]: ../special-types-and-traits.md#send
[`Sync`]: ../special-types-and-traits.md#sync
[`Arc<Self>`]: ../special-types-and-traits.md#arct
[`Box<Self>`]: ../special-types-and-traits.md#boxt
[`Pin<P>`]: ../special-types-and-traits.md#pinp
[`Rc<Self>`]: ../special-types-and-traits.md#rct
[`async`]: functions.md#async-functions
[`const`]: functions.md#const-functions
[type namespace]: ../names/namespaces.md


---

r[items.impl]
# Implementations

r[items.impl.syntax]
```grammar,items
Implementation -> InherentImpl | TraitImpl

InherentImpl ->
    `impl` GenericParams? Type WhereClause? `{`
        InnerAttribute*
        AssociatedItem*
    `}`

TraitImpl ->
    `unsafe`? `impl` GenericParams? `!`? TypePath `for` Type
    WhereClause?
    `{`
        InnerAttribute*
        AssociatedItem*
    `}`
```

r[items.impl.intro]
An _implementation_ is an item that associates items with an _implementing type_. Implementations are defined with the keyword `impl` and contain functions that belong to an instance of the type that is being implemented or to the type statically.

r[items.impl.kinds]
There are two types of implementations:

- inherent implementations
- [trait] implementations

r[items.impl.inherent]
## Inherent implementations

r[items.impl.inherent.intro]
An inherent implementation is defined as the sequence of the `impl` keyword, generic type declarations, a path to a nominal type, a where clause, and a bracketed set of associable items.

r[items.impl.inherent.implementing-type]
The nominal type is called the _implementing type_ and the associable items are the _associated items_ to the implementing type.

r[items.impl.inherent.associated-items]
Inherent implementations associate the contained items to the implementing type.

r[items.impl.inherent.associated-items.allowed-items]
Inherent implementations can contain [associated functions] (including [methods]) and [associated constants].

r[items.impl.inherent.type-alias]
They cannot contain associated type aliases.

r[items.impl.inherent.associated-item-path]
The [path] to an associated item is any path to the implementing type, followed by the associated item's identifier as the final path component.

r[items.impl.inherent.coherence]
A type can also have multiple inherent implementations. An implementing type must be defined within the same crate as the original type definition.

``` rust
pub mod color {
    pub struct Color(pub u8, pub u8, pub u8);

    impl Color {
        pub const WHITE: Color = Color(255, 255, 255);
    }
}

mod values {
    use super::color::Color;
    impl Color {
        pub fn red() -> Color {
            Color(255, 0, 0)
        }
    }
}

pub use self::color::Color;
fn main() {
    // Actual path to the implementing type and impl in the same module.
    color::Color::WHITE;

    // Impl blocks in different modules are still accessed through a path to the type.
    color::Color::red();

    // Re-exported paths to the implementing type also work.
    Color::red();

    // Does not work, because use in `values` is not pub.
    // values::Color::red();
}
```

r[items.impl.trait]
## Trait implementations

r[items.impl.trait.intro]
A _trait implementation_ is defined like an inherent implementation except that the optional generic type declarations are followed by a [trait], followed by the keyword `for`, followed by a path to a nominal type.

<!-- To understand this, you have to back-reference to the previous section. :( -->

r[items.impl.trait.implemented-trait]
The trait is known as the _implemented trait_. The implementing type implements the implemented trait.

r[items.impl.trait.def-requirement]
A trait implementation must define all non-default associated items declared by the implemented trait, may redefine default associated items defined by the implemented trait, and cannot define any other items.

r[items.impl.trait.associated-item-path]
The path to the associated items is `<` followed by a path to the implementing type followed by `as` followed by a path to the trait followed by `>` as a path component followed by the associated item's path component.

r[items.impl.trait.safety]
[Unsafe traits] require the trait implementation to begin with the `unsafe` keyword.

```rust
# #[derive(Copy, Clone)]
# struct Point {x: f64, y: f64};
# type Surface = i32;
# struct BoundingBox {x: f64, y: f64, width: f64, height: f64};
# trait Shape { fn draw(&self, s: Surface); fn bounding_box(&self) -> BoundingBox; }
# fn do_draw_circle(s: Surface, c: Circle) { }
struct Circle {
    radius: f64,
    center: Point,
}

impl Copy for Circle {}

impl Clone for Circle {
    fn clone(&self) -> Circle { *self }
}

impl Shape for Circle {
    fn draw(&self, s: Surface) { do_draw_circle(s, *self); }
    fn bounding_box(&self) -> BoundingBox {
        let r = self.radius;
        BoundingBox {
            x: self.center.x - r,
            y: self.center.y - r,
            width: 2.0 * r,
            height: 2.0 * r,
        }
    }
}
```

r[items.impl.trait.coherence]
### Trait implementation coherence

r[items.impl.trait.coherence.intro]
A trait implementation is considered incoherent if either the orphan rules check fails or there are overlapping implementation instances.

r[items.impl.trait.coherence.overlapping]
Two trait implementations overlap when there is a non-empty intersection of the traits the implementation is for, the implementations can be instantiated with the same type. <!-- This is probably wrong? Source: No two implementations can be instantiable with the same set of types for the input type parameters. -->

r[items.impl.trait.orphan-rule]
#### Orphan rules

r[items.impl.trait.orphan-rule.intro]
The *orphan rule* states that a trait implementation is only allowed if either the trait or at least one of the types in the implementation is defined in the current crate. It prevents conflicting trait implementations across different crates and is key to ensuring coherence.

An orphan implementation is one that implements a foreign trait for a foreign type. If these were freely allowed, two crates could implement the same trait for the same type in incompatible ways, creating a situation where adding or updating a dependency could break compilation due to conflicting implementations.

The orphan rule enables library authors to add new implementations to their traits without fear that they'll break downstream code. Without these restrictions, a library couldn't add an implementation like `impl<T: Display> MyTrait for T` without potentially conflicting with downstream implementations.

r[items.impl.trait.orphan-rule.def]
Given `impl<P1..=Pn> Trait<T1..=Tn> for T0`, an `impl` is valid only if at least one of the following is true:

- `Trait` is a [local trait]
- All of
  - At least one of the types `T0..=Tn` must be a [local type]. Let `Ti` be the first such type.
  - No [uncovered type] parameters `P1..=Pn` may appear in `T0..Ti` (excluding `Ti`)

r[items.impl.trait.uncovered-param]
Only the appearance of *uncovered* type parameters is restricted.

r[items.impl.trait.fundamental]
Note that for the purposes of coherence, [fundamental types] are special. The `T` in `Box<T>` is not considered covered, and `Box<LocalType>` is considered local.

r[items.impl.generics]
## Generic implementations

r[items.impl.generics.intro]
An implementation can take [generic parameters], which can be used in the rest of the implementation. Implementation parameters are written directly after the `impl` keyword.

```rust
# trait Seq<T> { fn dummy(&self, _: T) { } }
impl<T> Seq<T> for Vec<T> {
    /* ... */
}
impl Seq<bool> for u32 {
    /* Treat the integer as a sequence of bits */
}
```

r[items.impl.generics.use]
Generic parameters *constrain* an implementation if the parameter appears at least once in one of:

* The implemented trait, if it has one
* The implementing type
* As an [associated type] in the [bounds] of a type that contains another parameter that constrains the implementation

r[items.impl.generics.constrain]
Type and const parameters must always constrain the implementation. Lifetimes must constrain the implementation if the lifetime is used in an associated type.

Examples of constraining situations:

```rust
# trait Trait{}
# trait GenericTrait<T> {}
# trait HasAssocType { type Ty; }
# struct Struct;
# struct GenericStruct<T>(T);
# struct ConstGenericStruct<const N: usize>([(); N]);
// T constrains by being an argument to GenericTrait.
impl<T> GenericTrait<T> for i32 { /* ... */ }

// T constrains by being an argument to GenericStruct
impl<T> Trait for GenericStruct<T> { /* ... */ }

// Likewise, N constrains by being an argument to ConstGenericStruct
impl<const N: usize> Trait for ConstGenericStruct<N> { /* ... */ }

// T constrains by being in an associated type in a bound for type `U` which is
// itself a generic parameter constraining the trait.
impl<T, U> GenericTrait<U> for u32 where U: HasAssocType<Ty = T> { /* ... */ }

// Like previous, except the type is `(U, isize)`. `U` appears inside the type
// that includes `T`, and is not the type itself.
impl<T, U> GenericStruct<U> where (U, isize): HasAssocType<Ty = T> { /* ... */ }
```

Examples of non-constraining situations:

```rust,compile_fail
// The rest of these are errors, since they have type or const parameters that
// do not constrain.

// T does not constrain since it does not appear at all.
impl<T> Struct { /* ... */ }

// N does not constrain for the same reason.
impl<const N: usize> Struct { /* ... */ }

// Usage of T inside the implementation does not constrain the impl.
impl<T> Struct {
    fn uses_t(t: &T) { /* ... */ }
}

// T is used as an associated type in the bounds for U, but U does not constrain.
impl<T, U> Struct where U: HasAssocType<Ty = T> { /* ... */ }

// T is used in the bounds, but not as an associated type, so it does not constrain.
impl<T, U> GenericTrait<U> for u32 where U: GenericTrait<T> {}
```

Example of an allowed unconstraining lifetime parameter:

```rust
# struct Struct;
impl<'a> Struct {}
```

Example of a disallowed unconstraining lifetime parameter:

```rust,compile_fail
# struct Struct;
# trait HasAssocType { type Ty; }
impl<'a> HasAssocType for Struct {
    type Ty = &'a Struct;
}
```

r[items.impl.attributes]
## Attributes on implementations

Implementations may contain outer [attributes] before the `impl` keyword and inner [attributes] inside the brackets that contain the associated items. Inner attributes must come before any associated items. The attributes that have meaning here are [`cfg`], [`deprecated`], [`doc`], and [the lint check attributes].

[trait]: traits.md
[associated constants]: associated-items.md#associated-constants
[associated functions]: associated-items.md#associated-functions-and-methods
[associated type]: associated-items.md#associated-types
[attributes]: ../attributes.md
[bounds]: ../trait-bounds.md
[`cfg`]: ../conditional-compilation.md
[`deprecated`]: ../attributes/diagnostics.md#the-deprecated-attribute
[`doc`]: ../../rustdoc/the-doc-attribute.html
[generic parameters]: generics.md
[methods]: associated-items.md#methods
[path]: ../paths.md
[the lint check attributes]: ../attributes/diagnostics.md#lint-check-attributes
[Unsafe traits]: traits.md#unsafe-traits
[local trait]: ../glossary.md#local-trait
[local type]: ../glossary.md#local-type
[fundamental types]: ../glossary.md#fundamental-type-constructors
[uncovered type]: ../glossary.md#uncovered-type


---

r[items.extern]
# External blocks

r[items.extern.syntax]
```grammar,items
ExternBlock ->
    `unsafe`?[^unsafe-2024] `extern` Abi? `{`
        InnerAttribute*
        ExternalItem*
    `}`

ExternalItem ->
    OuterAttribute* (
        MacroInvocationSemi
      | Visibility? StaticItem
      | Visibility? Function
    )
```

[^unsafe-2024]: Starting with the 2024 Edition, the `unsafe` keyword is required semantically.

r[items.extern.intro]
External blocks provide _declarations_ of items that are not _defined_ in the current crate and are the basis of Rust's foreign function interface. These are akin to unchecked imports.

r[items.extern.allowed-kinds]
Two kinds of item _declarations_ are allowed in external blocks: [functions] and [statics].

r[items.extern.safety]
Calling unsafe functions or accessing unsafe statics that are declared in external blocks is only allowed in an [`unsafe` context].

r[items.extern.namespace]
The external block defines its functions and statics in the [value namespace] of the module or block where it is located.

r[items.extern.unsafe-required]
The `unsafe` keyword is semantically required to appear before the `extern` keyword on external blocks.

r[items.extern.edition2024]
> [!EDITION-2024]
> Prior to the 2024 edition, the `unsafe` keyword is optional. The `safe` and `unsafe` item qualifiers are only allowed if the external block itself is marked as `unsafe`.

r[items.extern.fn]
## Functions

r[items.extern.fn.body]
Functions within external blocks are declared in the same way as other Rust functions, with the exception that they must not have a body and are instead terminated by a semicolon.

r[items.extern.fn.param-patterns]
Patterns are not allowed in parameters, only [IDENTIFIER] or `_` may be used.

r[items.extern.fn.qualifiers]
The `safe` and `unsafe` function qualifiers are allowed, but other function qualifiers (e.g. `const`, `async`, `extern`) are not.

r[items.extern.fn.foreign-abi]
Functions within external blocks may be called by Rust code, just like functions defined in Rust. The Rust compiler automatically translates between the Rust ABI and the foreign ABI.

r[items.extern.fn.safety]
A function declared in an extern block is implicitly `unsafe` unless the `safe` function qualifier is present.

r[items.extern.fn.fn-ptr]
When coerced to a function pointer, a function declared in an extern block has type `extern "abi" for<'l1, ..., 'lm> fn(A1, ..., An) -> R`, where `'l1`, ... `'lm` are its lifetime parameters, `A1`, ..., `An` are the declared types of its parameters, and `R` is the declared return type.

r[items.extern.static]
## Statics

r[items.extern.static.intro]
Statics within external blocks are declared in the same way as [statics] outside of external blocks, except that they do not have an expression initializing their value.

r[items.extern.static.safety]
Unless a static item declared in an extern block is qualified as `safe`, it is `unsafe` to access that item, whether or not it's mutable, because there is nothing guaranteeing that the bit pattern at the static's memory is valid for the type it is declared with, since some arbitrary (e.g. C) code is in charge of initializing the static.

r[items.extern.static.mut]
Extern statics can be either immutable or mutable just like [statics] outside of external blocks.

r[items.extern.static.read-only]
An immutable static *must* be initialized before any Rust code is executed. It is not enough for the static to be initialized before Rust code reads from it. Once Rust code runs, mutating an immutable static (from inside or outside Rust) is UB, except if the mutation happens to bytes inside of an `UnsafeCell`.

r[items.extern.abi]
## ABI

r[items.extern.abi.intro]
The `extern` keyword can be followed by an optional [ABI] string. The ABI specifies the calling convention of the functions in the block. The calling convention defines a low-level interface for functions, such as how arguments are placed in registers or on the stack, how return values are passed, and who is responsible for cleaning up the stack.

> [!EXAMPLE]
> ```rust
> // Interface to the Windows API.
> unsafe extern "system" { /* ... */ }
> ```

r[items.extern.abi.default]
If the ABI string is not specified, it defaults to `"C"`.

> [!NOTE]
> The `extern` syntax without an explicit ABI is being phased out, so it's better to always write the ABI explicitly.
>
> For more details, see [Rust issue #134986](https://github.com/rust-lang/rust/issues/134986).

r[items.extern.abi.standard]
The following ABI strings are supported on all platforms:

r[items.extern.abi.rust]
* `unsafe extern "Rust"` --- The native calling convention for Rust functions and closures. This is the default when a function is declared without using [`extern fn`]. The Rust ABI offers no stability guarantees.

r[items.extern.abi.c]
* `unsafe extern "C"` --- The "C" ABI matches the default ABI chosen by the dominant C compiler for the target.

r[items.extern.abi.system]
* `unsafe extern "system"` --- This is equivalent to `extern "C"` except on Windows x86_32 where it is equivalent to `"stdcall"` for non-variadic functions, and equivalent to `"C"` for variadic functions.

  > [!NOTE]
  > As the correct underlying ABI on Windows is target-specific, it's best to use `extern "system"` when attempting to link Windows API functions that don't use an explicitly defined ABI.

r[items.extern.abi.unwind]
* `extern "C-unwind"` and `extern "system-unwind"` --- Identical to `"C"` and `"system"`, respectively, but with [different behavior][unwind-behavior] when the callee unwinds (by panicking or throwing a C++ style exception).

r[items.extern.abi.platform]
There are also some platform-specific ABI strings:

r[items.extern.abi.cdecl]
* `unsafe extern "cdecl"` --- The calling convention typically used with x86_32 C code.
  * Only available on x86_32 targets.
  * Corresponds to MSVC's `__cdecl` and GCC and clang's `__attribute__((cdecl))`.

  > [!NOTE]
  > For details, see:
  >
  > - <https://learn.microsoft.com/en-us/cpp/cpp/cdecl>
  > - <https://en.wikipedia.org/wiki/X86_calling_conventions#cdecl>

r[items.extern.abi.stdcall]
* `unsafe extern "stdcall"` --- The calling convention typically used by the [Win32 API] on x86_32.
  * Only available on x86_32 targets.
  * Corresponds to MSVC's `__stdcall` and GCC and clang's `__attribute__((stdcall))`.

  > [!NOTE]
  > For details, see:
  >
  > - <https://learn.microsoft.com/en-us/cpp/cpp/stdcall>
  > - <https://en.wikipedia.org/wiki/X86_calling_conventions#stdcall>

r[items.extern.abi.win64]
* `unsafe extern "win64"` --- The Windows x64 ABI.
  * Only available on x86_64 targets.
  * "win64" is the same as the "C" ABI on Windows x86_64 targets.
  * Corresponds to GCC and clang's `__attribute__((ms_abi))`.

  > [!NOTE]
  > For details, see:
  >
  > - <https://learn.microsoft.com/en-us/cpp/build/x64-software-conventions>
  > - <https://en.wikipedia.org/wiki/X86_calling_conventions#Microsoft_x64_calling_convention>

r[items.extern.abi.sysv64]
* `unsafe extern "sysv64"` --- The System V ABI.
  * Only available on x86_64 targets.
  * "sysv64" is the same as the "C" ABI on non-Windows x86_64 targets.
  * Corresponds to GCC and clang's `__attribute__((sysv_abi))`.

  > [!NOTE]
  > For details, see:
  >
  > - <https://wiki.osdev.org/System_V_ABI>
  > - <https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI>

r[items.extern.abi.aapcs]
* `unsafe extern "aapcs"` --- The soft-float ABI for ARM.
  * Only available on ARM32 targets.
  * "aapcs" is the same as the "C" ABI on soft-float ARM32.
  * Corresponds to clang's `__attribute__((pcs("aapcs")))`.

  > [!NOTE]
  > For details, see:
  >
  > - [Arm Procedure Call Standard](https://developer.arm.com/documentation/107656/0101/Getting-started-with-Armv8-M-based-systems/Procedure-Call-Standard-for-Arm-Architecture--AAPCS-)

r[items.extern.abi.fastcall]
* `unsafe extern "fastcall"` --- A "fast" variant of stdcall that passes some arguments in registers.
  * Only available on x86_32 targets.
  * Corresponds to MSVC's `__fastcall` and GCC and clang's `__attribute__((fastcall))`.

  > [!NOTE]
  > For details, see:
  >
  > - <https://learn.microsoft.com/en-us/cpp/cpp/fastcall>
  > - <https://en.wikipedia.org/wiki/X86_calling_conventions#Microsoft_fastcall>

r[items.extern.abi.thiscall]
* `unsafe extern "thiscall"` --- The calling convention typically used on C++ class member functions on x86_32 MSVC.
  * Only available on x86_32 targets.
  * Corresponds to MSVC's `__thiscall` and GCC and clang's `__attribute__((thiscall))`.

  > [!NOTE]
  > For details, see:
  >
  > - <https://en.wikipedia.org/wiki/X86_calling_conventions#thiscall>
  > - <https://learn.microsoft.com/en-us/cpp/cpp/thiscall>

r[items.extern.abi.efiapi]
* `unsafe extern "efiapi"` --- The ABI used for [UEFI] functions.
  * Only available on x86 and ARM targets (32bit and 64bit).

r[items.extern.abi.platform-unwind-variants]
Like `"C"` and `"system"`, most platform-specific ABI strings also have a [corresponding `-unwind` variant][unwind-behavior]; specifically, these are:

* `"aapcs-unwind"`
* `"cdecl-unwind"`
* `"fastcall-unwind"`
* `"stdcall-unwind"`
* `"sysv64-unwind"`
* `"thiscall-unwind"`
* `"win64-unwind"`

r[items.extern.variadic]
## Variadic functions

Functions within external blocks may be variadic by specifying `...` as the last argument. The variadic parameter may optionally be specified with an identifier.

```rust
unsafe extern "C" {
    unsafe fn foo(...);
    unsafe fn bar(x: i32, ...);
    unsafe fn with_name(format: *const u8, args: ...);
    // SAFETY: This function guarantees it will not access
    // variadic arguments.
    safe fn ignores_variadic_arguments(x: i32, ...);
}
```

> [!WARNING]
> The `safe` qualifier should not be used on a function in an `extern` block unless that function guarantees that it will not access the variadic arguments at all. Passing an unexpected number of arguments or arguments of unexpected type to a variadic function may lead to [undefined behavior][undefined].

r[items.extern.variadic.conventions]
Variadic parameters can only be specified within `extern` blocks with the following ABI strings or their corresponding [`-unwind` variants][items.fn.extern.unwind]:

- `"aapcs"`
- `"C"`
- `"cdecl"`
- `"efiapi"`
- `"system"`
- `"sysv64"`
- `"win64"`

r[items.extern.attributes]
## Attributes on extern blocks

r[items.extern.attributes.intro]
The following [attributes] control the behavior of external blocks.

r[items.extern.attributes.link]
### The `link` attribute

r[items.extern.attributes.link.intro]
The *`link` attribute* specifies the name of a native library that the compiler should link with for the items within an `extern` block.

r[items.extern.attributes.link.syntax]
It uses the [MetaListNameValueStr] syntax to specify its inputs. The `name` key is the name of the native library to link. The `kind` key is an optional value which specifies the kind of library with the following possible values:

r[items.extern.attributes.link.dylib]
- `dylib` --- Indicates a dynamic library. This is the default if `kind` is not specified.

r[items.extern.attributes.link.static]
- `static` --- Indicates a static library.

r[items.extern.attributes.link.framework]
- `framework` --- Indicates a macOS framework. This is only valid for macOS targets.

r[items.extern.attributes.link.raw-dylib]
- `raw-dylib` --- Indicates a dynamic library where the compiler will generate an import library to link against (see [`dylib` versus `raw-dylib`] below for details). This is only valid for Windows targets.

r[items.extern.attributes.link.name-requirement]
The `name` key must be included if `kind` is specified.

r[items.extern.attributes.link.modifiers]
The optional `modifiers` argument is a way to specify linking modifiers for the library to link.

r[items.extern.attributes.link.modifiers.syntax]
Modifiers are specified as a comma-delimited string with each modifier prefixed with either a `+` or `-` to indicate that the modifier is enabled or disabled, respectively.

r[items.extern.attributes.link.modifiers.multiple]
Specifying multiple `modifiers` arguments in a single `link` attribute, or multiple identical modifiers in the same `modifiers` argument is not currently supported. Example: `#[link(name = "mylib", kind = "static", modifiers = "+whole-archive")]`.

r[items.extern.attributes.link.wasm_import_module]
The `wasm_import_module` key may be used to specify the [WebAssembly module] name for the items within an `extern` block when importing symbols from the host environment. The default module name is `env` if `wasm_import_module` is not specified.

<!-- ignore: requires extern linking -->
```rust,ignore
#[link(name = "crypto")]
unsafe extern {
    // …
}

#[link(name = "CoreFoundation", kind = "framework")]
unsafe extern {
    // …
}

#[link(wasm_import_module = "foo")]
unsafe extern {
    // …
}
```

r[items.extern.attributes.link.empty-block]
It is valid to add the `link` attribute on an empty extern block. You can use this to satisfy the linking requirements of extern blocks elsewhere in your code (including upstream crates) instead of adding the attribute to each extern block.

r[items.extern.attributes.link.modifiers.bundle]
#### Linking modifiers: `bundle`

r[items.extern.attributes.link.modifiers.bundle.allowed-kinds]
This modifier is only compatible with the `static` linking kind. Using any other kind will result in a compiler error.

r[items.extern.attributes.link.modifiers.bundle.behavior]
When building a rlib or staticlib `+bundle` means that the native static library will be packed into the rlib or staticlib archive, and then retrieved from there during linking of the final binary.

r[items.extern.attributes.link.modifiers.bundle.behavior-negative]
When building a rlib `-bundle` means that the native static library is registered as a dependency of that rlib "by name", and object files from it are included only during linking of the final binary, the file search by that name is also performed during final linking. When building a staticlib `-bundle` means that the native static library is simply not included into the archive and some higher level build system will need to add it later during linking of the final binary.

r[items.extern.attributes.link.modifiers.bundle.no-effect]
This modifier has no effect when building other targets like executables or dynamic libraries.

r[items.extern.attributes.link.modifiers.bundle.default]
The default for this modifier is `+bundle`.

More implementation details about this modifier can be found in [`bundle` documentation for rustc].

r[items.extern.attributes.link.modifiers.whole-archive]
#### Linking modifiers: `whole-archive`

r[items.extern.attributes.link.modifiers.whole-archive.allowed-kinds]
This modifier is only compatible with the `static` linking kind. Using any other kind will result in a compiler error.

r[items.extern.attributes.link.modifiers.whole-archive.behavior]
`+whole-archive` means that the static library is linked as a whole archive without throwing any object files away.

r[items.extern.attributes.link.modifiers.whole-archive.default]
The default for this modifier is `-whole-archive`.

More implementation details about this modifier can be found in [`whole-archive` documentation for rustc].

r[items.extern.attributes.link.modifiers.verbatim]
### Linking modifiers: `verbatim`

r[items.extern.attributes.link.modifiers.verbatim.allowed-kinds]
This modifier is compatible with all linking kinds.

r[items.extern.attributes.link.modifiers.verbatim.behavior]
`+verbatim` means that rustc itself won't add any target-specified library prefixes or suffixes (like `lib` or `.a`) to the library name, and will try its best to ask for the same thing from the linker.

r[items.extern.attributes.link.modifiers.verbatim.behavior-negative]
`-verbatim` means that rustc will either add a target-specific prefix and suffix to the library name before passing it to linker, or won't prevent linker from implicitly adding it.

r[items.extern.attributes.link.modifiers.verbatim.default]
The default for this modifier is `-verbatim`.

More implementation details about this modifier can be found in [`verbatim` documentation for rustc].

r[items.extern.attributes.link.kind-raw-dylib]
#### `dylib` versus `raw-dylib`

r[items.extern.attributes.link.kind-raw-dylib.intro]
On Windows, linking against a dynamic library requires that an import library is provided to the linker: this is a special static library that declares all of the symbols exported by the dynamic library in such a way that the linker knows that they have to be dynamically loaded at runtime.

r[items.extern.attributes.link.kind-raw-dylib.import]
Specifying `kind = "dylib"` instructs the Rust compiler to link an import library based on the `name` key. The linker will then use its normal library resolution logic to find that import library. Alternatively, specifying `kind = "raw-dylib"` instructs the compiler to generate an import library during compilation and provide that to the linker instead.

r[items.extern.attributes.link.kind-raw-dylib.platform-specific]
`raw-dylib` is only supported on Windows. Using it when targeting other platforms will result in a compiler error.

r[items.extern.attributes.link.import_name_type]
#### The `import_name_type` key

r[items.extern.attributes.link.import_name_type.intro]
On x86 Windows, names of functions are "decorated" (i.e., have a specific prefix and/or suffix added) to indicate their calling convention. For example, a `stdcall` calling convention function with the name `fn1` that has no arguments would be decorated as `_fn1@0`. However, the [PE Format] does also permit names to have no prefix or be undecorated. Additionally, the MSVC and GNU toolchains use different decorations for the same calling conventions which means, by default, some Win32 functions cannot be called using the `raw-dylib` link kind via the GNU toolchain.

r[items.extern.attributes.link.import_name_type.values]
To allow for these differences, when using the `raw-dylib` link kind you may also specify the `import_name_type` key with one of the following values to change how functions are named in the generated import library:

* `decorated`: The function name will be fully-decorated using the MSVC toolchain format.
* `noprefix`: The function name will be decorated using the MSVC toolchain format, but skipping the leading `?`, `@`, or optionally `_`.
* `undecorated`: The function name will not be decorated.

r[items.extern.attributes.link.import_name_type.default]
If the `import_name_type` key is not specified, then the function name will be fully-decorated using the target toolchain's format.

r[items.extern.attributes.link.import_name_type.variables]
Variables are never decorated and so the `import_name_type` key has no effect on how they are named in the generated import library.

r[items.extern.attributes.link.import_name_type.platform-specific]
The `import_name_type` key is only supported on x86 Windows. Using it when targeting other platforms will result in a compiler error.

<!-- template:attributes -->
r[items.extern.attributes.link_name]
### The `link_name` attribute

r[items.extern.attributes.link_name.intro]
The *`link_name` [attribute][attributes]* may be applied to declarations inside an `extern` block to specify the symbol to import for the given function or static.

> [!EXAMPLE]
> ```rust
> unsafe extern "C" {
>     #[link_name = "actual_symbol_name"]
>     safe fn name_in_rust();
> }
> ```

r[items.extern.attributes.link_name.syntax]
The `link_name` attribute uses the [MetaNameValueStr] syntax.

r[items.extern.attributes.link_name.allowed-positions]
The `link_name` attribute may only be applied to a function or static item in an `extern` block.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[items.extern.attributes.link_name.duplicates]
Only the first use of `link_name` on an item has effect.

> [!NOTE]
> `rustc` lints against any use following the first with a future-compatibility warning. This may become an error in the future.

r[items.extern.attributes.link_name.link_ordinal]
The `link_name` attribute may not be used with the [`link_ordinal`] attribute.

r[items.extern.attributes.link_ordinal]
### The `link_ordinal` attribute

r[items.extern.attributes.link_ordinal.intro]
The *`link_ordinal` attribute* can be applied on declarations inside an `extern` block to indicate the numeric ordinal to use when generating the import library to link against. An ordinal is a unique number per symbol exported by a dynamic library on Windows and can be used when the library is being loaded to find that symbol rather than having to look it up by name.

> [!WARNING]
> `link_ordinal` should only be used in cases where the ordinal of the symbol is known to be stable: if the ordinal of a symbol is not explicitly set when its containing binary is built then one will be automatically assigned to it, and that assigned ordinal may change between builds of the binary.

```rust
# #[cfg(all(windows, target_arch = "x86"))]
#[link(name = "exporter", kind = "raw-dylib")]
unsafe extern "stdcall" {
    #[link_ordinal(15)]
    safe fn imported_function_stdcall(i: i32);
}
```

r[items.extern.attributes.link_ordinal.allowed-kinds]
This attribute is only used with the `raw-dylib` linking kind. Using any other kind will result in a compiler error.

r[items.extern.attributes.link_ordinal.exclusive]
Using this attribute with the `link_name` attribute will result in a compiler error.

r[items.extern.attributes.fn-parameters]
### Attributes on function parameters

Attributes on extern function parameters follow the same rules and restrictions as [regular function parameters].

[ABI]: glossary.abi
[PE Format]: https://learn.microsoft.com/windows/win32/debug/pe-format#import-name-type
[UEFI]: https://uefi.org/specifications
[WebAssembly module]: https://webassembly.github.io/spec/core/syntax/modules.html
[`bundle` documentation for rustc]: ../../rustc/command-line-arguments.html#linking-modifiers-bundle
[`dylib` versus `raw-dylib`]: #dylib-versus-raw-dylib
[`extern fn`]: items.fn.extern
[`unsafe` context]: ../unsafe-keyword.md
[`verbatim` documentation for rustc]: ../../rustc/command-line-arguments.html#linking-modifiers-verbatim
[`whole-archive` documentation for rustc]: ../../rustc/command-line-arguments.html#linking-modifiers-whole-archive
[attributes]: ../attributes.md
[functions]: functions.md
[regular function parameters]: functions.md#attributes-on-function-parameters
[statics]: static-items.md
[unwind-behavior]: functions.md#unwinding
[value namespace]: ../names/namespaces.md
[win32 api]: https://learn.microsoft.com/en-us/windows/win32/api/
[`link_ordinal`]: items.extern.attributes.link_ordinal


---

r[items.generics]
# Generic parameters

r[items.generics.syntax]
```grammar,items
GenericParams -> `<` ( GenericParam (`,` GenericParam)* `,`? )? `>`

GenericParam -> OuterAttribute* ( LifetimeParam | TypeParam | ConstParam )

LifetimeParam -> Lifetime ( `:` LifetimeBounds )?

TypeParam -> IDENTIFIER ( `:` TypeParamBounds? )? ( `=` Type )?

ConstParam ->
    `const` IDENTIFIER `:` Type
    ( `=` ( BlockExpression | IDENTIFIER | `-`?LiteralExpression ) )?
```

r[items.generics.syntax.intro]
[Functions], [type aliases], [structs], [enumerations], [unions], [traits], and [implementations] may be *parameterized* by types, constants, and lifetimes. These parameters are listed in angle <span class="parenthetical">brackets (`<...>`)</span>, usually immediately after the name of the item and before its definition. For implementations, which don't have a name, they come directly after `impl`.

r[items.generics.syntax.decl-order]
The order of generic parameters is restricted to lifetime parameters and then type and const parameters intermixed.

r[items.generics.syntax.duplicate-params]
The same parameter name may not be declared more than once in a [GenericParams] list.

Some examples of items with type, const, and lifetime parameters:

```rust
fn foo<'a, T>() {}
trait A<U> {}
struct Ref<'a, T> where T: 'a { r: &'a T }
struct InnerArray<T, const N: usize>([T; N]);
struct EitherOrderWorks<const N: bool, U>(U);
```

r[items.generics.syntax.scope]
Generic parameters are in scope within the item definition where they are declared. They are not in scope for items declared within the body of a function as described in [item declarations]. See [generic parameter scopes] for more details.

r[items.generics.builtin-generic-types]
[References], [raw pointers], [arrays], [slices], [tuples], and [function pointers] have lifetime or type parameters as well, but are not referred to with path syntax.

r[items.generics.invalid-lifetimes]
`'_` and `'static` are not valid lifetime parameter names.

r[items.generics.const]
### Const generics

r[items.generics.const.intro]
*Const generic parameters* allow items to be generic over constant values.

r[items.generics.const.namespace]
The const identifier introduces a name in the [value namespace] for the constant parameter, and all instances of the item must be instantiated with a value of the given type.

r[items.generics.const.allowed-types]
The only allowed types of const parameters are `u8`, `u16`, `u32`, `u64`, `u128`, `usize`, `i8`, `i16`, `i32`, `i64`, `i128`, `isize`, `char` and `bool`.

r[items.generics.const.use]
Const parameters can be used anywhere a [const item] can be used, with the exception that when used in a [type] or [array repeat expression], it must be standalone (as described below). That is, they are allowed in the following places:

1. As an applied const to any type which forms a part of the signature of the item in question.
2. As part of a const expression used to define an [associated const], or as a parameter to an [associated type].
3. As a value in any runtime expression in the body of any functions in the item.
4. As a parameter to any type used in the body of any functions in the item.
5. As a part of the type of any fields in the item.

```rust
// Examples where const generic parameters can be used.

// Used in the signature of the item itself.
fn foo<const N: usize>(arr: [i32; N]) {
    // Used as a type within a function body.
    let x: [i32; N];
    // Used as an expression.
    println!("{}", N * 2);
}

// Used as a field of a struct.
struct Foo<const N: usize>([i32; N]);

impl<const N: usize> Foo<N> {
    // Used as an associated constant.
    const CONST: usize = N * 4;
}

trait Trait {
    type Output;
}

impl<const N: usize> Trait for Foo<N> {
    // Used as an associated type.
    type Output = [i32; N];
}
```

```rust,compile_fail
// Examples where const generic parameters cannot be used.
fn foo<const N: usize>() {
    // Cannot use in item definitions within a function body.
    const BAD_CONST: [usize; N] = [1; N];
    static BAD_STATIC: [usize; N] = [1; N];
    fn inner(bad_arg: [usize; N]) {
        let bad_value = N * 2;
    }
    type BadAlias = [usize; N];
    struct BadStruct([usize; N]);
}
```

r[items.generics.const.standalone]
As a further restriction, const parameters may only appear as a standalone argument inside of a [type] or [array repeat expression]. In those contexts, they may only be used as a single segment [path expression], possibly inside a [block] (such as `N` or `{N}`). That is, they cannot be combined with other expressions.

```rust,compile_fail
// Examples where const parameters may not be used.

// Not allowed to combine in other expressions in types, such as the
// arithmetic expression in the return type here.
fn bad_function<const N: usize>() -> [u8; {N + 1}] {
    // Similarly not allowed for array repeat expressions.
    [1; {N + 1}]
}
```

r[items.generics.const.argument]
A const argument in a [path] specifies the const value to use for that item.

r[items.generics.const.argument.const-expr]
The argument must either be an [inferred const] or be a [const expression] of the type ascribed to the const parameter. The const expression must be a [block expression][block] (surrounded with braces) unless it is a single path segment (an [IDENTIFIER]) or a [literal] (with a possibly leading `-` token).

> [!NOTE]
> This syntactic restriction is necessary to avoid requiring infinite lookahead when parsing an expression inside of a type.

```rust
struct S<const N: i64>;
const C: i64 = 1;
fn f<const N: i64>() -> S<N> { S }

let _ = f::<1>(); // Literal.
let _ = f::<-1>(); // Negative literal.
let _ = f::<{ 1 + 2 }>(); // Constant expression.
let _ = f::<C>(); // Single segment path.
let _ = f::<{ C + 1 }>(); // Constant expression.
let _: S<1> = f::<_>(); // Inferred const.
let _: S<1> = f::<(((_)))>(); // Inferred const.
```

> [!NOTE]
> In a generic argument list, an [inferred const] is parsed as an [inferred type][InferredType] but then semantically treated as a separate kind of [const generic argument].

r[items.generics.const.inferred]
Where a const argument is expected, an `_` (optionally surrounded by any number of matching parentheses), called the *inferred const* ([path rules][paths.expr.complex-const-params], [array expression rules][expr.array.length-restriction]), can be used instead. This asks the compiler to infer the const argument if possible based on surrounding information.

```rust
fn make_buf<const N: usize>() -> [u8; N] {
    [0; _]
    //  ^ Infers `N`.
}
let _: [u8; 1024] = make_buf::<_>();
//                             ^ Infers `1024`.
```

> [!NOTE]
> An [inferred const] is not semantically an [expression][Expression] and so is not accepted within braces.
>
> ```rust,compile_fail
> fn f<const N: usize>() -> [u8; N] { [0; _] }
> let _: [_; 1] = f::<{ _ }>();
> //                    ^ ERROR `_` not allowed here
> ```

r[items.generics.const.inferred.constraint]
The inferred const cannot be used in item signatures.

```rust,compile_fail
fn f<const N: usize>(x: [u8; N]) -> [u8; _] { x }
//                                       ^ ERROR not allowed
```

r[items.generics.const.type-ambiguity]
When there is ambiguity if a generic argument could be resolved as either a type or const argument, it is always resolved as a type. Placing the argument in a block expression can force it to be interpreted as a const argument.

<!-- TODO: Rewrite the paragraph above to be in terms of namespaces, once namespaces are introduced, and it is clear which namespace each parameter lives in. -->

```rust,compile_fail
type N = u32;
struct Foo<const N: usize>;
// The following is an error, because `N` is interpreted as the type alias `N`.
fn foo<const N: usize>() -> Foo<N> { todo!() } // ERROR
// Can be fixed by wrapping in braces to force it to be interpreted as the `N`
// const parameter:
fn bar<const N: usize>() -> Foo<{ N }> { todo!() } // ok
```

r[items.generics.const.variance]
Unlike type and lifetime parameters, const parameters can be declared without being used inside of a parameterized item, with the exception of implementations as described in [generic implementations]:

```rust,compile_fail
// ok
struct Foo<const N: usize>;
enum Bar<const M: usize> { A, B }

// ERROR: unused parameter
struct Baz<T>;
struct Biz<'a>;
struct Unconstrained;
impl<const N: usize> Unconstrained {}
```

r[items.generics.const.exhaustiveness]
When resolving a trait bound obligation, the exhaustiveness of all implementations of const parameters is not considered when determining if the bound is satisfied. For example, in the following, even though all possible const values for the `bool` type are implemented, it is still an error that the trait bound is not satisfied:

```rust,compile_fail
struct Foo<const B: bool>;
trait Bar {}
impl Bar for Foo<true> {}
impl Bar for Foo<false> {}

fn needs_bar(_: impl Bar) {}
fn generic<const B: bool>() {
    let v = Foo::<B>;
    needs_bar(v); // ERROR: trait bound `Foo<B>: Bar` is not satisfied
}
```

r[items.generics.where]
## Where clauses

r[items.generics.where.syntax]
```grammar,items
WhereClause -> `where` ( WhereClauseItem `,` )* WhereClauseItem?

WhereClauseItem ->
      LifetimeWhereClauseItem
    | TypeBoundWhereClauseItem

LifetimeWhereClauseItem -> Lifetime `:` LifetimeBounds

TypeBoundWhereClauseItem -> ForLifetimes? Type `:` TypeParamBounds?
```

r[items.generics.where.intro]
*Where clauses* provide another way to specify bounds on type and lifetime parameters as well as a way to specify bounds on types that aren't type parameters.

r[items.generics.where.higher-ranked-lifetimes]
The `for` keyword can be used to introduce [higher-ranked lifetimes]. It only allows [LifetimeParam] parameters.

```rust
struct A<T>
where
    T: Iterator,            // Could use A<T: Iterator> instead
    T::Item: Copy,          // Bound on an associated type
    String: PartialEq<T>,   // Bound on `String`, using the type parameter
    i32: Default,           // Allowed, but not useful
{
    f: T,
}
```

r[items.generics.attributes]
## Attributes

Generic lifetime and type parameters allow [attributes] on them. There are no built-in attributes that do anything in this position, although custom derive attributes may give meaning to it.

This example shows using a custom derive attribute to modify the meaning of a generic parameter.

<!-- ignore: requires proc macro derive -->
```rust,ignore
// Assume that the derive for MyFlexibleClone declared `my_flexible_clone` as
// an attribute it understands.
#[derive(MyFlexibleClone)]
struct Foo<#[my_flexible_clone(unbounded)] H> {
    a: *const H
}
```

[array repeat expression]: ../expressions/array-expr.md
[arrays]: ../types/array.md
[slices]: ../types/slice.md
[associated const]: associated-items.md#associated-constants
[associated type]: associated-items.md#associated-types
[attributes]: ../attributes.md
[block]: ../expressions/block-expr.md
[const contexts]: ../const_eval.md#const-context
[const expression]: ../const_eval.md#constant-expressions
[const generic argument]: items.generics.const.argument
[const item]: constant-items.md
[enumerations]: enumerations.md
[functions]: functions.md
[function pointers]: ../types/function-pointer.md
[generic implementations]: implementations.md#generic-implementations
[generic parameter scopes]: ../names/scopes.md#generic-parameter-scopes
[higher-ranked lifetimes]: ../trait-bounds.md#higher-ranked-trait-bounds
[implementations]: implementations.md
[inferred const]: items.generics.const.inferred
[item declarations]: ../statements.md#item-declarations
[item]: ../items.md
[literal]: ../expressions/literal-expr.md
[path]: ../paths.md
[path expression]: ../expressions/path-expr.md
[raw pointers]: ../types/pointer.md#raw-pointers-const-and-mut
[references]: ../types/pointer.md#shared-references-
[structs]: structs.md
[tuples]: ../types/tuple.md
[trait object]: ../types/trait-object.md
[traits]: traits.md
[type aliases]: type-aliases.md
[type]: ../types.md
[unions]: unions.md
[value namespace]: ../names/namespaces.md


---

r[items.associated]
# Associated items

r[items.associated.syntax]
```grammar,items
AssociatedItem ->
    OuterAttribute* (
        MacroInvocationSemi
      | ( Visibility? ( TypeAlias | ConstantItem | Function ) )
    )
```

r[items.associated.intro]
*Associated Items* are the items declared in [traits] or defined in [implementations]. They are called this because they are defined on an associate type &mdash; the type in the implementation.

r[items.associated.kinds]
They are a subset of the kinds of items you can declare in a module. Specifically, there are [associated functions] (including methods), [associated types], and [associated constants].

[associated functions]: #associated-functions-and-methods
[associated types]: #associated-types
[associated constants]: #associated-constants

r[items.associated.related]
Associated items are useful when the associated item is logically related to the associating item. For example, the `is_some` method on `Option` is intrinsically related to Options, so should be associated.

r[items.associated.decl-def]
Every associated item kind comes in two varieties: definitions that contain the actual implementation and declarations that declare signatures for definitions.

r[items.associated.trait-items]
It is the declarations that make up the contract of traits and what is available on generic types.

r[items.associated.fn]
## Associated functions and methods

r[items.associated.fn.intro]
*Associated functions* are [functions] associated with a type.

r[items.associated.fn.decl]
An *associated function declaration* declares a signature for an associated function definition. It is written as a function item, except the function body is replaced with a `;`.

r[items.associated.name]
The identifier is the name of the function.

r[items.associated.same-signature]
The generics, parameter list, return type, and where clause of the associated function must be the same as the associated function declarations's.

r[items.associated.fn.def]
An *associated function definition* defines a function associated with another type. It is written the same as a [function item].

> [!NOTE]
> A common example is an associated function named `new` that returns a value of the type with which it is associated.

```rust
struct Struct {
    field: i32
}

impl Struct {
    fn new() -> Struct {
        Struct {
            field: 0i32
        }
    }
}

fn main () {
    let _struct = Struct::new();
}
```

r[items.associated.fn.qualified-self]
When the associated function is declared on a trait, the function can also be called with a [path] that is a path to the trait appended by the name of the trait. When this happens, it is substituted for `<_ as Trait>::function_name`.

```rust
trait Num {
    fn from_i32(n: i32) -> Self;
}

impl Num for f64 {
    fn from_i32(n: i32) -> f64 { n as f64 }
}

// These 4 are all equivalent in this case.
let _: f64 = Num::from_i32(42);
let _: f64 = <_ as Num>::from_i32(42);
let _: f64 = <f64 as Num>::from_i32(42);
let _: f64 = f64::from_i32(42);
```

r[items.associated.fn.method]
### Methods

r[items.associated.fn.method.intro]
Associated functions whose first parameter is named `self` are called *methods* and may be invoked using the [method call operator], for example, `x.foo()`, as well as the usual function call notation.

r[items.associated.fn.method.self-ty]
If the type of the `self` parameter is specified, it is limited to types resolving to one generated by the following grammar (where `'lt` denotes some arbitrary lifetime):

```text
P = &'lt S | &'lt mut S | Box<S> | Rc<S> | Arc<S> | Pin<P>
S = Self | P
```

The `Self` terminal in this grammar denotes a type resolving to the implementing type. This can also include the contextual type alias `Self`, other type aliases, or associated type projections resolving to the implementing type.

```rust
# use std::rc::Rc;
# use std::sync::Arc;
# use std::pin::Pin;
// Examples of methods implemented on struct `Example`.
struct Example;
type Alias = Example;
trait Trait { type Output; }
impl Trait for Example { type Output = Example; }
impl Example {
    fn by_value(self: Self) {}
    fn by_ref(self: &Self) {}
    fn by_ref_mut(self: &mut Self) {}
    fn by_box(self: Box<Self>) {}
    fn by_rc(self: Rc<Self>) {}
    fn by_arc(self: Arc<Self>) {}
    fn by_pin(self: Pin<&Self>) {}
    fn explicit_type(self: Arc<Example>) {}
    fn with_lifetime<'a>(self: &'a Self) {}
    fn nested<'a>(self: &mut &'a Arc<Rc<Box<Alias>>>) {}
    fn via_projection(self: <Example as Trait>::Output) {}
}
```

r[associated.fn.method.self-pat-shorthands]
Shorthand syntax can be used without specifying a type, which have the following equivalents:

Shorthand             | Equivalent
----------------------|-----------
`self`                | `self: Self`
`&'lifetime self`     | `self: &'lifetime Self`
`&'lifetime mut self` | `self: &'lifetime mut Self`

> [!NOTE]
> Lifetimes can be, and usually are, elided with this shorthand.

r[associated.fn.method.self-pat-mut]
If the `self` parameter is prefixed with `mut`, it becomes a mutable variable, similar to regular parameters using a `mut` [identifier pattern]. For example:

```rust
trait Changer: Sized {
    fn change(mut self) {}
    fn modify(mut self: Box<Self>) {}
}
```

As an example of methods on a trait, consider the following:

```rust
# type Surface = i32;
# type BoundingBox = i32;
trait Shape {
    fn draw(&self, surface: Surface);
    fn bounding_box(&self) -> BoundingBox;
}
```

This defines a trait with two methods. All values that have [implementations] of this trait while the trait is in scope can have their `draw` and `bounding_box` methods called.

```rust
# type Surface = i32;
# type BoundingBox = i32;
# trait Shape {
#     fn draw(&self, surface: Surface);
#     fn bounding_box(&self) -> BoundingBox;
# }
#
struct Circle {
    // ...
}

impl Shape for Circle {
    // ...
#   fn draw(&self, _: Surface) {}
#   fn bounding_box(&self) -> BoundingBox { 0i32 }
}

# impl Circle {
#     fn new() -> Circle { Circle{} }
# }
#
let circle_shape = Circle::new();
let bounding_box = circle_shape.bounding_box();
```

r[items.associated.fn.params.edition2018]
> [!EDITION-2018]
> In the 2015 edition, it is possible to declare trait methods with anonymous parameters (e.g. `fn foo(u8)`). This is deprecated and an error as of the 2018 edition. All parameters must have an argument name.

r[items.associated.fn.param-attributes]
#### Attributes on method parameters

Attributes on method parameters follow the same rules and restrictions as [regular function parameters].

r[items.associated.type]
## Associated types

r[items.associated.type.intro]
*Associated types* are [type aliases] associated with another type.

r[items.associated.type.restrictions]
Associated types cannot be defined in [inherent implementations] nor can they be given a default implementation in traits.

r[items.associated.type.decl]
An *associated type declaration* declares a signature for associated type definitions. It is written in one of the following forms, where `Assoc` is the name of the associated type, `Params` is a comma-separated list of type, lifetime or const parameters, `Bounds` is a plus-separated list of trait bounds that the associated type must meet, and `WhereBounds` is a comma-separated list of bounds that the parameters must meet:

<!-- ignore: illustrative example forms -->
```rust,ignore
type Assoc;
type Assoc: Bounds;
type Assoc<Params>;
type Assoc<Params>: Bounds;
type Assoc<Params> where WhereBounds;
type Assoc<Params>: Bounds where WhereBounds;
```

r[items.associated.type.name]
The identifier is the name of the declared type alias.

r[items.associated.type.impl-fulfillment]
The optional trait bounds must be fulfilled by the implementations of the type alias.

r[items.associated.type.sized]
There is an implicit [`Sized`] bound on associated types that can be relaxed using the special `?Sized` bound.

r[items.associated.type.def]
An *associated type definition* defines a type alias for the implementation of a trait on a type.

r[items.associated.type.def.restriction]
They are written similarly to an *associated type declaration*, but cannot contain `Bounds`, but instead must contain a `Type`:

<!-- ignore: illustrative example forms -->
```rust,ignore
type Assoc = Type;
type Assoc<Params> = Type; // the type `Type` here may reference `Params`
type Assoc<Params> = Type where WhereBounds;
type Assoc<Params> where WhereBounds = Type; // deprecated, prefer the form above
```

r[items.associated.type.alias]
If a type `Item` has an associated type `Assoc` from a trait `Trait`, then `<Item as Trait>::Assoc` is a type that is an alias of the type specified in the associated type definition.

r[items.associated.type.param]
Furthermore, if `Item` is a type parameter, then `Item::Assoc` can be used in type parameters.

r[items.associated.type.generic]
Associated types may include [generic parameters] and [where clauses]; these are often referred to as *generic associated types*, or *GATs*. If the type `Thing` has an associated type `Item` from a trait `Trait` with the generics `<'a>` , the type can be named like `<Thing as Trait>::Item<'x>`, where `'x` is some lifetime in scope. In this case, `'x` will be used wherever `'a` appears in the associated type definitions on impls.

```rust
trait AssociatedType {
    // Associated type declaration
    type Assoc;
}

struct Struct;

struct OtherStruct;

impl AssociatedType for Struct {
    // Associated type definition
    type Assoc = OtherStruct;
}

impl OtherStruct {
    fn new() -> OtherStruct {
        OtherStruct
    }
}

fn main() {
    // Usage of the associated type to refer to OtherStruct as <Struct as AssociatedType>::Assoc
    let _other_struct: OtherStruct = <Struct as AssociatedType>::Assoc::new();
}
```

An example of associated types with generics and where clauses:

```rust
struct ArrayLender<'a, T>(&'a mut [T; 16]);

trait Lend {
    // Generic associated type declaration
    type Lender<'a> where Self: 'a;
    fn lend<'a>(&'a mut self) -> Self::Lender<'a>;
}

impl<T> Lend for [T; 16] {
    // Generic associated type definition
    type Lender<'a> = ArrayLender<'a, T> where Self: 'a;

    fn lend<'a>(&'a mut self) -> Self::Lender<'a> {
        ArrayLender(self)
    }
}

fn borrow<'a, T: Lend>(array: &'a mut T) -> <T as Lend>::Lender<'a> {
    array.lend()
}

fn main() {
    let mut array = [0usize; 16];
    let lender = borrow(&mut array);
}
```

### Associated types container example

Consider the following example of a `Container` trait. Notice that the type is available for use in the method signatures:

```rust
trait Container {
    type E;
    fn empty() -> Self;
    fn insert(&mut self, elem: Self::E);
}
```

In order for a type to implement this trait, it must not only provide implementations for every method, but it must specify the type `E`. Here's an implementation of `Container` for the standard library type `Vec`:

```rust
# trait Container {
#     type E;
#     fn empty() -> Self;
#     fn insert(&mut self, elem: Self::E);
# }
impl<T> Container for Vec<T> {
    type E = T;
    fn empty() -> Vec<T> { Vec::new() }
    fn insert(&mut self, x: T) { self.push(x); }
}
```

### Relationship between `Bounds` and `WhereBounds`

In this example:

```rust
# use std::fmt::Debug;
trait Example {
    type Output<T>: Ord where T: Debug;
}
```

Given a reference to the associated type like `<X as Example>::Output<Y>`, the associated type itself must be `Ord`, and the type `Y` must be `Debug`.

r[items.associated.type.generic-where-clause]
### Required where clauses on generic associated types

r[items.associated.type.generic-where-clause.intro]
Generic associated type declarations on traits currently may require a list of where clauses, dependent on functions in the trait and how the GAT is used. These rules may be loosened in the future; updates can be found [on the generic associated types initiative repository](https://rust-lang.github.io/generic-associated-types-initiative/explainer/required_bounds.html).

r[items.associated.type.generic-where-clause.valid-fn]
In a few words, these where clauses are required in order to maximize the allowed definitions of the associated type in impls. To do this, any clauses that *can be proven to hold* on functions (using the parameters of the function or trait) where a GAT appears as an input or output must also be written on the GAT itself.

```rust
trait LendingIterator {
    type Item<'x> where Self: 'x;
    fn next<'a>(&'a mut self) -> Self::Item<'a>;
}
```

In the above, on the `next` function, we can prove that `Self: 'a`, because of the implied bounds from `&'a mut self`; therefore, we must write the equivalent bound on the GAT itself: `where Self: 'x`.

r[items.associated.type.generic-where-clause.intersection]
When there are multiple functions in a trait that use the GAT, then the *intersection* of the bounds from the different functions are used, rather than the union.

```rust
trait Check<T> {
    type Checker<'x>;
    fn create_checker<'a>(item: &'a T) -> Self::Checker<'a>;
    fn do_check(checker: Self::Checker<'_>);
}
```

In this example, no bounds are required on the `type Checker<'a>;`. While we know that `T: 'a` on `create_checker`, we do not know that on `do_check`. However, if `do_check` was commented out, then the `where T: 'x` bound would be required on `Checker`.

r[items.associated.type.generic-where-clause.forward]
The bounds on associated types also propagate required where clauses.

```rust
trait Iterable {
    type Item<'a> where Self: 'a;
    type Iterator<'a>: Iterator<Item = Self::Item<'a>> where Self: 'a;
    fn iter<'a>(&'a self) -> Self::Iterator<'a>;
}
```

Here, `where Self: 'a` is required on `Item` because of `iter`. However, `Item` is used in the bounds of `Iterator`, the `where Self: 'a` clause is also required there.

r[items.associated.type.generic-where-clause.static]
Finally, any explicit uses of `'static` on GATs in the trait do not count towards the required bounds.

```rust
trait StaticReturn {
    type Y<'a>;
    fn foo(&self) -> Self::Y<'static>;
}
```

r[items.associated.const]
## Associated constants

r[items.associated.const.intro]
*Associated constants* are [constants] associated with a type.

r[items.associated.const.decl]
An *associated constant declaration* declares a signature for associated constant definitions. It is written as `const`, then an identifier, then `:`, then a type, finished by a `;`.

r[items.associated.const.name]
The identifier is the name of the constant used in the path. The type is the type that the definition has to implement.

r[items.associated.const.def]
An *associated constant definition* defines a constant associated with a type. It is written the same as a [constant item].

r[items.associated.const.eval]
Associated constant definitions undergo [constant evaluation] only when referenced. Further, definitions that include [generic parameters] are evaluated after monomorphization.

```rust,compile_fail
struct Struct;
struct GenericStruct<const ID: i32>;

impl Struct {
    // Definition not immediately evaluated
    const PANIC: () = panic!("compile-time panic");
}

impl<const ID: i32> GenericStruct<ID> {
    // Definition not immediately evaluated
    const NON_ZERO: () = if ID == 0 {
        panic!("contradiction")
    };
}

fn main() {
    // Referencing Struct::PANIC causes compilation error
    let _ = Struct::PANIC;

    // Fine, ID is not 0
    let _ = GenericStruct::<1>::NON_ZERO;

    // Compilation error from evaluating NON_ZERO with ID=0
    let _ = GenericStruct::<0>::NON_ZERO;
}
```

### Associated constants examples

A basic example:

```rust
trait ConstantId {
    const ID: i32;
}

struct Struct;

impl ConstantId for Struct {
    const ID: i32 = 1;
}

fn main() {
    assert_eq!(1, Struct::ID);
}
```

Using default values:

```rust
trait ConstantIdDefault {
    const ID: i32 = 1;
}

struct Struct;
struct OtherStruct;

impl ConstantIdDefault for Struct {}

impl ConstantIdDefault for OtherStruct {
    const ID: i32 = 5;
}

fn main() {
    assert_eq!(1, Struct::ID);
    assert_eq!(5, OtherStruct::ID);
}
```

[`Arc<Self>`]: ../special-types-and-traits.md#arct
[`Box<Self>`]: ../special-types-and-traits.md#boxt
[`Pin<P>`]: ../special-types-and-traits.md#pinp
[`Rc<Self>`]: ../special-types-and-traits.md#rct
[`Sized`]: ../special-types-and-traits.md#sized
[traits]: traits.md
[type aliases]: type-aliases.md
[inherent implementations]: implementations.md#inherent-implementations
[identifier]: ../identifiers.md
[identifier pattern]: ../patterns.md#identifier-patterns
[implementations]: implementations.md
[type]: ../types.md#type-expressions
[constants]: constant-items.md
[constant item]: constant-items.md
[functions]: functions.md
[function item]: ../types/function-item.md
[method call operator]: ../expressions/method-call-expr.md
[path]: ../paths.md
[regular function parameters]: functions.md#attributes-on-function-parameters
[generic parameters]: generics.md
[where clauses]: generics.md#where-clauses
[constant evaluation]: ../const_eval.md
