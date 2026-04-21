r[names]
# Names

r[names.intro]
An *entity* is a language construct that can be referred to in some way within the source program, usually via a [path]. Entities include [types], [items], [generic parameters], [variable bindings], [loop labels], [lifetimes], [fields], [attributes], and [lints].

A *declaration* is a syntactical construct that can introduce a *name* to refer to an entity. Entity names are valid within a [*scope*] --- a region of source text where that name may be referenced.

Some entities are [explicitly declared](#explicitly-declared-entities) in the source code, and some are [implicitly declared](#implicitly-declared-entities) as part of the language or compiler extensions.

[*Paths*] are used to refer to an entity, possibly in another module or type.

Lifetimes and loop labels use a [dedicated syntax][lifetimes-and-loop-labels] using a leading quote.

Names are segregated into different [*namespaces*], allowing entities in different namespaces to share the same name without conflict.

[*Name resolution*] is the compile-time process of tying paths, identifiers, and labels to entity declarations.

Access to certain names may be restricted based on their [*visibility*].

r[names.explicit]
## Explicitly declared entities

r[names.explicit.list]
Entities that explicitly introduce a name in the source code are:

r[names.explicit.item-decl]
* [Items]:
    * [Module declarations]
    * [External crate declarations]
    * [Use declarations]
    * [Function declarations] and [function parameters]
    * [Type aliases]
    * [struct], [union], [enum], enum variant declarations, and their named fields
    * [Constant item declarations]
    * [Static item declarations]
    * [Trait item declarations] and their [associated items]
    * [External block items]
    * [`macro_rules` declarations] and [matcher metavariables]
    * [Implementation] associated items

r[names.explicit.expr]
* [Expressions]:
    * [Closure] parameters
    * [`while let`] pattern bindings
    * [`for`] pattern bindings
    * [`if let`] pattern bindings
    * [`match`] pattern bindings
    * [Loop labels]

r[names.explicit.generics]
* [Generic parameters]

r[names.explicit.higher-ranked-bounds]
* [Higher ranked trait bounds]

r[names.explicit.binding]
* [`let` statement] pattern bindings

r[names.explicit.macro_use]
* The [`macro_use` attribute] can introduce macro names from another crate

r[names.explicit.macro_export]
* The [`macro_export` attribute] can introduce an alias for the macro into the crate root

r[names.explicit.macro-invocation]
Additionally, [macro invocations] and [attributes] can introduce names by expanding to one of the above items.

r[names.implicit]
## Implicitly declared entities

r[names.implicit.list]
The following entities are implicitly defined by the language, or are introduced by compiler options and extensions:

r[names.implicit.primitive-types]
* [Language prelude]:
    * [Boolean type] --- `bool`
    * Textual types --- [`char`] and [`str`]
    * [Integer types] --- `i8`, `i16`, `i32`, `i64`, `i128`, `u8`, `u16`, `u32`, `u64`, `u128`
    * [Machine-dependent integer types] --- `usize` and `isize`
    * [floating-point types] --- `f32` and `f64`

r[names.implicit.builtin-attributes]
* [Built-in attributes]

r[names.implicit.prelude]
* [Standard library prelude] items, attributes, and macros

r[names.implicit.stdlib]
* [Standard library][extern-prelude] crates in the root module

r[names.implicit.extern-prelude]
* [External crates][extern-prelude] linked by the compiler

r[names.implicit.tool-attributes]
* [Tool attributes]

r[names.implicit.lints]
* [Lints] and [tool lint attributes]

r[names.implicit.derive-helpers]
* [Derive helper attributes] are valid within an item without being explicitly imported

r[names.implicit.lifetime-static]
* The [`'static`] lifetime

r[names.implicit.root]
Additionally, the crate root module does not have a name, but can be referred to with certain [path qualifiers] or aliases.

[*Name resolution*]: names/name-resolution.md
[*namespaces*]: names/namespaces.md
[*paths*]: paths.md
[*scope*]: names/scopes.md
[*visibility*]: visibility-and-privacy.md
[`'static`]: keywords.md#weak-keywords
[`char`]: types/char.md
[`for`]: expressions/loop-expr.md#iterator-loops
[`if let`]: expressions/if-expr.md#if-let-patterns
[`let` statement]: statements.md#let-statements
[`macro_export` attribute]: macros-by-example.md#the-macro_export-attribute
[`macro_rules` declarations]: macros-by-example.md
[`macro_use` attribute]: macros-by-example.md#the-macro_use-attribute
[`match`]: expressions/match-expr.md
[`str`]: types/str.md
[`while let`]: expressions/loop-expr.md#while-let-patterns
[associated items]: items/associated-items.md
[attributes]: attributes.md
[Boolean type]: types/boolean.md
[Built-in attributes]: attributes.md#built-in-attributes-index
[Closure]: expressions/closure-expr.md
[Constant item declarations]: items/constant-items.md
[Derive helper attributes]: procedural-macros.md#derive-macro-helper-attributes
[enum]: items/enumerations.md
[Expressions]: expressions.md
[extern-prelude]: names/preludes.md#extern-prelude
[External block items]: items/external-blocks.md
[External crate declarations]: items/extern-crates.md
[fields]: expressions/field-expr.md
[floating-point types]: types/numeric.md#floating-point-types
[Function declarations]: items/functions.md
[function parameters]: items/functions.md#function-parameters
[Generic parameters]: items/generics.md
[Higher ranked trait bounds]: trait-bounds.md#higher-ranked-trait-bounds
[Implementation]: items/implementations.md
[Integer types]: types/numeric.md#integer-types
[Items]: items.md
[Language prelude]: names/preludes.md#language-prelude
[lifetimes-and-loop-labels]: tokens.md#lifetimes-and-loop-labels
[lifetimes]: tokens.md#lifetimes-and-loop-labels
[Lints]: attributes/diagnostics.md#lint-check-attributes
[Loop labels]: expressions/loop-expr.md#loop-labels
[Machine-dependent integer types]: types/numeric.md#machine-dependent-integer-types
[macro invocations]: macros.md#macro-invocation
[matcher metavariables]: macros-by-example.md#metavariables
[Module declarations]: items/modules.md
[path]: paths.md
[path qualifiers]: paths.md#path-qualifiers
[Standard library prelude]: names/preludes.md#standard-library-prelude
[Static item declarations]: items/static-items.md
[struct]: items/structs.md
[Tool attributes]: attributes.md#tool-attributes
[tool lint attributes]: attributes/diagnostics.md#tool-lint-attributes
[Trait item declarations]: items/traits.md
[Type aliases]: items/type-aliases.md
[types]: types.md
[union]: items/unions.md
[Use declarations]: items/use-declarations.md
[variable bindings]: patterns.md


---

r[names.namespaces]
# Namespaces

r[names.namespaces.intro]
A *namespace* is a logical grouping of declared [names]. Names are segregated into separate namespaces based on the kind of entity the name refers to. Namespaces allow the occurrence of a name in one namespace to not conflict with the same name in another namespace.

There are several different namespaces that each contain different kinds of entities. The use of a name will look for the declaration of that name in different namespaces, based on the context, as described in the [name resolution] chapter.

r[names.namespaces.kinds]
The following is a list of namespaces, with their corresponding entities:

* Type Namespace
    * [Module declarations]
    * [External crate declarations]
    * [External crate prelude] items
    * [Struct], [union], [enum], enum variant declarations
    * [Trait item declarations]
    * [Type aliases]
    * [Associated type declarations]
    * Built-in types: [boolean], [numeric], [`char`], and [`str`]
    * [Generic type parameters]
    * [`Self` type]
    * [Tool attribute modules]
* Value Namespace
    * [Function declarations]
    * [Constant item declarations]
    * [Static item declarations]
    * [Struct constructors]
    * [Enum variant constructors]
    * [`Self` constructors]
    * [Generic const parameters]
    * [Associated const declarations]
    * [Associated function declarations]
    * Local bindings --- [`let`], [`if let`], [`while let`], [`for`], [`match`] arms, [function parameters], [closure parameters]
    * Captured [closure] variables
* Macro Namespace
    * [`macro_rules` declarations]
    * [Built-in attributes]
    * [Tool attributes]
    * [Function-like procedural macros]
    * [Derive macros]
    * [Derive macro helpers]
    * [Attribute macros]
* Lifetime Namespace
    * [Generic lifetime parameters]
* Label Namespace
    * [Loop labels]
    * [Block labels]

An example of how overlapping names in different namespaces can be used unambiguously:

```rust
// Foo introduces a type in the type namespace and a constructor in the value
// namespace.
struct Foo(u32);

// The `Foo` macro is declared in the macro namespace.
macro_rules! Foo {
    () => {};
}

// `Foo` in the `f` parameter type refers to `Foo` in the type namespace.
// `'Foo` introduces a new lifetime in the lifetime namespace.
fn example<'Foo>(f: Foo) {
    // `Foo` refers to the `Foo` constructor in the value namespace.
    let ctor = Foo;
    // `Foo` refers to the `Foo` macro in the macro namespace.
    Foo!{}
    // `'Foo` introduces a label in the label namespace.
    'Foo: loop {
        // `'Foo` refers to the `'Foo` lifetime parameter, and `Foo`
        // refers to the type namespace.
        let x: &'Foo Foo;
        // `'Foo` refers to the label.
        break 'Foo;
    }
}
```

r[names.namespaces.without]
## Named entities without a namespace

The following entities have explicit names, but the names are not a part of any specific namespace.

### Fields

r[names.namespaces.without.fields]
Even though struct, enum, and union fields are named, the named fields do not live in an explicit namespace. They can only be accessed via a [field expression], which only inspects the field names of the specific type being accessed.

### Use declarations

r[names.namespaces.without.use]
A [use declaration] has named aliases that it imports into scope, but the `use` item itself does not belong to a specific namespace. Instead, it can introduce aliases into multiple namespaces, depending on the item kind being imported.

r[names.namespaces.sub-namespaces]
## Sub-namespaces

r[names.namespaces.sub-namespaces.intro]
The macro namespace is split into two sub-namespaces: one for [bang-style macros] and one for [attributes]. When an attribute is resolved, any bang-style macros in scope will be ignored. And conversely resolving a bang-style macro will ignore attribute macros in scope. This prevents one style from shadowing another.

For example, the [`cfg` attribute] and the [`cfg` macro] are two different entities with the same name in the macro namespace, but they can still be used in their respective context.

<!-- ignore: requires external crates -->
> [!NOTE]
> `use` imports still cannot create duplicate bindings of the same name in a module or block, regardless of sub-namespace.
>
> ```rust,ignore
> #[macro_export]
> macro_rules! mymac {
>     () => {};
> }
>
> use myattr::mymac; // error[E0252]: the name `mymac` is defined multiple times.
> ```

[`cfg` attribute]: ../conditional-compilation.md#the-cfg-attribute
[`cfg` macro]: ../conditional-compilation.md#the-cfg-macro
[`char`]: ../types/char.md
[`for`]: ../expressions/loop-expr.md#iterator-loops
[`if let`]: ../expressions/if-expr.md#if-let-patterns
[`let`]: ../statements.md#let-statements
[`macro_rules` declarations]: ../macros-by-example.md
[`match`]: ../expressions/match-expr.md
[`Self` constructors]: ../paths.md#self-1
[`Self` type]: ../paths.md#self-1
[`str`]: ../types/str.md
[`use` import]: ../items/use-declarations.md
[`while let`]: ../expressions/loop-expr.md#while-let-patterns
[Associated const declarations]: ../items/associated-items.md#associated-constants
[Associated function declarations]: ../items/associated-items.md#associated-functions-and-methods
[Associated type declarations]: ../items/associated-items.md#associated-types
[Attribute macros]: ../procedural-macros.md#the-proc_macro_attribute-attribute
[attributes]: ../attributes.md
[bang-style macros]: ../macros.md
[Block labels]: expr.loop.block-labels
[boolean]: ../types/boolean.md
[Built-in attributes]: ../attributes.md#built-in-attributes-index
[closure parameters]: ../expressions/closure-expr.md
[closure]: ../expressions/closure-expr.md
[Constant item declarations]: ../items/constant-items.md
[Derive macro helpers]: ../procedural-macros.md#derive-macro-helper-attributes
[Derive macros]: macro.proc.derive
[entity]: ../glossary.md#entity
[Enum variant constructors]: ../items/enumerations.md
[enum]: ../items/enumerations.md
[External crate declarations]: ../items/extern-crates.md
[External crate prelude]: preludes.md#extern-prelude
[field expression]: ../expressions/field-expr.md
[Function declarations]: ../items/functions.md
[function parameters]: ../items/functions.md#function-parameters
[Function-like procedural macros]: ../procedural-macros.md#the-proc_macro-attribute
[Generic const parameters]: ../items/generics.md#const-generics
[Generic lifetime parameters]: ../items/generics.md
[Generic type parameters]: ../items/generics.md
[Loop labels]: ../expressions/loop-expr.md#loop-labels
[Module declarations]: ../items/modules.md
[name resolution]: name-resolution.md
[names]: ../names.md
[numeric]: ../types/numeric.md
[Static item declarations]: ../items/static-items.md
[Struct constructors]: ../items/structs.md
[Struct]: ../items/structs.md
[Tool attribute modules]: ../attributes.md#tool-attributes
[Tool attributes]: ../attributes.md#tool-attributes
[Trait item declarations]: ../items/traits.md
[Type aliases]: ../items/type-aliases.md
[union]: ../items/unions.md
[use declaration]: ../items/use-declarations.md


---

r[names.scopes]
# Scopes

r[names.scopes.intro]
A *scope* is the region of source text where a named [entity] may be referenced with that name. The following sections provide details on the scoping rules and behavior, which depend on the kind of entity and where it is declared. The process of how names are resolved to entities is described in the [name resolution] chapter. More information on "drop scopes" used for the purpose of running destructors may be found in the [destructors] chapter.

r[names.scopes.items]
## Item scopes

r[names.scopes.items.module]
The name of an [item][items] declared directly in a [module] has a scope that extends from the start of the module to the end of the module. These items are also members of the module and can be referred to with a [path] leading from their module.

r[names.scopes.items.statement]
The name of an item declared as a [statement] has a scope that extends from the start of the block the item statement is in until the end of the block.

r[names.scopes.items.duplicate]
It is an error to introduce an item with a duplicate name of another item in the same [namespace] within the same module or block. [Asterisk glob imports] have special behavior for dealing with duplicate names and shadowing, see the linked chapter for more details.

r[names.scopes.items.shadow-prelude]
Items in a module may shadow items in a [prelude](#prelude-scopes).

r[names.scopes.items.nested-modules]
Item names from outer modules are not in scope within a nested module. A [path] may be used to refer to an item in another module.

r[names.scopes.associated-items]
### Associated item scopes

r[names.scopes.associated-items.scope]
[Associated items] are not scoped and can only be referred to by using a [path] leading from the type or trait they are associated with. [Methods] can also be referred to via [call expressions].

r[names.scopes.associated-items.duplicate]
Similar to items within a module or block,  it is an error to introduce an item within a trait or implementation that is a duplicate of another item in the trait or impl in the same namespace.

r[names.scopes.pattern-bindings]
## Pattern binding scopes

The scope of a local variable [pattern] binding depends on where it is used:

r[names.scopes.pattern-bindings.let]
* [`let` statement] bindings range from just after the `let` statement until the end of the block where it is declared.
r[names.scopes.pattern-bindings.parameter]
* [Function parameter] bindings are within the body of the function.
r[names.scopes.pattern-bindings.closure]
* [Closure parameter] bindings are within the closure body.
r[names.scopes.pattern-bindings.loop]
* [`for`] bindings are within the loop body.
r[names.scopes.pattern-bindings.let-chains]
* [`if let`] and [`while let`] bindings are valid in the following conditions as well as the consequent block.
r[names.scopes.pattern-bindings.match-arm]
* [`match` arms] bindings are within the [match guard] and the match arm expression.
r[names.scopes.pattern-bindings.match-guard-let]
* [`match` guard `let`] bindings are valid in the following guard conditions and the match arm expression.

r[names.scopes.pattern-bindings.items]
Local variable scopes do not extend into item declarations.
<!-- Not entirely, see https://github.com/rust-lang/rust/issues/33118 -->

### Pattern binding shadowing

r[names.scopes.pattern-bindings.shadow]
Pattern bindings are allowed to shadow any name in scope with the following exceptions which are an error:

* [Const generic parameters]
* [Static items]
* [Const items]
* Constructors for [structs] and [enums]

The following example illustrates how local bindings can shadow item declarations:

```rust
fn shadow_example() {
    // Since there are no local variables in scope yet, this resolves to the function.
    foo(); // prints `function`
    let foo = || println!("closure");
    fn foo() { println!("function"); }
    // This resolves to the local closure since it shadows the item.
    foo(); // prints `closure`
}
```

r[names.scopes.generic-parameters]
## Generic parameter scopes

r[names.scopes.generic-parameters.param-list]
Generic parameters are declared in a [GenericParams] list. The scope of a generic parameter is within the item it is declared on.

r[names.scopes.generic-parameters.order-independent]
All parameters are in scope within the generic parameter list regardless of the order they are declared. The following shows some examples where a parameter may be referenced before it is declared:

```rust
// The 'b bound is referenced before it is declared.
fn params_scope<'a: 'b, 'b>() {}

