r[attributes]
# Attributes

r[attributes.syntax]
```grammar,attributes
InnerAttribute -> `#` `!` `[` Attr `]`

OuterAttribute -> `#` `[` Attr `]`

Attr ->
      SimplePath AttrInput?
    | `unsafe` `(` SimplePath AttrInput? `)`

AttrInput ->
      DelimTokenTree
    | `=` Expression
```

r[attributes.intro]
An _attribute_ is a general, free-form metadatum that is interpreted according to name, convention, language, and compiler version. Attributes are modeled on Attributes in [ECMA-335], with the syntax coming from [ECMA-334] \(C#).

r[attributes.inner]
_Inner attributes_, written with a bang (`!`) after the hash (`#`), apply to the form that the attribute is declared within.

> [!EXAMPLE]
> ```rust
> // General metadata applied to the enclosing module or crate.
> #![crate_type = "lib"]
>
> // Inner attribute applies to the entire function.
> fn some_unused_variables() {
>   #![allow(unused_variables)]
>
>   let x = ();
>   let y = ();
>   let z = ();
> }
> ```

r[attributes.outer]
_Outer attributes_, written without the bang after the hash, apply to the form that follows the attribute.

> [!EXAMPLE]
> ```rust
> // A function marked as a unit test
> #[test]
> fn test_foo() {
>     /* ... */
> }
>
> // A conditionally-compiled module
> #[cfg(target_os = "linux")]
> mod bar {
>     /* ... */
> }
>
> // A lint attribute used to suppress a warning/error
> #[allow(non_camel_case_types)]
> type int8_t = i8;
> ```

