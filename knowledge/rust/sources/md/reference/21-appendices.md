# Appendices


---

# Grammar summary

The following is a summary of the grammar production rules. For details on the syntax of this grammar, see *[notation.grammar.syntax]*.

{{ grammar-summary }}


---

# Syntax index

This appendix provides an index of tokens and common forms with links to where those elements are defined.

## Keywords

| Keyword       | Use |
|---------------|-----|
| `_`           | [wildcard pattern], [inferred const], [inferred type], [placeholder lifetime], [constant items], [extern crate], [use declarations], [destructuring assignment] |
| `abstract`    | [reserved keyword] |
| `as`          | [extern crate][items.extern-crate.as], [use declarations][items.use.forms.as], [type cast expressions], [qualified paths] |
| `async`       | [async functions], [async blocks], [async closures] |
| `await`       | [await expressions] |
| `become`      | [reserved keyword] |
| `box`         | [reserved keyword] |
| `break`       | [break expressions] |
| `const`       | [const functions], [const items], [const generics], [const blocks], [raw borrow operator], [raw pointer type], [const assembly operands] |
| `continue`    | [continue expressions] |
| `crate`       | [extern crate], [visibility], [paths] |
| `do`          | [reserved keyword] |
| `dyn`         | [trait objects] |
| `else`        | [let statements], [if expressions] |
| `enum`        | [enumerations] |
| `extern`      | [extern crate], [extern function qualifier], [external blocks], [extern function pointer types] |
| `false`       | [boolean type], [boolean expressions], [configuration predicates] |
| `final`       | [reserved keyword] |
| `fn`          | [functions], [function pointer types] |
| `for`         | [trait implementations], [iterator loops], [higher-ranked trait bounds] |
| `gen`         | [reserved keyword] |
| `if`          | [if expressions], [match guards] |
| `impl`        | [inherent impls], [trait impls], [impl trait types], [anonymous type parameters] |
| `in`          | [visibility], [iterator loops], [assembly operands] |
| `let`         | [let statements], [`if let` patterns] |
| `loop`        | [infinite loops] |
| `macro_rules` | [macros by example] |
| `macro`       | [reserved keyword] |
| `match`       | [match expressions] |
| `mod`         | [modules] |
| `move`        | [closure expressions], [async blocks] |
| `mut`         | [borrow expressions], [identifier patterns], [reference patterns], [struct patterns], [reference types], [raw pointer types], [self parameters], [static items] |
| `override`    | [reserved keyword] |
| `priv`        | [reserved keyword] |
| `pub`         | [visibility] |
| `raw`         | [borrow expressions], [raw assembly] |
| `ref`         | [identifier patterns], [struct patterns] |
| `return`      | [return expressions] |
| `safe`        | [external block functions], [external block statics] |
| `self`        | [extern crate][items.extern-crate.self], [self parameters], [visibility], [`self` paths] |
| `Self`        | [`Self` type paths], [use bounds] |
| `static`      | [static items], [`'static` lifetimes] |
| `struct`      | [structs] |
| `super`       | [super paths], [visibility] |
| `trait`       | [trait items] |
| `true`        | [boolean type], [boolean expressions], [configuration predicates] |
| `try`         | [reserved keyword] |
| `type`        | [type aliases] |
| `typeof`      | [reserved keyword] |
| `union`       | [union items] |
| `unsafe`      | [unsafe blocks], [unsafe attributes], [unsafe modules], [unsafe functions], [unsafe external blocks], [unsafe external functions], [unsafe external statics], [unsafe traits], [unsafe trait implementations] |
| `unsized`     | [reserved keyword] |
| `use`         | [use items], [use bounds] |
| `virtual`     | [reserved keyword] |
| `where`       | [where clauses] |
| `while`       | [predicate loops] |
| `yield`       | [reserved keyword] |

## Operators and punctuation

| Symbol | Name        | Use |
|--------|-------------|-----|
| `+`    | Plus        | [addition][arith], [trait bounds], [macro Kleene matcher] |
| `-`    | Minus       | [subtraction][arith], [negation] |
| `*`    | Star        | [multiplication][arith], [dereference], [raw pointers], [macro Kleene matcher], [glob imports] |
| `/`    | Slash       | [division][arith] |
| `%`    | Percent     | [remainder][arith] |
| `^`    | Caret       | [bitwise and logical XOR][arith] |
| `!`    | Not         | [bitwise and logical NOT][negation], [macro calls], [inner attributes][attributes], [never type], [negative impls] |
| `&`    | And         | [bitwise and logical AND][arith], [borrow], [references], [reference patterns] |
| `\|`   | Or | [bitwise and logical OR][arith], [closures], [or patterns], [if let], [while let] |
| `&&`   | AndAnd      | [lazy AND][lazy-bool], [borrow], [references], [reference patterns] |
| `\|\|` | OrOr | [lazy OR][lazy-bool], [closures] |
| `<<`   | Shl         | [shift left][arith], [nested generics][generics] |
| `>>`   | Shr         | [shift right][arith], [nested generics][generics] |
| `+=`   | PlusEq      | [addition assignment][compound] |
| `-=`   | MinusEq     | [subtraction assignment][compound] |
| `*=`   | StarEq      | [multiplication assignment][compound] |
| `/=`   | SlashEq     | [division assignment][compound] |
| `%=`   | PercentEq   | [remainder assignment][compound] |
| `^=`   | CaretEq     | [bitwise XOR assignment][compound] |
| `&=`   | AndEq       | [bitwise AND assignment][compound] |
| `\|=`  | OrEq | [bitwise OR assignment][compound] |
| `<<=`  | ShlEq       | [shift left assignment][compound] |
| `>>=`  | ShrEq       | [shift right assignment][compound], [nested generics][generics] |
| `=`    | Eq          | [assignment], [let statements], [attributes], various type definitions |
| `==`   | EqEq        | [equal][comparison] |
| `!=`   | Ne          | [not equal][comparison] |
| `>`    | Gt          | [greater than][comparison], [generics], [paths], [use bounds] |
| `<`    | Lt          | [less than][comparison], [generics], [paths], [use bounds] |
| `>=`   | Ge          | [greater than or equal to][comparison], [generics] |
| `<=`   | Le          | [less than or equal to][comparison] |
| `@`    | At          | [subpattern binding] |
| `.`    | Dot         | [field access][field], [tuple index], [method calls], [await expressions] |
| `..`   | DotDot      | [range expressions][expr.range], [struct expressions], [rest pattern], [range patterns], [struct patterns] |
| `...`  | DotDotDot   | [variadic functions], [range patterns] |
| `..=`  | DotDotEq    | [inclusive range expressions][expr.range], [range patterns] |
| `,`    | Comma       | various separators |
| `;`    | Semi        | terminator for various items and statements, [array expressions], [array types] |
| `:`    | Colon       | various separators |
| `::`   | PathSep     | [path separator][paths] |
| `->`   | RArrow      | [functions], [closures], [function pointer type] |
| `=>`   | FatArrow    | [match arms][match], [macros] |
| `<-`   | LArrow      | The left arrow symbol has been unused since before Rust 1.0, but it is still treated as a single token. |
| `#`    | Pound       | [attributes], [raw string literals], [raw byte string literals], [raw C string literals] |
| `$`    | Dollar      | [macros] |
| `?`    | Question    | [try propagation expressions][question], [relaxed trait bounds], [macro Kleene matcher] |
| `~`    | Tilde       | The tilde operator has been unused since before Rust 1.0, but its token may still be used. |