# trait SomeTrait<const Z: usize> {}
// The const N is referenced in the trait bound before it is declared.
fn f<T: SomeTrait<N>, const N: usize>() {}
```

r[names.scopes.generic-parameters.bounds]
Generic parameters are also in scope for type bounds and where clauses, for example:

```rust
# trait SomeTrait<'a, T> {}
// The <'a, U> for `SomeTrait` refer to the 'a and U parameters of `bounds_scope`.
fn bounds_scope<'a, T: SomeTrait<'a, U>, U>() {}

fn where_scope<'a, T, U>()
    where T: SomeTrait<'a, U>
{}
```

r[names.scopes.generic-parameters.inner-items]
It is an error for [items] declared inside a function to refer to a generic parameter from their outer scope.

```rust,compile_fail
fn example<T>() {
    fn inner(x: T) {} // ERROR: can't use generic parameters from outer function
}
```

### Generic parameter shadowing

r[names.scopes.generic-parameters.shadow]
It is an error to shadow a generic parameter with the exception that items declared within functions are allowed to shadow generic parameter names from the function.

```rust
fn example<'a, T, const N: usize>() {
    // Items within functions are allowed to shadow generic parameter in scope.
    fn inner_lifetime<'a>() {} // OK
    fn inner_type<T>() {} // OK
    fn inner_const<const N: usize>() {} // OK
}
```

```rust,compile_fail
trait SomeTrait<'a, T, const N: usize> {
    fn example_lifetime<'a>() {} // ERROR: 'a is already in use
    fn example_type<T>() {} // ERROR: T is already in use
    fn example_const<const N: usize>() {} // ERROR: N is already in use
    fn example_mixed<const T: usize>() {} // ERROR: T is already in use
}
```

r[names.scopes.lifetimes]
### Lifetime scopes

Lifetime parameters are declared in a [GenericParams] list and [higher-ranked trait bounds][hrtb].

r[names.scopes.lifetimes.special]
The `'static` lifetime and [placeholder lifetime] `'_` have a special meaning and cannot be declared as a parameter.

#### Lifetime generic parameter scopes

r[names.scopes.lifetimes.generic]
[Constant] and [static] items and [const contexts] only ever allow `'static` lifetime references, so no other lifetime may be in scope within them. [Associated consts] do allow referring to lifetimes declared in their trait or implementation.

#### Higher-ranked trait bound scopes

r[names.scopes.lifetimes.higher-ranked]
The scope of a lifetime parameter declared as a [higher-ranked trait bound][hrtb] depends on the scenario where it is used.

