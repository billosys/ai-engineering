---
concept: Advanced Functions and Macros
slug: rust-advanced-functions-and-macros
category: language-fundamentals
subcategory: metaprogramming
tier: advanced
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Advanced Features"
chapter_number: 20
pdf_page: null
section: "Advanced Functions and Closures, Macros"
extraction_confidence: high
aliases:
  - "function pointers"
  - "fn type"
  - "returning closures"
  - "declarative macros"
  - "macro_rules"
  - "procedural macros"
  - "derive macros"
  - "attribute-like macros"
  - "function-like macros"
  - "metaprogramming"
prerequisites: []
extends: []
related:
  - rust-advanced-traits-and-types
  - reference-macros-by-example
  - reference-procedural-macros
contrasts_with: []
answers_questions:
  - "What is the difference between fn (function pointer) and Fn (closure trait)?"
  - "Can you pass a named function where a closure is expected?"
  - "How do you return a closure from a function?"
  - "What is the difference between impl Fn and Box<dyn Fn> for return types?"
  - "What is a declarative macro and how does macro_rules! work?"
  - "How does a macro differ from a function?"
  - "What are the three kinds of procedural macros?"
  - "How do you write a custom derive macro?"
  - "What are attribute-like macros?"
  - "What are function-like macros?"
  - "What crates are used to write procedural macros (proc_macro, syn, quote)?"
  - "Can enum variant initializers be used as function pointers?"
---

# Quick Definition

Rust provides function pointers (`fn` type) that implement all three closure traits (`Fn`, `FnMut`, `FnOnce`), allowing named functions to be passed anywhere closures are accepted. Closures can be returned from functions using `impl Fn` (for a single closure type) or `Box<dyn Fn>` (for multiple closure types needing dynamic dispatch). Macros in Rust come in two families: declarative macros (`macro_rules!`) that use pattern matching on code structure, and procedural macros (custom `derive`, attribute-like, and function-like) that operate on `TokenStream` inputs and produce code as output. Macros enable metaprogramming -- writing code that writes code at compile time.

# Core Definition

**Function pointers (`fn` type):**
The `fn` type (lowercase) is a concrete type representing a function pointer, distinct from the `Fn` closure trait (uppercase). Function pointers implement all three closure traits (`Fn`, `FnMut`, `FnOnce`), so named functions can be passed wherever closures are expected: `list.iter().map(ToString::to_string)` or `(0..20).map(Status::Value)` (enum variant initializers are function pointers too).

When interfacing with C (which has no closures), you must accept `fn` rather than a generic `F: Fn(...)`. In pure Rust, prefer generic `F: Fn(...)` to accept both closures and function pointers.

**Returning closures:**
- `impl Fn(i32) -> i32` works when returning a single closure type from a function
- Different closures (even with the same signature) are distinct opaque types, so returning different closures conditionally requires `Box<dyn Fn(i32) -> i32>` for dynamic dispatch
- A closure that captures values cannot be returned as `fn` (function pointer)

**Macros vs functions:**
- Macros accept a variable number of arguments; functions have fixed signatures
- Macros are expanded at compile time before type checking; functions are called at runtime
- Macros can implement traits on types; functions cannot (traits must be implemented at compile time)
- Macros must be defined or brought into scope before use; functions can be defined anywhere
- Macro definitions are more complex and harder to maintain than function definitions

**Declarative macros (`macro_rules!`):**
Work like `match` on code structure. Example: `vec!` macro uses pattern `( $( $x:expr ),* )` to match zero or more comma-separated expressions, generating `push` calls for each. The `#[macro_export]` annotation makes the macro available when the crate is in scope. Macro pattern syntax (`$x:expr`, `$(...)*`) differs from value pattern syntax.

**Procedural macros** accept a `TokenStream` and produce a `TokenStream`. They must reside in their own crate with `proc-macro` crate type. Three kinds:
1. **Custom `derive` macros** -- `#[derive(HelloMacro)]` generates trait implementations. Uses `#[proc_macro_derive(Name)]` attribute. The `syn` crate parses `TokenStream` into a `DeriveInput` AST; the `quote` crate converts back to `TokenStream`.
2. **Attribute-like macros** -- `#[route(GET, "/")]` applied to any item (not just structs/enums). Uses `#[proc_macro_attribute]`. Takes two `TokenStream` args: the attribute arguments and the annotated item body.
3. **Function-like macros** -- `sql!(SELECT * FROM posts WHERE id=1)` looks like function calls but operates on tokens. Uses `#[proc_macro]`. More flexible than `macro_rules!` because they use full Rust code to transform tokens.