r[attributes.input]
The attribute consists of a path to the attribute, followed by an optional delimited token tree whose interpretation is defined by the attribute. Attributes other than macro attributes also allow the input to be an equals sign (`=`) followed by an expression. See the [meta item syntax](#meta-item-attribute-syntax) below for more details.

r[attributes.safety]
An attribute may be unsafe to apply. To avoid undefined behavior when using these attributes, certain obligations that cannot be checked by the compiler must be met. To assert these have been, the attribute is wrapped in `unsafe(..)`, e.g. `#[unsafe(no_mangle)]`.

The following attributes are unsafe:

* [`export_name`]
* [`link_section`]
* [`naked`]
* [`no_mangle`]

r[attributes.kind]
Attributes can be classified into the following kinds:

* [Built-in attributes]
* [Proc macro attributes][attribute macros]
* [Derive macro helper attributes]
* [Tool attributes](#tool-attributes)

r[attributes.allowed-position]
Attributes may be applied to many forms in the language:

* All [item declarations] accept outer attributes while [external blocks], [functions], [implementations], and [modules] accept inner attributes.
* Most [statements] accept outer attributes (see [Expression Attributes] for limitations on expression statements).
* [Block expressions] accept outer and inner attributes, but only when they are the outer expression of an [expression statement] or the final expression of another block expression.
* [Enum] variants and [struct] and [union] fields accept outer attributes.
* [Match expression arms][match expressions] accept outer attributes.
* [Generic lifetime or type parameter][generics] accept outer attributes.
* Expressions accept outer attributes in limited situations, see [Expression Attributes] for details.
* [Function][functions], [closure] and [function pointer] parameters accept outer attributes. This includes attributes on variadic parameters denoted with `...` in function pointers and [external blocks][variadic functions].
* [Inline assembly] template strings and operands accept outer attributes. Only certain attributes are accepted semantically; for details, see [asm.attributes.supported-attributes].

r[attributes.meta]
## Meta item attribute syntax

r[attributes.meta.intro]
A "meta item" is the syntax used for the [Attr] rule by most [built-in attributes]. It has the following grammar:

r[attributes.meta.syntax]
```grammar,attributes
@root MetaItem ->
      SimplePath
    | SimplePath `=` Expression
    | SimplePath `(` MetaSeq? `)`

MetaSeq ->
    MetaItemInner ( `,` MetaItemInner )* `,`?

MetaItemInner ->
      MetaItem
    | Expression
```

r[attributes.meta.literal-expr]
Expressions in meta items must macro-expand to literal expressions, which must not include integer or float type suffixes. Expressions which are not literal expressions will be syntactically accepted (and can be passed to proc-macros), but will be rejected after parsing.

r[attributes.meta.order]
Note that if the attribute appears within another macro, it will be expanded after that outer macro. For example, the following code will expand the `Serialize` proc-macro first, which must preserve the `include_str!` call in order for it to be expanded:

```rust ignore
#[derive(Serialize)]
struct Foo {
    #[doc = include_str!("x.md")]
    x: u32
}
```

r[attributes.meta.order-macro]
Additionally, macros in attributes will be expanded only after all other attributes applied to the item:

```rust ignore
#[macro_attr1] // expanded first
#[doc = mac!()] // `mac!` is expanded fourth.
#[macro_attr2] // expanded second
#[derive(MacroDerive1, MacroDerive2)] // expanded third
fn foo() {}
```

r[attributes.meta.builtin]
Various built-in attributes use different subsets of the meta item syntax to specify their inputs. The following grammar rules show some commonly used forms:

r[attributes.meta.builtin.syntax]
```grammar,attributes
@root MetaWord ->
    IDENTIFIER

MetaNameValueStr ->
    IDENTIFIER `=` (STRING_LITERAL | RAW_STRING_LITERAL)

@root MetaListPaths ->
    IDENTIFIER `(` ( SimplePath (`,` SimplePath)* `,`? )? `)`

@root MetaListIdents ->
    IDENTIFIER `(` ( IDENTIFIER (`,` IDENTIFIER)* `,`? )? `)`

@root MetaListNameValueStr ->
    IDENTIFIER `(` ( MetaNameValueStr (`,` MetaNameValueStr)* `,`? )? `)`
```

Some examples of meta items are:

Style | Example
------|--------
[MetaWord] | `no_std`
[MetaNameValueStr] | `doc = "example"`
[MetaListPaths] | `allow(unused, clippy::inline_always)`
[MetaListIdents] | `macro_use(foo, bar)`
[MetaListNameValueStr] | `link(name = "CoreFoundation", kind = "framework")`

r[attributes.activity]
## Active and inert attributes

r[attributes.activity.intro]
An attribute is either active or inert. During attribute processing, *active attributes* remove themselves from the form they are on while *inert attributes* stay on.

The [`cfg`] and [`cfg_attr`] attributes are active. [Attribute macros] are active. All other attributes are inert.

r[attributes.tool]
## Tool attributes

r[attributes.tool.intro]
The compiler may allow attributes for external tools where each tool resides in its own module in the [tool prelude]. The first segment of the attribute path is the name of the tool, with one or more additional segments whose interpretation is up to the tool.

r[attributes.tool.ignored]
When a tool is not in use, the tool's attributes are accepted without a warning. When the tool is in use, the tool is responsible for processing and interpretation of its attributes.

r[attributes.tool.prelude]
Tool attributes are not available if the [`no_implicit_prelude`] attribute is used.

```rust
// Tells the rustfmt tool to not format the following element.
#[rustfmt::skip]
struct S {
}

// Controls the "cyclomatic complexity" threshold for the clippy tool.
#[clippy::cyclomatic_complexity = "100"]
pub fn f() {}
```

> [!NOTE]
> `rustc` currently recognizes the tools "clippy", "rustfmt", "diagnostic", "miri", and "rust_analyzer".

r[attributes.builtin]
## Built-in attributes index

The following is an index of all built-in attributes.

- Conditional compilation
  - [`cfg`] --- Controls conditional compilation.
  - [`cfg_attr`] --- Conditionally includes attributes.

- Testing
  - [`test`] --- Marks a function as a test.
  - [`ignore`] --- Disables a test function.
  - [`should_panic`] --- Indicates a test should generate a panic.

- Derive
  - [`derive`] --- Automatic trait implementations.
  - [`automatically_derived`] --- Marker for implementations created by `derive`.

- Macros
  - [`macro_export`] --- Exports a `macro_rules` macro for cross-crate use.
  - [`macro_use`] --- Expands macro visibility, or imports macros from other crates.
  - [`proc_macro`] --- Defines a function-like macro.
  - [`proc_macro_derive`] --- Defines a derive macro.
  - [`proc_macro_attribute`] --- Defines an attribute macro.

- Diagnostics
  - [`allow`], [`expect`], [`warn`], [`deny`], [`forbid`] --- Alters the default lint level.
  - [`deprecated`] --- Generates deprecation notices.
  - [`must_use`] --- Generates a lint for unused values.
  - [`diagnostic::on_unimplemented`] --- Hints the compiler to emit a certain error message if a trait is not implemented.
  - [`diagnostic::do_not_recommend`] --- Hints the compiler to not show a certain trait impl in error messages.

- ABI, linking, symbols, and FFI
  - [`link`] --- Specifies a native library to link with an `extern` block.
  - [`link_name`] --- Specifies the name of the symbol for functions or statics in an `extern` block.
  - [`link_ordinal`] --- Specifies the ordinal of the symbol for functions or statics in an `extern` block.
  - [`no_link`] --- Prevents linking an extern crate.
  - [`repr`] --- Controls type layout.
  - [`crate_type`] --- Specifies the type of crate (library, executable, etc.).
  - [`no_main`] --- Disables emitting the `main` symbol.
  - [`export_name`] --- Specifies the exported symbol name for a function or static.
  - [`link_section`] --- Specifies the section of an object file to use for a function or static.
  - [`no_mangle`] --- Disables symbol name encoding.
  - [`used`] --- Forces the compiler to keep a static item in the output object file.
  - [`crate_name`] --- Specifies the crate name.

- Code generation
  - [`inline`] --- Hint to inline code.
  - [`cold`] --- Hint that a function is unlikely to be called.
  - [`naked`] --- Prevent the compiler from emitting a function prologue and epilogue.
  - [`no_builtins`] --- Disables use of certain built-in functions.
  - [`target_feature`] --- Configure platform-specific code generation.
  - [`track_caller`] --- Pass the parent call location to `std::panic::Location::caller()`.
  - [`instruction_set`] --- Specify the instruction set used to generate a function's code.

- Documentation
  - `doc` --- Specifies documentation. See [The Rustdoc Book] for more information. [Doc comments] are transformed into `doc` attributes.

- Preludes
  - [`no_std`] --- Removes std from the prelude.
  - [`no_implicit_prelude`] --- Disables prelude lookups within a module.

- Modules
  - [`path`] --- Specifies the filename for a module.

- Limits
  - [`recursion_limit`] --- Sets the maximum recursion limit for certain compile-time operations.
  - [`type_length_limit`] --- Sets the maximum size of a polymorphic type.

- Runtime
  - [`panic_handler`] --- Sets the function to handle panics.
  - [`global_allocator`] --- Sets the global memory allocator.
  - [`windows_subsystem`] --- Specifies the windows subsystem to link with.

- Features
  - `feature` --- Used to enable unstable or experimental compiler features. See [The Unstable Book] for features implemented in `rustc`.

- Type System
  - [`non_exhaustive`] --- Indicate that a type will have more fields/variants added in future.

- Debugger
  - [`debugger_visualizer`] --- Embeds a file that specifies debugger output for a type.
  - [`collapse_debuginfo`] --- Controls how macro invocations are encoded in debuginfo.

[Doc comments]: comments.md#doc-comments
[ECMA-334]: https://www.ecma-international.org/publications-and-standards/standards/ecma-334/
[ECMA-335]: https://www.ecma-international.org/publications-and-standards/standards/ecma-335/
[Expression Attributes]: expressions.md#expression-attributes
[The Rustdoc Book]: ../rustdoc/the-doc-attribute.html
[The Unstable Book]: ../unstable-book/index.html
[`allow`]: attributes/diagnostics.md#lint-check-attributes
[`automatically_derived`]: attributes/derive.md#the-automatically_derived-attribute
[`cfg_attr`]: conditional-compilation.md#the-cfg_attr-attribute
[`cfg`]: conditional-compilation.md#the-cfg-attribute
[`cold`]: attributes/codegen.md#the-cold-attribute
[`collapse_debuginfo`]: attributes/debugger.md#the-collapse_debuginfo-attribute
[`crate_name`]: crates-and-source-files.md#the-crate_name-attribute
[`crate_type`]: linkage.md
[`debugger_visualizer`]: attributes/debugger.md#the-debugger_visualizer-attribute
[`deny`]: attributes/diagnostics.md#lint-check-attributes
[`deprecated`]: attributes/diagnostics.md#the-deprecated-attribute
[`derive`]: attributes/derive.md
[`export_name`]: abi.md#the-export_name-attribute
[`expect`]: attributes/diagnostics.md#lint-check-attributes
[`forbid`]: attributes/diagnostics.md#lint-check-attributes
[`global_allocator`]: runtime.md#the-global_allocator-attribute
[`ignore`]: attributes/testing.md#the-ignore-attribute
[`inline`]: attributes/codegen.md#the-inline-attribute
[`instruction_set`]: attributes/codegen.md#the-instruction_set-attribute
[`link_name`]: items/external-blocks.md#the-link_name-attribute
[`link_ordinal`]: items/external-blocks.md#the-link_ordinal-attribute
[`link_section`]: abi.md#the-link_section-attribute
[`link`]: items/external-blocks.md#the-link-attribute
[`macro_export`]: macros-by-example.md#the-macro_export-attribute
[`macro_use`]: macros-by-example.md#the-macro_use-attribute
[`must_use`]: attributes/diagnostics.md#the-must_use-attribute
[`naked`]: attributes/codegen.md#the-naked-attribute
[`no_builtins`]: attributes/codegen.md#the-no_builtins-attribute
[`no_implicit_prelude`]: names/preludes.md#the-no_implicit_prelude-attribute
[`no_link`]: items/extern-crates.md#the-no_link-attribute
[`no_main`]: crates-and-source-files.md#the-no_main-attribute
[`no_mangle`]: abi.md#the-no_mangle-attribute
[`no_std`]: names/preludes.md#the-no_std-attribute
[`non_exhaustive`]: attributes/type_system.md#the-non_exhaustive-attribute
[`panic_handler`]: panic.md#the-panic_handler-attribute
[`path`]: items/modules.md#the-path-attribute
[`proc_macro_attribute`]: procedural-macros.md#the-proc_macro_attribute-attribute
[`proc_macro_derive`]: macro.proc.derive
[`proc_macro`]: procedural-macros.md#the-proc_macro-attribute
[`recursion_limit`]: attributes/limits.md#the-recursion_limit-attribute
[`repr`]: type-layout.md#representations
[`should_panic`]: attributes/testing.md#the-should_panic-attribute
[`target_feature`]: attributes/codegen.md#the-target_feature-attribute
[`test`]: attributes/testing.md#the-test-attribute
[`track_caller`]: attributes/codegen.md#the-track_caller-attribute
[`type_length_limit`]: attributes/limits.md#the-type_length_limit-attribute
[`used`]: abi.md#the-used-attribute
[`warn`]: attributes/diagnostics.md#lint-check-attributes
[`windows_subsystem`]: runtime.md#the-windows_subsystem-attribute
[attribute macros]: procedural-macros.md#the-proc_macro_attribute-attribute
[block expressions]: expressions/block-expr.md
[built-in attributes]: #built-in-attributes-index
[derive macro helper attributes]: procedural-macros.md#derive-macro-helper-attributes
[enum]: items/enumerations.md
[expression statement]: statements.md#expression-statements
[external blocks]: items/external-blocks.md
[functions]: items/functions.md
[generics]: items/generics.md
[implementations]: items/implementations.md
[item declarations]: items.md
[match expressions]: expressions/match-expr.md
[modules]: items/modules.md
[statements]: statements.md
[struct]: items/structs.md
[tool prelude]: names/preludes.md#tool-prelude
[union]: items/unions.md
[closure]: expressions/closure-expr.md
[function pointer]: types/function-pointer.md
[variadic functions]: items/external-blocks.html#variadic-functions
[`diagnostic::on_unimplemented`]: attributes/diagnostics.md#the-diagnosticon_unimplemented-attribute
[`diagnostic::do_not_recommend`]: attributes/diagnostics.md#the-diagnosticdo_not_recommend-attribute
[Inline assembly]: inline-assembly.md


---

r[attributes.testing]
# Testing attributes

The following [attributes] are used for specifying functions for performing
tests. Compiling a crate in "test" mode enables building the test functions
along with a test harness for executing the tests. Enabling the test mode also
enables the [`test` conditional compilation option].

<!-- template:attributes -->
r[attributes.testing.test]
## The `test` attribute

r[attributes.testing.test.intro]
The *`test` [attribute][attributes]* marks a function to be executed as a test.

> [!EXAMPLE]
> ```rust,no_run
> # pub fn add(left: u64, right: u64) -> u64 { left + right }
> #[test]
> fn it_works() {
>     let result = add(2, 2);
>     assert_eq!(result, 4);
> }
> ```

r[attributes.testing.test.syntax]
The `test` attribute uses the [MetaWord] syntax.

r[attributes.testing.test.allowed-positions]
The `test` attribute may only be applied to [free functions] that are monomorphic, that take no arguments, and where the return type implements the [`Termination`] trait.

> [!NOTE]
> Some of types that implement the [`Termination`] trait include:
> * `()`
> * `Result<T, E> where T: Termination, E: Debug`

r[attributes.testing.test.duplicates]
Only the first use of `test` on a function has effect.

> [!NOTE]
> `rustc` lints against any use following the first. This may become an error in the future.

<!-- TODO: This is a minor lie. Currently rustc warns that duplicates are ignored, but it then generates multiple test entries with the same name. I would vote for rejecting this in the future. -->

r[attributes.testing.test.stdlib]
The `test` attribute is exported from the standard library prelude as [`std::prelude::v1::test`].

r[attributes.testing.test.enabled]
These functions are only compiled when in test mode.

> [!NOTE]
> The test mode is enabled by passing the `--test` argument to `rustc` or using `cargo test`.

r[attributes.testing.test.success]
The test harness calls the returned value's [`report`] method, and classifies the test as passed or failed depending on whether the resulting [`ExitCode`] represents successful termination.
In particular:
* Tests that return `()` pass as long as they terminate and do not panic.
* Tests that return a `Result<(), E>` pass as long as they return `Ok(())`.
* Tests that return `ExitCode::SUCCESS` pass, and tests that return `ExitCode::FAILURE` fail.
* Tests that do not terminate neither pass nor fail.

> [!EXAMPLE]
> ```rust,no_run
> # use std::io;
> # fn setup_the_thing() -> io::Result<i32> { Ok(1) }
> # fn do_the_thing(s: &i32) -> io::Result<()> { Ok(()) }
> #[test]
> fn test_the_thing() -> io::Result<()> {
>     let state = setup_the_thing()?; // expected to succeed
>     do_the_thing(&state)?;          // expected to succeed
>     Ok(())
> }
> ```

<!-- template:attributes -->
r[attributes.testing.ignore]
## The `ignore` attribute

r[attributes.testing.ignore.intro]
The *`ignore` [attribute][attributes]* can be used with the [`test` attribute][attributes.testing.test] to tell the test harness to not execute that function as a test.

> [!EXAMPLE]
> ```rust,no_run
> #[test]
> #[ignore]
> fn check_thing() {
>     // …
> }
> ```

> [!NOTE]
> The `rustc` test harness supports the `--include-ignored` flag to force ignored tests to be run.

r[attributes.testing.ignore.syntax]
The `ignore` attribute uses the [MetaWord] and [MetaNameValueStr] syntaxes.

r[attributes.testing.ignore.reason]
The [MetaNameValueStr] form of the `ignore` attribute provides a way to specify a reason why the test is ignored.

> [!EXAMPLE]
> ```rust,no_run
> #[test]
> #[ignore = "not yet implemented"]
> fn mytest() {
>     // …
> }
> ```

r[attributes.testing.ignore.allowed-positions]
The `ignore` attribute may only be applied to functions annotated with the `test` attribute.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[attributes.testing.ignore.duplicates]
Only the first use of `ignore` on a function has effect.

> [!NOTE]
> `rustc` lints against any use following the first. This may become an error in the future.

r[attributes.testing.ignore.behavior]
Ignored tests are still compiled when in test mode, but they are not executed.

<!-- template:attributes -->
r[attributes.testing.should_panic]
## The `should_panic` attribute

r[attributes.testing.should_panic.intro]
The *`should_panic` [attribute][attributes]* causes a test to pass only if the [test function][attributes.testing.test] to which the attribute is applied panics.

> [!EXAMPLE]
> ```rust,no_run
> #[test]
> #[should_panic(expected = "values don't match")]
> fn mytest() {
>     assert_eq!(1, 2, "values don't match");
> }
> ```

r[attributes.testing.should_panic.syntax]
The `should_panic` attribute has these forms:

- [MetaWord]
  > [!EXAMPLE]
  > ```rust,no_run
  > #[test]
  > #[should_panic]
  > fn mytest() { panic!("error: some message, and more"); }
  > ```

- [MetaNameValueStr] --- The given string must appear within the panic message for the test to pass.
  > [!EXAMPLE]
  > ```rust,no_run
  > #[test]
  > #[should_panic = "some message"]
  > fn mytest() { panic!("error: some message, and more"); }
  > ```

- [MetaListNameValueStr] --- As with the [MetaNameValueStr] syntax, the given string must appear within the panic message.
  > [!EXAMPLE]
  > ```rust,no_run
  > #[test]
  > #[should_panic(expected = "some message")]
  > fn mytest() { panic!("error: some message, and more"); }
  > ```

r[attributes.testing.should_panic.allowed-positions]
The `should_panic` attribute may only be applied to functions annotated with the `test` attribute.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[attributes.testing.should_panic.duplicates]
Only the first use of `should_panic` on a function has effect.

> [!NOTE]
> `rustc` lints against any use following the first with a future-compatibility warning. This may become an error in the future.

r[attributes.testing.should_panic.expected]
When the [MetaNameValueStr] form or the [MetaListNameValueStr] form with the `expected` key is used, the given string must appear somewhere within the panic message for the test to pass.

r[attributes.testing.should_panic.return]
The return type of the test function must be `()`.

[`Termination`]: std::process::Termination
[`report`]: std::process::Termination::report
[`test` conditional compilation option]: ../conditional-compilation.md#test
[attributes]: ../attributes.md
[`ExitCode`]: std::process::ExitCode
[free functions]: ../glossary.md#free-item


---

<!-- template:attributes -->
r[attributes.derive]
# Derive

r[attributes.derive.intro]
The *`derive` [attribute][attributes]* invokes one or more [derive macros], allowing new [items] to be automatically generated for data structures. You can create `derive` macros with [procedural macros].

> [!EXAMPLE]
> The [`PartialEq`][macro@PartialEq] derive macro emits an [implementation] of [`PartialEq`] for `Foo<T> where T: PartialEq`. The [`Clone`][macro@Clone] derive macro does likewise for [`Clone`].
>
> ```rust
> #[derive(PartialEq, Clone)]
> struct Foo<T> {
>     a: i32,
>     b: T,
> }
> ```
>
> The generated `impl` items are equivalent to:
>
> ```rust
> # struct Foo<T> { a: i32, b: T }
> impl<T: PartialEq> PartialEq for Foo<T> {
>     fn eq(&self, other: &Foo<T>) -> bool {
>         self.a == other.a && self.b == other.b
>     }
> }
>
> impl<T: Clone> Clone for Foo<T> {
>     fn clone(&self) -> Self {
>         Foo { a: self.a.clone(), b: self.b.clone() }
>     }
> }
> ```

r[attributes.derive.syntax]
The `derive` attribute uses the [MetaListPaths] syntax to specify a list of paths to [derive macros] to invoke.

r[attributes.derive.allowed-positions]
The `derive` attribute may only be applied to [structs][items.struct], [enums][items.enum], and [unions][items.union].

r[attributes.derive.duplicates]
The `derive` attribute may be used any number of times on an item. All derive macros listed in all attributes are invoked.

r[attributes.derive.stdlib]
The `derive` attribute is exported in the standard library as:

- [`core::derive`]
- [`std::derive`]
- [`core::prelude::v1::derive`]
- [`std::prelude::v1::derive`]

r[attributes.derive.built-in]
Built-in derives are defined in the [language prelude][names.preludes.lang]. The list of built-in derives are:

- [`Clone`]
- [`Copy`]
- [`Debug`]
- [`Default`]
- [`Eq`]
- [`Hash`]
- [`Ord`]
- [`PartialEq`]
- [`PartialOrd`]

r[attributes.derive.built-in-automatically_derived]
The built-in derives include the [`automatically_derived` attribute][attributes.derive.automatically_derived] on the implementations they generate.

r[attributes.derive.behavior]
During macro expansion, for each element in the list of derives, the corresponding derive macro expands to zero or more [items].

<!-- template:attributes -->
r[attributes.derive.automatically_derived]
## The `automatically_derived` attribute

r[attributes.derive.automatically_derived.intro]
The *`automatically_derived` [attribute][attributes]* is used to annotate an [implementation] to indicate that it was automatically created by a [derive macro]. It has no direct effect, but it may be used by tools and diagnostic lints to detect these automatically generated implementations.

> [!EXAMPLE]
> Given [`#[derive(Clone)]`][macro@Clone] on `struct Example`, the [derive macro] may produce:
>
> ```rust
> # struct Example;
> #[automatically_derived]
> impl ::core::clone::Clone for Example {
>     #[inline]
>     fn clone(&self) -> Self {
>         Example
>     }
> }
> ```

r[attributes.derive.automatically_derived.syntax]
The `automatically_derived` attribute uses the [MetaWord] syntax.

r[attributes.derive.automatically_derived.allowed-positions]
The `automatically_derived` attribute may only be applied to an [implementation].

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[attributes.derive.automatically_derived.duplicates]
Using `automatically_derived` more than once on an implementation has the same effect as using it once.

> [!NOTE]
> `rustc` lints against any use following the first.

r[attributes.derive.automatically_derived.behavior]
The `automatically_derived` attribute has no behavior.

[items]: ../items.md
[derive macro]: macro.proc.derive
[derive macros]: macro.proc.derive
[implementation]: ../items/implementations.md
[items]: ../items.md
[procedural macros]: macro.proc.derive


---

r[attributes.diagnostics]
# Diagnostic attributes

The following [attributes] are used for controlling or generating diagnostic
messages during compilation.

r[attributes.diagnostics.lint]
## Lint check attributes

A lint check names a potentially undesirable coding pattern, such as
unreachable code or omitted documentation.

r[attributes.diagnostics.lint.level]
The lint attributes `allow`,
`expect`, `warn`, `deny`, and `forbid` use the [MetaListPaths] syntax
to specify a list of lint names to change the lint level for the entity
to which the attribute applies.

For any lint check `C`:

r[attributes.diagnostics.lint.allow]
* `#[allow(C)]` overrides the check for `C` so that violations will go
   unreported.

r[attributes.diagnostics.lint.expect]
* `#[expect(C)]` indicates that lint `C` is expected to be emitted. The
  attribute will suppress the emission of `C` or issue a warning, if the
  expectation is unfulfilled.

r[attributes.diagnostics.lint.warn]
* `#[warn(C)]` warns about violations of `C` but continues compilation.

r[attributes.diagnostics.lint.deny]
* `#[deny(C)]` signals an error after encountering a violation of `C`,

r[attributes.diagnostics.lint.forbid]
* `#[forbid(C)]` is the same as `deny(C)`, but also forbids changing the lint
   level afterwards,

> [!NOTE]
> The lint checks supported by `rustc` can be found via `rustc -W help`, along with their default settings and are documented in the [rustc book].

```rust
pub mod m1 {
    // Missing documentation is ignored here
    #[allow(missing_docs)]
    pub fn undocumented_one() -> i32 { 1 }

    // Missing documentation signals a warning here
    #[warn(missing_docs)]
    pub fn undocumented_too() -> i32 { 2 }

    // Missing documentation signals an error here
    #[deny(missing_docs)]
    pub fn undocumented_end() -> i32 { 3 }
}
```

r[attributes.diagnostics.lint.override]
Lint attributes can override the level specified from a previous attribute, as
long as the level does not attempt to change a forbidden lint
(except for `deny`, which is allowed inside a `forbid` context, but ignored).
Previous attributes are those from a higher level in the syntax tree, or from a
previous attribute on the same entity as listed in left-to-right source order.

This example shows how one can use `allow` and `warn` to toggle a particular
check on and off:

```rust
#[warn(missing_docs)]
pub mod m2 {
    #[allow(missing_docs)]
    pub mod nested {
        // Missing documentation is ignored here
        pub fn undocumented_one() -> i32 { 1 }

        // Missing documentation signals a warning here,
        // despite the allow above.
        #[warn(missing_docs)]
        pub fn undocumented_two() -> i32 { 2 }
    }

    // Missing documentation signals a warning here
    pub fn undocumented_too() -> i32 { 3 }
}
```

This example shows how one can use `forbid` to disallow uses of `allow` or
`expect` for that lint check:

```rust,compile_fail
#[forbid(missing_docs)]
pub mod m3 {
    // Attempting to toggle warning signals an error here
    #[allow(missing_docs)]
    /// Returns 2.
    pub fn undocumented_too() -> i32 { 2 }
}
```

> [!NOTE]
> `rustc` allows setting lint levels on the [command-line][rustc-lint-cli], and also supports [setting caps][rustc-lint-caps] on the lints that are reported.

r[attributes.diagnostics.lint.reason]
### Lint reasons

All lint attributes support an additional `reason` parameter, to give context why
a certain attribute was added. This reason will be displayed as part of the lint
message if the lint is emitted at the defined level.

```rust,edition2015,compile_fail
// `keyword_idents` is allowed by default. Here we deny it to
// avoid migration of identifiers when we update the edition.
#![deny(
    keyword_idents,
    reason = "we want to avoid these idents to be future compatible"
)]

// This name was allowed in Rust's 2015 edition. We still aim to avoid
// this to be future compatible and not confuse end users.
fn dyn() {}
```

Here is another example, where the lint is allowed with a reason:

```rust
use std::path::PathBuf;

pub fn get_path() -> PathBuf {
    // The `reason` parameter on `allow` attributes acts as documentation for the reader.
    #[allow(unused_mut, reason = "this is only modified on some platforms")]
    let mut file_name = PathBuf::from("git");

    #[cfg(target_os = "windows")]
    file_name.set_extension("exe");

    file_name
}
```

r[attributes.diagnostics.expect]
### The `#[expect]` attribute

r[attributes.diagnostics.expect.intro]
The `#[expect(C)]` attribute creates a lint expectation for lint `C`. The
expectation will be fulfilled, if a `#[warn(C)]` attribute at the same location
would result in a lint emission. If the expectation is unfulfilled, because
lint `C` would not be emitted, the `unfulfilled_lint_expectations` lint will
be emitted at the attribute.

```rust
fn main() {
    // This `#[expect]` attribute creates a lint expectation, that the `unused_variables`
    // lint would be emitted by the following statement. This expectation is
    // unfulfilled, since the `question` variable is used by the `println!` macro.
    // Therefore, the `unfulfilled_lint_expectations` lint will be emitted at the
    // attribute.
    #[expect(unused_variables)]
    let question = "who lives in a pineapple under the sea?";
    println!("{question}");

    // This `#[expect]` attribute creates a lint expectation that will be fulfilled, since
    // the `answer` variable is never used. The `unused_variables` lint, that would usually
    // be emitted, is suppressed. No warning will be issued for the statement or attribute.
    #[expect(unused_variables)]
    let answer = "SpongeBob SquarePants!";
}
```

r[attributes.diagnostics.expect.fulfillment]
The lint expectation is only fulfilled by lint emissions which have been suppressed by
the `expect` attribute. If the lint level is modified in the scope with other level
attributes like `allow` or `warn`, the lint emission will be handled accordingly and the
expectation will remain unfulfilled.

```rust
#[expect(unused_variables)]
fn select_song() {
    // This will emit the `unused_variables` lint at the warn level
    // as defined by the `warn` attribute. This will not fulfill the
    // expectation above the function.
    #[warn(unused_variables)]
    let song_name = "Crab Rave";

    // The `allow` attribute suppresses the lint emission. This will not
    // fulfill the expectation as it has been suppressed by the `allow`
    // attribute and not the `expect` attribute above the function.
    #[allow(unused_variables)]
    let song_creator = "Noisestorm";

    // This `expect` attribute will suppress the `unused_variables` lint emission
    // at the variable. The `expect` attribute above the function will still not
    // be fulfilled, since this lint emission has been suppressed by the local
    // expect attribute.
    #[expect(unused_variables)]
    let song_version = "Monstercat Release";
}
```

r[attributes.diagnostics.expect.independent]
If the `expect` attribute contains several lints, each one is expected separately. For a
lint group it's enough if one lint inside the group has been emitted:

```rust
// This expectation will be fulfilled by the unused value inside the function
// since the emitted `unused_variables` lint is inside the `unused` lint group.
#[expect(unused)]
pub fn thoughts() {
    let unused = "I'm running out of examples";
}

pub fn another_example() {
    // This attribute creates two lint expectations. The `unused_mut` lint will be
    // suppressed and with that fulfill the first expectation. The `unused_variables`
    // wouldn't be emitted, since the variable is used. That expectation will therefore
    // be unsatisfied, and a warning will be emitted.
    #[expect(unused_mut, unused_variables)]
    let mut link = "https://www.rust-lang.org/";

    println!("Welcome to our community: {link}");
}
```

> [!NOTE]
> The behavior of `#[expect(unfulfilled_lint_expectations)]` is currently defined to always generate the `unfulfilled_lint_expectations` lint.

r[attributes.diagnostics.lint.group]
### Lint groups

Lints may be organized into named groups so that the level of related lints
can be adjusted together. Using a named group is equivalent to listing out the
lints within that group.

```rust,compile_fail
// This allows all lints in the "unused" group.
#[allow(unused)]
// This overrides the "unused_must_use" lint from the "unused"
// group to deny.
#[deny(unused_must_use)]
fn example() {
    // This does not generate a warning because the "unused_variables"
    // lint is in the "unused" group.
    let x = 1;
    // This generates an error because the result is unused and
    // "unused_must_use" is marked as "deny".
    std::fs::remove_file("some_file"); // ERROR: unused `Result` that must be used
}
```

r[attributes.diagnostics.lint.group.warnings]
There is a special group named "warnings" which includes all lints at the
"warn" level. The "warnings" group ignores attribute order and applies to all
lints that would otherwise warn within the entity.

```rust,compile_fail
# unsafe fn an_unsafe_fn() {}
// The order of these two attributes does not matter.
#[deny(warnings)]
// The unsafe_code lint is normally "allow" by default.
#[warn(unsafe_code)]
fn example_err() {
    // This is an error because the `unsafe_code` warning has
    // been lifted to "deny".
    unsafe { an_unsafe_fn() } // ERROR: use of `unsafe` block
}
```

r[attributes.diagnostics.lint.tool]
### Tool lint attributes

r[attributes.diagnostics.lint.tool.intro]
Tool lints allows using scoped lints, to `allow`, `warn`, `deny` or `forbid`
lints of certain tools.

r[attributes.diagnostics.lint.tool.activation]
Tool lints only get checked when the associated tool is active. If a lint
attribute, such as `allow`, references a nonexistent tool lint, the compiler
will not warn about the nonexistent lint until you use the tool.

Otherwise, they work just like regular lint attributes:

```rust
// set the entire `pedantic` clippy lint group to warn
#![warn(clippy::pedantic)]
// silence warnings from the `filter_map` clippy lint
#![allow(clippy::filter_map)]

fn main() {
    // ...
}

// silence the `cmp_nan` clippy lint just for this function
#[allow(clippy::cmp_nan)]
fn foo() {
    // ...
}
```

> [!NOTE]
> `rustc` currently recognizes the tool lints for "[clippy]" and "[rustdoc]".

r[attributes.diagnostics.deprecated]
## The `deprecated` attribute

r[attributes.diagnostics.deprecated.intro]
The *`deprecated` attribute* marks an item as deprecated. `rustc` will issue
warnings on use of `#[deprecated]` items. `rustdoc` will show item
deprecation, including the `since` version and `note`, if available.

r[attributes.diagnostics.deprecated.syntax]
The `deprecated` attribute has several forms:

- `deprecated` --- Issues a generic message.
- `deprecated = "message"` --- Includes the given string in the deprecation
  message.
- [MetaListNameValueStr] syntax with two optional fields:
  - `since` --- Specifies a version number when the item was deprecated. `rustc`
    does not currently interpret the string, but external tools like [Clippy]
    may check the validity of the value.
  - `note` --- Specifies a string that should be included in the deprecation
    message. This is typically used to provide an explanation about the
    deprecation and preferred alternatives.

r[attributes.diagnostic.deprecated.allowed-positions]
The `deprecated` attribute may be applied to any [item], [trait item], [enum
variant], [struct field], [external block item], or [macro definition]. It
cannot be applied to [trait implementation items][trait-impl]. When applied to an item
containing other items, such as a [module] or [implementation], all child
items inherit the deprecation attribute.
<!-- NOTE: It is only rejected for trait impl items
(AnnotationKind::Prohibited). In all other locations, it is silently ignored.
Tuple struct fields are ignored.
-->

Here is an example:

```rust
#[deprecated(since = "5.2.0", note = "foo was rarely used. Users should instead use bar")]
pub fn foo() {}

pub fn bar() {}
```

The [RFC][1270-deprecation.md] contains motivations and more details.

[1270-deprecation.md]: https://github.com/rust-lang/rfcs/blob/master/text/1270-deprecation.md

<!-- template:attributes -->
r[attributes.diagnostics.must_use]
## The `must_use` attribute

r[attributes.diagnostics.must_use.intro]
The *`must_use` [attribute]* marks a value that should be used.

r[attributes.diagnostics.must_use.syntax]
The `must_use` attribute uses the [MetaWord] and [MetaNameValueStr] syntaxes.

> [!EXAMPLE]
> ```rust
> #[must_use]
> fn use_me1() -> u8 { 0 }
>
> #[must_use = "explanation of why it should be used"]
> fn use_me2() -> u8 { 0 }
> ```

r[attributes.diagnostics.must_use.allowed-positions]
The `must_use` attribute may be applied to a:

- [Struct]
- [Enumeration]
- [Union]
- [Function]
- [Trait]

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[attributes.diagnostics.must_use.duplicates]
The `must_use` attribute may be used only once on an item.

> [!NOTE]
> `rustc` lints against any use following the first. This may become an error in the future.

r[attributes.diagnostics.must_use.message]
The `must_use` attribute may include a message by using the [MetaNameValueStr] syntax, e.g., `#[must_use = "example message"]`. The message may be emitted as part of the lint.

r[attributes.diagnostics.must_use.type]
When the attribute is applied to a [struct], [enumeration], or [union], if the [expression] of an [expression statement] has that type, the use triggers the `unused_must_use` lint.

```rust,compile_fail
#![deny(unused_must_use)]
#[must_use]
struct MustUse();
MustUse(); // ERROR: Unused value that must be used.
```

r[attributes.diagnostics.must_use.type.uninhabited]
As an exception to [attributes.diagnostics.must_use.type], the lint does not fire for `Result<(), E>` when `E` is [uninhabited] or for `ControlFlow<B, ()>` when `B` is [uninhabited]. A `#[non_exhaustive]` type from an external crate is not considered uninhabited for this purpose, because it may gain constructors in the future.

```rust
#![deny(unused_must_use)]
# use core::ops::ControlFlow;
enum Empty {}
fn f1() -> Result<(), Empty> { Ok(()) }
f1(); // OK: `Empty` is uninhabited.
fn f2() -> ControlFlow<Empty, ()> { ControlFlow::Continue(()) }
f2(); // OK: `Empty` is uninhabited.
```

r[attributes.diagnostics.must_use.fn]
If the [expression] of an [expression statement] is a [call expression] or [method call expression] whose function operand is a function to which the attribute is applied, the use triggers the `unused_must_use` lint.

```rust,compile_fail
#![deny(unused_must_use)]
#[must_use]
fn f() {}
f(); // ERROR: Unused return value that must be used.
```

r[attributes.diagnostics.must_use.trait]
If the [expression] of an [expression statement] is a [call expression] or [method call expression] whose function operand is a function that returns an [impl trait] or a [dyn trait] type where one or more traits in the bound are marked with the attribute, the use triggers the `unused_must_use` lint.

```rust,compile_fail
#![deny(unused_must_use)]
#[must_use]
trait Tr {}
impl Tr for () {}
fn f() -> impl Tr {}
f(); // ERROR: Unused implementor that must be used.
```

r[attributes.diagnostics.must_use.trait-function]
When the attribute is applied to a function in a trait declaration, the rules described in [attributes.diagnostics.must_use.fn] also apply when the function operand of the [call expression] or [method call expression] is an implementation of that function.

```rust,compile_fail
#![deny(unused_must_use)]
trait Tr {
    #[must_use]
    fn use_me(&self);
}

impl Tr for () {
    fn use_me(&self) {}
}

().use_me(); // ERROR: Unused return value that must be used.
```

```rust,compile_fail
# #![deny(unused_must_use)]
# trait Tr {
#     #[must_use]
#     fn use_me(&self);
# }
#
# impl Tr for () {
#     fn use_me(&self) {}
# }
#
<() as Tr>::use_me(&());
//          ^^^^^^^^^^^ ERROR: Unused return value that must be used.
```

r[attributes.diagnostics.must_use.block-expr]
When checking the [expression] of an [expression statement] for [attributes.diagnostics.must_use.type], [attributes.diagnostics.must_use.fn], [attributes.diagnostics.must_use.trait], and [attributes.diagnostics.must_use.trait-function], the lint looks through [block expressions][block expression] (including [`unsafe` blocks] and [labeled block expressions]) to the trailing expression of each. This applies recursively for nested block expressions.

```rust,compile_fail
#![deny(unused_must_use)]
#[must_use]
fn f() {}

{ f() };        // ERROR: The lint looks through block expressions.
unsafe { f() }; // ERROR: The lint looks through `unsafe` blocks.
{ { f() } };    // ERROR: The lint looks through nested blocks.
```

r[attributes.diagnostics.must_use.trait-impl-function]
When used on a function in a trait implementation, the attribute does nothing.

```rust
#![deny(unused_must_use)]
trait Tr {
    fn f(&self);
}

impl Tr for () {
    #[must_use] // This has no effect.
    fn f(&self) {}
}

().f(); // OK.
```

> [!NOTE]
> `rustc` lints against use on functions in trait implementations. This may become an error in the future.

r[attributes.diagnostics.must_use.wrapping-suppression]
> [!NOTE]
> Wrapping the result of a `#[must_use]` function in certain expressions can suppress the [fn-based check][attributes.diagnostics.must_use.fn], because the [expression] of the [expression statement] is not a [call expression] or [method call expression] to a `#[must_use]` function.  The [type-based check][attributes.diagnostics.must_use.type] still applies if the type of the overall expression is `#[must_use]`.
>
> ```rust
> #![deny(unused_must_use)]
> #[must_use]
> fn f() {}
>
> // The fn-based check does not fire for any of these, because the
> // expression of the expression statement is not a call to a
> // `#[must_use]` function.
> (f(),);                    // Expression is a tuple, not a call.
> Some(f());                 // Callee `Some` is not `#[must_use]`.
> if true { f() } else {};   // Expression is an `if`, not a call.
> match true {               // Expression is a `match`, not a call.
>     _ => f()
> };
> ```
>
> ```rust,compile_fail
> #![deny(unused_must_use)]
> #[must_use]
> struct MustUse;
> fn g() -> MustUse { MustUse }
>
> // Despite the `if` expression not being a call, the type-based check
> // fires because the type of the expression is `MustUse`, which has
> // the `#[must_use]` attribute.
> if true { g() } else { MustUse }; // ERROR: Must be used.
> ```

r[attributes.diagnostics.must_use.underscore-idiom]
> [!NOTE]
> Using a [let statement] or [destructuring assignment] with a pattern of `_` when a must-used value is purposely discarded is idiomatic.
>
> ```rust
> #![deny(unused_must_use)]
> #[must_use]
> fn f() {}
> let _ = f(); // OK.
> _ = f(); // OK.
> ```

r[attributes.diagnostic.namespace]
## The `diagnostic` tool attribute namespace

r[attributes.diagnostic.namespace.intro]
The `#[diagnostic]` attribute namespace is a home for attributes to influence compile-time error messages.
The hints provided by these attributes are not guaranteed to be used.

r[attributes.diagnostic.namespace.unknown-invalid-syntax]
Unknown attributes in this namespace are accepted, though they may emit warnings for unused attributes.
Additionally, invalid inputs to known attributes will typically be a warning (see the attribute definitions for details).
This is meant to allow adding or discarding attributes and changing inputs in the future to allow changes without the need to keep the non-meaningful attributes or options working.

r[attributes.diagnostic.on_unimplemented]
### The `diagnostic::on_unimplemented` attribute

r[attributes.diagnostic.on_unimplemented.intro]
The `#[diagnostic::on_unimplemented]` attribute is a hint to the compiler to supplement the error message that would normally be generated in scenarios where a trait is required but not implemented on a type.

r[attributes.diagnostic.on_unimplemented.allowed-positions]
The attribute should be placed on a [trait declaration], though it is not an error to be located in other positions.

r[attributes.diagnostic.on_unimplemented.syntax]
The attribute uses the [MetaListNameValueStr] syntax to specify its inputs, though any malformed input to the attribute is not considered as an error to provide both forwards and backwards compatibility.

r[attributes.diagnostic.on_unimplemented.keys]
The following keys have the given meaning:
* `message` --- The text for the top level error message.
* `label` --- The text for the label shown inline in the broken code in the error message.
* `note` --- Provides additional notes.

r[attributes.diagnostic.on_unimplemented.note-repetition]
The `note` option can appear several times, which results in several note messages being emitted.

r[attributes.diagnostic.on_unimplemented.repetition]
If any of the other options appears several times the first occurrence of the relevant option specifies the actually used value. Subsequent occurrences generates a warning.

r[attributes.diagnostic.on_unimplemented.unknown-keys]
A warning is generated for any unknown keys.

r[attributes.diagnostic.on_unimplemented.format-string]
All three options accept a string as an argument, interpreted using the same formatting as a [`std::fmt`] string.

r[attributes.diagnostic.on_unimplemented.format-parameters]
Format parameters with the given named parameter will be replaced with the following text:
* `{Self}` --- The name of the type implementing the trait.
* `{` *GenericParameterName* `}` --- The name of the generic argument's type for the given generic parameter.

r[attributes.diagnostic.on_unimplemented.invalid-formats]
Any other format parameter will generate a warning, but will otherwise be included in the string as-is.

r[attributes.diagnostic.on_unimplemented.invalid-string]
Invalid format strings may generate a warning, but are otherwise allowed, but may not display as intended.
Format specifiers may generate a warning, but are otherwise ignored.

In this example:

```rust,compile_fail,E0277
#[diagnostic::on_unimplemented(
    message = "My Message for `ImportantTrait<{A}>` implemented for `{Self}`",
    label = "My Label",
    note = "Note 1",
    note = "Note 2"
)]
trait ImportantTrait<A> {}

fn use_my_trait(_: impl ImportantTrait<i32>) {}

fn main() {
    use_my_trait(String::new());
}
```

the compiler may generate an error message which looks like this:

```text
error[E0277]: My Message for `ImportantTrait<i32>` implemented for `String`
  --> src/main.rs:14:18
   |
14 |     use_my_trait(String::new());
   |     ------------ ^^^^^^^^^^^^^ My Label
   |     |
   |     required by a bound introduced by this call
   |
   = help: the trait `ImportantTrait<i32>` is not implemented for `String`
   = note: Note 1
   = note: Note 2
```

r[attributes.diagnostic.do_not_recommend]
### The `diagnostic::do_not_recommend` attribute

r[attributes.diagnostic.do_not_recommend.intro]
The `#[diagnostic::do_not_recommend]` attribute is a hint to the compiler to not show the annotated trait implementation as part of a diagnostic message.

> [!NOTE]
> Suppressing the recommendation can be useful if you know that the recommendation would normally not be useful to the programmer. This often occurs with broad, blanket impls. The recommendation may send the programmer down the wrong path, or the trait implementation may be an internal detail that you don't want to expose, or the bounds may not be able to be satisfied by the programmer.
>
> For example, in an error message about a type not implementing a required trait, the compiler may find a trait implementation that would satisfy the requirements if it weren't for specific bounds in the trait implementation. The compiler may tell the user that there is an impl, but the problem is the bounds in the trait implementation. The `#[diagnostic::do_not_recommend]` attribute can be used to tell the compiler to *not* tell the user about the trait implementation, and instead simply tell the user the type doesn't implement the required trait.

r[attributes.diagnostic.do_not_recommend.allowed-positions]
The attribute should be placed on a [trait implementation item][trait-impl], though it is not an error to be located in other positions.

r[attributes.diagnostic.do_not_recommend.syntax]
The attribute does not accept any arguments, though unexpected arguments are not considered as an error.

In the following example, there is a trait called `AsExpression` which is used for casting arbitrary types to the `Expression` type used in an SQL library. There is a method called `check` which takes an `AsExpression`.

```rust,compile_fail,E0277
# pub trait Expression {
#     type SqlType;
# }
#
# pub trait AsExpression<ST> {
#     type Expression: Expression<SqlType = ST>;
# }
#
# pub struct Text;
# pub struct Integer;
#
# pub struct Bound<T>(T);
# pub struct SelectInt;
#
# impl Expression for SelectInt {
#     type SqlType = Integer;
# }
#
# impl<T> Expression for Bound<T> {
#     type SqlType = T;
# }
#
# impl AsExpression<Integer> for i32 {
#     type Expression = Bound<Integer>;
# }
#
# impl AsExpression<Text> for &'_ str {
#     type Expression = Bound<Text>;
# }
#
# impl<T> Foo for T where T: Expression {}

// Uncomment this line to change the recommendation.
// #[diagnostic::do_not_recommend]
impl<T, ST> AsExpression<ST> for T
where
    T: Expression<SqlType = ST>,
{
    type Expression = T;
}

trait Foo: Expression + Sized {
    fn check<T>(&self, _: T) -> <T as AsExpression<<Self as Expression>::SqlType>>::Expression
    where
        T: AsExpression<Self::SqlType>,
    {
        todo!()
    }
}

fn main() {
    SelectInt.check("bar");
}
```

The `SelectInt` type's `check` method is expecting an `Integer` type. Calling it with an i32 type works, as it gets converted to an `Integer` by the `AsExpression` trait. However, calling it with a string does not, and generates a an error that may look like this:

```text
error[E0277]: the trait bound `&str: Expression` is not satisfied
  --> src/main.rs:53:15
   |
53 |     SelectInt.check("bar");
   |               ^^^^^ the trait `Expression` is not implemented for `&str`
   |
   = help: the following other types implement trait `Expression`:
             Bound<T>
             SelectInt
note: required for `&str` to implement `AsExpression<Integer>`
  --> src/main.rs:45:13
   |
45 | impl<T, ST> AsExpression<ST> for T
   |             ^^^^^^^^^^^^^^^^     ^
46 | where
47 |     T: Expression<SqlType = ST>,
   |        ------------------------ unsatisfied trait bound introduced here
```

By adding the `#[diagnostic::do_not_recommend]` attribute to the blanket `impl` for `AsExpression`, the message changes to:

```text
error[E0277]: the trait bound `&str: AsExpression<Integer>` is not satisfied
  --> src/main.rs:53:15
   |
53 |     SelectInt.check("bar");
   |               ^^^^^ the trait `AsExpression<Integer>` is not implemented for `&str`
   |
   = help: the trait `AsExpression<Integer>` is not implemented for `&str`
           but trait `AsExpression<Text>` is implemented for it
   = help: for that trait implementation, expected `Text`, found `Integer`
```

The first error message includes a somewhat confusing error message about the relationship of `&str` and `Expression`, as well as the unsatisfied trait bound in the blanket impl. After adding `#[diagnostic::do_not_recommend]`, it no longer considers the blanket impl for the recommendation. The message should be a little clearer, with an indication that a string cannot be converted to an `Integer`.

[Clippy]: https://github.com/rust-lang/rust-clippy
[`Drop`]: ../special-types-and-traits.md#drop
[`unsafe` blocks]: ../expressions/block-expr.md#unsafe-blocks
[attribute]: ../attributes.md
[attributes]: ../attributes.md
[block expression]: ../expressions/block-expr.md
[call expression]: ../expressions/call-expr.md
[destructuring assignment]: expr.assign.destructure
[method call expression]: ../expressions/method-call-expr.md
[dyn trait]: ../types/trait-object.md
[enum variant]: ../items/enumerations.md
[enumeration]: ../items/enumerations.md
[expression statement]: ../statements.md#expression-statements
[expression]: ../expressions.md
[external block item]: ../items/external-blocks.md
[functions]: ../items/functions.md
[impl trait]: ../types/impl-trait.md
[implementation]: ../items/implementations.md
[item]: ../items.md
[labeled block expressions]: ../expressions/block-expr.md#labeled-block-expressions
[let statement]: ../statements.md#let-statements
[macro definition]: ../macros-by-example.md
[module]: ../items/modules.md
[rustc book]: ../../rustc/lints/index.html
[rustc-lint-caps]: ../../rustc/lints/levels.html#capping-lints
[rustc-lint-cli]: ../../rustc/lints/levels.html#via-compiler-flag
[rustdoc]: ../../rustdoc/lints.html
[struct field]: ../items/structs.md
[struct]: ../items/structs.md
[external block]: ../items/external-blocks.md
[trait declaration]: ../items/traits.md
[trait item]: ../items/traits.md
[trait-impl]: ../items/implementations.md#trait-implementations
[traits]: ../items/traits.md
[uninhabited]: glossary.uninhabited
[union]: ../items/unions.md


---

r[attributes.codegen]
# Code generation attributes

The following [attributes] are used for controlling code generation.

<!-- template:attributes -->
r[attributes.codegen.inline]
### The `inline` attribute

r[attributes.codegen.inline.intro]
The *`inline` [attribute]* suggests whether a copy of the attributed function's code should be placed in the caller rather than generating a call to the function.

> [!EXAMPLE]
> ```rust
> #[inline]
> pub fn example1() {}
>
> #[inline(always)]
> pub fn example2() {}
>
> #[inline(never)]
> pub fn example3() {}
> ```

> [!NOTE]
> `rustc` automatically inlines functions when doing so seems worthwhile. Use this attribute carefully as poor decisions about what to inline can slow down programs.

r[attributes.codegen.inline.syntax]
The syntax for the `inline` attribute is:

```grammar,attributes
@root InlineAttribute ->
      `inline` `(` `always` `)`
    | `inline` `(` `never` `)`
    | `inline`
```

r[attributes.codegen.inline.allowed-positions]
The `inline` attribute may only be applied to functions with [bodies] --- [closures], [async blocks], [free functions], [associated functions] in an [inherent impl] or [trait impl], and associated functions in a [trait definition] when those functions have a [default definition] .

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

> [!NOTE]
> Though the attribute can be applied to [closures] and [async blocks], the usefulness of this is limited as we do not yet support attributes on expressions.
>
> ```rust
> // We allow attributes on statements.
> #[inline] || (); // OK
> #[inline] async {}; // OK
> ```
>
> ```rust,compile_fail,E0658
> // We don't yet allow attributes on expressions.
> let f = #[inline] || (); // ERROR
> ```

r[attributes.codegen.inline.duplicates]
Only the first use of `inline` on a function has effect.

> [!NOTE]
> `rustc` lints against any use following the first. This may become an error in the future.

r[attributes.codegen.inline.modes]
The `inline` attribute supports these modes:

- `#[inline]` *suggests* performing inline expansion.
- `#[inline(always)]` *suggests* that inline expansion should always be performed.
- `#[inline(never)]` *suggests* that inline expansion should never be performed.

> [!NOTE]
> In every form the attribute is a hint. The compiler may ignore it.

r[attributes.codegen.inline.trait]
When `inline` is applied to a function in a [trait], it applies only to the code of the [default definition].

r[attributes.codegen.inline.async]
When `inline` is applied to an [async function] or [async closure], it applies only to the code of the generated `poll` function.

> [!NOTE]
> For more details, see [Rust issue #129347](https://github.com/rust-lang/rust/issues/129347).

r[attributes.codegen.inline.externally-exported]
The `inline` attribute is ignored if the function is externally exported with [`no_mangle`] or [`export_name`].

<!-- template:attributes -->
r[attributes.codegen.cold]
### The `cold` attribute

r[attributes.codegen.cold.intro]
The *`cold` [attribute]* suggests that the attributed function is unlikely to be called which may help the compiler produce better code.

> [!EXAMPLE]
> ```rust
> #[cold]
> pub fn example() {}
> ```

r[attributes.codegen.cold.syntax]
The `cold` attribute uses the [MetaWord] syntax.

r[attributes.codegen.cold.allowed-positions]
The `cold` attribute may only be applied to functions with [bodies] --- [closures], [async blocks], [free functions], [associated functions] in an [inherent impl] or [trait impl], and associated functions in a [trait definition] when those functions have a [default definition] .

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

> [!NOTE]
> Though the attribute can be applied to [closures] and [async blocks], the usefulness of this is limited as we do not yet support attributes on expressions.

<!-- TODO: rustc currently seems to allow cold on a trait function without a body, but it appears to be ignored. I think that may be a bug, and it should at least warn if not reject (like inline does). -->

r[attributes.codegen.cold.duplicates]
Only the first use of `cold` on a function has effect.

> [!NOTE]
> `rustc` lints against any use following the first. This may become an error in the future.

r[attributes.codegen.cold.trait]
When `cold` is applied to a function in a [trait], it applies only to the code of the [default definition].

r[attributes.codegen.naked]
## The `naked` attribute

r[attributes.codegen.naked.intro]
The *`naked` [attribute]* prevents the compiler from emitting a function prologue and epilogue for the attributed function.

r[attributes.codegen.naked.body]
The [function body] must consist of exactly one [`naked_asm!`] macro invocation.

r[attributes.codegen.naked.prologue-epilogue]
No function prologue or epilogue is generated for the attributed function. The assembly code in the `naked_asm!` block constitutes the full body of a naked function.

r[attributes.codegen.naked.unsafe-attribute]
The `naked` attribute is an [unsafe attribute]. Annotating a function with `#[unsafe(naked)]` comes with the safety obligation that the body must respect the function's calling convention, uphold its signature, and either return or diverge (i.e., not fall through past the end of the assembly code).

r[attributes.codegen.naked.call-stack]
The assembly code may assume that the call stack and register state are valid on entry as per the signature and calling convention of the function.

r[attributes.codegen.naked.no-duplication]
The assembly code may not be duplicated by the compiler except when monomorphizing polymorphic functions.

> [!NOTE]
> Guaranteeing when the assembly code may or may not be duplicated is important for naked functions that define symbols.

r[attributes.codegen.naked.unused-variables]
The [`unused_variables`] lint is suppressed within naked functions.

r[attributes.codegen.naked.inline]
The [`inline`](#the-inline-attribute) attribute cannot by applied to a naked function.

r[attributes.codegen.naked.track_caller]
The [`track_caller`](#the-track_caller-attribute) attribute cannot be applied to a naked function.

r[attributes.codegen.naked.testing]
The [testing attributes](testing.md) cannot be applied to a naked function.

<!-- template:attributes -->
r[attributes.codegen.no_builtins]
## The `no_builtins` attribute

r[attributes.codegen.no_builtins.intro]
The *`no_builtins` [attribute]* disables optimization of certain code patterns related to calls to library functions that are assumed to exist.

<!-- TODO: This needs expanding, see <https://github.com/rust-lang/reference/issues/542>. -->

> [!EXAMPLE]
> ```rust
> #![no_builtins]
> ```

r[attributes.codegen.no_builtins.syntax]
The `no_builtins` attribute uses the [MetaWord] syntax.

r[attributes.codegen.no_builtins.allowed-positions]
The `no_builtins` attribute can only be applied to the crate root.

r[attributes.codegen.no_builtins.duplicates]
Only the first use of the `no_builtins` attribute has effect.

> [!NOTE]
> `rustc` lints against any use following the first.

r[attributes.codegen.target_feature]
## The `target_feature` attribute

r[attributes.codegen.target_feature.intro]
The *`target_feature` [attribute]* may be applied to a function to
enable code generation of that function for specific platform architecture
features. It uses the [MetaListNameValueStr] syntax with a single key of
`enable` whose value is a string of comma-separated feature names to enable.

```rust
# #[cfg(target_feature = "avx2")]
#[target_feature(enable = "avx2")]
fn foo_avx2() {}
```

r[attributes.codegen.target_feature.arch]
Each [target architecture] has a set of features that may be enabled. It is an
error to specify a feature for a target architecture that the crate is not
being compiled for.

r[attributes.codegen.target_feature.closures]
Closures defined within a `target_feature`-annotated function inherit the
attribute from the enclosing function.

r[attributes.codegen.target_feature.target-ub]
It is [undefined behavior] to call a function that is compiled with a feature
that is not supported on the current platform the code is running on, *except*
if the platform explicitly documents this to be safe.

r[attributes.codegen.target_feature.safety-restrictions]
The following restrictions apply unless otherwise specified by the platform rules below:

- Safe `#[target_feature]` functions (and closures that inherit the attribute) can only be safely called within a caller that enables all the `target_feature`s that the callee enables.
  This restriction does not apply in an `unsafe` context.
- Safe `#[target_feature]` functions (and closures that inherit the attribute) can only be coerced to *safe* function pointers in contexts that enable all the `target_feature`s that the coercee enables.
  This restriction does not apply to `unsafe` function pointers.

Implicitly enabled features are included in this rule. For example an `sse2` function can call ones marked with `sse`.

```rust
# #[cfg(target_feature = "sse2")] {
#[target_feature(enable = "sse")]
fn foo_sse() {}

fn bar() {
    // Calling `foo_sse` here is unsafe, as we must ensure that SSE is
    // available first, even if `sse` is enabled by default on the target
    // platform or manually enabled as compiler flags.
    unsafe {
        foo_sse();
    }
}

#[target_feature(enable = "sse")]
fn bar_sse() {
    // Calling `foo_sse` here is safe.
    foo_sse();
    || foo_sse();
}

#[target_feature(enable = "sse2")]
fn bar_sse2() {
    // Calling `foo_sse` here is safe because `sse2` implies `sse`.
    foo_sse();
}
# }
```

r[attributes.codegen.target_feature.fn-traits]
A function with a `#[target_feature]` attribute *never* implements the `Fn` family of traits, although closures inheriting features from the enclosing function do.

r[attributes.codegen.target_feature.allowed-positions]
The `#[target_feature]` attribute is not allowed on the following places:

- [the `main` function][crate.main]
- a [`panic_handler` function][panic.panic_handler]
- safe trait methods
- safe default functions in traits

r[attributes.codegen.target_feature.inline]
Functions marked with `target_feature` are not inlined into a context that
does not support the given features. The `#[inline(always)]` attribute may not
be used with a `target_feature` attribute.

r[attributes.codegen.target_feature.availability]
### Available features

The following is a list of the available feature names.

r[attributes.codegen.target_feature.x86]
#### `x86` or `x86_64`

Executing code with unsupported features is undefined behavior on this platform.
Hence on this platform use of `#[target_feature]` functions follows the
[above restrictions][attributes.codegen.target_feature.safety-restrictions].

Feature     | Implicitly Enables | Description
------------|--------------------|-------------------
`adx`       |          | [ADX] --- Multi-Precision Add-Carry Instruction Extensions
`aes`       | `sse2`   | [AES] --- Advanced Encryption Standard
`avx`       | `sse4.2` | [AVX] --- Advanced Vector Extensions
`avx2`      | `avx`    | [AVX2] --- Advanced Vector Extensions 2
`avx512bf16`        | `avx512bw`           | [AVX512-BF16] --- Advanced Vector Extensions 512-bit - Bfloat16 Extensions
`avx512bitalg`      | `avx512bw`           | [AVX512-BITALG] --- Advanced Vector Extensions 512-bit - Bit Algorithms
`avx512bw`          | `avx512f`            | [AVX512-BW] --- Advanced Vector Extensions 512-bit - Byte and Word Instructions
`avx512cd`          | `avx512f`            | [AVX512-CD] --- Advanced Vector Extensions 512-bit - Conflict Detection Instructions
`avx512dq`          | `avx512f`            | [AVX512-DQ] --- Advanced Vector Extensions 512-bit - Doubleword and Quadword Instructions
`avx512f`           | `avx2`, `fma`, `f16c`| [AVX512-F] --- Advanced Vector Extensions 512-bit - Foundation
`avx512fp16`        | `avx512bw`           | [AVX512-FP16] --- Advanced Vector Extensions 512-bit - Float16 Extensions
`avx512ifma`        | `avx512f`            | [AVX512-IFMA] --- Advanced Vector Extensions 512-bit - Integer Fused Multiply Add
`avx512vbmi`        | `avx512bw`           | [AVX512-VBMI] --- Advanced Vector Extensions 512-bit - Vector Byte Manipulation Instructions
`avx512vbmi2`       | `avx512bw`           | [AVX512-VBMI2] --- Advanced Vector Extensions 512-bit - Vector Byte Manipulation Instructions 2
`avx512vl`          | `avx512f`            | [AVX512-VL] --- Advanced Vector Extensions 512-bit - Vector Length Extensions
`avx512vnni`        | `avx512f`            | [AVX512-VNNI] --- Advanced Vector Extensions 512-bit - Vector Neural Network Instructions
`avx512vp2intersect`| `avx512f`            | [AVX512-VP2INTERSECT] --- Advanced Vector Extensions 512-bit - Vector Pair Intersection to a Pair of Mask Registers
`avx512vpopcntdq`   | `avx512f`            | [AVX512-VPOPCNTDQ] --- Advanced Vector Extensions 512-bit - Vector Population Count Instruction
`avxifma`           | `avx2`               | [AVX-IFMA] --- Advanced Vector Extensions - Integer Fused Multiply Add
`avxneconvert`      | `avx2`               | [AVX-NE-CONVERT] --- Advanced Vector Extensions - No-Exception Floating-Point conversion Instructions
`avxvnni`           | `avx2`               | [AVX-VNNI] --- Advanced Vector Extensions - Vector Neural Network Instructions
`avxvnniint16`      | `avx2`               | [AVX-VNNI-INT16] --- Advanced Vector Extensions - Vector Neural Network Instructions with 16-bit Integers
`avxvnniint8`       | `avx2`               | [AVX-VNNI-INT8] --- Advanced Vector Extensions - Vector Neural Network Instructions with 8-bit Integers
`bmi1`      |          | [BMI1] --- Bit Manipulation Instruction Sets
`bmi2`      |          | [BMI2] --- Bit Manipulation Instruction Sets 2
`cmpxchg16b`|          | [`cmpxchg16b`] --- Compares and exchange 16 bytes (128 bits) of data atomically
`f16c`      | `avx`    | [F16C] --- 16-bit floating point conversion instructions
`fma`       | `avx`    | [FMA3] --- Three-operand fused multiply-add
`fxsr`      |          | [`fxsave`] and [`fxrstor`] --- Save and restore x87 FPU, MMX Technology, and SSE State
`gfni`      | `sse2`   | [GFNI] --- Galois Field New Instructions
`kl`        | `sse2`   | [KEYLOCKER] --- Intel Key Locker Instructions
`lzcnt`     |          | [`lzcnt`] --- Leading zeros count
`movbe`     |          | [`movbe`] --- Move data after swapping bytes
`pclmulqdq` | `sse2`   | [`pclmulqdq`] --- Packed carry-less multiplication quadword
`popcnt`    |          | [`popcnt`] --- Count of bits set to 1
`rdrand`    |          | [`rdrand`] --- Read random number
`rdseed`    |          | [`rdseed`] --- Read random seed
`sha`       | `sse2`   | [SHA] --- Secure Hash Algorithm
`sha512`    | `avx2`   | [SHA512] --- Secure Hash Algorithm with 512-bit digest
`sm3`       | `avx`    | [SM3] --- ShangMi 3 Hash Algorithm
`sm4`       | `avx2`   | [SM4] --- ShangMi 4 Cipher Algorithm
`sse`       |          | [SSE] --- Streaming <abbr title="Single Instruction Multiple Data">SIMD</abbr> Extensions
`sse2`      | `sse`    | [SSE2] --- Streaming SIMD Extensions 2
`sse3`      | `sse2`   | [SSE3] --- Streaming SIMD Extensions 3
`sse4.1`    | `ssse3`  | [SSE4.1] --- Streaming SIMD Extensions 4.1
`sse4.2`    | `sse4.1` | [SSE4.2] --- Streaming SIMD Extensions 4.2
`sse4a`     | `sse3`   | [SSE4a] --- Streaming SIMD Extensions 4a
`ssse3`     | `sse3`   | [SSSE3] --- Supplemental Streaming SIMD Extensions 3
`tbm`       |          | [TBM] --- Trailing Bit Manipulation
`vaes`      | `avx2`, `aes`     | [VAES] --- Vector AES Instructions
`vpclmulqdq`| `avx`, `pclmulqdq`| [VPCLMULQDQ] --- Vector Carry-less multiplication of Quadwords
`widekl`    | `kl`     | [KEYLOCKER_WIDE] --- Intel Wide Keylocker Instructions
`xsave`     |          | [`xsave`] --- Save processor extended states
`xsavec`    |          | [`xsavec`] --- Save processor extended states with compaction
`xsaveopt`  |          | [`xsaveopt`] --- Save processor extended states optimized
`xsaves`    |          | [`xsaves`] --- Save processor extended states supervisor

<!-- Keep links near each table to make it easier to move and update. -->

[ADX]: https://en.wikipedia.org/wiki/Intel_ADX
[AES]: https://en.wikipedia.org/wiki/AES_instruction_set
[AVX]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions
[AVX2]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX2
[AVX512-BF16]: https://en.wikipedia.org/wiki/AVX-512#BF16
[AVX512-BITALG]: https://en.wikipedia.org/wiki/AVX-512#VPOPCNTDQ_and_BITALG
[AVX512-BW]: https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI
[AVX512-CD]: https://en.wikipedia.org/wiki/AVX-512#Conflict_detection
[AVX512-DQ]: https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI
[AVX512-F]: https://en.wikipedia.org/wiki/AVX-512
[AVX512-FP16]: https://en.wikipedia.org/wiki/AVX-512#FP16
[AVX512-IFMA]: https://en.wikipedia.org/wiki/AVX-512#IFMA
[AVX512-VBMI]: https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI
[AVX512-VBMI2]: https://en.wikipedia.org/wiki/AVX-512#VBMI2
[AVX512-VL]: https://en.wikipedia.org/wiki/AVX-512
[AVX512-VNNI]: https://en.wikipedia.org/wiki/AVX-512#VNNI
[AVX512-VP2INTERSECT]: https://en.wikipedia.org/wiki/AVX-512#VP2INTERSECT
[AVX512-VPOPCNTDQ]:https://en.wikipedia.org/wiki/AVX-512#VPOPCNTDQ_and_BITALG
[AVX-IFMA]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA
[AVX-NE-CONVERT]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA
[AVX-VNNI]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA
[AVX-VNNI-INT16]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA
[AVX-VNNI-INT8]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA
[BMI1]: https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets
[BMI2]: https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets#BMI2
[`cmpxchg16b`]: https://www.felixcloutier.com/x86/cmpxchg8b:cmpxchg16b
[F16C]: https://en.wikipedia.org/wiki/F16C
[FMA3]: https://en.wikipedia.org/wiki/FMA_instruction_set
[`fxsave`]: https://www.felixcloutier.com/x86/fxsave
[`fxrstor`]: https://www.felixcloutier.com/x86/fxrstor
[GFNI]: https://en.wikipedia.org/wiki/AVX-512#GFNI
[KEYLOCKER]: https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_Key_Locker_instructions
[KEYLOCKER_WIDE]: https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_Key_Locker_instructions
[`lzcnt`]: https://www.felixcloutier.com/x86/lzcnt
[`movbe`]: https://www.felixcloutier.com/x86/movbe
[`pclmulqdq`]: https://www.felixcloutier.com/x86/pclmulqdq
[`popcnt`]: https://www.felixcloutier.com/x86/popcnt
[`rdrand`]: https://en.wikipedia.org/wiki/RdRand
[`rdseed`]: https://en.wikipedia.org/wiki/RdRand
[SHA]: https://en.wikipedia.org/wiki/Intel_SHA_extensions
[SHA512]: https://en.wikipedia.org/wiki/Intel_SHA_extensions
[SM3]: https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_SHA_and_SM3_instructions
[SM4]: https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_SHA_and_SM3_instructions
[SSE]: https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions
[SSE2]: https://en.wikipedia.org/wiki/SSE2
[SSE3]: https://en.wikipedia.org/wiki/SSE3
[SSE4.1]: https://en.wikipedia.org/wiki/SSE4#SSE4.1
[SSE4.2]: https://en.wikipedia.org/wiki/SSE4#SSE4.2
[SSE4a]: https://en.wikipedia.org/wiki/SSE4#SSE4a
[SSSE3]: https://en.wikipedia.org/wiki/SSSE3
[TBM]: https://en.wikipedia.org/wiki/X86_Bit_manipulation_instruction_set#TBM_(Trailing_Bit_Manipulation)
[VAES]: https://en.wikipedia.org/wiki/AVX-512#VAES
[VPCLMULQDQ]: https://en.wikipedia.org/wiki/AVX-512#VPCLMULQDQ
[`xsave`]: https://www.felixcloutier.com/x86/xsave
[`xsavec`]: https://www.felixcloutier.com/x86/xsavec
[`xsaveopt`]: https://www.felixcloutier.com/x86/xsaveopt
[`xsaves`]: https://www.felixcloutier.com/x86/xsaves

r[attributes.codegen.target_feature.aarch64]
#### `aarch64`

On this platform the use of `#[target_feature]` functions follows the
[above restrictions][attributes.codegen.target_feature.safety-restrictions].

Further documentation on these features can be found in the [ARM Architecture
Reference Manual], or elsewhere on [developer.arm.com].

[ARM Architecture Reference Manual]: https://developer.arm.com/documentation/ddi0487/latest
[developer.arm.com]: https://developer.arm.com

> [!NOTE]
> The following pairs of features should both be marked as enabled or disabled together if used:
> - `paca` and `pacg`, which LLVM currently implements as one feature.

Feature        | Implicitly Enables | Feature Name
-------        | ------------------ | ------------
`aes`          | `neon`             | FEAT_AES & FEAT_PMULL --- Advanced <abbr title="Single Instruction Multiple Data">SIMD</abbr> AES & PMULL instructions
`bf16`         |                    | FEAT_BF16 --- BFloat16 instructions
`bti`          |                    | FEAT_BTI --- Branch Target Identification
`crc`          |                    | FEAT_CRC --- CRC32 checksum instructions
`dit`          |                    | FEAT_DIT  --- Data Independent Timing instructions
`dotprod`      | `neon`             | FEAT_DotProd --- Advanced SIMD Int8 dot product instructions
`dpb`          |                    | FEAT_DPB --- Data cache clean to point of persistence
`dpb2`         | `dpb`              | FEAT_DPB2 --- Data cache clean to point of deep persistence
`f32mm`        | `sve`              | FEAT_F32MM --- SVE single-precision FP matrix multiply instruction
`f64mm`        | `sve`              | FEAT_F64MM --- SVE double-precision FP matrix multiply instruction
`fcma`         | `neon`             | FEAT_FCMA --- Floating point complex number support
`fhm`          | `fp16`             | FEAT_FHM --- Half-precision FP FMLAL instructions
`flagm`        |                    | FEAT_FLAGM --- Conditional flag manipulation
`fp16`         | `neon`             | FEAT_FP16 --- Half-precision FP data processing
`frintts`      |                    | FEAT_FRINTTS --- Floating-point to int helper instructions
`i8mm`         |                    | FEAT_I8MM --- Int8 Matrix Multiplication
`jsconv`       | `neon`             | FEAT_JSCVT --- JavaScript conversion instruction
`lor`          |                    | FEAT_LOR --- Limited Ordering Regions extension
`lse`          |                    | FEAT_LSE --- Large System Extensions
`mte`          |                    | FEAT_MTE & FEAT_MTE2 --- Memory Tagging Extension
`neon`         |                    | FEAT_AdvSimd & FEAT_FP --- Floating Point and Advanced SIMD extension
`paca`         |                    | FEAT_PAUTH --- Pointer Authentication (address authentication)
`pacg`         |                    | FEAT_PAUTH --- Pointer Authentication (generic authentication)
`pan`          |                    | FEAT_PAN --- Privileged Access-Never extension
`pmuv3`        |                    | FEAT_PMUv3 --- Performance Monitors extension (v3)
`rand`         |                    | FEAT_RNG --- Random Number Generator
`ras`          |                    | FEAT_RAS & FEAT_RASv1p1 --- Reliability, Availability and Serviceability extension
`rcpc`         |                    | FEAT_LRCPC --- Release consistent Processor Consistent
`rcpc2`        | `rcpc`             | FEAT_LRCPC2 --- RcPc with immediate offsets
`rdm`          | `neon`             | FEAT_RDM --- Rounding Double Multiply accumulate
`sb`           |                    | FEAT_SB --- Speculation Barrier
`sha2`         | `neon`             | FEAT_SHA1 & FEAT_SHA256 --- Advanced SIMD SHA instructions
`sha3`         | `sha2`             | FEAT_SHA512 & FEAT_SHA3 --- Advanced SIMD SHA instructions
`sm4`          | `neon`             | FEAT_SM3 & FEAT_SM4 --- Advanced SIMD SM3/4 instructions
`spe`          |                    | FEAT_SPE --- Statistical Profiling Extension
`ssbs`         |                    | FEAT_SSBS & FEAT_SSBS2 --- Speculative Store Bypass Safe
`sve`          | `neon`             | FEAT_SVE --- Scalable Vector Extension
`sve2`         | `sve`              | FEAT_SVE2 --- Scalable Vector Extension 2
`sve2-aes`     | `sve2`, `aes`      | FEAT_SVE_AES & FEAT_SVE_PMULL128 --- SVE AES instructions
`sve2-bitperm` | `sve2`             | FEAT_SVE2_BitPerm --- SVE Bit Permute
`sve2-sha3`    | `sve2`, `sha3`     | FEAT_SVE2_SHA3 --- SVE SHA3 instructions
`sve2-sm4`     | `sve2`, `sm4`      | FEAT_SVE2_SM4 --- SVE SM4 instructions
`tme`          |                    | FEAT_TME --- Transactional Memory Extension
`vh`           |                    | FEAT_VHE --- Virtualization Host Extensions

r[attributes.codegen.target_feature.loongarch]
#### `loongarch`

On this platform the use of `#[target_feature]` functions follows the
[above restrictions][attributes.codegen.target_feature.safety-restrictions].

Feature     | Implicitly Enables  | Description
------------|---------------------|-------------------
`f`         |                     | [F][la-f] --- Single-precision float-point instructions
`d`         | `f`                 | [D][la-d] --- Double-precision float-point instructions
`frecipe`   |                     | [FRECIPE][la-frecipe] --- Reciprocal approximation instructions
`lasx`      | `lsx`               | [LASX][la-lasx] --- 256-bit vector instructions
`lbt`       |                     | [LBT][la-lbt] --- Binary translation instructions
`lsx`       | `d`                 | [LSX][la-lsx] --- 128-bit vector instructions
`lvz`       |                     | [LVZ][la-lvz] --- Virtualization instructions

<!-- Keep links near each table to make it easier to move and update. -->

[la-f]: https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-fp_sp
[la-d]: https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-fp_dp
[la-frecipe]: https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-frecipe
[la-lasx]: https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lasx
[la-lbt]: https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lbt_x86
[la-lsx]: https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lsx
[la-lvz]: https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lvz

r[attributes.codegen.target_feature.riscv]
#### `riscv32` or `riscv64`

On this platform the use of `#[target_feature]` functions follows the
[above restrictions][attributes.codegen.target_feature.safety-restrictions].

Further documentation on these features can be found in their respective
specification. Many specifications are described in the [RISC-V ISA Manual],
[version 20250508], or in another manual hosted on the [RISC-V GitHub Account].

[RISC-V ISA Manual]: https://github.com/riscv/riscv-isa-manual
[version 20250508]: https://github.com/riscv/riscv-isa-manual/tree/20250508
[RISC-V GitHub Account]: https://github.com/riscv

Feature     | Implicitly Enables  | Description
------------|---------------------|-------------------
`a`         | `zaamo`, `zalrsc`   | [A][rv-a] --- Atomic instructions
`b`         | `zba`, `zbc`, `zbs` | [B][rv-b] --- Bit Manipulation instructions
`c`         | `zca`               | [C][rv-c] --- Compressed instructions
`m`         |                     | [M][rv-m] --- Integer Multiplication and Division instructions
`za64rs`    | `za128rs`           | [Za64rs][rv-za64rs] --- Platform Behavior: Naturally aligned Reservation sets with ≦ 64 Bytes
`za128rs`   |                     | [Za128rs][rv-za128rs] --- Platform Behavior: Naturally aligned Reservation sets with ≦ 128 Bytes
`zaamo`     |                     | [Zaamo][rv-zaamo] --- Atomic Memory Operation instructions
`zabha`     | `zaamo`             | [Zabha][rv-zabha] --- Byte and Halfword Atomic Memory Operation instructions
`zacas`     | `zaamo`             | [Zacas][rv-zacas] --- Atomic Compare-and-Swap (CAS) instructions
`zalrsc`    |                     | [Zalrsc][rv-zalrsc] --- Load-Reserved/Store-Conditional instructions
`zama16b`   |                     | [Zama16b][rv-zama16b] --- Platform Behavior: Misaligned loads, stores, and AMOs to main memory regions that do not cross a naturally aligned 16-byte boundary are atomic
`zawrs`     |                     | [Zawrs][rv-zawrs] --- Wait-on-Reservation-Set instructions
`zba`       |                     | [Zba][rv-zba] --- Address Generation instructions
`zbb`       |                     | [Zbb][rv-zbb] --- Basic bit-manipulation
`zbc`       | `zbkc`              | [Zbc][rv-zbc] --- Carry-less multiplication
`zbkb`      |                     | [Zbkb][rv-zbkb] --- Bit Manipulation Instructions for Cryptography
`zbkc`      |                     | [Zbkc][rv-zbkc] --- Carry-less multiplication for Cryptography
`zbkx`      |                     | [Zbkx][rv-zbkx] --- Crossbar permutations
`zbs`       |                     | [Zbs][rv-zbs] --- Single-bit instructions
`zca`       |                     | [Zca][rv-zca] --- Compressed instructions: integer part subset
`zcb`       | `zca`               | [Zcb][rv-zcb] --- Simple Code-size Saving Compressed instructions
`zcmop`     | `zca`               | [Zcmop][rv-zcmop] --- Compressed May-Be-Operations
`zic64b`    |                     | [Zic64b][rv-zic64b] --- Platform Behavior: Naturally aligned 64 byte Cache blocks
`zicbom`    |                     | [Zicbom][rv-zicbom] --- Cache-Block Management instructions
`zicbop`    |                     | [Zicbop][rv-zicbop] --- Cache-Block Prefetch Hint instructions
`zicboz`    |                     | [Zicboz][rv-zicboz] --- Cache-Block Zero instruction
`ziccamoa`  |                     | [Ziccamoa][rv-ziccamoa] --- Platform Behavior: Cacheable and Coherent Main memory supports all basic atomic operations
`ziccif`    |                     | [Ziccif][rv-ziccif] --- Platform Behavior: Cacheable and Coherent Main memory supports instruction fetch and fetches of naturally aligned power-of-2 sizes up to `min(ILEN,XLEN)` are atomic
`zicclsm`   |                     | [Zicclsm][rv-zicclsm] --- Platform Behavior: Cacheable and Coherent Main memory supports misaligned load/store accesses
`ziccrse`   |                     | [Ziccrse][rv-ziccrse] --- Platform Behavior: Cacheable and Coherent Main memory guarantees eventual success on LR/SC sequences
`zicntr`    | `zicsr`             | [Zicntr][rv-zicntr] --- Base Counters and Timers
`zicond`    |                     | [Zicond][rv-zicond] --- Integer Conditional Operation instructions
`zicsr`     |                     | [Zicsr][rv-zicsr] --- Control and Status Register (CSR) instructions
`zifencei`  |                     | [Zifencei][rv-zifencei] --- Instruction-Fetch Fence instruction
`zihintntl`   |                   | [Zihintntl][rv-zihintntl] --- Non-Temporal Locality Hint instructions
`zihintpause` |                   | [Zihintpause][rv-zihintpause] --- Pause Hint instruction
`zihpm`     | `zicsr`             | [Zihpm][rv-zihpm] --- Hardware Performance Counters
`zimop`     |                     | [Zimop][rv-zimop] --- May-Be-Operations
`zk`        | `zkn`, `zkr`, `zks`, `zkt`, `zbkb`, `zbkc`, `zkbx` | [Zk][rv-zk] --- Scalar Cryptography
`zkn`       | `zknd`, `zkne`, `zknh`, `zbkb`, `zbkc`, `zkbx`     | [Zkn][rv-zkn] --- NIST Algorithm suite extension
`zknd`      |                                                    | [Zknd][rv-zknd] --- NIST Suite: AES Decryption
`zkne`      |                                                    | [Zkne][rv-zkne] --- NIST Suite: AES Encryption
`zknh`      |                                                    | [Zknh][rv-zknh] --- NIST Suite: Hash Function Instructions
`zkr`       |                                                    | [Zkr][rv-zkr] --- Entropy Source Extension
`zks`       | `zksed`, `zksh`, `zbkb`, `zbkc`, `zkbx`            | [Zks][rv-zks] --- ShangMi Algorithm Suite
`zksed`     |                                                    | [Zksed][rv-zksed] --- ShangMi Suite: SM4 Block Cipher Instructions
`zksh`      |                                                    | [Zksh][rv-zksh] --- ShangMi Suite: SM3 Hash Function Instructions
`zkt`       |                                                    | [Zkt][rv-zkt] --- Data Independent Execution Latency Subset
`ztso`      |                     | [Ztso][rv-ztso] --- Total Store Ordering

<!-- Keep links near each table to make it easier to move and update. -->

[rv-a]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc
[rv-b]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-c]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/c-st-ext.adoc
[rv-m]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/m-st-ext.adoc
[rv-za64rs]: https://github.com/riscv/riscv-profiles/blob/rva23-rvb23-ratified/src/rva23-profile.adoc
[rv-za128rs]: https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc
[rv-zaamo]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc
[rv-zabha]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zabha.adoc
[rv-zacas]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zacas.adoc
[rv-zalrsc]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc
[rv-zama16b]: https://github.com/riscv/riscv-profiles/blob/rva23-rvb23-ratified/src/rva23-profile.adoc
[rv-zawrs]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zawrs.adoc
[rv-zba]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-zbb]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-zbc]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-zbkb]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-zbkc]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-zbkx]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-zbs]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc
[rv-zca]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zc.adoc
[rv-zcb]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zc.adoc
[rv-zcmop]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zimop.adoc
[rv-zic64b]: https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc
[rv-zicbom]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc
[rv-zicbop]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc
[rv-zicboz]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc
[rv-ziccamoa]: https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc
[rv-ziccif]: https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc
[rv-zicclsm]: https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc
[rv-ziccrse]: https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc
[rv-zicntr]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/counters.adoc
[rv-zicond]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zicond.adoc
[rv-zicsr]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zicsr.adoc
[rv-zifencei]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zifencei.adoc
[rv-zihintntl]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zihintntl.adoc
[rv-zihintpause]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zihintpause.adoc
[rv-zihpm]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/counters.adoc
[rv-zimop]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zimop.adoc
[rv-zk]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zkn]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zkne]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zknd]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zknh]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zkr]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zks]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zksed]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zksh]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-zkt]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc
[rv-ztso]: https://github.com/riscv/riscv-isa-manual/blob/20250508/src/ztso-st-ext.adoc