## Comments

| Comment  | Use |
|----------|-----|
| `//`     | [line comment][comments] |
| `//!`    | [inner line comment][comments] |
| `///`    | [outer line doc comment][comments] |
| `/*…*/`  | [block comment][comments] |
| `/*!…*/` | [inner block doc comment][comments] |
| `/**…*/` | [outer block doc comment][comments] |

## Other tokens

| Token        | Use |
|--------------|-----|
| `ident`      | [identifiers] |
| `r#ident`    | [raw identifiers] |
| `'ident`     | [lifetimes and loop labels] |
| `'r#ident`   | [raw lifetimes and loop labels] |
| `…u8`, `…i32`, `…f64`, `…usize`, … | [number literals] |
| `"…"`        | [string literals] |
| `r"…"`, `r#"…"#`, `r##"…"##`, … | [raw string literals] |
| `b"…"`       | [byte string literals] |
| `br"…"`, `br#"…"#`, `br##"…"##`, … | [raw byte string literals] |
| `'…'`        | [character literals] |
| `b'…'`       | [byte literals] |
| `c"…"`       | [C string literals] |
| `cr"…"`, `cr#"…"#`, `cr##"…"##`, … | [raw C string literals] |

## Macros

| Syntax                                     | Use |
|--------------------------------------------|-----|
| `ident!(…)`<br>`ident! {…}`<br>`ident![…]` | [macro invocations] |
| `$ident`                                   | [macro metavariable] |
| `$ident:kind`                              | [macro matcher fragment specifier] |
| `$(…)…`                                    | [macro repetition] |

## Attributes

| Syntax     | Use |
|------------|-----|
| `#[meta]`  | [outer attribute] |
| `#![meta]` | [inner attribute] |

## Expressions

| Expression                | Use |
|---------------------------|-----|
| `\|…\| expr`<br>`\|…\| -> Type { … }` | [closures] |
| `ident::…`                | [paths] |
| `::crate_name::…`         | [explicit crate paths] |
| `crate::…`                | [crate-relative paths] |
| `self::…`                 | [module-relative paths] |
| `super::…`                | [parent module paths] |
| `Type::…`<br>`<Type as Trait>::ident` | [associated items] |
| `<Type>::…`               | [qualified paths] which can be used for types without names such as `<&T>::…`, `<[T]>::…`, etc. |
| `Trait::method(…)`<br>`Type::method(…)`<br>`<Type as Trait>::method(…)` | [disambiguated method calls] |
| `method::<…>(…)`<br>`path::<…>` | [generic arguments], aka turbofish |
| `()`                      | [unit] |
| `(expr)`                  | [parenthesized expressions] |
| `(expr,)`                 | [single-element tuple expressions] |
| `(expr, …)`               | [tuple expressions] |
| `expr(expr, …)`           | [call expressions] |
| `expr.0`, `expr.1`, …     | [tuple indexing expressions] |
| `expr.ident`              | [field access expressions] |
| `{…}`                     | [block expressions] |
| `Type {…}`                | [struct expressions] |
| `Type(…)`                 | [tuple struct constructors] |
| `[…]`                     | [array expressions] |
| `[expr; len]`             | [repeat array expressions] |
| `expr[..]`, `expr[a..]`, `expr[..b]`, `expr[a..b]`, `expr[a..=b]`, `expr[..=b]` | [array and slice indexing expressions] |
| `if expr {…} else {…}`    | [if expressions] |
| `match expr { pattern => {…} }` | [match expressions] |
| `loop {…}`                | [infinite loop expressions] |
| `while expr {…}`          | [predicate loop expressions] |
| `for pattern in expr {…}` | [iterator loops] |
| `&expr`<br>`&mut expr`    | [borrow expressions] |
| `&raw const expr`<br>`&raw mut expr` | [raw borrow expressions] |
| `*expr`                   | [dereference expressions] |
| `expr?`                   | [try propagation expressions] |
| `-expr`                   | [negation expressions] |
| `!expr`                   | [bitwise and logical NOT expressions] |
| `expr as Type`            | [type cast expressions] |

## Items

[Items] are the components of a crate.

| Item                          | Use |
|-------------------------------|-----|
| `mod ident;`<br>`mod ident {…}` | [modules] |
| `use path;`                   | [use declarations] |
| `fn ident(…) {…}`             | [functions] |
| `type Type = Type;`           | [type aliases] |
| `struct ident {…}`            | [structs] |
| `enum ident {…}`              | [enumerations] |
| `union ident {…}`             | [unions] |
| `trait ident {…}`             | [traits] |
| `impl Type {…}`<br>`impl Type for Trait {…}` | [implementations] |
| `const ident = expr;`         | [constant items] |
| `static ident = expr;`        | [static items] |
| `extern "C" {…}`              | [external blocks] |
| `fn ident<…>(…) …`<br>`struct ident<…> {…}`<br>`enum ident<…> {…}`<br>`impl<…> Type<…> {…}` | [generic definitions] |

## Type expressions

[Type expressions] are used to refer to types.

| Type                                  | Use |
|---------------------------------------|-----|
| `bool`, `u8`, `f64`, `str`, …         | [primitive types] |
| `for<…>`                              | [higher-ranked trait bounds] |
| `T: TraitA + TraitB`                  | [trait bounds] |
| `T: 'a + 'b`                          | [lifetime bounds] |
| `T: TraitA + 'a`                      | [trait and lifetime bounds] |
| `T: ?Sized`                           | [relaxed trait bounds] |
| `[Type; len]`                         | [array types] |
| `(Type, …)`                           | [tuple types] |
| `[Type]`                              | [slice types] |
| `(Type)`                              | [parenthesized types] |
| `impl Trait`                          | [impl trait types], [anonymous type parameters] |
| `dyn Trait`                           | [trait object types] |
| `ident`<br>`ident::…`                 | [type paths] (can refer to [structs], [enumerations], [unions], [type aliases], [traits], [generics], etc.) |
| `Type<…>`<br>`Trait<…>`               | [generic arguments] (e.g. `Vec<u8>`) |
| `Trait<ident = Type>`                 | [associated type bindings] (e.g. `Iterator<Item = T>`) |
| `Trait<ident: …>`                     | [associated type bounds] (e.g. `Iterator<Item: Send>`) |
| `&Type`<br>`&mut Type`                | [reference types] |
| `*mut Type`<br>`*const Type`          | [raw pointer types] |
| `fn(…) -> Type`                       | [function pointer types] |
| `_`                                   | [inferred type], [inferred const] |
| `'_`                                  | [placeholder lifetime] |
| `!`                                   | [never type] |