* As a [TypeBoundWhereClauseItem] the declared lifetimes are in scope in the type and the type bounds.
* As a [TraitBound] the declared lifetimes are in scope within the bound type path.
* As a [BareFunctionType] the declared lifetimes are in scope within the function parameters and return type.

```rust
# trait Trait<'a>{}

fn where_clause<T>()
    // 'a is in scope in both the type and the type bounds.
    where for <'a> &'a T: Trait<'a>
{}

fn bound<T>()
    // 'a is in scope within the bound.
    where T: for <'a> Trait<'a>
{}

# struct Example<'a> {
#     field: &'a u32
# }

// 'a is in scope in both the parameters and return type.
type FnExample = for<'a> fn(x: Example<'a>) -> Example<'a>;
```

#### Impl trait restrictions

r[names.scopes.lifetimes.impl-trait]
[Impl trait] types can only reference lifetimes declared on a function or implementation.

<!-- not able to demonstrate the scope error because the compiler panics
     https://github.com/rust-lang/rust/issues/67830
-->
```rust
# trait Trait1 {
#     type Item;
# }
# trait Trait2<'a> {}
#
# struct Example;
#
# impl Trait1 for Example {
#     type Item = Element;
# }
#
# struct Element;
# impl<'a> Trait2<'a> for Element {}
#
// The `impl Trait2` here is not allowed to refer to 'b but it is allowed to
// refer to 'a.
fn foo<'a>() -> impl for<'b> Trait1<Item = impl Trait2<'a> + use<'a>> {
    // ...
#    Example
}
```

r[names.scopes.loop-label]
## Loop label scopes

r[names.scopes.loop-label.scope]
[Loop labels] may be declared by a [loop expression]. The scope of a loop label is from the point it is declared till the end of the loop expression. The scope does not extend into [items], [closures], [async blocks], [const arguments], [const contexts], and the iterator expression of the defining [`for` loop].

```rust
'a: for n in 0..3 {
    if n % 2 == 0 {
        break 'a;
    }
    fn inner() {
        // Using 'a here would be an error.
        // break 'a;
    }
}

// The label is in scope for the expression of `while` loops.
'a: while break 'a {}         // Loop does not run.
'a: while let _ = break 'a {} // Loop does not run.

// The label is not in scope in the defining `for` loop:
'a: for outer in 0..5 {
    // This will break the outer loop, skipping the inner loop and stopping
    // the outer loop.
    'a: for inner in { break 'a; 0..1 } {
        println!("{}", inner); // This does not run.
    }
    println!("{}", outer); // This does not run, either.
}

```

r[names.scopes.loop-label.shadow]
Loop labels may shadow labels of the same name in outer scopes. References to a label refer to the closest definition.

```rust
// Loop label shadowing example.
'a: for outer in 0..5 {
    'a: for inner in 0..5 {
        // This terminates the inner loop, but the outer loop continues to run.
        break 'a;
    }
}
```

r[names.scopes.prelude]
## Prelude scopes

r[names.scopes.prelude.intro]
[Preludes] bring entities into scope of every module. The entities are not members of the module, but are implicitly queried during [name resolution].

r[names.scopes.prelude.shadow]
The prelude names may be shadowed by declarations in a module.

r[names.scopes.prelude.layers]
The preludes are layered such that one shadows another if they contain entities of the same name. The order that preludes may shadow other preludes is the following where earlier entries may shadow later ones:

1. [Extern prelude]
2. [Tool prelude]
3. [`macro_use` prelude]
4. [Standard library prelude]
5. [Language prelude]

r[names.scopes.macro_rules]
## `macro_rules` scopes

The scope of `macro_rules` macros is described in the [Macros By Example] chapter. The behavior depends on the use of the [`macro_use`] and [`macro_export`] attributes.

r[names.scopes.derive]
## Derive macro helper attributes

r[names.scopes.derive.scope]
[Derive macro helper attributes] are in scope in the item where their corresponding [`derive` attribute] is specified. The scope extends from just after the `derive` attribute to the end of the item. <!-- Note: Not strictly true, see https://github.com/rust-lang/rust/issues/79202, but this is the intention. -->

r[names.scopes.derive.shadow]
Helper attributes shadow other attributes of the same name in scope.

r[names.scopes.self]
## `Self` scope

r[names.scopes.self.intro]
Although [`Self`] is a keyword with special meaning, it interacts with name resolution in a way similar to normal names.