r[attributes.codegen.target_feature.wasm]
#### `wasm32` or `wasm64`

Safe `#[target_feature]` functions may always be used in safe contexts on Wasm
platforms. It is impossible to cause undefined behavior via the
`#[target_feature]` attribute because attempting to use instructions
unsupported by the Wasm engine will fail at load time without the risk of being
interpreted in a way different from what the compiler expected.

Feature               | Implicitly Enables  | Description
----------------------|---------------------|-------------------
`bulk-memory`         |                     | [WebAssembly bulk memory operations proposal][bulk-memory]
`extended-const`      |                     | [WebAssembly extended const expressions proposal][extended-const]
`mutable-globals`     |                     | [WebAssembly mutable global proposal][mutable-globals]
`nontrapping-fptoint` |                     | [WebAssembly non-trapping float-to-int conversion proposal][nontrapping-fptoint]
`relaxed-simd`        | `simd128`           | [WebAssembly relaxed simd proposal][relaxed-simd]
`sign-ext`            |                     | [WebAssembly sign extension operators Proposal][sign-ext]
`simd128`             |                     | [WebAssembly simd proposal][simd128]
`multivalue`          |                     | [WebAssembly multivalue proposal][multivalue]
`reference-types`     |                     | [WebAssembly reference-types proposal][reference-types]
`tail-call`           |                     | [WebAssembly tail-call proposal][tail-call]