## Patterns

[Patterns] are used to match values.

| Pattern                           | Use |
|-----------------------------------|-----|
| `"foo"`, `'a'`, `123`, `2.4`, …   | [literal patterns] |
| `ident`                           | [identifier patterns] |
| `_`                               | [wildcard pattern] |
| `..`                              | [rest pattern] |
| `a..`, `..b`, `a..b`, `a..=b`, `..=b` | [range patterns] |
| `&pattern`<br>`&mut pattern`      | [reference patterns] |
| `path {…}`                        | [struct patterns] |
| `path(…)`                         | [tuple struct patterns] |
| `(pattern, …)`                    | [tuple patterns] |
| `(pattern)`                       | [grouped patterns] |
| `[pattern, …]`                    | [slice patterns] |
| `CONST`, `Enum::Variant`, …       | [path patterns] |

[`'static` lifetimes]: bound
[`if let` patterns]: expr.if.let
[`self` paths]: paths.qualifiers.mod-self
[`Self` type paths]: paths.qualifiers.type-self
[anonymous type parameters]: type.impl-trait.param
[arith]: expr.arith-logic
[array and slice indexing expressions]: expr.array.index
[array expressions]: expr.array
[array types]: type.array
[assembly operands]: asm.operand-type.supported-operands.in
[assignment]: expr.assign
[associated items]: items.associated
[associated type bindings]: paths.expr
[associated type bounds]: paths.expr
[async blocks]: expr.block.async
[async closures]: expr.closure.async
[async functions]: items.fn.async
[await expressions]: expr.await
[bitwise and logical NOT expressions]: expr.negate
[block expressions]: expr.block
[boolean expressions]: expr.literal
[boolean type]: type.bool
[borrow expressions]: expr.operator.borrow
[borrow]: expr.operator.borrow
[break expressions]: expr.loop.break
[byte literals]: lex.token.byte
[byte string literals]: lex.token.str-byte
[C string literals]: lex.token.str-c
[call expressions]: expr.call
[character literals]: lex.token.literal.char
[closure expressions]: expr.closure
[closures]: expr.closure
[comparison]: expr.cmp
[compound]: expr.compound-assign
[configuration predicates]: cfg
[const assembly operands]: asm.operand-type.supported-operands.const
[const blocks]: expr.block.const
[const functions]: const-eval.const-fn
[const generics]: items.generics.const
[const items]: items.const
[constant items]: items.const
[continue expressions]: expr.loop.continue
[crate-relative paths]: paths.qualifiers.crate
[dereference expressions]: expr.deref
[dereference]: expr.deref
[destructuring assignment]: expr.placeholder
[disambiguated method calls]: expr.call.desugar
[enumerations]: items.enum
[explicit crate paths]: paths.qualifiers.global-root
[extern crate]: items.extern-crate
[extern function pointer types]: type.fn-pointer.qualifiers
[extern function qualifier]: items.fn.extern
[external block functions]: items.extern.fn
[external block statics]: items.extern.static
[external blocks]: items.extern
[field access expressions]: expr.field
[field]: expr.field
[function pointer type]: type.fn-pointer
[function pointer types]: type.fn-pointer
[functions]: items.fn
[generic arguments]: items.generics
[generic definitions]: items.generics
[generics]: items.generics
[glob imports]: items.use.glob
[grouped patterns]: patterns.paren
[higher-ranked trait bounds]: bound.higher-ranked
[identifier patterns]: patterns.ident
[identifiers]: ident
[if expressions]: expr.if
[if let]: expr.if.let
[impl trait types]: type.impl-trait.return
[implementations]: items.impl
[inferred const]: items.generics.const.inferred
[inferred type]: type.inferred
[infinite loop expressions]: expr.loop.infinite
[infinite loops]: expr.loop.infinite
[inherent impls]: items.impl.inherent
[inner attribute]: attributes.inner
[iterator loops]: expr.loop.for
[lazy-bool]: expr.bool-logic
[let statements]: statement.let
[lifetime bounds]: bound.lifetime
[lifetimes and loop labels]: lex.token.life
[literal patterns]: patterns.literal
[macro calls]: macro.invocation
[macro invocations]: macro.invocation
[macro Kleene matcher]: macro.decl.repetition
[macro matcher fragment specifier]: macro.decl.meta.specifier
[macro metavariable]: macro.decl.meta
[macro repetition]: macro.decl.repetition
[macros by example]: macro.decl
[macros]: macro.decl
[match expressions]: expr.match
[match guards]: expr.match.guard
[match]: expr.match
[method calls]: expr.method
[module-relative paths]: paths.qualifiers.mod-self
[modules]: items.mod
[negation expressions]: expr.negate
[negation]: expr.negate
[negative impls]: items.impl
[never type]: type.never
[number literals]: lex.token.literal.num
[or patterns]: patterns.or
[outer attribute]: attributes.outer
[parent module paths]: paths.qualifiers.super
[parenthesized expressions]: expr.paren
[parenthesized types]: type.name.parenthesized
[path patterns]: patterns.path
[placeholder lifetime]: lifetime-elision.function.explicit-placeholder
[predicate loop expressions]: expr.loop.while
[predicate loops]: expr.loop.while
[primitive types]: type.kinds
[qualified paths]: paths.qualified
[question]: expr.try
[range patterns]: patterns.range
[raw assembly]: asm.options.supported-options.raw
[raw borrow expressions]: expr.borrow.raw
[raw borrow operator]: expr.borrow.raw
[raw byte string literals]: lex.token.str-byte-raw
[raw C string literals]: lex.token.str-c-raw
[raw identifiers]: ident.raw
[raw lifetimes and loop labels]: lex.token.life
[raw pointer type]: type.pointer.raw
[raw pointer types]: type.pointer.raw
[raw pointers]: type.pointer.raw
[raw string literals]: lex.token.literal.str-raw
[reference patterns]: patterns.ref
[reference types]: type.pointer.reference
[references]: type.pointer.reference
[relaxed trait bounds]: bound.sized
[repeat array expressions]: expr.array
[reserved keyword]: lex.keywords.reserved
[rest pattern]: patterns.rest
[return expressions]: expr.return
[self parameters]: items.fn.params.self-pat
[single-element tuple expressions]: expr.tuple
[slice patterns]: patterns.slice
[slice types]: type.slice
[static items]: items.static
[string literals]: lex.token.literal.str
[struct expressions]: expr.struct
[struct patterns]: patterns.struct
[structs]: items.struct
[subpattern binding]: patterns.ident.scrutinized
[super paths]: paths.qualifiers.super
[trait and lifetime bounds]: bound
[trait bounds]: bound
[trait implementations]: items.impl.trait
[trait impls]: items.impl.trait
[trait items]: items.traits
[trait object types]: type.trait-object
[trait objects]: type.trait-object
[traits]: items.traits
[try propagation expressions]: expr.try
[tuple expressions]: expr.tuple
[tuple index]: expr.tuple-index
[tuple indexing expressions]: expr.tuple-index
[tuple patterns]: patterns.tuple
[tuple struct constructors]: items.struct.tuple
[tuple struct patterns]: patterns.tuple-struct
[tuple types]: type.tuple
[type aliases]: items.type
[type cast expressions]: expr.as
[Type expressions]: type.name
[type paths]: type.name.path
[union items]: items.union
[unions]: items.union
[unit]: type.tuple.unit
[unsafe attributes]: attributes.safety
[unsafe blocks]: expr.block.unsafe
[unsafe external blocks]: unsafe.extern
[unsafe external functions]: items.extern.fn.safety
[unsafe external statics]: items.extern.static.safety
[unsafe functions]: unsafe.fn
[unsafe modules]: items.mod.unsafe
[unsafe trait implementations]: items.impl.trait.safety
[unsafe traits]: items.traits.safety
[use bounds]: bound.use
[use declarations]: items.use
[use items]: items.use
[variadic functions]: items.extern.variadic
[visibility]: vis
[where clauses]: items.generics.where
[while let]: expr.loop.while.let
[wildcard pattern]: patterns.wildcard