# Prerequisites

Understanding of closures and the `Fn`/`FnMut`/`FnOnce` traits (Ch 13), trait objects (Ch 18), and basic trait implementation.

# Key Properties

1. `fn` (lowercase) is a type, not a trait -- you specify it directly as a parameter type: `fn do_twice(f: fn(i32) -> i32, arg: i32)`
2. Function pointers implement all three closure traits, so they can always be used where closures are expected, but not vice versa
3. Enum variant initializers (like `Status::Value`) are function pointers and can be passed to higher-order functions like `map`
4. `impl Fn` as a return type creates an opaque type unique to each function -- two functions returning `impl Fn(i32) -> i32` return different types
5. To store closures from different sources in a `Vec` or return them conditionally, use `Box<dyn Fn(...)>` for dynamic dispatch
6. Declarative macros compare against Rust code structure (not values); `$x:expr` matches any expression, `*` means zero or more repetitions
7. `macro_rules!` macros must be defined before use in the file; procedural macros must reside in a separate crate with `proc-macro` crate type
8. The `syn` crate parses `TokenStream` into an AST (`DeriveInput`); `quote` turns AST manipulations back into `TokenStream`
9. `stringify!` (used in macro examples) converts a Rust expression into a string literal at compile time without evaluating it
10. Procedural macros' `proc_macro_derive` functions must return `TokenStream` (not `Result`), so they use `unwrap`/`panic!` for error handling

# Construction / Recognition

## To pass a function as an argument:
1. Accept a generic closure: `fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 { f(x) }`
2. Or accept a function pointer: `fn apply(f: fn(i32) -> i32, x: i32) -> i32 { f(x) }`
3. Call with a named function: `apply(add_one, 5)` -- works for both approaches

## To return a closure:
1. Single closure type: `fn make_adder(x: i32) -> impl Fn(i32) -> i32 { move |y| x + y }`
2. Multiple closure types: `fn choose(flag: bool) -> Box<dyn Fn(i32) -> i32> { if flag { Box::new(|x| x + 1) } else { Box::new(|x| x - 1) } }`

## To write a declarative macro:
1. Use `#[macro_export]` for visibility
2. `macro_rules! name { (pattern) => { expansion }; }`
3. Use `$var:kind` for metavariables and `$(...)*` for repetition

## To write a derive macro:
1. Create a separate crate with `proc-macro = true` in Cargo.toml
2. Add `syn` and `quote` as dependencies
3. Parse input: `let ast = syn::parse(input).unwrap();`
4. Generate code: `let expanded = quote! { impl MyTrait for #name { ... } };`
5. Return: `expanded.into()`

# Context & Application

The Advanced Functions and Closures section completes the closure story started in Chapter 13 by addressing function pointers and closure return types. The key insight is that `fn` and `Fn` are different things: `fn` is a concrete type (always the same size, no captures), while `Fn` is a trait (closures implementing it can have different sizes due to captures).

The Macros section is the book's primary introduction to metaprogramming. Declarative macros (`macro_rules!`) are the most commonly used form -- `vec!`, `println!`, `assert!`, and `format!` are all declarative macros. The section deliberately simplifies the `vec!` definition for pedagogy while noting that the real implementation includes pre-allocation optimizations.

Procedural macros are presented as the more powerful but more complex alternative. The custom derive walkthrough (HelloMacro) is a complete end-to-end example showing crate structure, `syn` parsing, `quote` code generation, and the `proc_macro_derive` attribute. This pattern is used extensively in the Rust ecosystem: `serde`, `thiserror`, `clap`, and many other libraries provide custom derive macros.

The chapter ties back to Chapter 21's web server project, where the thread pool uses `Box<dyn FnOnce()>` as a type alias for job closures, demonstrating these concepts in practice.

# Examples

**Example 1** (Ch. 20, "Function Pointers"): Passing a function to `map`:
```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> =
    list_of_numbers.iter().map(ToString::to_string).collect();
```