r[names.scopes.self.def-scope]
The implicit `Self` type in the definition of a [struct], [enum], [union], [trait], or [implementation] is treated similarly to a [generic parameter](#generic-parameter-scopes), and is in scope in the same way as a generic type parameter.

r[names.scopes.self.impl-scope]
The implicit `Self` constructor in the value [namespace] of an [implementation] is in scope within the body of the implementation (the implementation's [associated items]).

```rust
// Self type within struct definition.
struct Recursive {
    f1: Option<Box<Self>>
}

// Self type within generic parameters.
struct SelfGeneric<T: Into<Self>>(T);

// Self value constructor within an implementation.
struct ImplExample();
impl ImplExample {
    fn example() -> Self { // Self type
        Self() // Self value constructor
    }
}
```

[`derive` attribute]: ../attributes/derive.md
[`for` loop]: ../expressions/loop-expr.md#iterator-loops
[`for`]: ../expressions/loop-expr.md#iterator-loops
[`if let`]: ../expressions/if-expr.md#if-let-patterns
[`while let`]: ../expressions/loop-expr.md#while-let-patterns
[`let` statement]: ../statements.md#let-statements
[`macro_export`]: ../macros-by-example.md#the-macro_export-attribute
[`macro_use` prelude]: preludes.md#macro_use-prelude
[`macro_use`]: ../macros-by-example.md#the-macro_use-attribute
[`match` arms]: ../expressions/match-expr.md
[`match` guard `let`]: expr.match.guard.let
[`Self`]: ../paths.md#self-1
[Associated consts]: ../items/associated-items.md#associated-constants
[associated items]: ../items/associated-items.md
[Asterisk glob imports]: ../items/use-declarations.md
[async blocks]: ../expressions/block-expr.md#async-blocks
[call expressions]: ../expressions/call-expr.md
[Closure parameter]: ../expressions/closure-expr.md
[closures]: ../expressions/closure-expr.md
[const arguments]: ../items/generics.md#const-generics
[const contexts]: ../const_eval.md#const-context
[Const generic parameters]: ../items/generics.md#const-generics
[Const items]: ../items/constant-items.md
[Constant]: ../items/constant-items.md
[Derive macro helper attributes]: ../procedural-macros.md#derive-macro-helper-attributes
[destructors]: ../destructors.md
[entity]: ../names.md
[enum]: ../items/enumerations.mdr
[enums]: ../items/enumerations.md
[Extern prelude]: preludes.md#extern-prelude
[Function parameter]: ../items/functions.md#function-parameters
[hrtb]: ../trait-bounds.md#higher-ranked-trait-bounds
[Impl trait]: ../types/impl-trait.md
[implementation]: ../items/implementations.md
[items]: ../items.md
[Language prelude]: preludes.md#language-prelude
[loop expression]: ../expressions/loop-expr.md
[Loop labels]: ../expressions/loop-expr.md#loop-labels
[Macros By Example]: ../macros-by-example.md
[match guard]: ../expressions/match-expr.md#match-guards
[methods]: ../items/associated-items.md#methods
[module]: ../items/modules.md
[name resolution]: name-resolution.md
[namespace]: namespaces.md
[path]: ../paths.md
[pattern]: ../patterns.md
[placeholder lifetime]: ../lifetime-elision.md
[preludes]: preludes.md
[Standard library prelude]: preludes.md#standard-library-prelude
[statement]: ../statements.md
[Static items]: ../items/static-items.md
[static]: ../items/static-items.md
[struct]: ../items/structs.md
[structs]: ../items/structs.md
[Tool prelude]: preludes.md#tool-prelude
[trait]: ../items/traits.md
[union]: ../items/unions.md


---

r[names.preludes]
# Preludes

r[names.preludes.intro]
A *prelude* is a collection of names that are automatically brought into scope of every module in a crate.

These prelude names are not part of the module itself: they are implicitly queried during [name resolution]. For example, even though something like [`Box`] is in scope in every module, you cannot refer to it as `self::Box` because it is not a member of the current module.

r[names.preludes.kinds]
There are several different preludes:

- [Standard library prelude]
- [Extern prelude]
- [Language prelude]
- [`macro_use` prelude]
- [Tool prelude]

r[names.preludes.std]
## Standard library prelude

r[names.preludes.std.intro]
Each crate has a standard library prelude, which consists of the names from a single standard library module.

r[names.preludes.std.module]
The module used depends on the crate's edition, and on whether the [`no_std` attribute] is applied to the crate:

Edition | `no_std` not applied        | `no_std` applied
--------| --------------------------- | ----------------------------
2015    | [`std::prelude::rust_2015`] | [`core::prelude::rust_2015`]
2018    | [`std::prelude::rust_2018`] | [`core::prelude::rust_2018`]
2021    | [`std::prelude::rust_2021`] | [`core::prelude::rust_2021`]
2024    | [`std::prelude::rust_2024`] | [`core::prelude::rust_2024`]

> [!NOTE]
> [`std::prelude::rust_2015`] and [`std::prelude::rust_2018`] have the same contents as [`std::prelude::v1`].
>
> [`core::prelude::rust_2015`] and [`core::prelude::rust_2018`] have the same contents as [`core::prelude::v1`].

> [!NOTE]
> When one of [`core::panic!`] or [`std::panic!`] is brought into scope due to the [standard library prelude], and a user-written [glob import] brings the other into scope, `rustc` currently allows use of `panic!`, even though it is ambiguous. The user-written glob import takes precedence to resolve this ambiguity.
>
> For details, see [names.resolution.expansion.imports.ambiguity.panic-hack].

r[names.preludes.extern]
## Extern prelude

r[names.preludes.extern.intro]
External crates imported with [`extern crate`] in the root module or provided to the compiler (as with the `--extern` flag with `rustc`) are added to the *extern prelude*. If imported with an alias such as `extern crate orig_name as new_name`, then the symbol `new_name` is instead added to the prelude.

r[names.preludes.extern.core]
The [`core`] crate is always added to the extern prelude.

r[names.preludes.extern.std]
The [`std`] crate is added as long as the [`no_std` attribute] is not specified in the crate root.

r[names.preludes.extern.edition2018]
> [!EDITION-2018]
> In the 2015 edition, crates in the extern prelude cannot be referenced via [use declarations], so it is generally standard practice to include `extern crate` declarations to bring them into scope.
>
> Beginning in the 2018 edition, [use declarations] can reference crates in the extern prelude, so it is considered unidiomatic to use `extern crate`.

> [!NOTE]
> Additional crates that ship with `rustc`, such as [`alloc`], and [`test`](mod@test), are not automatically included with the `--extern` flag when using Cargo. They must be brought into scope with an `extern crate` declaration, even in the 2018 edition.
>
> ```rust
> extern crate alloc;
> use alloc::rc::Rc;
> ```
>
> Cargo does bring in `proc_macro` to the extern prelude for proc-macro crates only.

<!--
See https://github.com/rust-lang/rust/issues/57288 for more about the alloc/test limitation.
-->

<!-- template:attributes -->
r[names.preludes.extern.no_std]
### The `no_std` attribute

r[names.preludes.extern.no_std.intro]
The *`no_std` [attribute][attributes]* causes the [`std`] crate to not be linked automatically and the [standard library prelude] to instead use the `core` prelude.

> [!EXAMPLE]
> <!-- ignore: test infrastructure can't handle no_std -->
> ```rust,ignore
> #![no_std]
> ```

> [!NOTE]
> Using `no_std` is useful when either the crate is targeting a platform that does not support the standard library or is purposefully not using the capabilities of the standard library. Those capabilities are mainly dynamic memory allocation (e.g. `Box` and `Vec`) and file and network capabilities (e.g. `std::fs` and `std::io`).

> [!WARNING]
> Using `no_std` does not prevent the standard library from being linked. It is still valid to write `extern crate std` in the crate or in one of its dependencies; this will cause the compiler to link the `std` crate into the program.

r[names.preludes.extern.no_std.syntax]
The `no_std` attribute uses the [MetaWord] syntax.

r[names.preludes.extern.no_std.allowed-positions]
The `no_std` attribute may only be applied to the crate root.

r[names.preludes.extern.no_std.duplicates]
The `no_std` attribute may be used any number of times on a form.

> [!NOTE]
> `rustc` lints against any use following the first.

r[names.preludes.extern.no_std.module]
The `no_std` attribute changes the [standard library prelude] to use the `core` prelude instead of the `std` prelude.

r[names.preludes.extern.no_std.edition2018]
> [!EDITION-2018]
> Before the 2018 edition, `std` is injected into the crate root by default. If `no_std` is specified, `core` is injected instead. Starting with the 2018 edition, regardless of `no_std` being specified, neither is injected into the crate root.

r[names.preludes.lang]
## Language prelude

r[names.preludes.lang.intro]
The language prelude includes names of types and attributes that are built-in to the language. The language prelude is always in scope.

r[names.preludes.lang.entities]
It includes the following:

* [Type namespace]
    * [Boolean type] --- `bool`
    * [`char`]
    * [`str`]
    * [Integer types] --- `i8`, `i16`, `i32`, `i64`, `i128`, `u8`, `u16`, `u32`, `u64`, `u128`
    * [Machine-dependent integer types] --- `usize` and `isize`
    * [floating-point types] --- `f32` and `f64`
* [Macro namespace]
    * [Built-in attributes]
    * [Built-in derive macros][attributes.derive.built-in]

r[names.preludes.macro_use]
## `macro_use` prelude

r[names.preludes.macro_use.intro]
The `macro_use` prelude includes macros from external crates that were imported by the [`macro_use` attribute] applied to an [`extern crate`].

r[names.preludes.tool]
## Tool prelude

r[names.preludes.tool.intro]
The tool prelude includes tool names for external tools in the [type namespace]. See the [tool attributes] section for more details.

<!-- template:attributes -->
r[names.preludes.no_implicit_prelude]
## The `no_implicit_prelude` attribute

r[names.preludes.no_implicit_prelude.intro]
The *`no_implicit_prelude` [attribute]* is used to prevent implicit preludes from being brought into scope.

> [!EXAMPLE]
> ```rust
> // The attribute can be applied to the crate root to affect
> // all modules.
> #![no_implicit_prelude]
>
> // Or it can be applied to a module to only affect that module
> // and its descendants.
> #[no_implicit_prelude]
> mod example {
>     // ...
> }
> ```

r[names.preludes.no_implicit_prelude.syntax]
The `no_implicit_prelude` attribute uses the [MetaWord] syntax.

r[names.preludes.no_implicit_prelude.allowed-positions]
The `no_implicit_prelude` attribute may only be applied to the crate or to a module.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[names.preludes.no_implicit_prelude.duplicates]
The `no_implicit_prelude` attribute may be used any number of times on a form.

> [!NOTE]
> `rustc` lints against any use following the first.

r[names.preludes.no_implicit_prelude.excluded-preludes]
The `no_implicit_prelude` attribute prevents the [standard library prelude], [extern prelude], [`macro_use` prelude], and the [tool prelude] from being brought into scope for the module and its descendants.

r[names.preludes.no_implicit_prelude.implicitly-imported-macros]
> [!NOTE]
> Despite `#![no_implicit_prelude]`, `rustc` currently brings certain macros implicitly into scope. Those macros are:
>
> - [`assert!`]
> - [`cfg!`]
> - [`cfg_select!`]
> - [`column!`]
> - [`compile_error!`]
> - [`concat!`]
> - [`concat_bytes!`]
> - [`env!`]
> - [`file!`]
> - [`format_args!`]
> - [`include!`]
> - [`include_bytes!`]
> - [`include_str!`]
> - [`line!`]
> - [`module_path!`]
> - [`option_env!`]
> - [`panic!`]
> - [`stringify!`]
> - [`unreachable!`]
>
> E.g., this works:
>
> ```rust
> #![no_implicit_prelude]
> fn main() { assert!(true); }
> ```
>
> Don't rely on this behavior; it may be removed in the future. Always bring the items you need into scope explicitly when using `#![no_implicit_prelude]`.
>
> For details, see [Rust PR #62086](https://github.com/rust-lang/rust/pull/62086) and [Rust PR #139493](https://github.com/rust-lang/rust/pull/139493).

r[names.preludes.no_implicit_prelude.lang]
The `no_implicit_prelude` attribute does not affect the [language prelude].

r[names.preludes.no_implicit_prelude.edition2018]
> [!EDITION-2018]
> In the 2015 edition, the `no_implicit_prelude` attribute does not affect the [`macro_use` prelude], and all macros exported from the standard library are still included in the `macro_use` prelude. Starting in the 2018 edition, the attribute does remove the `macro_use` prelude.

[`char`]: ../types/char.md
[`extern crate`]: ../items/extern-crates.md
[`macro_use` attribute]: ../macros-by-example.md#the-macro_use-attribute
[`macro_use` prelude]: #macro_use-prelude
[`no_std` attribute]: #the-no_std-attribute
[`str`]: ../types/str.md
[attribute]: ../attributes.md
[Boolean type]: ../types/boolean.md
[Built-in attributes]: ../attributes.md#built-in-attributes-index
[extern prelude]: #extern-prelude
[floating-point types]: ../types/numeric.md#floating-point-types
[glob import]: items.use.glob
[Integer types]: ../types/numeric.md#integer-types
[Language prelude]: #language-prelude
[Machine-dependent integer types]: ../types/numeric.md#machine-dependent-integer-types
[Macro namespace]: namespaces.md
[name resolution]: name-resolution.md
[standard library prelude]: names.preludes.std
[tool attributes]: ../attributes.md#tool-attributes
[Tool prelude]: #tool-prelude
[Type namespace]: namespaces.md
[use declarations]: ../items/use-declarations.md


---

r[paths]
# Paths

r[paths.intro]
A *path* is a sequence of one or more path segments separated by `::` tokens. Paths are used to refer to [items], values, [types], [macros], and [attributes].

Two examples of simple paths consisting of only identifier segments:

<!-- ignore: syntax fragment -->
```rust,ignore
x;
x::y::z;
```

## Types of paths

r[paths.simple]
### Simple paths

r[paths.simple.syntax]
```grammar,paths
SimplePath ->
    `::`? SimplePathSegment (`::` SimplePathSegment)*

SimplePathSegment ->
    IDENTIFIER | `super` | `self` | `crate` | `$crate`
```

r[paths.simple.intro]
Simple paths are used in [visibility] markers, [attributes], [macros][mbe], and [`use`] items. For example:

```rust
use std::io::{self, Write};
mod m {
    #[clippy::cyclomatic_complexity = "0"]
    pub (in super) fn f1() {}
}
```

r[paths.expr]
### Paths in expressions

r[paths.expr.syntax]
```grammar,paths
PathInExpression ->
    `::`? PathExprSegment (`::` PathExprSegment)*

PathExprSegment ->
    PathIdentSegment (`::` GenericArgs)?

PathIdentSegment ->
    IDENTIFIER | `super` | `self` | `Self` | `crate` | `$crate`

GenericArgs ->
      `<` `>`
    | `<` ( GenericArg `,` )* GenericArg `,`? `>`

GenericArg ->
    Lifetime | Type | GenericArgsConst | GenericArgsBinding | GenericArgsBounds

GenericArgsConst ->
      BlockExpression
    | LiteralExpression
    | `-` LiteralExpression
    | SimplePathSegment

GenericArgsBinding ->
    IDENTIFIER GenericArgs? `=` Type

GenericArgsBounds ->
    IDENTIFIER GenericArgs? `:` TypeParamBounds
```

r[paths.expr.intro]
Paths in expressions allow for paths with generic arguments to be specified. They are used in various places in [expressions] and [patterns].

r[paths.expr.turbofish]
The `::` token is required before the opening `<` for generic arguments to avoid ambiguity with the less-than operator. This is colloquially known as "turbofish" syntax.

```rust
(0..10).collect::<Vec<_>>();
Vec::<u8>::with_capacity(1024);
```

r[paths.expr.argument-order]
The order of generic arguments is restricted to lifetime arguments, then type arguments, then const arguments, then equality constraints.

r[paths.expr.complex-const-params]
Const arguments must be surrounded by braces unless they are a [literal], an [inferred const], or a single segment path. An [inferred const] may not be surrounded by braces.

```rust
mod m {
    pub const C: usize = 1;
}
const C: usize = m::C;
fn f<const N: usize>() -> [u8; N] { [0; N] }

let _ = f::<1>(); // Literal.
let _: [_; 1] = f::<_>(); // Inferred const.
let _: [_; 1] = f::<(((_)))>(); // Inferred const.
let _ = f::<C>(); // Single segment path.
let _ = f::<{ m::C }>(); // Multi-segment path must be braced.
```

```rust,compile_fail
fn f<const N: usize>() -> [u8; N] { [0; _] }
let _: [_; 1] = f::<{ _ }>();
//                    ^ ERROR `_` not allowed here
```

> [!NOTE]
> In a generic argument list, an [inferred const] is parsed as an [inferred type][InferredType] but then semantically treated as a separate kind of [const generic argument].

r[paths.expr.impl-trait-params]
The synthetic type parameters corresponding to `impl Trait` types are implicit, and these cannot be explicitly specified.

r[paths.qualified]
## Qualified paths

r[paths.qualified.syntax]
```grammar,paths
QualifiedPathInExpression -> QualifiedPathType (`::` PathExprSegment)+

QualifiedPathType -> `<` Type (`as` TypePath)? `>`

QualifiedPathInType -> QualifiedPathType (`::` TypePathSegment)+
```

r[paths.qualified.intro]
Fully qualified paths allow for disambiguating the path for [trait implementations] and for specifying [canonical paths](#canonical-paths). When used in a type specification, it supports using the type syntax specified below.

```rust
struct S;
impl S {
    fn f() { println!("S"); }
}
trait T1 {
    fn f() { println!("T1 f"); }
}
impl T1 for S {}
trait T2 {
    fn f() { println!("T2 f"); }
}
impl T2 for S {}
S::f();  // Calls the inherent impl.
<S as T1>::f();  // Calls the T1 trait function.
<S as T2>::f();  // Calls the T2 trait function.
```

r[paths.type]
### Paths in types

r[paths.type.syntax]
```grammar,paths
TypePath -> `::`? TypePathSegment (`::` TypePathSegment)*

TypePathSegment -> PathIdentSegment (`::`? (GenericArgs | TypePathFn))?

TypePathFn -> `(` TypePathFnInputs? `)` (`->` TypeNoBounds)?

TypePathFnInputs -> Type (`,` Type)* `,`?
```

r[paths.type.intro]
Type paths are used within type definitions, trait bounds, type parameter bounds, and qualified paths.

r[paths.type.turbofish]
Although the `::` token is allowed before the generics arguments, it is not required because there is no ambiguity like there is in [PathInExpression].

```rust
# mod ops {
#     pub struct Range<T> {f1: T}
#     pub trait Index<T> {}
#     pub struct Example<'a> {f1: &'a i32}
# }
# struct S;
impl ops::Index<ops::Range<usize>> for S { /*...*/ }
fn i<'a>() -> impl Iterator<Item = ops::Example<'a>> {
    // ...
#    const EXAMPLE: Vec<ops::Example<'static>> = Vec::new();
#    EXAMPLE.into_iter()
}
type G = std::boxed::Box<dyn std::ops::FnOnce(isize) -> isize>;
```

r[paths.qualifiers]
## Path qualifiers

Paths can be denoted with various leading qualifiers to change the meaning of how it is resolved.

> [!NOTE]
> [`use` declarations] have additional behaviors and restrictions for `self`, `super`, `crate`, and `$crate`.

r[paths.qualifiers.global-root]
### `::`

r[paths.qualifiers.global-root.intro]
Paths starting with `::` are considered to be *global paths* where the segments of the path start being resolved from a place which differs based on edition. Each identifier in the path must resolve to an item.

r[paths.qualifiers.global-root.edition2018]
> [!EDITION-2018]
> In the 2015 Edition, identifiers resolve from the "crate root" (`crate::` in the 2018 edition), which contains a variety of different items, including external crates, default crates such as `std` or `core`, and items in the top level of the crate (including `use` imports).
>
> Beginning with the 2018 Edition, paths starting with `::` resolve from crates in the [extern prelude]. That is, they must be followed by the name of a crate.

```rust
pub fn foo() {
    // In the 2018 edition, this accesses `std` via the extern prelude.
    // In the 2015 edition, this accesses `std` via the crate root.
    let now = ::std::time::Instant::now();
    println!("{:?}", now);
}
```

```rust,edition2015
// 2015 Edition
mod a {
    pub fn foo() {}
}
mod b {
    pub fn foo() {
        ::a::foo(); // call `a`'s foo function
        // In Rust 2018, `::a` would be interpreted as the crate `a`.
    }
}
# fn main() {}
```

r[paths.qualifiers.mod-self]
### `self`

r[paths.qualifiers.mod-self.intro]
`self` resolves the path relative to the current module.

r[paths.qualifiers.mod-self.restriction]
`self` can only be used as the first segment, without a preceding `::`.

r[paths.qualifiers.self-pat]
In a method body, a path which consists of a single `self` segment resolves to the method's self parameter.

```rust
fn foo() {}
fn bar() {
    self::foo();
}
struct S(bool);
impl S {
  fn baz(self) {
        self.0;
    }
}
# fn main() {}
```

r[paths.qualifiers.type-self]
### `Self`

r[paths.qualifiers.type-self.intro]
`Self`, with a capital "S", is used to refer to the current type being implemented or defined. It may be used in the following situations:

r[paths.qualifiers.type-self.trait]
* In a [trait] definition, it refers to the type implementing the trait.

r[paths.qualifiers.type-self.impl]
* In an [implementation], it refers to the type being implemented. When implementing a tuple or unit [struct], it also refers to the constructor in the [value namespace].

r[paths.qualifiers.type-self.type]
* In the definition of a [struct], [enumeration], or [union], it refers to the type being defined. The definition is not allowed to be infinitely recursive (there must be an indirection).

r[paths.qualifiers.type-self.scope]
The scope of `Self` behaves similarly to a generic parameter; see the [`Self` scope] section for more details.

r[paths.qualifiers.type-self.allowed-positions]
`Self` can only be used as the first segment, without a preceding `::`.

r[paths.qualifiers.type-self.no-generics]
The `Self` path cannot include generic arguments (as in `Self::<i32>`).

```rust
trait T {
    type Item;
    const C: i32;
    // `Self` will be whatever type that implements `T`.
    fn new() -> Self;
    // `Self::Item` will be the type alias in the implementation.
    fn f(&self) -> Self::Item;
}
struct S;
impl T for S {
    type Item = i32;
    const C: i32 = 9;
    fn new() -> Self {           // `Self` is the type `S`.
        S
    }
    fn f(&self) -> Self::Item {  // `Self::Item` is the type `i32`.
        Self::C                  // `Self::C` is the constant value `9`.
    }
}

// `Self` is in scope within the generics of a trait definition,
// to refer to the type being defined.
trait Add<Rhs = Self> {
    type Output;
    // `Self` can also reference associated items of the
    // type being implemented.
    fn add(self, rhs: Rhs) -> Self::Output;
}

struct NonEmptyList<T> {
    head: T,
    // A struct can reference itself (as long as it is not
    // infinitely recursive).
    tail: Option<Box<Self>>,
}
```

r[paths.qualifiers.super]
### `super`

r[paths.qualifiers.super.intro]
`super` in a path resolves to the parent module.

r[paths.qualifiers.super.allowed-positions]
It may only be used in leading segments of the path, possibly after an initial `self` segment.

```rust
mod a {
    pub fn foo() {}
}
mod b {
    pub fn foo() {
        super::a::foo(); // call a's foo function
    }
}
# fn main() {}
```

r[paths.qualifiers.super.repetition]
`super` may be repeated several times after the first `super` or `self` to refer to ancestor modules.

```rust
mod a {
    fn foo() {}

    mod b {
        mod c {
            fn foo() {
                super::super::foo(); // call a's foo function
                self::super::super::foo(); // call a's foo function
            }
        }
    }
}
# fn main() {}
```

r[paths.qualifiers.crate]
### `crate`

r[paths.qualifiers.crate.intro]
`crate` resolves the path relative to the current crate.

r[paths.qualifiers.crate.allowed-positions]
`crate` can only be used as the first segment, without a preceding `::`.

```rust
fn foo() {}
mod a {
    fn bar() {
        crate::foo();
    }
}
# fn main() {}
```

r[paths.qualifiers.macro-crate]
### `$crate`

r[paths.qualifiers.macro-crate.allowed-positions]
[`$crate`] is only used within [macro transcribers], and can only be used as the first segment, without a preceding `::`.

r[paths.qualifiers.macro-crate.hygiene]
[`$crate`] will expand to a path to access items from the top level of the crate where the macro is defined, regardless of which crate the macro is invoked.

```rust
pub fn increment(x: u32) -> u32 {
    x + 1
}

#[macro_export]
macro_rules! inc {
    ($x:expr) => ( $crate::increment($x) )
}
# fn main() { }
```

r[paths.canonical]
## Canonical paths

r[paths.canonical.intro]
Each item defined in a module or implementation has a *canonical path* that corresponds to where within its crate it is defined.

r[paths.canonical.alias]
All other paths to these items are aliases.

r[paths.canonical.def]
The canonical path is defined as a *path prefix* appended by the path segment the item itself defines.

r[paths.canonical.non-canonical]
[Implementations] and [use declarations] do not have canonical paths, although the items that implementations define do have them. Items defined in block expressions do not have canonical paths. Items defined in a module that does not have a canonical path do not have a canonical path. Associated items defined in an implementation that refers to an item without a canonical path, e.g. as the implementing type, the trait being implemented, a type parameter or bound on a type parameter, do not have canonical paths.

r[paths.canonical.module-prefix]
The path prefix for modules is the canonical path to that module.

r[paths.canonical.bare-impl-prefix]
For bare implementations, it is the canonical path of the item being implemented surrounded by <span class="parenthetical">angle (`<>`)</span> brackets.

r[paths.canonical.trait-impl-prefix]
For [trait implementations], it is the canonical path of the item being implemented followed by `as` followed by the canonical path to the trait all surrounded in <span class="parenthetical">angle (`<>`)</span> brackets.

r[paths.canonical.local-canonical-path]
The canonical path is only meaningful within a given crate. There is no global namespace across crates; an item's canonical path merely identifies it within the crate.

```rust
// Comments show the canonical path of the item.

mod a { // crate::a
    pub struct Struct; // crate::a::Struct

    pub trait Trait { // crate::a::Trait
        fn f(&self); // crate::a::Trait::f
    }

    impl Trait for Struct {
        fn f(&self) {} // <crate::a::Struct as crate::a::Trait>::f
    }

    impl Struct {
        fn g(&self) {} // <crate::a::Struct>::g
    }
}

mod without { // crate::without
    fn canonicals() { // crate::without::canonicals
        struct OtherStruct; // None

        trait OtherTrait { // None
            fn g(&self); // None
        }

        impl OtherTrait for OtherStruct {
            fn g(&self) {} // None
        }

        impl OtherTrait for crate::a::Struct {
            fn g(&self) {} // None
        }

        impl crate::a::Trait for OtherStruct {
            fn f(&self) {} // None
        }
    }
}

# fn main() {}
```

[`$crate`]: macro.decl.hygiene.crate
[implementations]: items/implementations.md
[items]: items.md
[literal]: expressions/literal-expr.md
[use declarations]: items/use-declarations.md
[`Self` scope]: names/scopes.md#self-scope
[`use`]: items/use-declarations.md
[attributes]: attributes.md
[const generic argument]: items.generics.const.argument
[enumeration]: items/enumerations.md
[expressions]: expressions.md
[extern prelude]: names/preludes.md#extern-prelude
[implementation]: items/implementations.md
[inferred const]: items.generics.const.inferred
[macro transcribers]: macros-by-example.md
[macros]: macros.md
[mbe]: macros-by-example.md
[patterns]: patterns.md
[struct]: items/structs.md
[trait implementations]: items/implementations.md#trait-implementations
[trait]: items/traits.md
[traits]: items/traits.md
[types]: types.md
[union]: items/unions.md
[`use` declarations]: items/use-declarations.md
[value namespace]: names/namespaces.md
[visibility]: visibility-and-privacy.md


---

r[names.resolution]
# Name resolution

r[names.resolution.intro]
_Name resolution_ is the process of tying paths and other identifiers to the declarations of those entities. Names are segregated into different [namespaces], allowing entities in different namespaces to share the same name without conflict. Each name is valid within a [scope], or a region of source text where that name may be referenced. Access to a name may be restricted based on its [visibility].

Name resolution is split into three stages throughout the compilation process. The first stage, *expansion-time resolution*, resolves all [`use` declarations] and [macro invocations]. The second stage, *primary resolution*, resolves all names that have not yet been resolved and that do not depend on type information to resolve. The last stage, *type-relative resolution*, resolves the remaining names once type information is available.

> [!NOTE]
> Expansion-time resolution is also known as *early resolution*. Primary resolution is also known as *late resolution*.

r[names.resolution.general]
## General

r[names.resolution.general.intro]
The rules within this section apply to all stages of name resolution.

r[names.resolution.general.scopes]
### Scopes

r[names.resolution.general.scopes.intro]
> [!NOTE]
> This is a placeholder for future expansion about resolution of names within various scopes.

r[names.resolution.expansion]
## Expansion-time name resolution

r[names.resolution.expansion.intro]
Expansion-time name resolution is the stage of name resolution necessary to complete macro expansion and fully generate a crate's [AST]. This stage requires the resolution of macro invocations and `use` declarations. Resolving `use` declarations is required for macro invocations that resolve via [path-based scope]. Resolving macro invocations is required in order to expand them.

r[names.resolution.expansion.unresolved-invocations]
After expansion-time name resolution, the AST must not contain any unexpanded macro invocations. Every macro invocation resolves to a valid definition that exists in the final AST or in an external crate.

```rust,compile_fail
m!(); // ERROR: Cannot find macro `m` in this scope.
```

r[names.resolution.expansion.expansion-order-stability]
The resolution of names must be stable. After expansion, names in the fully expanded AST must resolve to the same definition regardless of the order in which macros are expanded and imports are resolved.

r[names.resolution.expansion.speculation]
All name resolution candidates selected during macro expansion are considered speculative. Once the crate has been fully expanded, all speculative import resolutions are validated to ensure that macro expansion did not introduce any new ambiguities.

> [!NOTE]
> Due to the iterative nature of macro expansion, this causes so-called time traveling ambiguities, such as when a macro or glob import introduces an item that is ambiguous with its own base path.
>
> ```rust,compile_fail,E0659
> # fn main() {}
> macro_rules! f {
>     () => {
>         mod m {
>             pub(crate) use f;
>         }
>     }
> }
> f!();
>
> const _: () = {
>     // Initially, we speculatively resolve `m` to the module in
>     // the crate root.
>     //
>     // Expansion of `f` introduces a second `m` module inside this
>     // body.
>     //
>     // Expansion-time resolution finalizes resolutions by re-
>     // resolving all imports and macro invocations, sees the
>     // introduced ambiguity and reports it as an error.
>     m::f!(); // ERROR: `m` is ambiguous.
> };
> ```

r[names.resolution.expansion.imports]
### Imports
r[names.resolution.expansion.imports.intro]
All `use` declarations are fully resolved during this stage of resolution. [Type-relative paths] cannot be resolved at this stage and will produce an error.

```rust,no_run
mod m {
    pub const C: () = ();
    pub enum E { V }
    pub type A = E;
    impl E {
        pub const C: () = ();
    }
}

// Valid imports resolved at expansion-time:
use m::C; // OK.
use m::E; // OK.
use m::A; // OK.
use m::E::V; // OK.

// Valid expressions resolved during type-relative resolution:
let _ = m::A::V; // OK.
let _ = m::E::C; // OK.
```

```rust,compile_fail,E0432
# mod m {
#     pub const C: () = ();
#     pub enum E { V }
#     pub type A = E;
#     impl E {
#         pub const C: () = ();
#     }
# }
// Invalid type-relative imports that can't resolve at expansion-time:
use m::A::V; // ERROR: Unresolved import `m::A::V`.
use m::E::C; // ERROR: Unresolved import `m::E::C`.
```

r[names.resolution.expansion.imports.shadowing]
Names introduced via `use` declarations in an [outer scope] are shadowed by candidates in the same namespace with the same name from an inner scope except where otherwise restricted by [name resolution ambiguities].

```rust,no_run
pub mod m1 {
    pub mod ambig {
        pub const C: u8 = 1;
    }
}

pub mod m2 {
    pub mod ambig {
        pub const C: u8 = 2;
    }
}

// This introduces the name `ambig` in the outer scope.
use m1::ambig;
const _: () = {
    // This shadows `ambig` in the inner scope.
    use m2::ambig;
    // The inner candidate is selected here
    // as the resolution of `ambig`.
    use ambig::C;
    assert!(C == 2);
};
```

r[names.resolution.expansion.imports.shadowing.shared-scope]
Shadowing of names introduced via `use` declarations within a single scope is permitted in the following situations:

- [`use` glob shadowing]
- [Macro textual scope shadowing]

r[names.resolution.expansion.imports.ambiguity]
#### Ambiguities

r[names.resolution.expansion.imports.ambiguity.intro]
There are certain situations during expansion-time resolution where there are multiple macro definitions, `use` declarations, or modules an import or macro invocation's name could refer to where the compiler cannot consistently determine which candidate should shadow the other. Shadowing cannot be permitted in these situations and the compiler instead emits ambiguity errors.

r[names.resolution.expansion.imports.ambiguity.glob-vs-glob]
Names may not be resolved through ambiguous glob imports. Glob imports are allowed to import conflicting names in the same namespace as long as the name is not used. Names with conflicting candidates from ambiguous glob imports may still be shadowed by non-glob imports and used without producing an error. The errors occur at time of use, not time of import.

```rust,compile_fail,E0659
mod m1 {
    pub struct Ambig;
}

mod m2 {
    pub struct Ambig;
}

// OK: This brings conficting names in the same namespace into scope
// but they have not been used yet.
use m1::*;
use m2::*;

const _: () = {
    // The error happens when the name with the conflicting candidates
    // is used.
    let x = Ambig; // ERROR: `Ambig` is ambiguous.
};
```

```rust,no_run
# mod m1 {
#     pub struct Ambig;
# }
#
# mod m2 {
#     pub struct Ambig;
# }
#
# use m1::*;
# use m2::*; // OK: No name conflict.
const _: () = {
    // This is permitted, since resolution is not through the
    // ambiguous globs.
    struct Ambig;
    let x = Ambig; // OK.
};
```

Multiple glob imports are allowed to import the same name, and that name is allowed to be used if the imports are of the same item (following reexports). The visibility of the name is the maximum visibility of the imports.

```rust,no_run
mod m1 {
    pub struct Ambig;
}

mod m2 {
    // This reexports the same `Ambig` item from a second module.
    pub use super::m1::Ambig;
}

mod m3 {
    // These both import the same `Ambig`.
    //
    // The visibility of `Ambig` is `pub` because that is the
    // maximum visibility between these two `use` declarations.
    pub use super::m1::*;
    use super::m2::*;
}

mod m4 {
    // `Ambig` can be used through the `m3` globs and still has
    // `pub` visibility.
    pub use crate::m3::Ambig;
}

const _: () = {
    // Therefore, we can use it here.
    let _ = m4::Ambig; // OK.
};
# fn main() {}
```

r[names.resolution.expansion.imports.ambiguity.glob-vs-outer]
Names in imports and macro invocations may not be resolved through glob imports when there is another candidate available in an [outer scope].

r[names.resolution.expansion.imports.ambiguity.panic-hack]
> [!NOTE]
> When one of [`core::panic!`] or [`std::panic!`] is brought into scope due to the [standard library prelude], and a user-written [glob import] brings the other into scope, `rustc` currently allows use of `panic!`, even though it is ambiguous. The user-written glob import takes precedence to resolve this ambiguity.
>
> In Rust 2021 and later, [`core::panic!`] and [`std::panic!`] operate identically. But in earlier editions, they differ; only [`std::panic!`] accepts a [`String`] as the format argument.
>
> E.g., this is an error:
>
> ```rust,edition2018,compile_fail,E0308
> extern crate core;
> use ::core::prelude::v1::*;
> fn main() {
>     panic!(std::string::String::new()); // ERROR.
> }
> ```
>
> And this is accepted:
>
> <!-- ignore: Can't test with `no_std`. -->
> ```rust,edition2018,ignore
> #![no_std]
> extern crate std;
> use ::std::prelude::v1::*;
> fn main() {
>     panic!(std::string::String::new()); // OK.
> }
> ```
>
> Don't rely on this behavior; the plan is to remove it.
>
> For details, see [Rust issue #147319](https://github.com/rust-lang/rust/issues/147319).

```rust,compile_fail,E0659
mod glob {
    pub mod ambig {
        pub struct Name;
    }
}

// Outer `ambig` candidate.
pub mod ambig {
    pub struct Name;
}

const _: () = {
    // Cannot resolve `ambig` through this glob
    // because of the outer `ambig` candidate above.
    use glob::*;
    use ambig::Name; // ERROR: `ambig` is ambiguous.
};
```

```rust,compile_fail,E0659
// As above, but with macros.
pub mod m {
    macro_rules! f {
        () => {};
    }
    pub(crate) use f;
}
pub mod glob {
    macro_rules! f {
        () => {};
    }
    pub(crate) use f as ambig;
}

use m::f as ambig;

const _: () = {
    use glob::*;
    ambig!(); // ERROR: `ambig` is ambiguous.
};
```

> [!NOTE]
> These ambiguity errors are specific to expansion-time resolution. Having multiple candidates available for a given name during later stages of resolution is not considered an error. So long as none of the imports themselves are ambiguous, there will always be a single unambiguous closest resolution.
>
> ```rust,no_run
> mod glob {
>     pub const AMBIG: u8 = 1;
> }
>
> mod outer {
>     pub const AMBIG: u8 = 2;
> }
>
> use outer::AMBIG;
>
> const C: () = {
>     use glob::*;
>     assert!(AMBIG == 1);
>     //      ^---- This `AMBIG` is resolved during primary resolution.
> };
> ```

r[names.resolution.expansion.imports.ambiguity.path-vs-textual-macro]
Names may not be resolved through ambiguous macro reexports. Macro reexports are ambiguous when they would shadow a textual macro candidate for the same name in an [outer scope].

```rust,compile_fail,E0659
// Textual macro candidate.
macro_rules! ambig {
    () => {}
}

// Path-based macro candidate.
macro_rules! path_based {
    () => {}
}

pub fn f() {
    // This reexport of the `path_based` macro definition
    // as `ambig` may not shadow the `ambig` macro definition
    // which is resolved via textual macro scope.
    use path_based as ambig;
    ambig!(); // ERROR: `ambig` is ambiguous.
}
```

> [!NOTE]
> This restriction is needed due to implementation details in the compiler, specifically the current scope visitation logic and the complexity of supporting this behavior. This ambiguity error may be removed in the future.

r[names.resolution.expansion.macros]
### Macros

r[names.resolution.expansion.macros.intro]
Macros are resolved by iterating through the available scopes to find the available candidates. Macros are split into two sub-namespaces, one for function-like macros, and the other for attributes and derives. Resolution candidates from the incorrect sub-namespace are ignored.

r[names.resolution.expansion.macros.visitation-order]
The available scope kinds are visited in the following order. Each of these scope kinds represent one or more scopes.

* [Derive helpers]
* [Textual scope macros]
* [Path-based scope macros]
* [`macro_use` prelude]
* [Standard library prelude]
* [Builtin attributes]

> [!NOTE]
> The compiler will attempt to resolve derive helpers that are used before their associated macro introduces them into scope. This scope is visited after the scope for resolving derive helper candidates that are correctly in scope. This behavior is slated for removal.
>
> For more info see [derive helper scope].

> [!NOTE]
> This visitation order may change in the future, such as interleaving the visitation of textual and path-based scope candidates based on their lexical scopes.

> [!EDITION-2018]
> Starting in edition 2018 the `#[macro_use]` prelude is not visited when [`#[no_implicit_prelude]`][names.preludes.no_implicit_prelude] is present.

r[names.resolution.expansion.macros.reserved-names]
The names `cfg` and `cfg_attr` are reserved in the macro attribute [sub-namespace].

r[names.resolution.expansion.macros.ambiguity]
#### Ambiguities

r[names.resolution.expansion.macros.ambiguity.more-expanded-vs-outer]
Names may not be resolved through ambiguous candidates inside of macro expansions. Candidates inside of macro expansions are ambiguous when they would shadow a candidate for the same name from outside of the first candidate's macro expansion and the invocation of the name being resolved is also from outside of the first candidate's macro expansion.

```rust,compile_fail,E0659
macro_rules! define_ambig {
    () => {
        macro_rules! ambig {
            () => {}
        }
    }
}

// Introduce outer candidate definition for `ambig` macro invocation.
macro_rules! ambig {
    () => {}
}

// Introduce a second candidate definition for `ambig` inside of a
// macro expansion.
define_ambig!();

// The definition of `ambig` from the second invocation
// of `define_ambig` is the innermost canadidate.
//
// The definition of `ambig` from the first invocation of
// `define_ambig` is the second candidate.
//
// The compiler checks that the first candidate is inside of a macro
// expansion, that the second candidate is not from within the same
// macro expansion, and that the name being resolved is not from
// within the same macro expansion.
ambig!(); // ERROR: `ambig` is ambiguous.
```

The reverse is not considered ambiguous.

```rust,no_run
# macro_rules! define_ambig {
#     () => {
#         macro_rules! ambig {
#             () => {}
#         }
#     }
# }
// Swap order of definitions.
define_ambig!();
macro_rules! ambig {
    () => {}
}
// The innermost candidate is now less expanded so it may shadow more
// the macro expanded definition above it.
ambig!();
```

Nor is it ambiguous if the invocation being resolved is within the innermost candidate's expansion.

```rust,no_run
macro_rules! ambig {
    () => {}
}

macro_rules! define_and_invoke_ambig {
    () => {
        // Define innermost candidate.
        macro_rules! ambig {
            () => {}
        }

        // Invocation of `ambig` is in the same expansion as the
        // innermost candidate.
        ambig!(); // OK
    }
}

define_and_invoke_ambig!();
```

It doesn't matter if both definitions come from invocations of the same macro; the outermost candidate is still considered "less expanded" because it is not within the expansion containing the innermost candidate's definition.

```rust,compile_fail,E0659
# macro_rules! define_ambig {
#     () => {
#         macro_rules! ambig {
#             () => {}
#         }
#     }
# }
define_ambig!();
define_ambig!();
ambig!(); // ERROR: `ambig` is ambiguous.
```

This also applies to imports so long as the innermost candidate for the name is from within a macro expansion.

```rust,compile_fail,E0659
macro_rules! define_ambig {
    () => {
        mod ambig {
            pub struct Name;
        }
    }
}

mod ambig {
    pub struct Name;
}

const _: () = {
    // Introduce innermost candidate for
    // `ambig` mod in this macro expansion.
    define_ambig!();
    use ambig::Name; // ERROR: `ambig` is ambiguous.
};
```

r[names.resolution.expansion.macros.ambiguity.built-in-attr]
User-defined attributes or derive macros may not shadow built-in non-macro attributes (e.g. inline).

<!-- ignore: test doesn't support proc-macro -->
```rust,ignore
// with-helper/src/lib.rs
# use proc_macro::TokenStream;
#[proc_macro_derive(WithHelperAttr, attributes(non_exhaustive))]
//                                             ^^^^^^^^^^^^^^
//                                   User-defined attribute candidate.
// ...
# pub fn derive_with_helper_attr(_item: TokenStream) -> TokenStream {
#     TokenStream::new()
# }
```

<!-- ignore: requires external crates -->
```rust,ignore
// src/lib.rs
#[derive(with_helper::WithHelperAttr)]
#[non_exhaustive] // ERROR: `non_exhaustive` is ambiguous.
struct S;
```

> [!NOTE]
> This applies regardless of the name the built-in attribute is a candidate for:
>
> <!-- ignore: test doesn't support proc-macro -->
> ```rust,ignore
> // with-helper/src/lib.rs
> # use proc_macro::TokenStream;
> #
> #[proc_macro_derive(WithHelperAttr, attributes(helper))]
> //                                             ^^^^^^
> //                                 User-defined attribute candidate.
> // ...
> # pub fn derive_with_helper_attr(_item: TokenStream) -> TokenStream {
> #     TokenStream::new()
> # }
> ```
>
> <!-- ignore: requires external crates -->
> ```rust,ignore
> // src/lib.rs
> use inline as helper;
> //            ^----- Built-in attribute candidate via reexport.
>
> #[derive(with_helper::WithHelperAttr)]
> #[helper] // ERROR: `helper` is ambiguous.
> struct S;
> ```

r[names.resolution.primary]
## Primary name resolution
> [!NOTE]
> This is a placeholder for future expansion about primary name resolution.

r[names.resolution.type-relative]
## Type-relative resolution
> [!NOTE]
> This is a placeholder for future expansion about type-dependent resolution.

[AST]: glossary.ast
[Builtin attributes]: ./preludes.md#r-names.preludes.lang
[Derive helpers]: ../procedural-macros.md#r-macro.proc.derive.attributes
[Macros]: ../macros.md
[Path-based scope macros]: ../macros.md#r-macro.invocation.name-resolution
[Standard library prelude]: ./preludes.md#r-names.preludes.std
[Textual scope macros]: ../macros-by-example.md#r-macro.decl.scope.textual
[`let` bindings]: ../statements.md#let-statements
[`macro_use` prelude]: ./preludes.md#r-names.preludes.macro_use
[`use` declarations]: ../items/use-declarations.md
[`use` glob shadowing]: ../items/use-declarations.md#r-items.use.glob.shadowing
[derive helper scope]: ../procedural-macros.md#r-macro.proc.derive.attributes.scope
[glob import]: items.use.glob
[item definitions]: ../items.md
[macro invocations]: ../macros.md#macro-invocation
[macro textual scope shadowing]: ../macros-by-example.md#r-macro.decl.scope.textual.shadow
[name resolution ambiguities]: #r-names.resolution.expansion.imports.ambiguity
[namespaces]: ../names/namespaces.md
[outer scope]: #r-names.resolution.general.scopes
[path-based scope]: ../macros.md#r-macro.invocation.name-resolution
[scope]: ../names/scopes.md
[sub-namespace]: ../names/namespaces.md#r-names.namespaces.sub-namespaces
[type-relative paths]: names.resolution.type-relative
[visibility]: ../visibility-and-privacy.md


---

r[vis]
# Visibility and privacy

r[vis.syntax]
```grammar,items
Visibility ->
      `pub`
    | `pub` `(` `crate` `)`
    | `pub` `(` `self` `)`
    | `pub` `(` `super` `)`
    | `pub` `(` `in` SimplePath `)`
```

r[vis.intro]
These two terms are often used interchangeably, and what they are attempting to convey is the answer to the question "Can this item be used at this location?"

r[vis.name-hierarchy]
Rust's name resolution operates on a global hierarchy of namespaces. Each level in the hierarchy can be thought of as some item. The items are one of those mentioned above, but also include external crates. Declaring or defining a new module can be thought of as inserting a new tree into the hierarchy at the location of the definition.

r[vis.privacy]
To control whether interfaces can be used across modules, Rust checks each use of an item to see whether it should be allowed or not. This is where privacy warnings are generated, or otherwise "you used a private item of another module and weren't allowed to."

r[vis.default]
By default, everything is *private*, with two exceptions: Associated items in a `pub` Trait are public by default; Enum variants in a `pub` enum are also public by default. When an item is declared as `pub`, it can be thought of as being accessible to the outside world. For example:

```rust
# fn main() {}
// Declare a private struct
struct Foo;

// Declare a public struct with a private field
pub struct Bar {
    field: i32,
}

// Declare a public enum with two public variants
pub enum State {
    PubliclyAccessibleState,
    PubliclyAccessibleState2,
}
```

r[vis.access]
With the notion of an item being either public or private, Rust allows item accesses in two cases:

1. If an item is public, then it can be accessed externally from some module `m` if you can access all the item's ancestor modules from `m`. You can also potentially be able to name the item through re-exports. See below.
2. If an item is private, it may be accessed by the current module and its descendants.

These two cases are surprisingly powerful for creating module hierarchies exposing public APIs while hiding internal implementation details. To help explain, here's a few use cases and what they would entail:

* A library developer needs to expose functionality to crates which link against their library. As a consequence of the first case, this means that anything which is usable externally must be `pub` from the root down to the destination item. Any private item in the chain will disallow external accesses.

* A crate needs a global available "helper module" to itself, but it doesn't want to expose the helper module as a public API. To accomplish this, the root of the crate's hierarchy would have a private module which then internally has a "public API". Because the entire crate is a descendant of the root, then the entire local crate can access this private module through the second case.

* When writing unit tests for a module, it's often a common idiom to have an immediate child of the module to-be-tested named `mod test`. This module could access any items of the parent module through the second case, meaning that internal implementation details could also be seamlessly tested from the child module.

In the second case, it mentions that a private item "can be accessed" by the current module and its descendants, but the exact meaning of accessing an item depends on what the item is.

r[vis.use]
Accessing a module, for example, would mean looking inside of it (to import more items). On the other hand, accessing a function would mean that it is invoked. Additionally, path expressions and import statements are considered to access an item in the sense that the import/expression is only valid if the destination is in the current visibility scope.

Here's an example of a program which exemplifies the three cases outlined above:

```rust
// This module is private, meaning that no external crate can access this
// module. Because it is private at the root of this current crate, however, any
// module in the crate may access any publicly visible item in this module.
mod crate_helper_module {

    // This function can be used by anything in the current crate
    pub fn crate_helper() {}

    // This function *cannot* be used by anything else in the crate. It is not
    // publicly visible outside of the `crate_helper_module`, so only this
    // current module and its descendants may access it.
    fn implementation_detail() {}
}

// This function is "public to the root" meaning that it's available to external
// crates linking against this one.
pub fn public_api() {}

// Similarly to 'public_api', this module is public so external crates may look
// inside of it.
pub mod submodule {
    use crate::crate_helper_module;

    pub fn my_method() {
        // Any item in the local crate may invoke the helper module's public
        // interface through a combination of the two rules above.
        crate_helper_module::crate_helper();
    }

    // This function is hidden to any module which is not a descendant of
    // `submodule`
    fn my_implementation() {}

    #[cfg(test)]
    mod test {

        #[test]
        fn test_my_implementation() {
            // Because this module is a descendant of `submodule`, it's allowed
            // to access private items inside of `submodule` without a privacy
            // violation.
            super::my_implementation();
        }
    }
}

# fn main() {}
```

For a Rust program to pass the privacy checking pass, all paths must be valid accesses given the two rules above. This includes all use statements, expressions, types, etc.

r[vis.scoped]
## `pub(in path)`, `pub(crate)`, `pub(super)`, and `pub(self)`

r[vis.scoped.intro]
In addition to public and private, Rust allows users to declare an item as visible only within a given scope. The rules for `pub` restrictions are as follows:

r[vis.scoped.in]
- `pub(in path)` makes an item visible within the provided `path`. `path` must be a simple path which resolves to an ancestor module of the item whose visibility is being declared. Each identifier in `path` must refer directly to a module (not to a name introduced by a `use` statement).

r[vis.scoped.crate]
- `pub(crate)` makes an item visible within the current crate.

r[vis.scoped.super]
- `pub(super)` makes an item visible to the parent module. This is equivalent to `pub(in super)`.

r[vis.scoped.self]
- `pub(self)` makes an item visible to the current module. This is equivalent to `pub(in self)` or not using `pub` at all.

r[vis.scoped.edition2018]
> [!EDITION-2018]
> Starting with the 2018 edition, paths for `pub(in path)` must start with `crate`, `self`, or `super`. The 2015 edition may also use paths starting with `::` or modules from the crate root.

Here's an example:

```rust,edition2015
pub mod outer_mod {
    pub mod inner_mod {
        // This function is visible within `outer_mod`
        pub(in crate::outer_mod) fn outer_mod_visible_fn() {}
        // Same as above, this is only valid in the 2015 edition.
        pub(in outer_mod) fn outer_mod_visible_fn_2015() {}

        // This function is visible to the entire crate
        pub(crate) fn crate_visible_fn() {}

        // This function is visible within `outer_mod`
        pub(super) fn super_mod_visible_fn() {
            // This function is visible since we're in the same `mod`
            inner_mod_visible_fn();
        }

        // This function is visible only within `inner_mod`,
        // which is the same as leaving it private.
        pub(self) fn inner_mod_visible_fn() {}
    }
    pub fn foo() {
        inner_mod::outer_mod_visible_fn();
        inner_mod::crate_visible_fn();
        inner_mod::super_mod_visible_fn();

        // This function is no longer visible since we're outside of `inner_mod`
        // Error! `inner_mod_visible_fn` is private
        //inner_mod::inner_mod_visible_fn();
    }
}

fn bar() {
    // This function is still visible since we're in the same crate
    outer_mod::inner_mod::crate_visible_fn();

    // This function is no longer visible since we're outside of `outer_mod`
    // Error! `super_mod_visible_fn` is private
    //outer_mod::inner_mod::super_mod_visible_fn();

    // This function is no longer visible since we're outside of `outer_mod`
    // Error! `outer_mod_visible_fn` is private
    //outer_mod::inner_mod::outer_mod_visible_fn();

    outer_mod::foo();
}

fn main() { bar() }
```

> [!NOTE]
> This syntax only adds another restriction to the visibility of an item. It does not guarantee that the item is visible within all parts of the specified scope. To access an item, all of its parent items up to the current scope must still be visible as well.

r[vis.reexports]
## Re-exporting and visibility

r[vis.reexports.intro]
Rust allows publicly re-exporting items through a `pub use` directive. Because this is a public directive, this allows the item to be used in the current module through the rules above. It essentially allows public access into the re-exported item. For example, this program is valid:

```rust
pub use self::implementation::api;

mod implementation {
    pub mod api {
        pub fn f() {}
    }
}

# fn main() {}
```

This means that any external crate referencing `implementation::api::f` would receive a privacy violation, while the path `api::f` would be allowed.

r[vis.reexports.private-item]
When re-exporting a private item, it can be thought of as allowing the "privacy chain" being short-circuited through the reexport instead of passing through the namespace hierarchy as it normally would.
