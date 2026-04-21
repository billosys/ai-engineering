% Building Blocks

Reusable snippets of macro code.


---

% AST Coercion

The Rust parser is not very robust in the face of `tt` substitutions.  Problems can arise when the parser is expecting a particular grammar construct and *instead* finds a lump of substituted `tt` tokens.  Rather than attempt to parse them, it will often just *give up*.  In these cases, it is necessary to employ an AST coercion.

```rust
# #![allow(dead_code)]
# 
macro_rules! as_expr { ($e:expr) => {$e} }
macro_rules! as_item { ($i:item) => {$i} }
macro_rules! as_pat  { ($p:pat) =>  {$p} }
macro_rules! as_stmt { ($s:stmt) => {$s} }
# 
# as_item!{struct Dummy;}
# 
# fn main() {
#     as_stmt!(let as_pat!(_) = as_expr!(42));
# }
```

These coercions are often used with [push-down accumulation] macros in order to get the parser to treat the final `tt` sequence as a particular kind of grammar construct.

Note that this specific set of macros is determined by what macros are allowed to expand to, *not* what they are able to capture.  That is, because macros cannot appear in type position[^issue-27245], you cannot have an `as_ty!` macro.

[push-down accumulation]: pat-push-down-accumulation.html

[^issue-27245]: See [Issue #27245](https://github.com/rust-lang/rust/issues/27245).


---

% Counting

## Repetition with replacement

Counting things in a macro is a surprisingly tricky task.  The simplest way is to use replacement with a repetition match.

```rust
macro_rules! replace_expr {
    ($_t:tt $sub:expr) => {$sub};
}

macro_rules! count_tts {
    ($($tts:tt)*) => {0usize $(+ replace_expr!($tts 1usize))*};
}
# 
# fn main() {
#     assert_eq!(count_tts!(0 1 2), 3);
# }
```

This is a fine approach for smallish numbers, but will likely *crash the compiler* with inputs of around 500 or so tokens.  Consider that the output will look something like this:

```ignore
0usize + 1usize + /* ~500 `+ 1usize`s */ + 1usize
```

The compiler must parse this into an AST, which will produce what is effectively a perfectly unbalanced binary tree 500+ levels deep.

## Recursion

An older approach is to use recursion.

```rust
macro_rules! count_tts {
    () => {0usize};
    ($_head:tt $($tail:tt)*) => {1usize + count_tts!($($tail)*)};
}
# 
# fn main() {
#     assert_eq!(count_tts!(0 1 2), 3);
# }
```

> **Note**: As of `rustc` 1.2, the compiler has *grevious* performance problems when large numbers of integer literals of unknown type must undergo inference.  We are using explicitly `usize`-typed literals here to avoid that.
>
> If this is not suitable (such as when the type must be substitutable), you can help matters by using `as` (*e.g.* `0 as $ty`, `1 as $ty`, *etc.*).

This *works*, but will trivially exceed the recursion limit.  Unlike the repetition approach, you can extend the input size by matching multiple tokens at once.

```rust
macro_rules! count_tts {
    ($_a:tt $_b:tt $_c:tt $_d:tt $_e:tt
     $_f:tt $_g:tt $_h:tt $_i:tt $_j:tt
     $_k:tt $_l:tt $_m:tt $_n:tt $_o:tt
     $_p:tt $_q:tt $_r:tt $_s:tt $_t:tt
     $($tail:tt)*)
        => {20usize + count_tts!($($tail)*)};
    ($_a:tt $_b:tt $_c:tt $_d:tt $_e:tt
     $_f:tt $_g:tt $_h:tt $_i:tt $_j:tt
     $($tail:tt)*)
        => {10usize + count_tts!($($tail)*)};
    ($_a:tt $_b:tt $_c:tt $_d:tt $_e:tt
     $($tail:tt)*)
        => {5usize + count_tts!($($tail)*)};
    ($_a:tt
     $($tail:tt)*)
        => {1usize + count_tts!($($tail)*)};
    () => {0usize};
}

fn main() {
    assert_eq!(700, count_tts!(
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        
        // Repetition breaks somewhere after this
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,

        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
        ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,, ,,,,,,,,,,
    ));
}
```

This particular formulation will work up to ~1,200 tokens.

## Slice length

A third approach is to help the compiler construct a shallow AST that won't lead to a stack overflow.  This can be done by constructing an array literal and calling the `len` method.

```rust
macro_rules! replace_expr {
    ($_t:tt $sub:expr) => {$sub};
}

macro_rules! count_tts {
    ($($tts:tt)*) => {<[()]>::len(&[$(replace_expr!($tts ())),*])};
}
# 
# fn main() {
#     assert_eq!(count_tts!(0 1 2), 3);
# }
```

This has been tested to work up to 10,000 tokens, and can probably go much higher.  The *downside* is that as of Rust 1.2, this *cannot* be used to produce a constant expression.  Although the result can be optimised to a simple constant (in debug builds it compiles down to a load from memory), it still cannot be used in constant positions (such as the value of `const`s, or a fixed array's size).

However, if a non-constant count is acceptable, this is very much the preferred method.

## Enum counting

This approach can be used where you need to count a set of mutually distinct identifiers.  Additionally, the result of this approach is usable as a constant.

```rust
macro_rules! count_idents {
    ($($idents:ident),* $(,)*) => {
        {
            #[allow(dead_code, non_camel_case_types)]
            enum Idents { $($idents,)* __CountIdentsLast }
            const COUNT: u32 = Idents::__CountIdentsLast as u32;
            COUNT
        }
    };
}
# 
# fn main() {
#     const COUNT: u32 = count_idents!(A, B, C);
#     assert_eq!(COUNT, 3);
# }
```

This method does have two drawbacks.  First, as implied above, it can *only* count valid identifiers (which are also not keywords), and it does not allow those identifiers to repeat.

Secondly, this approach is *not* hygienic, meaning that if whatever identifier you use in place of `__CountIdentsLast` is provided as input, the macro will fail due to the duplicate variants in the `enum`.


---

% Enum Parsing

```rust
macro_rules! parse_unitary_variants {
    (@as_expr $e:expr) => {$e};
    (@as_item $($i:item)+) => {$($i)+};
    
    // Exit rules.
    (
        @collect_unitary_variants ($callback:ident ( $($args:tt)* )),
        ($(,)*) -> ($($var_names:ident,)*)
    ) => {
        parse_unitary_variants! {
            @as_expr
            $callback!{ $($args)* ($($var_names),*) }
        }
    };

    (
        @collect_unitary_variants ($callback:ident { $($args:tt)* }),
        ($(,)*) -> ($($var_names:ident,)*)
    ) => {
        parse_unitary_variants! {
            @as_item
            $callback!{ $($args)* ($($var_names),*) }
        }
    };

    // Consume an attribute.
    (
        @collect_unitary_variants $fixed:tt,
        (#[$_attr:meta] $($tail:tt)*) -> ($($var_names:tt)*)
    ) => {
        parse_unitary_variants! {
            @collect_unitary_variants $fixed,
            ($($tail)*) -> ($($var_names)*)
        }
    };

    // Handle a variant, optionally with an with initialiser.
    (
        @collect_unitary_variants $fixed:tt,
        ($var:ident $(= $_val:expr)*, $($tail:tt)*) -> ($($var_names:tt)*)
    ) => {
        parse_unitary_variants! {
            @collect_unitary_variants $fixed,
            ($($tail)*) -> ($($var_names)* $var,)
        }
    };

    // Abort on variant with a payload.
    (
        @collect_unitary_variants $fixed:tt,
        ($var:ident $_struct:tt, $($tail:tt)*) -> ($($var_names:tt)*)
    ) => {
        const _error: () = "cannot parse unitary variants from enum with non-unitary variants";
    };
    
    // Entry rule.
    (enum $name:ident {$($body:tt)*} => $callback:ident $arg:tt) => {
        parse_unitary_variants! {
            @collect_unitary_variants
            ($callback $arg), ($($body)*,) -> ()
        }
    };
}
# 
# fn main() {
#     assert_eq!(
#         parse_unitary_variants!(
#             enum Dummy { A, B, C }
#             => stringify(variants:)
#         ),
#         "variants : ( A , B , C )"
#     );
# }
```

This macro shows how you can use an [incremental tt muncher] and [push-down accumulation] to parse the variants of an `enum` where all variants are unitary (*i.e.* they have no payload).  Upon completion, `parse_unitary_variants!` invokes a [callback] macro with the list of variants (plus any other arbitrary arguments supplied).

This can be modified to also parse `struct` fields, compute tag values for the variants, or even extract the names of *all* variants in an arbitrary `enum`.

[incremental tt muncher]: pat-incremental-tt-munchers.html
[push-down accumulation]: pat-push-down-accumulation.html
[callback]: pat-callbacks.html