**Example 2** (Ch. 20, "Enum Initializers as Function Pointers"):
```rust
enum Status { Value(u32), Stop }
let list_of_statuses: Vec<Status> = (0u32..20).map(Status::Value).collect();
```

**Example 3** (Ch. 20, "Declarative Macro"): Simplified `vec!` definition:
```rust
#[macro_export]
macro_rules! vec {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )*
            temp_vec
        }
    };
}
// vec![1, 2, 3] expands to: { let mut temp_vec = Vec::new(); temp_vec.push(1); temp_vec.push(2); temp_vec.push(3); temp_vec }
```

**Example 4** (Ch. 20, "Custom Derive Macro"): The `impl_hello_macro` function using `quote`:
```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!("Hello, Macro! My name is {}!", stringify!(#name));
            }
        }
    };
    gen.into()
}
```

# Relationships

## Builds Upon
(none listed -- builds on Ch 13 closures, but that is not in this extraction set)

## Enables
(none)

## Related
- **rust-advanced-traits-and-types** -- associated types and trait objects interact with closure return types and macro-generated trait implementations
- **reference-macros-by-example** -- The Rust Reference's formal specification of declarative macro syntax
- **reference-procedural-macros** -- The Rust Reference's formal specification of procedural macros

## Contrasts With
(none)

# Common Errors

- **Error**: Trying to return different closures from `if`/`else` branches using `impl Fn` -- the compiler reports mismatched opaque types.
  **Correction**: Use `Box<dyn Fn(i32) -> i32>` to erase the concrete closure types and enable dynamic dispatch.

- **Error**: Writing a `macro_rules!` macro without `#[macro_export]` and wondering why it cannot be used from other modules.
  **Correction**: Add `#[macro_export]` above the `macro_rules!` definition to make the macro available when the crate is brought into scope.

- **Error**: Placing a procedural macro definition in the same crate as the code that uses it.
  **Correction**: Procedural macros must reside in their own crate with `proc-macro = true` in `Cargo.toml`. Convention: for crate `foo`, the proc macro crate is `foo_derive`.

# Common Confusions

- **Confusion**: Thinking `fn` (function pointer type) and `Fn` (closure trait) are the same thing.
  **Clarification**: `fn` is a concrete type for function pointers (no captures, fixed size). `Fn` is a trait that closures implement (closures may capture variables, each has a unique anonymous type). Function pointers implement `Fn`, but closures that capture variables are not `fn`.

- **Confusion**: Thinking declarative macros (`macro_rules!`) and procedural macros are interchangeable.
  **Clarification**: Declarative macros use pattern matching on token structure and are simpler. Procedural macros use arbitrary Rust code to transform `TokenStream` and can do more complex processing (parsing, generating implementations), but require a separate crate and dependencies like `syn` and `quote`.

- **Confusion**: Expecting `stringify!` to evaluate an expression like `format!` does.
  **Clarification**: `stringify!` converts the expression to a string literal at compile time without evaluating it. `stringify!(1 + 2)` produces `"1 + 2"`, not `"3"`.

# Source Reference

Chapter 20 of The Rust Programming Language, sections "Advanced Functions and Closures" (~190 lines) and "Macros" (~530 lines). Functions and Closures covers: function pointers (`fn` type), relationship between `fn` and `Fn`/`FnMut`/`FnOnce`, enum initializers as function pointers, returning closures with `impl Fn` vs `Box<dyn Fn>`. Macros covers: macros vs functions, declarative macros (`macro_rules!`, `vec!` example, pattern syntax), procedural macros (TokenStream, separate crate requirement, syn/quote), custom derive macros (HelloMacro walkthrough), attribute-like macros, and function-like macros.

# Verification Notes

- Definition source: Directly extracted from Chapter 20 "Advanced Functions and Closures" and "Macros" sections
- Key Properties: All derived from explicit explanations and code examples in the source text
- Confidence rationale: HIGH -- authoritative book by the Rust team with a complete custom derive macro walkthrough
- Uncertainties: The requirement for procedural macros to be in a separate crate is noted as potentially being lifted in the future
- Cross-reference status: reference-macros-by-example and reference-procedural-macros provide the formal specification of macro syntax