[bulk-memory]: https://github.com/WebAssembly/bulk-memory-operations
[extended-const]: https://github.com/WebAssembly/extended-const
[mutable-globals]: https://github.com/WebAssembly/mutable-global
[nontrapping-fptoint]: https://github.com/WebAssembly/nontrapping-float-to-int-conversions
[relaxed-simd]: https://github.com/WebAssembly/relaxed-simd
[sign-ext]: https://github.com/WebAssembly/sign-extension-ops
[simd128]: https://github.com/webassembly/simd
[reference-types]: https://github.com/webassembly/reference-types
[tail-call]: https://github.com/webassembly/tail-call
[multivalue]: https://github.com/webassembly/multi-value

r[attributes.codegen.target_feature.s390x]
#### `s390x`

On `s390x` targets, use of functions with the `#[target_feature]` attribute follows the [above restrictions][attributes.codegen.target_feature.safety-restrictions].

Further documentation on these features can be found in the "Additions to z/Architecture" section of Chapter 1 of the *[z/Architecture Principles of Operation]*.

Feature                                | Implicitly Enables                    | Description
---------------------------------------|---------------------------------------|---------------------
`vector`                               |                                       | 128-bit vector instructions
`vector-enhancements-1`                | `vector`                              | vector enhancements 1
`vector-enhancements-2`                | `vector-enhancements-1`               | vector enhancements 2
`vector-enhancements-3`                | `vector-enhancements-2`               | vector enhancements 3
`vector-packed-decimal`                | `vector`                              | vector packed-decimal
`vector-packed-decimal-enhancement`    | `vector-packed-decimal`               | vector packed-decimal enhancement
`vector-packed-decimal-enhancement-2`  | `vector-packed-decimal-enhancement-2` | vector packed-decimal enhancement 2
`vector-packed-decimal-enhancement-3`  | `vector-packed-decimal-enhancement-3` | vector packed-decimal enhancement 3
`nnp-assist`                           | `vector`                              | nnp assist
`miscellaneous-extensions-2`           |                                       | miscellaneous extensions 2
`miscellaneous-extensions-3`           |                                       | miscellaneous extensions 3
`miscellaneous-extensions-4`           |                                       | miscellaneous extensions 4