---

r[macro.ambiguity]
# Appendix: Macro follow-set ambiguity formal specification

This page documents the formal specification of the follow rules for [Macros By Example]. They were originally specified in [RFC 550], from which the bulk of this text is copied, and expanded upon in subsequent RFCs.

r[macro.ambiguity.convention]
## Definitions & conventions

r[macro.ambiguity.convention.defs]
  - `macro`: anything invocable as `foo!(...)` in source code.
  - `MBE`: macro-by-example, a macro defined by `macro_rules`.
  - `matcher`: the left-hand-side of a rule in a `macro_rules` invocation, or a subportion thereof.
  - `macro parser`: the bit of code in the Rust parser that will parse the input using a grammar derived from all of the matchers.
  - `fragment`: The class of Rust syntax that a given matcher will accept (or "match").
  - `repetition` : a fragment that follows a regular repeating pattern
  - `NT`: non-terminal, the various "meta-variables" or repetition matchers that can appear in a matcher, specified in MBE syntax with a leading `$` character.
  - `simple NT`: a "meta-variable" non-terminal (further discussion below).
  - `complex NT`: a repetition matching non-terminal, specified via repetition operators (`*`, `+`, `?`).
  - `token`: an atomic element of a matcher; i.e. identifiers, operators, open/close delimiters, *and* simple NT's.
  - `token tree`: a tree structure formed from tokens (the leaves), complex NT's, and finite sequences of token trees.
  - `delimiter token`: a token that is meant to divide the end of one fragment and the start of the next fragment.
  - `separator token`: an optional delimiter token in an complex NT that separates each pair of elements in the matched repetition.
  - `separated complex NT`: a complex NT that has its own separator token.
  - `delimited sequence`: a sequence of token trees with appropriate open- and close-delimiters at the start and end of the sequence.
  - `empty fragment`: The class of invisible Rust syntax that separates tokens, i.e. whitespace, or (in some lexical contexts), the empty token sequence.
  - `fragment specifier`: The identifier in a simple NT that specifies which fragment the NT accepts.
  - `language`: a context-free language.

Example:

```rust,compile_fail
macro_rules! i_am_an_mbe {
    (start $foo:expr $($i:ident),* end) => ($foo)
}
```

r[macro.ambiguity.convention.matcher]
`(start $foo:expr $($i:ident),* end)` is a matcher. The whole matcher is a delimited sequence (with open- and close-delimiters `(` and `)`), and `$foo` and `$i` are simple NT's with `expr` and `ident` as their respective fragment specifiers.

r[macro.ambiguity.convention.complex-nt]
`$(i:ident),*` is *also* an NT; it is a complex NT that matches a comma-separated repetition of identifiers. The `,` is the separator token for the complex NT; it occurs in between each pair of elements (if any) of the matched fragment.

Another example of a complex NT is `$(hi $e:expr ;)+`, which matches any fragment of the form `hi <expr>; hi <expr>; ...` where `hi <expr>;` occurs at least once. Note that this complex NT does not have a dedicated separator token.