[z/Architecture Principles of Operation]: https://publibfp.dhe.ibm.com/epubs/pdf/a227832d.pdf

r[attributes.codegen.target_feature.info]
### Additional information

r[attributes.codegen.target_feature.remark-cfg]
See the [`target_feature` conditional compilation option] for selectively
enabling or disabling compilation of code based on compile-time settings. Note
that this option is not affected by the `target_feature` attribute, and is
only driven by the features enabled for the entire crate.

r[attributes.codegen.target_feature.remark-rt]
Whether a feature is enabled can be checked at runtime using a platform-specific macro from the standard library, for instance [`is_x86_feature_detected`] or [`is_aarch64_feature_detected`].

> [!NOTE]
> `rustc` has a default set of features enabled for each target and CPU. The CPU may be chosen with the [`-C target-cpu`] flag. Individual features may be enabled or disabled for an entire crate with the [`-C target-feature`] flag.

r[attributes.codegen.track_caller]
## The `track_caller` attribute

r[attributes.codegen.track_caller.allowed-positions]
The `track_caller` attribute may be applied to any function with [`"Rust"` ABI][rust-abi]
with the exception of the entry point `fn main`.

r[attributes.codegen.track_caller.traits]
When applied to functions and methods in trait declarations, the attribute applies to all implementations. If the trait provides a
default implementation with the attribute, then the attribute also applies to override implementations.