(Note that Rust's parser ensures that delimited sequences always occur with proper nesting of token tree structure and correct matching of open- and close-delimiters.)

r[macro.ambiguity.convention.vars]
We will tend to use the variable "M" to stand for a matcher, variables "t" and "u" for arbitrary individual tokens, and the variables "tt" and "uu" for arbitrary token trees. (The use of "tt" does present potential ambiguity with its additional role as a fragment specifier; but it will be clear from context which interpretation is meant.)

r[macro.ambiguity.convention.set]
"SEP" will range over separator tokens, "OP" over the repetition operators `*`, `+`, and `?`, "OPEN"/"CLOSE" over matching token pairs surrounding a delimited sequence (e.g. `[` and `]`).

r[macro.ambiguity.convention.sequence-vars]
Greek letters "α" "β" "γ" "δ"  stand for potentially empty token-tree sequences. (However, the Greek letter "ε" (epsilon) has a special role in the presentation and does not stand for a token-tree sequence.)

  * This Greek letter convention is usually just employed when the presence of a sequence is a technical detail; in particular, when we wish to *emphasize* that we are operating on a sequence of token-trees, we will use the notation "tt ..." for the sequence, not a Greek letter.

Note that a matcher is merely a token tree. A "simple NT", as mentioned above, is an meta-variable NT; thus it is a non-repetition. For example, `$foo:ty` is a simple NT but `$($foo:ty)+` is a complex NT.

Note also that in the context of this formalism, the term "token" generally *includes* simple NTs.

Finally, it is useful for the reader to keep in mind that according to the definitions of this formalism, no simple NT matches the empty fragment, and likewise no token matches the empty fragment of Rust syntax. (Thus, the *only* NT that can match the empty fragment is a complex NT.) This is not actually true, because the `vis` matcher can match an empty fragment. Thus, for the purposes of the formalism, we will treat `$v:vis` as actually being `$($v:vis)?`, with a requirement that the matcher match an empty fragment.

r[macro.ambiguity.invariant]
### The matcher invariants

r[macro.ambiguity.invariant.list]
To be valid, a matcher must meet the following three invariants. The definitions of FIRST and FOLLOW are described later.

1.  For any two successive token tree sequences in a matcher `M` (i.e. `M = ... tt uu ...`) with `uu ...` nonempty, we must have FOLLOW(`... tt`) ∪ {ε} ⊇ FIRST(`uu ...`).
1.  For any separated complex NT in a matcher, `M = ... $(tt ...) SEP OP ...`, we must have `SEP` ∈ FOLLOW(`tt ...`).
1.  For an unseparated complex NT in a matcher, `M = ... $(tt ...) OP ...`, if OP = `*` or `+`, we must have FOLLOW(`tt ...`) ⊇ FIRST(`tt ...`).

r[macro.ambiguity.invariant.follow-matcher]
The first invariant says that whatever actual token that comes after a matcher, if any, must be somewhere in the predetermined follow set.  This ensures that a legal macro definition will continue to assign the same determination as to where `... tt` ends and `uu ...` begins, even as new syntactic forms are added to the language.

r[macro.ambiguity.invariant.separated-complex-nt]
The second invariant says that a separated complex NT must use a separator token that is part of the predetermined follow set for the internal contents of the NT. This ensures that a legal macro definition will continue to parse an input fragment into the same delimited sequence of `tt ...`'s, even as new syntactic forms are added to the language.

r[macro.ambiguity.invariant.unseparated-complex-nt]
The third invariant says that when we have a complex NT that can match two or more copies of the same thing with no separation in between, it must be permissible for them to be placed next to each other as per the first invariant. This invariant also requires they be nonempty, which eliminates a possible ambiguity.

**NOTE: The third invariant is currently unenforced due to historical oversight and significant reliance on the behaviour. It is currently undecided what to do about this going forward. Macros that do not respect the behaviour may become invalid in a future edition of Rust. See the [tracking issue].**

r[macro.ambiguity.sets]
### FIRST and FOLLOW, informally

r[macro.ambiguity.sets.intro]
A given matcher M maps to three sets: FIRST(M), LAST(M) and FOLLOW(M).

Each of the three sets is made up of tokens. FIRST(M) and LAST(M) may also contain a distinguished non-token element ε ("epsilon"), which indicates that M can match the empty fragment. (But FOLLOW(M) is always just a set of tokens.)

Informally:

r[macro.ambiguity.sets.first]
  * FIRST(M): collects the tokens potentially used first when matching a fragment to M.

r[macro.ambiguity.sets.last]
  * LAST(M): collects the tokens potentially used last when matching a fragment to M.

r[macro.ambiguity.sets.follow]
  * FOLLOW(M): the set of tokens allowed to follow immediately after some fragment matched by M.

    In other words: t ∈ FOLLOW(M) if and only if there exists (potentially empty) token sequences α, β, γ, δ where:

      * M matches β,

      * t matches γ, and

      * The concatenation α β γ δ is a parseable Rust program.

r[macro.ambiguity.sets.universe]
We use the shorthand ANYTOKEN to denote the set of all tokens (including simple NTs). For example, if any token is legal after a matcher M, then FOLLOW(M) = ANYTOKEN.

(To review one's understanding of the above informal descriptions, the reader at this point may want to jump ahead to the [examples of FIRST/LAST](#examples-of-first-and-last) before reading their formal definitions.)

r[macro.ambiguity.sets.def]
### FIRST, LAST

r[macro.ambiguity.sets.def.intro]
Below are formal inductive definitions for FIRST and LAST.

r[macro.ambiguity.sets.def.notation]
"A ∪ B" denotes set union, "A ∩ B" denotes set intersection, and "A \ B" denotes set difference (i.e. all elements of A that are not present in B).

r[macro.ambiguity.sets.def.first]
#### FIRST

r[macro.ambiguity.sets.def.first.intro]
FIRST(M) is defined by case analysis on the sequence M and the structure of its first token-tree (if any):

r[macro.ambiguity.sets.def.first.epsilon]
  * if M is the empty sequence, then FIRST(M) = { ε },

r[macro.ambiguity.sets.def.first.token]
  * if M starts with a token t, then FIRST(M) = { t },

    (Note: this covers the case where M starts with a delimited token-tree sequence, `M = OPEN tt ... CLOSE ...`, in which case `t = OPEN` and thus FIRST(M) = { `OPEN` }.)

    (Note: this critically relies on the property that no simple NT matches the empty fragment.)

r[macro.ambiguity.sets.def.first.complex]
  * Otherwise, M is a token-tree sequence starting with a complex NT: `M = $( tt ... ) OP α`, or `M = $( tt ... ) SEP OP α`, (where `α` is the (potentially empty) sequence of token trees for the rest of the matcher).

      * Let SEP\_SET(M) = { SEP } if SEP is present and ε ∈ FIRST(`tt ...`); otherwise SEP\_SET(M) = {}.

  * Let ALPHA\_SET(M) = FIRST(`α`) if OP = `*` or `?` and ALPHA\_SET(M) = {} if OP = `+`.
  * FIRST(M) = (FIRST(`tt ...`) \\ {ε}) ∪ SEP\_SET(M) ∪ ALPHA\_SET(M).

The definition for complex NTs deserves some justification. SEP\_SET(M) defines the possibility that the separator could be a valid first token for M, which happens when there is a separator defined and the repeated fragment could be empty. ALPHA\_SET(M) defines the possibility that the complex NT could be empty, meaning that M's valid first tokens are those of the following token-tree sequences `α`. This occurs when either `*` or `?` is used, in which case there could be zero repetitions. In theory, this could also occur if `+` was used with a potentially-empty repeating fragment, but this is forbidden by the third invariant.

From there, clearly FIRST(M) can include any token from SEP\_SET(M) or ALPHA\_SET(M), and if the complex NT match is nonempty, then any token starting FIRST(`tt ...`) could work too. The last piece to consider is ε. SEP\_SET(M) and FIRST(`tt ...`) \ {ε} cannot contain ε, but ALPHA\_SET(M) could. Hence, this definition allows M to accept ε if and only if ε ∈ ALPHA\_SET(M) does. This is correct because for M to accept ε in the complex NT case, both the complex NT and α must accept it. If OP = `+`, meaning that the complex NT cannot be empty, then by definition ε ∉ ALPHA\_SET(M). Otherwise, the complex NT can accept zero repetitions, and then ALPHA\_SET(M) = FOLLOW(`α`). So this definition is correct with respect to \varepsilon as well.

r[macro.ambiguity.sets.def.last]
#### LAST

r[macro.ambiguity.sets.def.last.intro]
LAST(M), defined by case analysis on M itself (a sequence of token-trees):

r[macro.ambiguity.sets.def.last.empty]
  * if M is the empty sequence, then LAST(M) = { ε }

r[macro.ambiguity.sets.def.last.token]
  * if M is a singleton token t, then LAST(M) = { t }

r[macro.ambiguity.sets.def.last.rep-star]
  * if M is the singleton complex NT repeating zero or more times, `M = $( tt ... ) *`, or `M = $( tt ... ) SEP *`

      * Let sep_set = { SEP } if SEP present; otherwise sep_set = {}.

      * if ε ∈ LAST(`tt ...`) then LAST(M) = LAST(`tt ...`) ∪ sep_set

      * otherwise, the sequence `tt ...` must be non-empty; LAST(M) = LAST(`tt ...`) ∪ {ε}.

r[macro.ambiguity.sets.def.last.rep-plus]
  * if M is the singleton complex NT repeating one or more times, `M = $( tt ... ) +`, or `M = $( tt ... ) SEP +`

      * Let sep_set = { SEP } if SEP present; otherwise sep_set = {}.

      * if ε ∈ LAST(`tt ...`) then LAST(M) = LAST(`tt ...`) ∪ sep_set

      * otherwise, the sequence `tt ...` must be non-empty; LAST(M) = LAST(`tt ...`)

r[macro.ambiguity.sets.def.last.rep-question]
  * if M is the singleton complex NT repeating zero or one time, `M = $( tt ...) ?`, then LAST(M) = LAST(`tt ...`) ∪ {ε}.

r[macro.ambiguity.sets.def.last.delim]
  * if M is a delimited token-tree sequence `OPEN tt ... CLOSE`, then LAST(M) = { `CLOSE` }.

r[macro.ambiguity.sets.def.last.sequence]
  * if M is a non-empty sequence of token-trees `tt uu ...`,

      * If ε ∈ LAST(`uu ...`), then LAST(M) = LAST(`tt`) ∪ (LAST(`uu ...`) \ { ε }).

      * Otherwise, the sequence `uu ...` must be non-empty; then LAST(M) = LAST(`uu ...`).

### Examples of FIRST and LAST

Below are some examples of FIRST and LAST. (Note in particular how the special ε element is introduced and eliminated based on the interaction between the pieces of the input.)

Our first example is presented in a tree structure to elaborate on how the analysis of the matcher composes. (Some of the simpler subtrees have been elided.)

```text
INPUT:  $(  $d:ident   $e:expr   );*    $( $( h )* );*    $( f ; )+   g
            ~~~~~~~~   ~~~~~~~                ~
                |         |                   |
FIRST:   { $d:ident }  { $e:expr }          { h }


INPUT:  $(  $d:ident   $e:expr   );*    $( $( h )* );*    $( f ; )+
            ~~~~~~~~~~~~~~~~~~             ~~~~~~~           ~~~
                        |                      |               |
FIRST:          { $d:ident }               { h, ε }         { f }

INPUT:  $(  $d:ident   $e:expr   );*    $( $( h )* );*    $( f ; )+   g
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~~~~~~~~    ~~~~~~~~~   ~
                        |                       |              |       |
FIRST:        { $d:ident, ε }            {  h, ε, ;  }      { f }   { g }


INPUT:  $(  $d:ident   $e:expr   );*    $( $( h )* );*    $( f ; )+   g
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                        |
FIRST:                       { $d:ident, h, ;,  f }
```

Thus:

 * FIRST(`$($d:ident $e:expr );* $( $(h)* );* $( f ;)+ g`) = { `$d:ident`, `h`, `;`, `f` }

Note however that:

 * FIRST(`$($d:ident $e:expr );* $( $(h)* );* $($( f ;)+ g)*`) = { `$d:ident`, `h`, `;`, `f`, ε }

Here are similar examples but now for LAST.

 * LAST(`$d:ident $e:expr`) = { `$e:expr` }
 * LAST(`$( $d:ident $e:expr );*`) = { `$e:expr`, ε }
 * LAST(`$( $d:ident $e:expr );* $(h)*`) = { `$e:expr`, ε, `h` }
 * LAST(`$( $d:ident $e:expr );* $(h)* $( f ;)+`) = { `;` }
 * LAST(`$( $d:ident $e:expr );* $(h)* $( f ;)+ g`) = { `g` }

r[macro.ambiguity.sets.def.follow]
### FOLLOW(M)

r[macro.ambiguity.sets.def.follow.intro]
Finally, the definition for FOLLOW(M) is built up as follows. pat, expr, etc. represent simple nonterminals with the given fragment specifier.

r[macro.ambiguity.sets.def.follow.pat]
  * FOLLOW(pat) = {`=>`, `,`, `=`, `|`, `if`, `in`}`.

r[macro.ambiguity.sets.def.follow.expr-stmt]
  * FOLLOW(expr) = FOLLOW(expr_2021) = FOLLOW(stmt) =  {`=>`, `,`, `;`}`.

r[macro.ambiguity.sets.def.follow.ty-path]
  * FOLLOW(ty) = FOLLOW(path) = {`{`, `[`, `,`, `=>`, `:`, `=`, `>`, `>>`, `;`, `|`, `as`, `where`, block nonterminals}.

r[macro.ambiguity.sets.def.follow.vis]
  * FOLLOW(vis) = {`,`l any keyword or identifier except a non-raw `priv`; any token that can begin a type; ident, ty, and path nonterminals}.

r[macro.ambiguity.sets.def.follow.simple]
  * FOLLOW(t) = ANYTOKEN for any other simple token, including block, ident, tt, item, lifetime, literal and meta simple nonterminals, and all terminals.

r[macro.ambiguity.sets.def.follow.other-matcher]
  * FOLLOW(M), for any other M, is defined as the intersection, as t ranges over (LAST(M) \ {ε}), of FOLLOW(t).

r[macro.ambiguity.sets.def.follow.type-first]
The tokens that can begin a type are, as of this writing, {`(`, `[`, `!`, `*`, `&`, `&&`, `?`, lifetimes, `>`, `>>`, `::`, any non-keyword identifier, `super`, `self`, `Self`, `extern`, `crate`, `$crate`, `_`, `for`, `impl`, `fn`, `unsafe`, `typeof`, `dyn`}, although this list may not be complete because people won't always remember to update the appendix when new ones are added.

Examples of FOLLOW for complex M:

 * FOLLOW(`$( $d:ident $e:expr )*`) = FOLLOW(`$e:expr`)
 * FOLLOW(`$( $d:ident $e:expr )* $(;)*`) = FOLLOW(`$e:expr`) ∩ ANYTOKEN = FOLLOW(`$e:expr`)
 * FOLLOW(`$( $d:ident $e:expr )* $(;)* $( f |)+`) = ANYTOKEN

### Examples of valid and invalid matchers

With the above specification in hand, we can present arguments for why particular matchers are legal and others are not.

 * `($ty:ty < foo ,)` : illegal, because FIRST(`< foo ,`) = { `<` } ⊈ FOLLOW(`ty`)

 * `($ty:ty , foo <)` : legal, because FIRST(`, foo <`) = { `,` }  is ⊆ FOLLOW(`ty`).

 * `($pa:pat $pb:pat $ty:ty ,)` : illegal, because FIRST(`$pb:pat $ty:ty ,`) = { `$pb:pat` } ⊈ FOLLOW(`pat`), and also FIRST(`$ty:ty ,`) = { `$ty:ty` } ⊈ FOLLOW(`pat`).

 * `( $($a:tt $b:tt)* ; )` : legal, because FIRST(`$b:tt`) = { `$b:tt` } is ⊆ FOLLOW(`tt`) = ANYTOKEN, as is FIRST(`;`) = { `;` }.

 * `( $($t:tt),* , $(t:tt),* )` : legal,  (though any attempt to actually use this macro will signal a local ambiguity error during expansion).

 * `($ty:ty $(; not sep)* -)` : illegal, because FIRST(`$(; not sep)* -`) = { `;`, `-` } is not in FOLLOW(`ty`).

 * `($($ty:ty)-+)` : illegal, because separator `-` is not in FOLLOW(`ty`).

 * `($($e:expr)*)` : illegal, because expr NTs are not in FOLLOW(expr NT).

[Macros by Example]: macros-by-example.md
[RFC 550]: https://github.com/rust-lang/rfcs/blob/master/text/0550-macro-future-proofing.md
[tracking issue]: https://github.com/rust-lang/rust/issues/56575


---

# Influences

Rust is not a particularly original language, with design elements coming from a wide range of sources. Some of these are listed below (including elements that have since been removed):

* SML, OCaml: algebraic data types, pattern matching, type inference, semicolon statement separation
* C++: references, RAII, smart pointers, move semantics, monomorphization, memory model
* ML Kit, Cyclone: region based memory management
* Haskell (GHC): typeclasses, type families
* Newsqueak, Alef, Limbo: channels, concurrency
* Erlang: message passing, thread failure, ~~linked thread failure~~, ~~lightweight concurrency~~
* Swift: optional bindings
* Scheme: hygienic macros
* C#: attributes
* Ruby: closure syntax, ~~block syntax~~
* NIL, Hermes: ~~typestate~~
* [Unicode Annex #31](http://www.unicode.org/reports/tr31/): identifier and pattern syntax


---

# Test summary

The following is a summary of the total tests that are linked to individual rule identifiers within the reference.

{{summary-table}}


---

# Glossary

r[glossary.ast]
### Abstract syntax tree

An ‘abstract syntax tree’, or ‘AST’, is an intermediate representation of the structure of the program when the compiler is compiling it.

### Alignment

The alignment of a value specifies what addresses values are preferred to start at. Always a power of two. References to a value must be aligned. [More][alignment].

r[glossary.abi]
### Application binary interface (ABI)

An *application binary interface* (ABI) defines how compiled code interacts with other compiled code. With [`extern` blocks] and [`extern fn`], *ABI strings* affect:

- **Calling convention**: How function arguments are passed, values are returned (e.g., in registers or on the stack), and who is responsible for cleaning up the stack.
- **Unwinding**: Whether stack unwinding is allowed. For example, the `"C-unwind"` ABI allows unwinding across the FFI boundary, while the `"C"` ABI does not.

### Arity

Arity refers to the number of arguments a function or operator takes. For some examples, `f(2, 3)` and `g(4, 6)` have arity 2, while `h(8, 2, 6)` has arity 3. The `!` operator has arity 1.

### Array

An array, sometimes also called a fixed-size array or an inline array, is a value describing a collection of elements, each selected by an index that can be computed at run time by the program. It occupies a contiguous region of memory.

### Associated item

An associated item is an item that is associated with another item. Associated items are defined in [implementations] and declared in [traits]. Only functions, constants, and type aliases can be associated. Contrast to a [free item].

### Blanket implementation

Any implementation where a type appears [uncovered](#uncovered-type). `impl<T> Foo for T`, `impl<T> Bar<T> for T`, `impl<T> Bar<Vec<T>> for T`, and `impl<T> Bar<T> for Vec<T>` are considered blanket impls. However, `impl<T> Bar<Vec<T>> for Vec<T>` is not a blanket impl, as all instances of `T` which appear in this `impl` are covered by `Vec`.

### Bound

Bounds are constraints on a type or trait. For example, if a bound is placed on the argument a function takes, types passed to that function must abide by that constraint.

### Combinator

Combinators are higher-order functions that apply only functions and earlier defined combinators to provide a result from its arguments. They can be used to manage control flow in a modular fashion.

### Crate

A crate is the unit of compilation and linking. There are different [types of crates], such as libraries or executables. Crates may link and refer to other library crates, called external crates. A crate has a self-contained tree of [modules], starting from an unnamed root module called the crate root. [Items] may be made visible to other crates by marking them as public in the crate root, including through [paths] of public modules. [More][crate].

### Dispatch

Dispatch is the mechanism to determine which specific version of code is actually run when it involves polymorphism. Two major forms of dispatch are static dispatch and dynamic dispatch. Rust supports dynamic dispatch through the use of [trait objects][type.trait-object].

### Dynamically sized type

A dynamically sized type (DST) is a type without a statically known size or alignment.

### Entity

An [*entity*] is a language construct that can be referred to in some way within the source program, usually via a [path][paths]. Entities include [types], [items], [generic parameters], [variable bindings], [loop labels], [lifetimes], [fields], [attributes], and [lints].

### Expression

An expression is a combination of values, constants, variables, operators and functions that evaluate to a single value, with or without side-effects.

For example, `2 + (3 * 4)` is an expression that returns the value 14.

### Free item

An [item] that is not a member of an [implementation], such as a *free function* or a *free const*. Contrast to an [associated item].

### Fundamental traits

A fundamental trait is one where adding an impl of it for an existing type is a breaking change. The `Fn` traits and `Sized` are fundamental.

### Fundamental type constructors

A fundamental type constructor is a type where implementing a [blanket implementation](#blanket-implementation) over it is a breaking change. `&`, `&mut`, `Box`, and `Pin`  are fundamental.

Any time a type `T` is considered [local](#local-type), `&T`, `&mut T`, `Box<T>`, and `Pin<T>` are also considered local. Fundamental type constructors cannot [cover](#uncovered-type) other types. Any time the term "covered type" is used, the `T` in `&T`, `&mut T`, `Box<T>`, and `Pin<T>` is not considered covered.

### Inhabited

A type is inhabited if it has constructors and therefore can be instantiated. An inhabited type is not "empty" in the sense that there can be values of the type. Opposite of [Uninhabited](#uninhabited).

### Inherent implementation

An [implementation] that applies to a nominal type, not to a trait-type pair. [More][inherent implementation].

### Inherent method

A [method] defined in an [inherent implementation], not in a trait implementation.

### Initialized

A variable is initialized if it has been assigned a value and hasn't since been moved from. All other memory locations are assumed to be uninitialized. Only unsafe Rust can create a memory location without initializing it.

### Local trait

A `trait` which was defined in the current crate. A trait definition is local or not independent of applied type arguments. Given `trait Foo<T, U>`, `Foo` is always local, regardless of the types substituted for `T` and `U`.

### Local type

A `struct`, `enum`, or `union` which was defined in the current crate. This is not affected by applied type arguments. `struct Foo` is considered local, but `Vec<Foo>` is not. `LocalType<ForeignType>` is local. Type aliases do not affect locality.

### Module

A module is a container for zero or more [items]. Modules are organized in a tree, starting from an unnamed module at the root called the crate root or the root module. [Paths] may be used to refer to items from other modules, which may be restricted by [visibility rules]. [More][modules]

### Name

A [*name*] is an [identifier] or [lifetime or loop label] that refers to an [entity](#entity). A *name binding* is when an entity declaration introduces an identifier or label associated with that entity. [Paths], identifiers, and labels are used to refer to an entity.

### Name resolution

[*Name resolution*] is the compile-time process of tying [paths], [identifiers], and [labels] to [entity](#entity) declarations.

### Namespace

A *namespace* is a logical grouping of declared [names](#name) based on the kind of [entity](#entity) the name refers to. Namespaces allow the occurrence of a name in one namespace to not conflict with the same name in another namespace.

Within a namespace, names are organized in a hierarchy, where each level of the hierarchy has its own collection of named entities.

### Nominal types

Types that can be referred to by a path directly. Specifically [enums], [structs], [unions], and [trait object types].

### Dyn-compatible traits

[Traits] that can be used in [trait object types] (`dyn Trait`). Only traits that follow specific [rules][dyn compatibility] are *dyn compatible*.

These were formerly known as *object safe* traits.

### Path

A [*path*] is a sequence of one or more path segments used to refer to an [entity](#entity) in the current scope or other levels of a [namespace](#namespace) hierarchy.

### Prelude

Prelude, or The Rust Prelude, is a small collection of items - mostly traits - that are imported into every module of every crate. The traits in the prelude are pervasive.

### Scope

A [*scope*] is the region of source text where a named [entity](#entity) may be referenced with that name.

### Scrutinee

A scrutinee is the expression that is matched on in `match` expressions and similar pattern matching constructs. For example, in `match x { A => 1, B => 2 }`, the expression `x` is the scrutinee.

### Size

The size of a value has two definitions.

The first is that it is how much memory must be allocated to store that value.

The second is that it is the offset in bytes between successive elements in an array with that item type.

It is a multiple of the alignment, including zero. The size can change depending on compiler version (as new optimizations are made) and target platform (similar to how `usize` varies per-platform).

[More][alignment].

### Slice

A slice is dynamically-sized view into a contiguous sequence, written as `[T]`.

It is often seen in its borrowed forms, either mutable or shared. The shared slice type is `&[T]`, while the mutable slice type is `&mut [T]`, where `T` represents the element type.

### Statement

A statement is the smallest standalone element of a programming language that commands a computer to perform an action.

### String literal

A string literal is a string stored directly in the final binary, and so will be valid for the `'static` duration.

Its type is `'static` duration borrowed string slice, `&'static str`.

### String slice

A string slice is the most primitive string type in Rust, written as `str`. It is often seen in its borrowed forms, either mutable or shared. The shared string slice type is `&str`, while the mutable string slice type is `&mut str`.

Strings slices are always valid UTF-8.

### Trait

A trait is a language item that is used for describing the functionalities a type must provide. It allows a type to make certain promises about its behavior.

Generic functions and generic structs can use traits to constrain, or bound, the types they accept.

### Turbofish

Paths with generic parameters in expressions must prefix the opening brackets with a `::`. Combined with the angular brackets for generics, this looks like a fish `::<>`. As such, this syntax is colloquially referred to as turbofish syntax.

Examples:

```rust
let ok_num = Ok::<_, ()>(5);
let vec = [1, 2, 3].iter().map(|n| n * 2).collect::<Vec<_>>();
```

This `::` prefix is required to disambiguate generic paths with multiple comparisons in a comma-separate list. See [the bastion of the turbofish][turbofish test] for an example where not having the prefix would be ambiguous.

### Uncovered type

A type which does not appear as an argument to another type. For example, `T` is uncovered, but the `T` in `Vec<T>` is covered. This is only relevant for type arguments.

### Undefined behavior

Compile-time or run-time behavior that is not specified. This may result in, but is not limited to: process termination or corruption; improper, incorrect, or unintended computation; or platform-specific results. [More][undefined-behavior].

r[glossary.uninhabited]
### Uninhabited

A type is uninhabited if it has no constructors and therefore can never be instantiated. An uninhabited type is "empty" in the sense that there are no values of the type. The canonical example of an uninhabited type is the [never type] `!`, or an enum with no variants `enum Never { }`. Opposite of [Inhabited](#inhabited).

[`extern` blocks]: items.extern
[`extern fn`]: items.fn.extern
[alignment]: type-layout.md#size-and-alignment
[associated item]: #associated-item
[attributes]: attributes.md
[*entity*]: names.md
[crate]: crates-and-source-files.md
[dyn compatibility]: items/traits.md#dyn-compatibility
[enums]: items/enumerations.md
[fields]: expressions/field-expr.md
[free item]: #free-item
[generic parameters]: items/generics.md
[identifier]: identifiers.md
[identifiers]: identifiers.md
[implementation]: items/implementations.md
[implementations]: items/implementations.md
[inherent implementation]: items/implementations.md#inherent-implementations
[item]: items.md
[items]: items.md
[labels]: tokens.md#lifetimes-and-loop-labels
[lifetime or loop label]: tokens.md#lifetimes-and-loop-labels
[lifetimes]: tokens.md#lifetimes-and-loop-labels
[lints]: attributes/diagnostics.md#lint-check-attributes
[loop labels]: tokens.md#lifetimes-and-loop-labels
[method]: items/associated-items.md#methods
[modules]: items/modules.md
[*Name resolution*]: names/name-resolution.md
[*name*]: names.md
[*namespace*]: names/namespaces.md
[never type]: types/never.md
[*path*]: paths.md
[Paths]: paths.md
[*scope*]: names/scopes.md
[structs]: items/structs.md
[trait object types]: types/trait-object.md
[traits]: items/traits.md
[turbofish test]: https://github.com/rust-lang/rust/blob/1.58.0/src/test/ui/parser/bastion-of-the-turbofish.rs
[types of crates]: linkage.md
[types]: types.md
[undefined-behavior]: behavior-considered-undefined.md
[unions]: items/unions.md
[variable bindings]: patterns.md
[visibility rules]: visibility-and-privacy.md