r[attributes.codegen.track_caller.extern]
When applied to a function in an `extern` block the attribute must also be applied to any linked
implementations, otherwise undefined behavior results. When applied to a function which is made
available to an `extern` block, the declaration in the `extern` block must also have the attribute,
otherwise undefined behavior results.

r[attributes.codegen.track_caller.behavior]
### Behavior

Applying the attribute to a function `f` allows code within `f` to get a hint of the [`Location`] of
the "topmost" tracked call that led to `f`'s invocation. At the point of observation, an
implementation behaves as if it walks up the stack from `f`'s frame to find the nearest frame of an
*unattributed* function `outer`, and it returns the [`Location`] of the tracked call in `outer`.

```rust
#[track_caller]
fn f() {
    println!("{}", std::panic::Location::caller());
}
```

> [!NOTE]
> `core` provides [`core::panic::Location::caller`] for observing caller locations. It wraps the [`core::intrinsics::caller_location`] intrinsic implemented by `rustc`.

> [!NOTE]
> Because the resulting `Location` is a hint, an implementation may halt its walk up the stack early. See [Limitations](#limitations) for important caveats.

#### Examples

When `f` is called directly by `calls_f`, code in `f` observes its callsite within `calls_f`:

```rust
# #[track_caller]
# fn f() {
#     println!("{}", std::panic::Location::caller());
# }
fn calls_f() {
    f(); // <-- f() prints this location
}
```

When `f` is called by another attributed function `g` which is in turn called by `calls_g`, code in
both `f` and `g` observes `g`'s callsite within `calls_g`:

```rust
# #[track_caller]
# fn f() {
#     println!("{}", std::panic::Location::caller());
# }
#[track_caller]
fn g() {
    println!("{}", std::panic::Location::caller());
    f();
}

fn calls_g() {
    g(); // <-- g() prints this location twice, once itself and once from f()
}
```

When `g` is called by another attributed function `h` which is in turn called by `calls_h`, all code
in `f`, `g`, and `h` observes `h`'s callsite within `calls_h`:

```rust
# #[track_caller]
# fn f() {
#     println!("{}", std::panic::Location::caller());
# }
# #[track_caller]
# fn g() {
#     println!("{}", std::panic::Location::caller());
#     f();
# }
#[track_caller]
fn h() {
    println!("{}", std::panic::Location::caller());
    g();
}

fn calls_h() {
    h(); // <-- prints this location three times, once itself, once from g(), once from f()
}
```

And so on.

r[attributes.codegen.track_caller.limits]
### Limitations

r[attributes.codegen.track_caller.hint]
This information is a hint and implementations are not required to preserve it.

r[attributes.codegen.track_caller.decay]
In particular, coercing a function with `#[track_caller]` to a function pointer creates a shim which
appears to observers to have been called at the attributed function's definition site, losing actual
caller information across virtual calls. A common example of this coercion is the creation of a
trait object whose methods are attributed.

> [!NOTE]
> The aforementioned shim for function pointers is necessary because `rustc` implements `track_caller` in a codegen context by appending an implicit parameter to the function ABI, but this would be unsound for an indirect call because the parameter is not a part of the function's type and a given function pointer type may or may not refer to a function with the attribute. The creation of a shim hides the implicit parameter from callers of the function pointer, preserving soundness.

<!-- template:attributes -->
r[attributes.codegen.instruction_set]
## The `instruction_set` attribute

r[attributes.codegen.instruction_set.intro]
The *`instruction_set` [attribute]* specifies the instruction set that a function will use during code generation. This allows mixing more than one instruction set in a single program.

> [!EXAMPLE]
> <!-- ignore: arm-only -->
> ```rust,ignore
> #[instruction_set(arm::a32)]
> fn arm_code() {}
>
> #[instruction_set(arm::t32)]
> fn thumb_code() {}
> ```

r[attributes.codegen.instruction_set.syntax]
The `instruction_set` attribute uses the [MetaListPaths] syntax to specify a single path consisting of the architecture family name and instruction set name.

r[attributes.codegen.instruction_set.allowed-positions]
The `instruction_set` attribute may only be applied to functions with [bodies] --- [closures], [async blocks], [free functions], [associated functions] in an [inherent impl] or [trait impl], and associated functions in a [trait definition] when those functions have a [default definition] .

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

> [!NOTE]
> Though the attribute can be applied to [closures] and [async blocks], the usefulness of this is limited as we do not yet support attributes on expressions.

r[attributes.codegen.instruction_set.duplicates]
The `instruction_set` attribute may be used only once on a function.

r[attributes.codegen.instruction_set.target-limits]
The `instruction_set` attribute may only be used with a target that supports the given value.

r[attributes.codegen.instruction_set.inline-asm]
When the `instruction_set` attribute is used, any inline assembly in the function must use the specified instruction set instead of the target default.

r[attributes.codegen.instruction_set.arm]
### `instruction_set` on ARM

When targeting the `ARMv4T` and `ARMv5te` architectures, the supported values for `instruction_set` are:

- `arm::a32` --- Generate the function as A32 "ARM" code.
- `arm::t32` --- Generate the function as T32 "Thumb" code.

If the address of the function is taken as a function pointer, the low bit of the address will depend on the selected instruction set:

- For `arm::a32` ("ARM"), it will be 0.
- For `arm::t32` ("Thumb"), it will be 1.

[`-C target-cpu`]: ../../rustc/codegen-options/index.html#target-cpu
[`-C target-feature`]: ../../rustc/codegen-options/index.html#target-feature
[`export_name`]: abi.export_name
[`is_aarch64_feature_detected`]: ../../std/arch/macro.is_aarch64_feature_detected.html
[`is_x86_feature_detected`]: ../../std/arch/macro.is_x86_feature_detected.html
[`Location`]: core::panic::Location
[`naked_asm!`]: ../inline-assembly.md
[`no_mangle`]: abi.no_mangle
[`target_feature` conditional compilation option]: ../conditional-compilation.md#target_feature
[`unused_variables`]: ../../rustc/lints/listing/warn-by-default.html#unused-variables
[associated functions]: items.associated.fn
[async blocks]: expr.block.async
[async closure]: expr.closure.async
[async function]: items.fn.async
[attribute]: ../attributes.md
[attributes]: ../attributes.md
[bodies]: items.fn.body
[closures]: expr.closure
[default definition]: items.traits.associated-item-decls
[free functions]: items.fn
[function body]: ../items/functions.md#function-body
[functions]: ../items/functions.md
[inherent impl]: items.impl.inherent
[rust-abi]: ../items/external-blocks.md#abi
[target architecture]: ../conditional-compilation.md#target_arch
[trait]: items.traits
[trait definition]: items.traits
[trait impl]: items.impl.trait
[undefined behavior]: ../behavior-considered-undefined.md
[unsafe attribute]: ../attributes.md#r-attributes.safety


---

r[attributes.limits]
# Limits

The following [attributes] affect compile-time limits.

r[attributes.limits.recursion_limit]
## The `recursion_limit` attribute

r[attributes.limits.recursion_limit.intro]
The *`recursion_limit` attribute* may be applied at the [crate] level to set the
maximum depth for potentially infinitely-recursive compile-time operations
like macro expansion or auto-dereference.

r[attributes.limits.recursion_limit.syntax]
It uses the [MetaNameValueStr]
syntax to specify the recursion depth.

> [!NOTE]
> The default in `rustc` is 128.

```rust,compile_fail
#![recursion_limit = "4"]

macro_rules! a {
    () => { a!(1); };
    (1) => { a!(2); };
    (2) => { a!(3); };
    (3) => { a!(4); };
    (4) => { };
}

// This fails to expand because it requires a recursion depth greater than 4.
a!{}
```

```rust,compile_fail
#![recursion_limit = "1"]

// This fails because it requires two recursive steps to auto-dereference.
(|_: &u8| {})(&&&1);
```

<!-- template:attributes -->
r[attributes.limits.type_length_limit]
## The `type_length_limit` attribute

r[attributes.limits.type_length_limit.intro]
The *`type_length_limit` [attribute][attributes]* sets the maximum number of type substitutions allowed when constructing a concrete type during monomorphization.

> [!NOTE]
> `rustc` only enforces the limit when the nightly `-Zenforce-type-length-limit` flag is active.
>
> For more information, see [Rust PR #127670](https://github.com/rust-lang/rust/pull/127670).

> [!EXAMPLE]
> <!-- ignore: not enforced without nightly flag -->
> ```rust,ignore
> #![type_length_limit = "4"]
>
> fn f<T>(x: T) {}
>
> // This fails to compile because monomorphizing to
> // `f::<((((i32,), i32), i32), i32)>` requires more
> // than 4 type elements.
> f(((((1,), 2), 3), 4));
> ```

> [!NOTE]
> The default value in `rustc` is `1048576`.

r[attributes.limits.type_length_limit.syntax]
The `type_length_limit` attribute uses the [MetaNameValueStr] syntax. The value in the string must be a non-negative number.

r[attributes.limits.type_length_limit.allowed-positions]
The `type_length_limit` attribute may only be applied to the crate root.

> [!NOTE]
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

r[attributes.limits.type_length_limit.duplicates]
Only the first use of `type_length_limit` on an item has effect.

> [!NOTE]
> `rustc` lints against any use following the first. This may become an error in the future.

[attributes]: ../attributes.md
[crate]: ../crates-and-source-files.md


---

r[attributes.type-system]
# Type system attributes

The following [attributes] are used for changing how a type can be used.

r[attributes.type-system.non_exhaustive]
## The `non_exhaustive` attribute

r[attributes.type-system.non_exhaustive.intro]
The *`non_exhaustive` attribute* indicates that a type or variant may have
more fields or variants added in the future.

r[attributes.type-system.non_exhaustive.allowed-positions]
It can be applied to [`struct`s][struct], [`enum`s][enum], and `enum` variants.

r[attributes.type-system.non_exhaustive.syntax]
The `non_exhaustive` attribute uses the [MetaWord] syntax and thus does not
take any inputs.

r[attributes.type-system.non_exhaustive.same-crate]
Within the defining crate, `non_exhaustive` has no effect.

```rust
#[non_exhaustive]
pub struct Config {
    pub window_width: u16,
    pub window_height: u16,
}

#[non_exhaustive]
pub struct Token;

#[non_exhaustive]
pub struct Id(pub u64);

#[non_exhaustive]
pub enum Error {
    Message(String),
    Other,
}

pub enum Message {
    #[non_exhaustive] Send { from: u32, to: u32, contents: String },
    #[non_exhaustive] Reaction(u32),
    #[non_exhaustive] Quit,
}

// Non-exhaustive structs can be constructed as normal within the defining crate.
let config = Config { window_width: 640, window_height: 480 };
let token = Token;
let id = Id(4);

// Non-exhaustive structs can be matched on exhaustively within the defining crate.
let Config { window_width, window_height } = config;
let Token = token;
let Id(id_number) = id;

let error = Error::Other;
let message = Message::Reaction(3);

// Non-exhaustive enums can be matched on exhaustively within the defining crate.
match error {
    Error::Message(ref s) => { },
    Error::Other => { },
}

match message {
    // Non-exhaustive variants can be matched on exhaustively within the defining crate.
    Message::Send { from, to, contents } => { },
    Message::Reaction(id) => { },
    Message::Quit => { },
}
```

r[attributes.type-system.non_exhaustive.external-crate]
Outside of the defining crate, types annotated with `non_exhaustive` have limitations that
preserve backwards compatibility when new fields or variants are added.

r[attributes.type-system.non_exhaustive.construction]
Non-exhaustive types cannot be constructed outside of the defining crate:

- Non-exhaustive variants ([`struct`][struct] or [`enum` variant][enum]) cannot be constructed
  with a [StructExpression] \(including with [functional update syntax]).
- The implicitly defined same-named constant of a [unit-like struct][struct],
  or the same-named constructor function of a [tuple struct][struct],
  has a [visibility] no greater than `pub(crate)`.
  That is, if the struct’s visibility is `pub`, then the constant or constructor’s visibility
  is `pub(crate)`, and otherwise the visibility of the two items is the same
  (as is the case without `#[non_exhaustive]`).
- [`enum`][enum] instances can be constructed.

The following examples of construction do not compile when outside the defining crate:

<!-- ignore: requires external crates -->
```rust,ignore
// These are types defined in an upstream crate that have been annotated as
// `#[non_exhaustive]`.
use upstream::{Config, Token, Id, Error, Message};

// Cannot construct an instance of `Config`; if new fields were added in
// a new version of `upstream` then this would fail to compile, so it is
// disallowed.
let config = Config { window_width: 640, window_height: 480 };

// Cannot construct an instance of `Token`; if new fields were added, then
// it would not be a unit-like struct any more, so the same-named constant
// created by it being a unit-like struct is not public outside the crate;
// this code fails to compile.
let token = Token;

// Cannot construct an instance of `Id`; if new fields were added, then
// its constructor function signature would change, so its constructor
// function is not public outside the crate; this code fails to compile.
let id = Id(5);

// Can construct an instance of `Error`; new variants being introduced would
// not result in this failing to compile.
let error = Error::Message("foo".to_string());

// Cannot construct an instance of `Message::Send` or `Message::Reaction`;
// if new fields were added in a new version of `upstream` then this would
// fail to compile, so it is disallowed.
let message = Message::Send { from: 0, to: 1, contents: "foo".to_string(), };
let message = Message::Reaction(0);

// Cannot construct an instance of `Message::Quit`; if this were converted to
// a tuple enum variant `upstream`, this would fail to compile.
let message = Message::Quit;
```

r[attributes.type-system.non_exhaustive.match]
There are limitations when matching on non-exhaustive types outside of the defining crate:

- When pattern matching on a non-exhaustive variant ([`struct`][struct] or [`enum` variant][enum]), a [StructPattern] must be used which must include a `..`. A tuple enum variant's constructor's [visibility] is reduced to be no greater than `pub(crate)`.
- When pattern matching on a non-exhaustive [`enum`][enum], matching on a variant does not contribute towards the exhaustiveness of the arms. The following examples of matching do not compile when outside the defining crate:

<!-- ignore: requires external crates -->
```rust, ignore
// These are types defined in an upstream crate that have been annotated as
// `#[non_exhaustive]`.
use upstream::{Config, Token, Id, Error, Message};

// Cannot match on a non-exhaustive enum without including a wildcard arm.
match error {
  Error::Message(ref s) => { },
  Error::Other => { },
  // would compile with: `_ => {},`
}

// Cannot match on a non-exhaustive struct without a wildcard.
if let Ok(Config { window_width, window_height }) = config {
    // would compile with: `..`
}

// Cannot match a non-exhaustive unit-like or tuple struct except by using
// braced struct syntax with a wildcard.
// This would compile as `let Token { .. } = token;`
let Token = token;
// This would compile as `let Id { 0: id_number, .. } = id;`
let Id(id_number) = id;

match message {
  // Cannot match on a non-exhaustive struct enum variant without including a wildcard.
  Message::Send { from, to, contents } => { },
  // Cannot match on a non-exhaustive tuple or unit enum variant.
  Message::Reaction(type) => { },
  Message::Quit => { },
}
```

It's also not allowed to use numeric casts (`as`) on enums that contain any non-exhaustive variants.

For example, the following enum can be cast because it doesn't contain any non-exhaustive variants:

```rust
#[non_exhaustive]
pub enum Example {
    First,
    Second,
}
```

However, if the enum contains even a single non-exhaustive variant, casting will result in an error. Consider this modified version of the same enum:

```rust
#[non_exhaustive]
pub enum EnumWithNonExhaustiveVariants {
    First,
    #[non_exhaustive]
    Second,
}
```

<!-- ignore: needs multiple crates -->
```rust,ignore
use othercrate::EnumWithNonExhaustiveVariants;

// Error: cannot cast an enum with a non-exhaustive variant when it's defined in another crate
let _ = EnumWithNonExhaustiveVariants::First as u8;
```

Non-exhaustive types are always considered inhabited in downstream crates.

[`match`]: ../expressions/match-expr.md
[attributes]: ../attributes.md
[enum]: ../items/enumerations.md
[functional update syntax]: ../expressions/struct-expr.md#functional-update-syntax
[struct]: ../items/structs.md
[visibility]: ../visibility-and-privacy.md


---

r[attributes.debugger]
# Debugger attributes

The following [attributes] are used for enhancing the debugging experience when using third-party debuggers like GDB or WinDbg.

<!-- template:attributes -->
r[attributes.debugger.debugger_visualizer]
## The `debugger_visualizer` attribute

r[attributes.debugger.debugger_visualizer.intro]
The *`debugger_visualizer` [attribute][attributes]* can be used to embed a debugger visualizer file into the debug information. This improves the debugger experience when displaying values.

> [!EXAMPLE]
> <!-- ignore: requires external files-->
> ```rust,ignore
> #![debugger_visualizer(natvis_file = "Example.natvis")]
> #![debugger_visualizer(gdb_script_file = "example.py")]
> ```

r[attributes.debugger.debugger_visualizer.syntax]
The `debugger_visualizer` attribute uses the [MetaListNameValueStr] syntax to specify its inputs. One of the following keys must be specified:

- [`natvis_file`][attributes.debugger.debugger_visualizer.natvis]
- [`gdb_script_file`][attributes.debugger.debugger_visualizer.gdb]

r[attributes.debugger.debugger_visualizer.allowed-positions]
The `debugger_visualizer` attribute may only be applied to a [module] or to the crate root.

r[attributes.debugger.debugger_visualizer.duplicates]
The `debugger_visualizer` attribute may be used any number of times on a form. All specified visualizer files will be loaded.

r[attributes.debugger.debugger_visualizer.natvis]
### Using `debugger_visualizer` with Natvis

r[attributes.debugger.debugger_visualizer.natvis.intro]
Natvis is an XML-based framework for Microsoft debuggers (such as Visual Studio and WinDbg) that uses declarative rules to customize the display of types. For detailed information on the Natvis format, refer to Microsoft's [Natvis documentation].

r[attributes.debugger.debugger_visualizer.natvis.msvc]
This attribute only supports embedding Natvis files on `-windows-msvc` targets.

r[attributes.debugger.debugger_visualizer.natvis.path]
The path to the Natvis file is specified with the `natvis_file` key, which is a path relative to the source file.

> [!EXAMPLE]
> <!-- ignore: requires external files and msvc -->
> ```rust ignore
> #![debugger_visualizer(natvis_file = "Rectangle.natvis")]
>
> struct FancyRect {
>     x: f32,
>     y: f32,
>     dx: f32,
>     dy: f32,
> }
>
> fn main() {
>     let fancy_rect = FancyRect { x: 10.0, y: 10.0, dx: 5.0, dy: 5.0 };
>     println!("set breakpoint here");
> }
> ```
>
> `Rectangle.natvis` contains:
>
> ```xml
> <?xml version="1.0" encoding="utf-8"?>
> <AutoVisualizer xmlns="http://schemas.microsoft.com/vstudio/debugger/natvis/2010">
>     <Type Name="foo::FancyRect">
>       <DisplayString>({x},{y}) + ({dx}, {dy})</DisplayString>
>       <Expand>
>         <Synthetic Name="LowerLeft">
>           <DisplayString>({x}, {y})</DisplayString>
>         </Synthetic>
>         <Synthetic Name="UpperLeft">
>           <DisplayString>({x}, {y + dy})</DisplayString>
>         </Synthetic>
>         <Synthetic Name="UpperRight">
>           <DisplayString>({x + dx}, {y + dy})</DisplayString>
>         </Synthetic>
>         <Synthetic Name="LowerRight">
>           <DisplayString>({x + dx}, {y})</DisplayString>
>         </Synthetic>
>       </Expand>
>     </Type>
> </AutoVisualizer>
> ```
>
> When viewed under WinDbg, the `fancy_rect` variable would be shown as follows:
>
> ```text
> > Variables:
>   > fancy_rect: (10.0, 10.0) + (5.0, 5.0)
>     > LowerLeft: (10.0, 10.0)
>     > UpperLeft: (10.0, 15.0)
>     > UpperRight: (15.0, 15.0)
>     > LowerRight: (15.0, 10.0)
> ```

r[attributes.debugger.debugger_visualizer.gdb]
### Using `debugger_visualizer` with GDB

r[attributes.debugger.debugger_visualizer.gdb.pretty]
GDB supports the use of a structured Python script, called a *pretty printer*, that describes how a type should be visualized in the debugger view. For detailed information on pretty printers, refer to GDB's [pretty printing documentation].

> [!NOTE]
> Embedded pretty printers are not automatically loaded when debugging a binary under GDB.
>
> There are two ways to enable auto-loading embedded pretty printers:
>
> 1. Launch GDB with extra arguments to explicitly add a directory or binary to the auto-load safe path: `gdb -iex "add-auto-load-safe-path safe-path path/to/binary" path/to/binary` For more information, see GDB's [auto-loading documentation].
> 1. Create a file named `gdbinit` under `$HOME/.config/gdb` (you may need to create the directory if it doesn't already exist). Add the following line to that file: `add-auto-load-safe-path path/to/binary`.

r[attributes.debugger.debugger_visualizer.gdb.path]
These scripts are embedded using the `gdb_script_file` key, which is a path relative to the source file.

> [!EXAMPLE]
> <!-- ignore: requires external files -->
> ```rust ignore
> #![debugger_visualizer(gdb_script_file = "printer.py")]
>
> struct Person {
>     name: String,
>     age: i32,
> }
>
> fn main() {
>     let bob = Person { name: String::from("Bob"), age: 10 };
>     println!("set breakpoint here");
> }
> ```
>
> `printer.py` contains:
>
> ```python
> import gdb
>
> class PersonPrinter:
>     "Print a Person"
>
>     def __init__(self, val):
>         self.val = val
>         self.name = val["name"]
>         self.age = int(val["age"])
>
>     def to_string(self):
>         return "{} is {} years old.".format(self.name, self.age)
>
> def lookup(val):
>     lookup_tag = val.type.tag
>     if lookup_tag is None:
>         return None
>     if "foo::Person" == lookup_tag:
>         return PersonPrinter(val)
>
>     return None
>
> gdb.current_objfile().pretty_printers.append(lookup)
> ```
>
> When the crate's debug executable is passed into GDB[^rust-gdb], `print bob` will display:
>
> ```text
> "Bob" is 10 years old.
> ```
>
> [^rust-gdb]: Note: This assumes you are using the `rust-gdb` script which configures pretty-printers for standard library types like `String`.

[auto-loading documentation]: https://sourceware.org/gdb/onlinedocs/gdb/Auto_002dloading-safe-path.html
[attributes]: ../attributes.md
[Natvis documentation]: https://docs.microsoft.com/en-us/visualstudio/debugger/create-custom-views-of-native-objects
[pretty printing documentation]: https://sourceware.org/gdb/onlinedocs/gdb/Pretty-Printing.html

<!-- template:attributes -->
r[attributes.debugger.collapse_debuginfo]
## The `collapse_debuginfo` attribute

r[attributes.debugger.collapse_debuginfo.intro]
The *`collapse_debuginfo` [attribute]* controls whether code locations from a macro definition are collapsed into a single location associated with the macro's call site when generating debuginfo for code calling this macro.

> [!EXAMPLE]
> ```rust
> #[collapse_debuginfo(yes)]
> macro_rules! example {
>     () => {
>         println!("hello!");
>     };
> }
> ```
>
> When using a debugger, invoking the `example` macro may appear as though it is calling a function. That is, when you step to the invocation site, it may show the macro invocation rather than the expanded code.

<!-- TODO: I think it would be nice to extend this to explain a little more about why this is useful, and the kinds of scenarios where you would want one vs the other. See https://github.com/rust-lang/rfcs/pull/2117 for some guidance. -->

r[attributes.debugger.collapse_debuginfo.syntax]
The syntax for the `collapse_debuginfo` attribute is:

```grammar,attributes
@root CollapseDebuginfoAttribute -> `collapse_debuginfo` `(` CollapseDebuginfoOption `)`

CollapseDebuginfoOption ->
      `yes`
    | `no`
    | `external`
```

r[attributes.debugger.collapse_debuginfo.allowed-positions]
The `collapse_debuginfo` attribute may only be applied to a [`macro_rules` definition].

r[attributes.debugger.collapse_debuginfo.duplicates]
The `collapse_debuginfo` attribute may used only once on a macro.

r[attributes.debugger.collapse_debuginfo.options]
The `collapse_debuginfo` attribute accepts these options:

- `#[collapse_debuginfo(yes)]` --- Code locations in debuginfo are collapsed.
- `#[collapse_debuginfo(no)]` --- Code locations in debuginfo are not collapsed.
- `#[collapse_debuginfo(external)]` --- Code locations in debuginfo are collapsed only if the macro comes from a different crate.

r[attributes.debugger.collapse_debuginfo.default]
The `external` behavior is the default for macros that don't have this attribute unless they are built-in macros. For built-in macros the default is `yes`.

> [!NOTE]
> `rustc` has a [`-C collapse-macro-debuginfo`] CLI option to override both the default behavior and the values of any `#[collapse_debuginfo]` attributes.

[`-C collapse-macro-debuginfo`]: ../../rustc/codegen-options/index.html#collapse-macro-debuginfo
[`macro_rules` definition]: ../macros-by-example.md
[attribute]: ../attributes.md
[module]: ../items/modules.md
