r[stmt-expr]
# Statements and expressions

Rust is _primarily_ an expression language. This means that most forms of value-producing or effect-causing evaluation are directed by the uniform syntax category of _expressions_. Each kind of expression can typically _nest_ within each other kind of expression, and rules for evaluation of expressions involve specifying both the value produced by the expression and the order in which its sub-expressions are themselves evaluated.

In contrast, statements serve _mostly_ to contain and explicitly sequence expression evaluation.


---

r[statement]
# Statements

r[statement.syntax]
```grammar,statements
Statement ->
      `;`
    | Item
    | LetStatement
    | ExpressionStatement
    | OuterAttribute* MacroInvocationSemi
```

r[statement.intro]
A *statement* is a component of a [block], which is in turn a component of an outer [expression] or [function].

r[statement.kind]
Rust has two kinds of statement: [declaration statements](#declaration-statements) and [expression statements](#expression-statements).

r[statement.decl]
## Declaration statements

A *declaration statement* is one that introduces one or more *names* into the enclosing statement block. The declared names may denote new variables or new [items][item].

The two kinds of declaration statements are item declarations and `let` statements.

r[statement.item]
### Item declarations

r[statement.item.intro]
An *item declaration statement* has a syntactic form identical to an [item declaration][item] within a [module].

r[statement.item.scope]
Declaring an item within a statement block restricts its [scope] to the block containing the statement. The item is not given a [canonical path] nor are any sub-items it may declare.

r[statement.item.associated-scope]
The exception to this is that associated items defined by [implementations] are still accessible in outer scopes as long as the item and, if applicable, trait are accessible. It is otherwise identical in meaning to declaring the item inside a module.

r[statement.item.outer-generics]
There is no implicit capture of the containing function's generic parameters, parameters, and local variables. For example, `inner` may not access `outer_var`.

```rust
fn outer() {
  let outer_var = true;

  fn inner() { /* outer_var is not in scope here */ }

  inner();
}
```

r[statement.let]
### `let` statements

r[statement.let.syntax]
```grammar,statements
LetStatement ->
    OuterAttribute* `let` PatternNoTopAlt ( `:` Type )?
    (
          `=` Expression
        | `=` Expression _except [LazyBooleanExpression] or end with a `}`_ `else` BlockExpression
    )? `;`
```

r[statement.let.intro]
A *`let` statement* introduces a new set of [variables], given by a [pattern]. The pattern is followed optionally by a type annotation and then either ends, or is followed by an initializer expression plus an optional `else` block.

r[statement.let.inference]
When no type annotation is given, the compiler will infer the type, or signal an error if insufficient type information is available for definite inference.

r[statement.let.scope]
Any variables introduced by a variable declaration are visible from the point of declaration until the end of the enclosing block scope, except when they are shadowed by another variable declaration.

r[statement.let.constraint]
If an `else` block is not present, the pattern must be irrefutable. If an `else` block is present, the pattern may be refutable.

r[statement.let.behavior]
If the pattern does not match (this requires it to be refutable), the `else` block is executed. The `else` block must always diverge (evaluate to the [never type]).

```rust
let (mut v, w) = (vec![1, 2, 3], 42); // The bindings may be mut or const
let Some(t) = v.pop() else { // Refutable patterns require an else block
    panic!(); // The else block must diverge
};
let [u, v] = [v[0], v[1]] else { // This pattern is irrefutable, so the compiler
                                 // will lint as the else block is redundant.
    panic!();
};
```

r[statement.expr]
## Expression statements

r[statement.expr.syntax]
```grammar,statements
ExpressionStatement ->
      ExpressionWithoutBlock `;`
    | ExpressionWithBlock `;`?
```

r[statement.expr.intro]
An *expression statement* is one that evaluates an [expression] and ignores its result. As a rule, an expression statement's purpose is to trigger the effects of evaluating its expression.

r[statement.expr.restriction-semicolon]
An expression that consists of only a [block expression][block] or control flow expression, if used in a context where a statement is permitted, can omit the trailing semicolon. This can cause an ambiguity between it being parsed as a standalone statement and as a part of another expression; in this case, it is parsed as a statement.

r[statement.expr.constraint-block]
The type of [ExpressionWithBlock] expressions when used as statements must be the unit type.

```rust
# let mut v = vec![1, 2, 3];
v.pop();          // Ignore the element returned from pop
if v.is_empty() {
    v.push(5);
} else {
    v.remove(0);
}                 // Semicolon can be omitted.
[1];              // Separate expression statement, not an indexing expression.
```

When the trailing semicolon is omitted, the result must be type `()`.

```rust
// bad: the block's type is i32, not ()
// Error: expected `()` because of default return type
// if true {
//   1
// }

// good: the block's type is i32
if true {
  1
} else {
  2
};
```

r[statement.attribute]
## Attributes on statements

Statements accept [outer attributes]. The attributes that have meaning on a statement are [`cfg`], and [the lint check attributes].

[block]: expressions/block-expr.md
[expression]: expressions.md
[function]: items/functions.md
[item]: items.md
[module]: items/modules.md
[never type]: types/never.md
[canonical path]: paths.md#canonical-paths
[implementations]: items/implementations.md
[variables]: variables.md
[outer attributes]: attributes.md
[`cfg`]: conditional-compilation.md
[the lint check attributes]: attributes/diagnostics.md#lint-check-attributes
[pattern]: patterns.md
[scope]: names/scopes.md


---

r[expr]
# Expressions

r[expr.syntax]
```grammar,expressions
Expression ->
      ExpressionWithoutBlock
    | ExpressionWithBlock

ExpressionWithoutBlock ->
    OuterAttribute* ExpressionWithoutBlockNoAttrs

ExpressionWithoutBlockNoAttrs ->
      LiteralExpression
    | PathExpression
    | OperatorExpression
    | GroupedExpression
    | ArrayExpression
    | AwaitExpression
    | IndexExpression
    | TupleExpression
    | TupleIndexingExpression
    | StructExpression
    | CallExpression
    | MethodCallExpression
    | FieldExpression
    | ClosureExpression
    | AsyncBlockExpression
    | ContinueExpression
    | BreakExpression
    | RangeExpression
    | ReturnExpression
    | UnderscoreExpression
    | MacroInvocation

ExpressionWithBlock ->
    OuterAttribute* ExpressionWithBlockNoAttrs

ExpressionWithBlockNoAttrs ->
      BlockExpression
    | ConstBlockExpression
    | UnsafeBlockExpression
    | LoopExpression
    | IfExpression
    | MatchExpression
```

r[expr.intro]
An expression may have two roles: it always produces a *value*, and it may have *effects* (otherwise known as "side effects").

r[expr.evaluation]
An expression *evaluates to* a value, and has effects during *evaluation*.

r[expr.operands]
Many expressions contain sub-expressions, called the *operands* of the expression.

r[expr.behavior]
The meaning of each kind of expression dictates several things:

* Whether or not to evaluate the operands when evaluating the expression
* The order in which to evaluate the operands
* How to combine the operands' values to obtain the value of the expression

r[expr.structure]
In this way, the structure of expressions dictates the structure of execution. Blocks are just another kind of expression, so blocks, statements, expressions, and blocks again can recursively nest inside each other to an arbitrary depth.

> [!NOTE]
> We give names to the operands of expressions so that we may discuss them, but these names are not stable and may be changed.

r[expr.precedence]
## Expression precedence

The precedence of Rust operators and expressions is ordered as follows, going from strong to weak. Binary Operators at the same precedence level are grouped in the order given by their associativity.

| Operator/Expression         | Associativity       |
|-----------------------------|---------------------|
| [Paths][expr.path]          |                     |
| [Method calls][expr.method] |                     |
| [Field expressions][expr.field] | left to right   |
| [Function calls][expr.call], [array indexing][expr.array.index] | |
| [`?`][expr.try]             |                     |
| Unary [`-`][expr.negate] [`!`][expr.negate] [`*`][expr.deref] [borrow][expr.operator.borrow] | |
| [`as`][expr.as]             | left to right       |
| [`*`][expr.arith-logic] [`/`][expr.arith-logic] [`%`][expr.arith-logic] | left to right       |
| [`+`][expr.arith-logic] [`-`][expr.arith-logic] | left to right       |
| [`<<`][expr.arith-logic] [`>>`][expr.arith-logic] | left to right     |
| [`&`][expr.arith-logic]     | left to right       |
| [`^`][expr.arith-logic]     | left to right       |
| [<code>&#124;</code>][expr.arith-logic] | left to right       |
| [`==`][expr.cmp] [`!=`][expr.cmp] [`<`][expr.cmp] [`>`][expr.cmp] [`<=`][expr.cmp] [`>=`][expr.cmp] | Require parentheses |
| [`&&`][expr.bool-logic]     | left to right       |
| [<code>&#124;&#124;</code>][expr.bool-logic] | left to right       |
| [`..`][expr.range] [`..=`][expr.range] | Require parentheses |
| [`=`][expr.assign] [`+=`][expr.compound-assign] [`-=`][expr.compound-assign] [`*=`][expr.compound-assign] [`/=`][expr.compound-assign] [`%=`][expr.compound-assign] <br> [`&=`][expr.compound-assign] [<code>&#124;=</code>][expr.compound-assign] [`^=`][expr.compound-assign] [`<<=`][expr.compound-assign] [`>>=`][expr.compound-assign] | right to left |
| [`return`][expr.return] [`break`][expr.loop.break] [closures][expr.closure]  | |

r[expr.operand-order]
## Evaluation order of operands

r[expr.operand-order.default]
The following list of expressions all evaluate their operands the same way, as described after the list. Other expressions either don't take operands or evaluate them conditionally as described on their respective pages.

* Dereference expression
* Error propagation expression
* Negation expression
* Arithmetic and logical binary operators
* Comparison operators
* Type cast expression
* Grouped expression
* Array expression
* Await expression
* Index expression
* Tuple expression
* Tuple index expression
* Struct expression
* Call expression
* Method call expression
* Field expression
* Break expression
* Range expression
* Return expression

r[expr.operand-order.operands-before-primary]
The operands of these expressions are evaluated prior to applying the effects of the expression. Expressions taking multiple operands are evaluated left to right as written in the source code.

> [!NOTE]
> Which subexpressions are the operands of an expression is determined by expression precedence as per the previous section.

For example, the two `next` method calls will always be called in the same order:

```rust
# // Using vec instead of array to avoid references
# // since there is no stable owned array iterator
# // at the time this example was written.
let mut one_two = vec![1, 2].into_iter();
assert_eq!(
    (1, 2),
    (one_two.next().unwrap(), one_two.next().unwrap())
);
```

> [!NOTE]
> Since this is applied recursively, these expressions are also evaluated from innermost to outermost, ignoring siblings until there are no inner subexpressions.

r[expr.place-value]
## Place expressions and value expressions

r[expr.place-value.intro]
Expressions are divided into two main categories: place expressions and value expressions; there is also a third, minor category of expressions called assignee expressions. Within each expression, operands may likewise occur in either place context or value context. The evaluation of an expression depends both on its own category and the context it occurs within.

r[expr.place-value.place-memory-location]
A *place expression* is an expression that represents a memory location.

r[expr.place-value.place-expr-kinds]
These expressions are [paths] which refer to local variables, [static variables], [dereferences][deref] (`*expr`), [array indexing] expressions (`expr[expr]`), [field] references (`expr.f`) and parenthesized place expressions.

r[expr.place-value.value-expr-kinds]
All other expressions are value expressions.

r[expr.place-value.value-result]
A *value expression* is an expression that represents an actual value.

r[expr.place-value.place-context]
The following contexts are *place expression* contexts:

* The left operand of a [compound assignment] expression.
* The operand of a unary [borrow], [raw borrow] or [dereference][deref] operator.
* The operand of a [field expression].
* The indexed operand of an [array indexing expression].
* The tuple operand of a [tuple indexing expression].
* The operand of any [implicit borrow].
* The initializer of a [let statement].
* The [scrutinee] of an [`if let`], [`match`][match], or [`while let`] expression.
* The base of a [functional update] struct expression.

> [!NOTE]
> Historically, place expressions were called *lvalues* and value expressions were called *rvalues*.

r[expr.place-value.assignee]
An *assignee expression* is an expression that appears in the left operand of an [assignment][assign] expression. Explicitly, the assignee expressions are:

- Place expressions.
- [Underscores].
- [Tuples] of assignee expressions.
- [Slices][expr.array.index] of assignee expressions.
- [Tuple structs] of assignee expressions.
- [Structs] of assignee expressions (with optionally named fields).
- [Unit structs]

r[expr.place-value.parenthesis]
Arbitrary parenthesisation is permitted inside assignee expressions.

r[expr.move]
### Moved and copied types

r[expr.move.intro]
When a place expression is evaluated in a value expression context, or is bound by value in a pattern, it denotes the value held _in_ that memory location.

r[expr.move.copy]
If the type of that value implements [`Copy`], then the value will be copied.

r[expr.move.requires-sized]
In the remaining situations, if that type is [`Sized`], then it may be possible to move the value.

r[expr.move.movable-place]
Only the following place expressions may be moved out of:

* [Variables] which are not currently borrowed.
* [Temporary values](#temporaries).
* [Fields][field] of a place expression which can be moved out of and don't implement [`Drop`].
* The result of [dereferencing][deref] an expression with type [`Box<T>`] and that can also be moved out of.

r[expr.move.deinitialization]
After moving out of a place expression that evaluates to a local variable, the location is deinitialized and cannot be read from again until it is reinitialized.

r[expr.move.place-invalid]
In all other cases, trying to use a place expression in a value expression context is an error.

r[expr.mut]
### Mutability

r[expr.mut.intro]
For a place expression to be [assigned][assign] to, mutably [borrowed][borrow], [implicitly mutably borrowed], or bound to a pattern containing `ref mut`, it must be _mutable_. We call these *mutable place expressions*. In contrast, other place expressions are called *immutable place expressions*.

r[expr.mut.valid-places]
The following expressions can be mutable place expression contexts:

* Mutable [variables] which are not currently borrowed.
* [Mutable `static` items].
* [Temporary values].
* [Fields][field]: this evaluates the subexpression in a mutable place expression context.
* [Dereferences][deref] of a `*mut T` pointer.
* Dereference of a variable, or field of a variable, with type `&mut T`. Note: This is an exception to the requirement of the next rule.
* Dereferences of a type that implements `DerefMut`: this then requires that the value being dereferenced is evaluated in a mutable place expression context.
* [Array indexing] of a type that implements `IndexMut`: this then evaluates the value being indexed, but not the index, in mutable place expression context.

r[expr.temporary]
### Temporaries

When using a value expression in most place expression contexts, a temporary unnamed memory location is created and initialized to that value. The expression evaluates to that location instead, except if [promoted] to a `static`. The [drop scope] of the temporary is usually the end of the enclosing statement.

r[expr.super-macros]
### Super macros

r[expr.super-macros.intro]
Certain built-in macros may create [temporaries] whose [scopes][temporary scopes] may be [extended]. These temporaries are *super temporaries* and these macros are *super macros*. [Invocations][macro invocations] of these macros are *super macro call expressions*. Arguments to these macros may be *super operands*.

> [!NOTE]
> When a super macro call expression is an [extending expression], its super operands are [extending expressions] and the [scopes][temporary scopes] of the super temporaries are [extended]. See [destructors.scope.lifetime-extension.exprs].

r[expr.super-macros.format_args]
#### `format_args!`

r[expr.super-macros.format_args.super-operands]
Except for the format string argument, all arguments passed to [`format_args!`] are *super operands*.

```rust,edition2024
# fn temp() -> String { String::from("") }
// Due to the call being an extending expression and the argument
// being a super operand, the inner block is an extending expression,
// so the scope of the temporary created in its trailing expression
// is extended.
let _ = format_args!("{}", { &temp() }); // OK
```

r[expr.super-macros.format_args.super-temporaries]
The super operands of [`format_args!`] are [implicitly borrowed] and are therefore [place expression contexts]. When a [value expression] is passed as an argument, it creates a *super temporary*.

```rust
# fn temp() -> String { String::from("") }
let x = format_args!("{}", temp());
x; // <-- The temporary is extended, allowing use here.
```

The expansion of a call to [`format_args!`] sometimes creates other internal *super temporaries*.

```rust,compile_fail,E0716
let x = {
    // This call creates an internal temporary.
    let x = format_args!("{:?}", 0);
    x // <-- The temporary is extended, allowing its use here.
}; // <-- The temporary is dropped here.
x; // ERROR
```

```rust
// This call doesn't create an internal temporary.
let x = { let x = format_args!("{}", 0); x };
x; // OK
```

> [!NOTE]
> The details of when [`format_args!`] does or does not create internal temporaries are currently unspecified.

r[expr.super-macros.pin]
#### `pin!`

r[expr.super-macros.pin.super-operands]
The argument to [`pin!`] is a *super operand*.

```rust,edition2024
# use core::pin::pin;
# fn temp() {}
// As above for `format_args!`.
let _ = pin!({ &temp() }); // OK
```

r[expr.super-macros.pin.super-temporaries]
The argument to [`pin!`] is a [value expression context] and creates a *super temporary*.

```rust
# use core::pin::pin;
# fn temp() {}
// The argument is evaluated into a super temporary.
let x = pin!(temp());
// The temporary is extended, allowing its use here.
x; // OK
```

r[expr.implicit-borrow]
### Implicit borrows

r[expr.implicit-borrow-intro]
Certain expressions will treat an expression as a place expression by implicitly borrowing it. For example, it is possible to compare two unsized [slices][slice] for equality directly, because the `==` operator implicitly borrows its operands:

```rust
# let c = [1, 2, 3];
# let d = vec![1, 2, 3];
let a: &[i32];
let b: &[i32];
# a = &c;
# b = &d;
// ...
*a == *b;
// Equivalent form:
::std::cmp::PartialEq::eq(&*a, &*b);
```

r[expr.implicit-borrow.application]
Implicit borrows may be taken in the following expressions:

* Left operand in [method-call] expressions.
* Left operand in [field] expressions.
* Left operand in [call expressions].
* Left operand in [array indexing] expressions.
* Operand of the [dereference operator][deref] (`*`).
* Operands of [comparison].
* Left operands of the [compound assignment].
* Arguments to [`format_args!`] except the format string.

r[expr.overload]
## Overloading traits

Many of the following operators and expressions can also be overloaded for other types using traits in `std::ops` or `std::cmp`. These traits also exist in `core::ops` and `core::cmp` with the same names.

r[expr.attr]
## Expression attributes

r[expr.attr.restriction]
[Outer attributes] before an expression are allowed only in a few specific cases:

* Before an expression used as a [statement].
* Elements of [array expressions], [tuple expressions], [call expressions], and tuple-style [struct] expressions.
* The tail expression of [block expressions].
<!-- Keep list in sync with block-expr.md -->

r[expr.attr.never-before]
They are never allowed before:
* [Range] expressions.
* Binary operator expressions ([ArithmeticOrLogicalExpression], [ComparisonExpression], [LazyBooleanExpression], [TypeCastExpression], [AssignmentExpression], [CompoundAssignmentExpression]).

[`Box<T>`]:             special-types-and-traits.md#boxt
[`Copy`]:               special-types-and-traits.md#copy
[`Drop`]:               special-types-and-traits.md#drop
[`if let`]:             expressions/if-expr.md#if-let-patterns
[`format_args!`]:       core::format_args
[`pin!`]:               core::pin::pin
[`Sized`]:              special-types-and-traits.md#sized
[`while let`]:          expressions/loop-expr.md#while-let-patterns
[array expressions]:    expressions/array-expr.md
[array indexing]:       expressions/array-expr.md#array-and-slice-indexing-expressions
[array indexing expression]: expr.array.index
[assign]:               expressions/operator-expr.md#assignment-expressions
[block expressions]:    expressions/block-expr.md
[borrow]:               expressions/operator-expr.md#borrow-operators
[call expressions]:     expressions/call-expr.md
[comparison]:           expressions/operator-expr.md#comparison-operators
[compound assignment]:  expressions/operator-expr.md#compound-assignment-expressions
[deref]:                expressions/operator-expr.md#the-dereference-operator
[destructors]:          destructors.md
[drop scope]:           destructors.md#drop-scopes
[extended]:             destructors.scope.lifetime-extension
[extending expression]: destructors.scope.lifetime-extension.exprs
[extending expressions]: destructors.scope.lifetime-extension.exprs
[field]:                expressions/field-expr.md
[field expression]:     expr.field
[functional update]:    expressions/struct-expr.md#functional-update-syntax
[implicit borrow]:      #implicit-borrows
[implicitly borrowed]:  expr.implicit-borrow
[implicitly mutably borrowed]: #implicit-borrows
[interior mutability]:  interior-mutability.md
[let statement]:        statements.md#let-statements
[macro invocations]:    macro.invocation
[match]:                expressions/match-expr.md
[method-call]:          expressions/method-call-expr.md
[Mutable `static` items]: items/static-items.md#mutable-statics
[Outer attributes]:     attributes.md
[paths]:                expressions/path-expr.md
[place expression contexts]: expr.place-value
[promoted]:             destructors.md#constant-promotion
[Range]:                expressions/range-expr.md
[raw borrow]:           expressions/operator-expr.md#raw-borrow-operators
[scrutinee]:            glossary.md#scrutinee
[slice]:                types/slice.md
[statement]:            statements.md
[static variables]:     items/static-items.md
[struct]:               expressions/struct-expr.md
[Structs]:              expr.struct
[temporaries]:          expr.temporary
[temporary scopes]:     destructors.scope.temporary
[Temporary values]:     #temporaries
[tuple expressions]:    expressions/tuple-expr.md
[tuple indexing expression]: expr.tuple-index
[Tuple structs]:        items.struct.tuple
[Tuples]:               expressions/tuple-expr.md
[Underscores]:          expressions/underscore-expr.md
[Unit structs]:         items.struct.unit
[value expression context]: expr.place-value
[value expression]:     expr.place-value
[Variables]:            variables.md


---

r[expr.literal]
# Literal expressions

r[expr.literal.syntax]
```grammar,expressions
LiteralExpression ->
      CHAR_LITERAL
    | STRING_LITERAL
    | RAW_STRING_LITERAL
    | BYTE_LITERAL
    | BYTE_STRING_LITERAL
    | RAW_BYTE_STRING_LITERAL
    | C_STRING_LITERAL
    | RAW_C_STRING_LITERAL
    | INTEGER_LITERAL
    | FLOAT_LITERAL
    | `true`
    | `false`
```

r[expr.literal.intro]
A _literal expression_ is an expression consisting of a single token, rather than a sequence of tokens, that immediately and directly denotes the value it evaluates to, rather than referring to it by name or some other evaluation rule.

r[expr.literal.const-expr]
A literal is a form of [constant expression], so is evaluated (primarily) at compile time.

r[expr.literal.literal-token]
Each of the lexical [literal][literal tokens] forms described earlier can make up a literal expression, as can the keywords `true` and `false`.

```rust
"hello";   // string type
'5';       // character type
5;         // integer type
```

r[expr.literal.string-representation]
In the descriptions below, the _string representation_ of a token is the sequence of characters from the input which matched the token's production in a *Lexer* grammar snippet.

> [!NOTE]
> This string representation never includes a character `U+000D` (CR) immediately followed by `U+000A` (LF): this pair would have been previously transformed into a single `U+000A` (LF).

r[expr.literal.escape]
## Escapes

r[expr.literal.escape.intro]
The descriptions of textual literal expressions below make use of several forms of _escape_.

r[expr.literal.escape.sequence]
Each form of escape is characterised by:
 * an _escape sequence_: a sequence of characters, which always begins with `U+005C` (`\`)
 * an _escaped value_: either a single character or an empty sequence of characters

In the definitions of escapes below:
 * An _octal digit_ is any of the characters in the range \[`0`-`7`].
 * A _hexadecimal digit_ is any of the characters in the ranges \[`0`-`9`], \[`a`-`f`], or \[`A`-`F`].

r[expr.literal.escape.simple]
### Simple escapes

Each sequence of characters occurring in the first column of the following table is an escape sequence.

In each case, the escaped value is the character given in the corresponding entry in the second column.

| Escape sequence | Escaped value            |
|-----------------|--------------------------|
| `\0`            | U+0000 (NUL)             |
| `\t`            | U+0009 (HT)              |
| `\n`            | U+000A (LF)              |
| `\r`            | U+000D (CR)              |
| `\"`            | U+0022 (QUOTATION MARK)  |
| `\'`            | U+0027 (APOSTROPHE)      |
| `\\`            | U+005C (REVERSE SOLIDUS) |

r[expr.literal.escape.hex-octet]
### 8-bit escapes

The escape sequence consists of `\x` followed by two hexadecimal digits.

The escaped value is the character whose [Unicode scalar value] is the result of interpreting the final two characters in the escape sequence as a hexadecimal integer, as if by [`u8::from_str_radix`] with radix 16.

> [!NOTE]
> The escaped value therefore has a [Unicode scalar value] in the range of [`u8`][numeric types].

r[expr.literal.escape.hex-ascii]
### 7-bit escapes

The escape sequence consists of `\x` followed by an octal digit then a hexadecimal digit.

The escaped value is the character whose [Unicode scalar value] is the result of interpreting the final two characters in the escape sequence as a hexadecimal integer, as if by [`u8::from_str_radix`] with radix 16.

r[expr.literal.escape.unicode]
### Unicode escapes

The escape sequence consists of `\u{`, followed by a sequence of characters each of which is a hexadecimal digit or `_`, followed by `}`.

The escaped value is the character whose [Unicode scalar value] is the result of interpreting the hexadecimal digits contained in the escape sequence as a hexadecimal integer, as if by [`u32::from_str_radix`] with radix 16.

> [!NOTE]
> The permitted forms of a [CHAR_LITERAL] or [STRING_LITERAL] token ensure that there is such a character.

r[expr.literal.continuation]
### String continuation escapes

The escape sequence consists of `\` followed immediately by `U+000A` (LF), and all following whitespace characters before the next non-whitespace character. For this purpose, the whitespace characters are `U+0009` (HT), `U+000A` (LF), `U+000D` (CR), and `U+0020` (SPACE).

The escaped value is an empty sequence of characters.

> [!NOTE]
> The effect of this form of escape is that a string continuation skips following whitespace, including additional newlines. Thus `a`, `b` and `c` are equal:
>
> ```rust
> let a = "foobar";
> let b = "foo\
>          bar";
> let c = "foo\
>
>      bar";
>
> assert_eq!(a, b);
> assert_eq!(b, c);
> ```
>
> Skipping additional newlines (as in example c) is potentially confusing and unexpected. This behavior may be adjusted in the future. Until a decision is made, it is recommended to avoid relying on skipping multiple newlines with line continuations. See [this issue](https://github.com/rust-lang/reference/pull/1042) for more information.

r[expr.literal.char]
## Character literal expressions

r[expr.literal.char.intro]
A character literal expression consists of a single [CHAR_LITERAL] token.

r[expr.literal.char.type]
The expression's type is the primitive [`char`] type.

r[expr.literal.char.no-suffix]
The token must not have a suffix.

r[expr.literal.char.literal-content]
The token's _literal content_ is the sequence of characters following the first `U+0027` (`'`) and preceding the last `U+0027` (`'`) in the string representation of the token.

r[expr.literal.char.represented]
The literal expression's _represented character_ is derived from the literal content as follows:

r[expr.literal.char.escape]
* If the literal content is one of the following forms of escape sequence, the represented character is the escape sequence's escaped value:
    * [Simple escapes]
    * [7-bit escapes]
    * [Unicode escapes]

r[expr.literal.char.single]
* Otherwise the represented character is the single character that makes up the literal content.

r[expr.literal.char.result]
The expression's value is the [`char`] corresponding to the represented character's [Unicode scalar value].

> [!NOTE]
> The permitted forms of a [CHAR_LITERAL] token ensure that these rules always produce a single character.

Examples of character literal expressions:

```rust
'R';                               // R
'\'';                              // '
'\x52';                            // R
'\u{00E6}';                        // LATIN SMALL LETTER AE (U+00E6)
```

r[expr.literal.string]
## String literal expressions

r[expr.literal.string.intro]
A string literal expression consists of a single [STRING_LITERAL] or [RAW_STRING_LITERAL] token.

r[expr.literal.string.type]
The expression's type is a shared reference (with `static` lifetime) to the primitive [`str`] type. That is, the type is `&'static str`.

r[expr.literal.string.no-suffix]
The token must not have a suffix.

r[expr.literal.string.literal-content]
The token's _literal content_ is the sequence of characters following the first `U+0022` (`"`) and preceding the last `U+0022` (`"`) in the string representation of the token.

r[expr.literal.string.represented]
The literal expression's _represented string_ is a sequence of characters derived from the literal content as follows:

r[expr.literal.string.escape]
* If the token is a [STRING_LITERAL], each escape sequence of any of the following forms occurring in the literal content is replaced by the escape sequence's escaped value.
    * [Simple escapes]
    * [7-bit escapes]
    * [Unicode escapes]
    * [String continuation escapes]

  These replacements take place in left-to-right order. For example, the token `"\\x41"` is converted to the characters `\` `x` `4` `1`.

r[expr.literal.string.raw]
* If the token is a [RAW_STRING_LITERAL], the represented string is identical to the literal content.

r[expr.literal.string.result]
The expression's value is a reference to a statically allocated [`str`] containing the UTF-8 encoding of the represented string.

Examples of string literal expressions:

```rust
"foo"; r"foo";                     // foo
"\"foo\""; r#""foo""#;             // "foo"

"foo #\"# bar";
r##"foo #"# bar"##;                // foo #"# bar

"\x52"; "R"; r"R";                 // R
"\\x52"; r"\x52";                  // \x52
```

r[expr.literal.byte-char]
## Byte literal expressions

r[expr.literal.byte-char.intro]
A byte literal expression consists of a single [BYTE_LITERAL] token.

r[expr.literal.byte-char.literal]
The expression's type is the primitive [`u8`][numeric types] type.

r[expr.literal.byte-char.no-suffix]
The token must not have a suffix.

r[expr.literal.byte-char.literal-content]
The token's _literal content_ is the sequence of characters following the first `U+0027` (`'`) and preceding the last `U+0027` (`'`) in the string representation of the token.

r[expr.literal.byte-char.represented]
The literal expression's _represented character_ is derived from the literal content as follows:

r[expr.literal.byte-char.escape]
* If the literal content is one of the following forms of escape sequence, the represented character is the escape sequence's escaped value:
    * [Simple escapes]
    * [8-bit escapes]

r[expr.literal.byte-char.single]
* Otherwise the represented character is the single character that makes up the literal content.

r[expr.literal.byte-char.result]
The expression's value is the represented character's [Unicode scalar value].

> [!NOTE]
> The permitted forms of a [BYTE_LITERAL] token ensure that these rules always produce a single character, whose Unicode scalar value is in the range of [`u8`][numeric types].

Examples of byte literal expressions:

```rust
b'R';                              // 82
b'\'';                             // 39
b'\x52';                           // 82
b'\xA0';                           // 160
```

r[expr.literal.byte-string]
## Byte string literal expressions

r[expr.literal.byte-string.intro]
A byte string literal expression consists of a single [BYTE_STRING_LITERAL] or [RAW_BYTE_STRING_LITERAL] token.

r[expr.literal.byte-string.type]
The expression's type is a shared reference (with `static` lifetime) to an array whose element type is [`u8`][numeric types]. That is, the type is `&'static [u8; N]`, where `N` is the number of bytes in the represented string described below.

r[expr.literal.byte-string.no-suffix]
The token must not have a suffix.

r[expr.literal.byte-string.literal-content]
The token's _literal content_ is the sequence of characters following the first `U+0022` (`"`) and preceding the last `U+0022` (`"`) in the string representation of the token.

r[expr.literal.byte-string.represented]
The literal expression's _represented string_ is a sequence of characters derived from the literal content as follows:

r[expr.literal.byte-string.escape]
* If the token is a [BYTE_STRING_LITERAL], each escape sequence of any of the following forms occurring in the literal content is replaced by the escape sequence's escaped value.
    * [Simple escapes]
    * [8-bit escapes]
    * [String continuation escapes]

  These replacements take place in left-to-right order. For example, the token `b"\\x41"` is converted to the characters `\` `x` `4` `1`.

r[expr.literal.byte-string.raw]
* If the token is a [RAW_BYTE_STRING_LITERAL], the represented string is identical to the literal content.

r[expr.literal.byte-string.result]
The expression's value is a reference to a statically allocated array containing the [Unicode scalar values] of the characters in the represented string, in the same order.

> [!NOTE]
> The permitted forms of [BYTE_STRING_LITERAL] and [RAW_BYTE_STRING_LITERAL] tokens ensure that these rules always produce array element values in the range of [`u8`][numeric types].

Examples of byte string literal expressions:

```rust
b"foo"; br"foo";                     // foo
b"\"foo\""; br#""foo""#;             // "foo"

b"foo #\"# bar";
br##"foo #"# bar"##;                 // foo #"# bar

b"\x52"; b"R"; br"R";                // R
b"\\x52"; br"\x52";                  // \x52
```

r[expr.literal.c-string]
## C string literal expressions

r[expr.literal.c-string.intro]
A C string literal expression consists of a single [C_STRING_LITERAL] or [RAW_C_STRING_LITERAL] token.

r[expr.literal.c-string.type]
The expression's type is a shared reference (with `static` lifetime) to the standard library [CStr] type. That is, the type is `&'static core::ffi::CStr`.

r[expr.literal.c-string.no-suffix]
The token must not have a suffix.

r[expr.literal.c-string.literal-content]
The token's _literal content_ is the sequence of characters following the first `"` and preceding the last `"` in the string representation of the token.

r[expr.literal.c-string.represented]
The literal expression's _represented bytes_ are a sequence of bytes derived from the literal content as follows:

r[expr.literal.c-string.escape]
* If the token is a [C_STRING_LITERAL], the literal content is treated as a sequence of items, each of which is either a single Unicode character other than `\` or an [escape]. The sequence of items is converted to a sequence of bytes as follows:
  * Each single Unicode character contributes its UTF-8 representation.
  * Each [simple escape] contributes the [Unicode scalar value] of its escaped value.
  * Each [8-bit escape] contributes a single byte containing the [Unicode scalar value] of its escaped value.
  * Each [unicode escape] contributes the UTF-8 representation of its escaped value.
  * Each [string continuation escape] contributes no bytes.

r[expr.literal.c-string.raw]
* If the token is a [RAW_C_STRING_LITERAL], the represented bytes are the UTF-8 encoding of the literal content.

> [!NOTE]
> The permitted forms of [C_STRING_LITERAL] and [RAW_C_STRING_LITERAL] tokens ensure that the represented bytes never include a null byte.

r[expr.literal.c-string.result]
The expression's value is a reference to a statically allocated [CStr] whose array of bytes contains the represented bytes followed by a null byte.

Examples of C string literal expressions:

```rust
c"foo"; cr"foo";                     // foo
c"\"foo\""; cr#""foo""#;             // "foo"

c"foo #\"# bar";
cr##"foo #"# bar"##;                 // foo #"# bar

c"\x52"; c"R"; cr"R";                // R
c"\\x52"; cr"\x52";                  // \x52

c"æ";                                // LATIN SMALL LETTER AE (U+00E6)
c"\u{00E6}";                         // LATIN SMALL LETTER AE (U+00E6)
c"\xC3\xA6";                         // LATIN SMALL LETTER AE (U+00E6)

c"\xE6".to_bytes();                  // [230]
c"\u{00E6}".to_bytes();              // [195, 166]
```

r[expr.literal.int]
## Integer literal expressions

r[expr.literal.int.intro]
An integer literal expression consists of a single [INTEGER_LITERAL] token.

r[expr.literal.int.suffix]
If the token has a [suffix], the suffix must be the name of one of the [primitive integer types][numeric types]: `u8`, `i8`, `u16`, `i16`, `u32`, `i32`, `u64`, `i64`, `u128`, `i128`, `usize`, or `isize`, and the expression has that type.

r[expr.literal.int.infer]
If the token has no suffix, the expression's type is determined by type inference:

r[expr.literal.int.inference-unique-type]
* If an integer type can be _uniquely_ determined from the surrounding program context, the expression has that type.

r[expr.literal.int.inference-default]
* If the program context under-constrains the type, it defaults to the signed 32-bit integer `i32`.

r[expr.literal.int.inference-error]
* If the program context over-constrains the type, it is considered a static type error.

Examples of integer literal expressions:

```rust
123;                               // type i32
123i32;                            // type i32
123u32;                            // type u32
123_u32;                           // type u32
let a: u64 = 123;                  // type u64

0xff;                              // type i32
0xff_u8;                           // type u8

0o70;                              // type i32
0o70_i16;                          // type i16

0b1111_1111_1001_0000;             // type i32
0b1111_1111_1001_0000i64;          // type i64

0usize;                            // type usize
```

r[expr.literal.int.representation]
The value of the expression is determined from the string representation of the token as follows:

r[expr.literal.int.radix]
* An integer radix is chosen by inspecting the first two characters of the string, as follows:

    * `0b` indicates radix 2
    * `0o` indicates radix 8
    * `0x` indicates radix 16
    * otherwise the radix is 10.

r[expr.literal.int.radix-prefix-stripped]
* If the radix is not 10, the first two characters are removed from the string.

r[expr.literal.int.type-suffix-stripped]
* Any suffix is removed from the string.

r[expr.literal.int.separators-stripped]
* Any underscores are removed from the string.

r[expr.literal.int.u128-value]
* The string is converted to a `u128` value as if by [`u128::from_str_radix`] with the chosen radix. If the value does not fit in `u128`, it is a compiler error.

r[expr.literal.int.cast]
* The `u128` value is converted to the expression's type via a [numeric cast].

> [!NOTE]
> The final cast will truncate the value of the literal if it does not fit in the expression's type. `rustc` includes a [lint check] named `overflowing_literals`, defaulting to `deny`, which rejects expressions where this occurs.

> [!NOTE]
> `-1i8`, for example, is an application of the [negation operator] to the literal expression `1i8`, not a single integer literal expression. See [Overflow] for notes on representing the most negative value for a signed type.

r[expr.literal.float]
## Floating-point literal expressions

r[expr.literal.float.intro]
A floating-point literal expression has one of two forms:
 * a single [FLOAT_LITERAL] token
 * a single [INTEGER_LITERAL] token which has a suffix and no radix indicator

r[expr.literal.float.suffix]
If the token has a [suffix], the suffix must be the name of one of the [primitive floating-point types][floating-point types]: `f32` or `f64`, and the expression has that type.

r[expr.literal.float.infer]
If the token has no suffix, the expression's type is determined by type inference:

r[expr.literal.float.inference-unique-type]
* If a floating-point type can be _uniquely_ determined from the surrounding program context, the expression has that type.

r[expr.literal.float.inference-default]
* If the program context under-constrains the type, it defaults to `f64`.

r[expr.literal.float.inference-error]
* If the program context over-constrains the type, it is considered a static type error.

Examples of floating-point literal expressions:

```rust
123.0f64;        // type f64
0.1f64;          // type f64
0.1f32;          // type f32
12E+99_f64;      // type f64
5f32;            // type f32
let x: f64 = 2.; // type f64
```

r[expr.literal.float.result]
The value of the expression is determined from the string representation of the token as follows:

r[expr.literal.float.type-suffix-stripped]
* Any suffix is removed from the string.

r[expr.literal.float.separators-stripped]
* Any underscores are removed from the string.

r[expr.literal.float.value]
* The string is converted to the expression's type as if by [`f32::from_str`] or [`f64::from_str`].

> [!NOTE]
> `-1.0`, for example, is an application of the [negation operator] to the literal expression `1.0`, not a single floating-point literal expression.

> [!NOTE]
> `inf` and `NaN` are not literal tokens. The [`f32::INFINITY`], [`f64::INFINITY`], [`f32::NAN`], and [`f64::NAN`] constants can be used instead of literal expressions. In `rustc`, a literal large enough to be evaluated as infinite will trigger the `overflowing_literals` lint check.

r[expr.literal.bool]
## Boolean literal expressions

r[expr.literal.bool.intro]
A boolean literal expression consists of one of the keywords `true` or `false`.

r[expr.literal.bool.result]
The expression's type is the primitive [boolean type], and its value is:
 * true if the keyword is `true`
 * false if the keyword is `false`

[Escape]: #escapes
[Simple escape]: #simple-escapes
[Simple escapes]: #simple-escapes
[8-bit escape]: #8-bit-escapes
[8-bit escapes]: #8-bit-escapes
[7-bit escape]: #7-bit-escapes
[7-bit escapes]: #7-bit-escapes
[Unicode escape]: #unicode-escapes
[Unicode escapes]: #unicode-escapes
[String continuation escape]: #string-continuation-escapes
[String continuation escapes]: #string-continuation-escapes
[boolean type]: ../types/boolean.md
[constant expression]: ../const_eval.md#constant-expressions
[CStr]: core::ffi::CStr
[floating-point types]: ../types/numeric.md#floating-point-types
[lint check]: ../attributes/diagnostics.md#lint-check-attributes
[literal tokens]: ../tokens.md#literals
[numeric cast]: operator-expr.md#numeric-cast
[numeric types]: ../types/numeric.md
[suffix]: ../tokens.md#suffixes
[negation operator]: operator-expr.md#negation-operators
[overflow]: operator-expr.md#overflow
[Unicode scalar value]: http://www.unicode.org/glossary/#unicode_scalar_value
[Unicode scalar values]: http://www.unicode.org/glossary/#unicode_scalar_value
[`char`]: ../types/char.md
[`f32::from_str`]: ../../core/primitive.f32.md#method.from_str
[`f64::from_str`]: ../../core/primitive.f64.md#method.from_str
[`str`]: ../types/str.md


---

r[expr.path]
# Path expressions

r[expr.path.syntax]
```grammar,expressions
PathExpression ->
      PathInExpression
    | QualifiedPathInExpression
```

r[expr.path.intro]
A [path] used as an expression context denotes either a local variable or an item.

r[expr.path.place]
Path expressions that resolve to local or static variables are [place expressions]; other paths are [value expressions].

r[expr.path.safety]
Using a [`static mut`] variable requires an [`unsafe` block].

```rust
# mod globals {
#     pub static STATIC_VAR: i32 = 5;
#     pub static mut STATIC_MUT_VAR: i32 = 7;
# }
# let local_var = 3;
local_var;
globals::STATIC_VAR;
unsafe { globals::STATIC_MUT_VAR };
let some_constructor = Some::<i32>;
let push_integer = Vec::<i32>::push;
let slice_reverse = <[i32]>::reverse;
```

r[expr.path.const]
Evaluation of associated constants is handled the same way as [`const` blocks].

[place expressions]: ../expressions.md#place-expressions-and-value-expressions
[value expressions]: ../expressions.md#place-expressions-and-value-expressions
[path]: ../paths.md
[`static mut`]: ../items/static-items.md#mutable-statics
[`unsafe` block]: block-expr.md#unsafe-blocks
[`const` blocks]: block-expr.md#const-blocks


---

r[expr.block]
# Block expressions

r[expr.block.syntax]
```grammar,expressions
BlockExpression ->
    `{`
        InnerAttribute*
        Statements?
    `}`

Statements ->
      Statement+
    | Statement+ ExpressionWithoutBlock
    | ExpressionWithoutBlock
```

r[expr.block.intro]
A *block expression*, or *block*, is a control flow expression and anonymous namespace scope for items and variable declarations.

r[expr.block.sequential-evaluation]
As a control flow expression, a block sequentially executes its component non-item declaration statements and then its final optional expression.

r[expr.block.namespace]
As an anonymous namespace scope, item declarations are only in scope inside the block itself and variables declared by `let` statements are in scope from the next statement until the end of the block. See the [scopes] chapter for more details.

r[expr.block.inner-attributes]
The syntax for a block is `{`, then any [inner attributes], then any number of [statements], then an optional expression, called the final operand, and finally a `}`.

r[expr.block.statements]
Statements are usually required to be followed by a semicolon, with two exceptions:

1. Item declaration statements do not need to be followed by a semicolon.
2. Expression statements usually require a following semicolon except if its outer expression is a flow control expression.

r[expr.block.null-statement]
Furthermore, extra semicolons between statements are allowed, but these semicolons do not affect semantics.

r[expr.block.evaluation]
When evaluating a block expression, each statement, except for item declaration statements, is executed sequentially.

r[expr.block.result]
Then the final operand is executed, if given.

r[expr.block.value-trailing-expr]
When a block contains a [final operand], the block has the type and value of that final operand.

```rust
let x: u8 = { 0u8 }; // `0u8` is the final operand.
assert_eq!(x, 0);
let x: u8 = { (); 0u8 }; // As above.
assert_eq!(x, 0);
```

r[expr.block.value-no-trailing-expr]
When a block does not contain a [final operand] and the block does not diverge, the block has [unit type] and [unit value].

```rust
let x: () = {}; // Has no final operand.
assert_eq!(x, ());
let x: () = { 0u8; }; // As above.
assert_eq!(x, ());
```

r[expr.block.value-diverges-no-trailing-expr]
When a block does not contain a [final operand] and the block [diverges], the block has the [never type] and has no final value (because its type is [uninhabited]).

```rust,no_run
fn f() -> ! { loop {}; } // Diverges and has no final operand.
//          ^^^^^^^^^^^^
// The body of a function is a block expression.
```

> [!NOTE]
> Observe that a block having no final operand is distinct from having an explicit final operand with unit type.  E.g., even though this block diverges, the type of the block is [unit] rather than [never].
>
> ```rust,compile_fail,E0308
> fn f() -> ! { loop {}; () } // ERROR: Mismatched types.
> //          ^^^^^^^^^^^^^^^ This block has unit type.
> ```

> [!NOTE]
> As a control flow expression, if a block expression is the outer expression of an expression statement, the expected type is `()` unless it is followed immediately by a semicolon.

r[expr.block.diverging]
A block is considered to be [diverging][divergence] if all reachable control flow paths contain a diverging expression, unless that expression is a [place expression] that is not read from.

```rust,no_run
# #![ feature(never_type) ]
fn no_control_flow() -> ! {
    // There are no conditional statements, so this entire function body is diverging.
    loop {}
}

fn control_flow_diverging() -> ! {
    // All paths are diverging, so this entire function body is diverging.
    if true {
        loop {}
    } else {
        loop {}
    }
}

fn control_flow_not_diverging() -> () {
    // Some paths are not diverging, so this entire block is not diverging.
    if true {
        ()
    } else {
        loop {}
    }
}

// Note: This makes use of the unstable never type which is only available on
// Rust's nightly channel. This is done for illustration purposes. It is
// possible to encounter this scenario in stable Rust, but requires a more
// convoluted example.
struct Foo {
    x: !,
}

fn make<T>() -> T { loop {} }

fn diverging_place_read() -> ! {
    let foo = Foo { x: make() };
    // A read of a place expression produces a diverging block.
    let _x = foo.x;
}
```

```rust,compile_fail,E0308
# #![ feature(never_type) ]
# fn make<T>() -> T { loop {} }
# struct Foo {
#     x: !,
# }
fn diverging_place_not_read() -> ! {
    let foo = Foo { x: make() };
    // Assignment to `_` means the place is not read.
    let _ = foo.x;
} // ERROR: Mismatched types.
```

r[expr.block.value]
Blocks are always [value expressions] and evaluate the last operand in value expression context.

> [!NOTE]
> This can be used to force moving a value if really needed. For example, the following example fails on the call to `consume_self` because the struct was moved out of `s` in the block expression.
>
> ```rust,compile_fail
> struct Struct;
>
> impl Struct {
>     fn consume_self(self) {}
>     fn borrow_self(&self) {}
> }
>
> fn move_by_block_expression() {
>     let s = Struct;
>
>     // Move the value out of `s` in the block expression.
>     (&{ s }).borrow_self();
>
>     // Fails to execute because `s` is moved out of.
>     s.consume_self();
> }
> ```

r[expr.block.async]
## `async` blocks

r[expr.block.async.syntax]
```grammar,expressions
AsyncBlockExpression -> `async` `move`? BlockExpression
```

r[expr.block.async.intro]
An *async block* is a variant of a block expression which evaluates to a future.

r[expr.block.async.future-result]
The final expression of the block, if present, determines the result value of the future.

r[expr.block.async.anonymous-type]
Executing an async block is similar to executing a closure expression: its immediate effect is to produce and return an anonymous type.

r[expr.block.async.future]
Whereas closures return a type that implements one or more of the [`std::ops::Fn`] traits, however, the type returned for an async block implements the [`std::future::Future`] trait.

r[expr.block.async.layout-unspecified]
The actual data format for this type is unspecified.

> [!NOTE]
> The future type that rustc generates is roughly equivalent to an enum with one variant per `await` point, where each variant stores the data needed to resume from its corresponding point.

r[expr.block.async.edition2018]
> [!EDITION-2018]
> Async blocks are only available beginning with Rust 2018.

r[expr.block.async.capture]
### Capture modes

Async blocks capture variables from their environment using the same [capture modes] as closures. Like closures, when written `async { .. }` the capture mode for each variable will be inferred from the content of the block. `async move { .. }` blocks however will move all referenced variables into the resulting future.

r[expr.block.async.context]
### Async context

Because async blocks construct a future, they define an **async context** which can in turn contain [`await` expressions]. Async contexts are established by async blocks as well as the bodies of async functions, whose semantics are defined in terms of async blocks.

r[expr.block.async.function]
### Control-flow operators

r[expr.block.async.function.intro]
Async blocks act like a function boundary, much like closures.

r[expr.block.async.function.return-try]
Therefore, the `?` operator and `return` expressions both affect the output of the future, not the enclosing function or other context. That is, `return <expr>` from within an async block will return the result of `<expr>` as the output of the future. Similarly, if `<expr>?` propagates an error, that error is propagated as the result of the future.

r[expr.block.async.function.control-flow]
Finally, the `break` and `continue` keywords cannot be used to branch out from an async block. Therefore the following is illegal:

```rust,compile_fail
loop {
    async move {
        break; // error[E0267]: `break` inside of an `async` block
    }
}
```

r[expr.block.const]
## `const` blocks

r[expr.block.const.syntax]
```grammar,expressions
ConstBlockExpression -> `const` BlockExpression
```

r[expr.block.const.intro]
A *const block* is a variant of a block expression whose body evaluates at compile-time instead of at runtime.

r[expr.block.const.context]
Const blocks allows you to define a constant value without having to define new [constant items], and thus they are also sometimes referred as *inline consts*. It also supports type inference so there is no need to specify the type, unlike [constant items].

r[expr.block.const.generic-params]
Const blocks have the ability to reference generic parameters in scope, unlike [free][free item] constant items. They are desugared to constant items with generic parameters in scope (similar to associated constants, but without a trait or type they are associated with). For example, this code:

```rust
fn foo<T>() -> usize {
    const { std::mem::size_of::<T>() + 1 }
}
```

is equivalent to:

```rust
fn foo<T>() -> usize {
    {
        struct Const<T>(T);
        impl<T> Const<T> {
            const CONST: usize = std::mem::size_of::<T>() + 1;
        }
        Const::<T>::CONST
    }
}
```

r[expr.block.const.evaluation]

If the const block expression is executed at runtime, then the constant is guaranteed to be evaluated, even if its return value is ignored:

```rust
fn foo<T>() -> usize {
    // If this code ever gets executed, then the assertion has definitely
    // been evaluated at compile-time.
    const { assert!(std::mem::size_of::<T>() > 0); }
    // Here we can have unsafe code relying on the type being non-zero-sized.
    /* ... */
    42
}
```

r[expr.block.const.not-executed]

If the const block expression is not executed at runtime, it may or may not be evaluated:
```rust,compile_fail
if false {
    // The panic may or may not occur when the program is built.
    const { panic!(); }
}
```

r[expr.block.unsafe]
## `unsafe` blocks

r[expr.block.unsafe.syntax]
```grammar,expressions
UnsafeBlockExpression -> `unsafe` BlockExpression
```

r[expr.block.unsafe.intro]
_See [`unsafe` blocks] for more information on when to use `unsafe`_.

A block of code can be prefixed with the `unsafe` keyword to permit [unsafe operations]. Examples:

```rust
unsafe {
    let b = [13u8, 17u8];
    let a = &b[0] as *const u8;
    assert_eq!(*a, 13);
    assert_eq!(*a.offset(1), 17);
}

# unsafe fn an_unsafe_fn() -> i32 { 10 }
let a = unsafe { an_unsafe_fn() };
```

r[expr.block.label]
## Labeled block expressions

Labeled block expressions are documented in the [Loops and other breakable expressions] section.

r[expr.block.attributes]
## Attributes on block expressions

r[expr.block.attributes.inner-attributes]
[Inner attributes] are allowed directly after the opening brace of a block expression in the following situations:

* [Function] and [method] bodies.
* Loop bodies ([`loop`], [`while`], and [`for`]).
* Block expressions used as a [statement].
* Block expressions as elements of [array expressions], [tuple expressions], [call expressions], and tuple-style [struct] expressions.
* A block expression as the tail expression of another block expression.
<!-- Keep list in sync with expressions.md -->

r[expr.block.attributes.valid]
The attributes that have meaning on a block expression are [`cfg`] and [the lint check attributes].

For example, this function returns `true` on unix platforms and `false` on other platforms.

```rust
fn is_unix_platform() -> bool {
    #[cfg(unix)] { true }
    #[cfg(not(unix))] { false }
}
```

[`await` expressions]: await-expr.md
[`cfg`]: ../conditional-compilation.md
[`for`]: loop-expr.md#iterator-loops
[`loop`]: loop-expr.md#infinite-loops
[`unsafe` blocks]: ../unsafe-keyword.md#unsafe-blocks-unsafe-
[`while`]: loop-expr.md#predicate-loops
[array expressions]: array-expr.md
[call expressions]: call-expr.md
[capture modes]: ../types/closure.md#capture-modes
[constant items]: ../items/constant-items.md
[diverges]: expr.block.diverging
[final operand]: expr.block.inner-attributes
[free item]: ../glossary.md#free-item
[function]: ../items/functions.md
[inner attributes]: ../attributes.md
[method]: ../items/associated-items.md#methods
[mutable reference]: ../types/pointer.md#mutables-references-
[never type]: type.never
[never]: type.never
[place expression]: expr.place-value.place-memory-location
[scopes]: ../names/scopes.md
[shared references]: ../types/pointer.md#shared-references-
[statement]: ../statements.md
[statements]: ../statements.md
[struct]: struct-expr.md
[the lint check attributes]: ../attributes/diagnostics.md#lint-check-attributes
[tuple expressions]: tuple-expr.md
[uninhabited]: glossary.uninhabited
[unit type]: type.tuple.unit
[unit value]: type.tuple.unit
[unit]: type.tuple.unit
[unsafe operations]: ../unsafety.md
[value expressions]: ../expressions.md#place-expressions-and-value-expressions
[Loops and other breakable expressions]: expr.loop.block-labels


---

r[expr.operator]
# Operator expressions

r[expr.operator.syntax]
```grammar,expressions
OperatorExpression ->
      BorrowExpression
    | DereferenceExpression
    | TryPropagationExpression
    | NegationExpression
    | ArithmeticOrLogicalExpression
    | ComparisonExpression
    | LazyBooleanExpression
    | TypeCastExpression
    | AssignmentExpression
    | CompoundAssignmentExpression
```

r[expr.operator.intro]
Operators are defined for built in types by the Rust language.

r[expr.operator.trait]
Many of the following operators can also be overloaded using traits in `std::ops` or `std::cmp`.

r[expr.operator.int-overflow]
## Overflow

r[expr.operator.int-overflow.intro]
Integer operators will panic when they overflow when compiled in debug mode. The `-C debug-assertions` and `-C overflow-checks` compiler flags can be used to control this more directly. The following things are considered to be overflow:

r[expr.operator.int-overflow.binary-arith]
* When `+`, `*` or binary `-` create a value greater than the maximum value, or less than the minimum value that can be stored.

r[expr.operator.int-overflow.unary-neg]
* Applying unary `-` to the most negative value of any signed integer type, unless the operand is a [literal expression] (or a literal expression standing alone inside one or more [grouped expressions][grouped expression]).

r[expr.operator.int-overflow.div]
* Using `/` or `%`, where the left-hand argument is the smallest integer of a signed integer type and the right-hand argument is `-1`. These checks occur even when `-C overflow-checks` is disabled, for legacy reasons.

r[expr.operator.int-overflow.shift]
* Using `<<` or `>>` where the right-hand argument is greater than or equal to the number of bits in the type of the left-hand argument, or is negative.

> [!NOTE]
> The exception for literal expressions behind unary `-` means that forms such as `-128_i8` or `let j: i8 = -(128)` never cause a panic and have the expected value of -128.
>
> In these cases, the literal expression already has the most negative value for its type (for example, `128_i8` has the value -128) because integer literals are truncated to their type per the description in [Integer literal expressions][literal expression].
>
> Negation of these most negative values leaves the value unchanged due to two's complement overflow conventions.
>
> In `rustc`, these most negative expressions are also ignored by the `overflowing_literals` lint check.

r[expr.operator.borrow]
## Borrow operators

r[expr.operator.borrow.syntax]
```grammar,expressions
BorrowExpression ->
      (`&`|`&&`) Expression
    | (`&`|`&&`) `mut` Expression
    | (`&`|`&&`) `raw` `const` Expression
    | (`&`|`&&`) `raw` `mut` Expression
```

r[expr.operator.borrow.intro]
The `&` (shared borrow) and `&mut` (mutable borrow) operators are unary prefix operators.

r[expr.operator.borrow.result]
When applied to a [place expression], this expressions produces a reference (pointer) to the location that the value refers to.

r[expr.operator.borrow.lifetime]
The memory location is also placed into a borrowed state for the duration of the reference. For a shared borrow (`&`), this implies that the place may not be mutated, but it may be read or shared again. For a mutable borrow (`&mut`), the place may not be accessed in any way until the borrow expires.

r[expr.operator.borrow.mut]
`&mut` evaluates its operand in a mutable place expression context.

r[expr.operator.borrow.temporary]
If the `&` or `&mut` operators are applied to a [value expression], then a [temporary value] is created.

These operators cannot be overloaded.

```rust
{
    // a temporary with value 7 is created that lasts for this scope.
    let shared_reference = &7;
}
let mut array = [-2, 3, 9];
{
    // Mutably borrows `array` for this scope.
    // `array` may only be used through `mutable_reference`.
    let mutable_reference = &mut array;
}
```

r[expr.borrow.and-and-syntax]
Even though `&&` is a single token ([the lazy 'and' operator](#lazy-boolean-operators)), when used in the context of borrow expressions it works as two borrows:

```rust
// same meanings:
let a = &&  10;
let a = & & 10;

// same meanings:
let a = &&&&  mut 10;
let a = && && mut 10;
let a = & & & & mut 10;
```

r[expr.borrow.raw]
### Raw borrow operators

r[expr.borrow.raw.intro]
`&raw const` and `&raw mut` are the *raw borrow operators*.

r[expr.borrow.raw.place]
The operand expression of these operators is evaluated in place expression context.

r[expr.borrow.raw.result]
`&raw const expr` then creates a const raw pointer of type `*const T` to the given place, and `&raw mut expr` creates a mutable raw pointer of type `*mut T`.

r[expr.borrow.raw.invalid-ref]
The raw borrow operators must be used instead of a borrow operator whenever the place expression could evaluate to a place that is not properly aligned or does not store a valid value as determined by its type, or whenever creating a reference would introduce incorrect aliasing assumptions. In those situations, using a borrow operator would cause [undefined behavior] by creating an invalid reference, but a raw pointer may still be constructed.

The following is an example of creating a raw pointer to an unaligned place through a `packed` struct:

```rust
#[repr(packed)]
struct Packed {
    f1: u8,
    f2: u16,
}

let packed = Packed { f1: 1, f2: 2 };
// `&packed.f2` would create an unaligned reference, and thus be undefined behavior!
let raw_f2 = &raw const packed.f2;
assert_eq!(unsafe { raw_f2.read_unaligned() }, 2);
```

The following is an example of creating a raw pointer to a place that does not contain a valid value:

```rust
use std::mem::MaybeUninit;

struct Demo {
    field: bool,
}

let mut uninit = MaybeUninit::<Demo>::uninit();
// `&uninit.as_mut().field` would create a reference to an uninitialized `bool`,
// and thus be undefined behavior!
let f1_ptr = unsafe { &raw mut (*uninit.as_mut_ptr()).field };
unsafe { f1_ptr.write(true); }
let init = unsafe { uninit.assume_init() };
```

r[expr.deref]
## The dereference operator

r[expr.deref.syntax]
```grammar,expressions
DereferenceExpression -> `*` Expression
```

r[expr.deref.intro]
The `*` (dereference) operator is also a unary prefix operator.

r[expr.deref.result]
When applied to a [pointer](../types/pointer.md) or [`Box`], it denotes the pointed-to location.

r[expr.deref.mut]
If the expression is of type `&mut T`, `*mut T`, or `Box<T>`, and is either a local variable, a (nested) field of a local variable or is a mutable [place expression], then the resulting memory location can be assigned to.

r[expr.deref.box]
When applied to a [`Box`], the resultant place may be [moved from].

r[expr.deref.safety]
Dereferencing a raw pointer requires `unsafe`.

r[expr.deref.traits]
On non-pointer types `*x` is equivalent to `*std::ops::Deref::deref(&x)` in an [immutable place expression context](../expressions.md#mutability) and `*std::ops::DerefMut::deref_mut(&mut x)` in a mutable place expression context, except that when `*x` undergoes [temporary lifetime extension], the dereferenced expression `x` also has its [temporary scope] extended.

```rust
# struct NoCopy;
let a = &7;
assert_eq!(*a, 7);
let b = &mut 9;
*b = 11;
assert_eq!(*b, 11);
let c = Box::new(NoCopy);
let d: NoCopy = *c;
```

```rust
// The temporary holding the result of `String::new()` is extended
// to live to the end of the block, so `x` may be used in subsequent
// statements.
let x = &*String::new();
# x;
```

```rust,compile_fail,E0716
// The temporary holding the result of `String::new()` is dropped at
// the end of the statement, so it's an error to use `y` after.
let y = &*std::ops::Deref::deref(&String::new()); // ERROR
# y;
```

r[expr.try]
## The try propagation expression

r[expr.try.syntax]
```grammar,expressions
TryPropagationExpression -> Expression `?`
```

r[expr.try.intro]
The try propagation expression uses the value of the inner expression and the [`Try`] trait to decide whether to produce a value, and if so, what value to produce, or whether to return a value to the caller, and if so, what value to return.

> [!EXAMPLE]
> ```rust
> # use std::num::ParseIntError;
> fn try_to_parse() -> Result<i32, ParseIntError> {
>     let x: i32 = "123".parse()?; // `x` is `123`.
>     let y: i32 = "24a".parse()?; // Returns an `Err()` immediately.
>     Ok(x + y)                    // Doesn't run.
> }
>
> let res = try_to_parse();
> println!("{res:?}");
> # assert!(res.is_err())
> ```
>
> ```rust
> fn try_option_some() -> Option<u8> {
>     let val = Some(1)?;
>     Some(val)
> }
> assert_eq!(try_option_some(), Some(1));
>
> fn try_option_none() -> Option<u8> {
>     let val = None?;
>     Some(val)
> }
> assert_eq!(try_option_none(), None);
> ```
>
> ```rust
> use std::ops::ControlFlow;
>
> pub struct TreeNode<T> {
>     value: T,
>     left: Option<Box<TreeNode<T>>>,
>     right: Option<Box<TreeNode<T>>>,
> }
>
> impl<T> TreeNode<T> {
>     pub fn traverse_inorder<B>(&self, f: &mut impl FnMut(&T) -> ControlFlow<B>) -> ControlFlow<B> {
>         if let Some(left) = &self.left {
>             left.traverse_inorder(f)?;
>         }
>         f(&self.value)?;
>         if let Some(right) = &self.right {
>             right.traverse_inorder(f)?;
>         }
>         ControlFlow::Continue(())
>     }
> }
> #
> # fn main() {
> #     let n = TreeNode {
> #         value: 1,
> #         left: Some(Box::new(TreeNode{value: 2, left: None, right: None})),
> #         right: None,
> #     };
> #     let v = n.traverse_inorder(&mut |t| {
> #         if *t == 2 {
> #             ControlFlow::Break("found")
> #         } else {
> #             ControlFlow::Continue(())
> #         }
> #     });
> #     assert_eq!(v, ControlFlow::Break("found"));
> # }
> ```

> [!NOTE]
> The [`Try`] trait is currently unstable, and thus cannot be implemented for user types.
>
> The try propagation expression is currently roughly equivalent to:
>
> ```rust
> # #![ feature(try_trait_v2) ]
> # fn example() -> Result<(), ()> {
> # let expr = Ok(());
> match core::ops::Try::branch(expr) {
>     core::ops::ControlFlow::Continue(val) => val,
>     core::ops::ControlFlow::Break(residual) =>
>         return core::ops::FromResidual::from_residual(residual),
> }
> # Ok(())
> # }
> ```

> [!NOTE]
> The try propagation operator is sometimes called *the question mark operator*, *the `?` operator*, or *the try operator*.

r[expr.try.restricted-types]
The try propagation operator can be applied to expressions with the type of:

- [`Result<T, E>`]
    - `Result::Ok(val)` evaluates to `val`.
    - `Result::Err(e)` returns `Result::Err(From::from(e))`.
- [`Option<T>`]
    - `Option::Some(val)` evaluates to `val`.
    - `Option::None` returns `Option::None`.
- [`ControlFlow<B, C>`][core::ops::ControlFlow]
    - `ControlFlow::Continue(c)` evaluates to `c`.
    - `ControlFlow::Break(b)` returns `ControlFlow::Break(b)`.
- [`Poll<Result<T, E>>`][core::task::Poll]
    - `Poll::Ready(Ok(val))` evaluates to `Poll::Ready(val)`.
    - `Poll::Ready(Err(e))` returns `Poll::Ready(Err(From::from(e)))`.
    - `Poll::Pending` evaluates to `Poll::Pending`.
- [`Poll<Option<Result<T, E>>>`][`core::task::Poll`]
    - `Poll::Ready(Some(Ok(val)))` evaluates to `Poll::Ready(Some(val))`.
    - `Poll::Ready(Some(Err(e)))` returns `Poll::Ready(Some(Err(From::from(e))))`.
    - `Poll::Ready(None)` evaluates to `Poll::Ready(None)`.
    - `Poll::Pending` evaluates to `Poll::Pending`.

r[expr.negate]
## Negation operators

r[expr.negate.syntax]
```grammar,expressions
NegationExpression ->
      `-` Expression
    | `!` Expression
```

r[expr.negate.intro]
These are the last two unary operators.

r[expr.negate.results]
This table summarizes the behavior of them on primitive types and which traits are used to overload these operators for other types. Remember that signed integers are always represented using two's complement. The operands of all of these operators are evaluated in [value expression context][value expression] so are moved or copied.

| Symbol | Integer     | `bool`        | Floating Point | Overloading Trait  |
|--------|-------------|-------------- |----------------|--------------------|
| `-`    | Negation*   |               | Negation       | `std::ops::Neg`    |
| `!`    | Bitwise NOT | [Logical NOT] |                | `std::ops::Not`    |

\* Only for signed integer types.

Here are some example of these operators

```rust
let x = 6;
assert_eq!(-x, -6);
assert_eq!(!x, -7);
assert_eq!(true, !false);
```

r[expr.arith-logic]
## Arithmetic and logical binary operators

r[expr.arith-logic.syntax]
```grammar,expressions
ArithmeticOrLogicalExpression ->
      Expression `+` Expression
    | Expression `-` Expression
    | Expression `*` Expression
    | Expression `/` Expression
    | Expression `%` Expression
    | Expression `&` Expression
    | Expression `|` Expression
    | Expression `^` Expression
    | Expression `<<` Expression
    | Expression `>>` Expression
```

r[expr.arith-logic.intro]
Binary operators expressions are all written with infix notation.

r[expr.arith-logic.behavior]
This table summarizes the behavior of arithmetic and logical binary operators on primitive types and which traits are used to overload these operators for other types. Remember that signed integers are always represented using two's complement. The operands of all of these operators are evaluated in [value expression context][value expression] so are moved or copied.

| Symbol | Integer                 | `bool`        | Floating Point | Overloading Trait  | Overloading Compound Assignment Trait |
|--------|-------------------------|---------------|----------------|--------------------| ------------------------------------- |
| `+`    | Addition                |               | Addition       | `std::ops::Add`    | `std::ops::AddAssign`                 |
| `-`    | Subtraction             |               | Subtraction    | `std::ops::Sub`    | `std::ops::SubAssign`                 |
| `*`    | Multiplication          |               | Multiplication | `std::ops::Mul`    | `std::ops::MulAssign`                 |
| `/`    | Division*†              |               | Division       | `std::ops::Div`    | `std::ops::DivAssign`                 |
| `%`    | Remainder**†            |               | Remainder      | `std::ops::Rem`    | `std::ops::RemAssign`                 |
| `&`    | Bitwise AND             | [Logical AND] |                | `std::ops::BitAnd` | `std::ops::BitAndAssign`              |
| `\|` | Bitwise OR | [Logical OR]  |                | `std::ops::BitOr`  | `std::ops::BitOrAssign`               |
| `^`    | Bitwise XOR             | [Logical XOR] |                | `std::ops::BitXor` | `std::ops::BitXorAssign`              |
| `<<`   | Left Shift              |               |                | `std::ops::Shl`    | `std::ops::ShlAssign`                 |
| `>>`   | Right Shift***          |               |                | `std::ops::Shr`    |  `std::ops::ShrAssign`                |

\* Integer division rounds towards zero.

\*\* Rust uses a remainder defined with [truncating division](https://en.wikipedia.org/wiki/Modulo_operation#Variants_of_the_definition). Given `remainder = dividend % divisor`, the remainder will have the same sign as the dividend.

\*\*\* Arithmetic right shift on signed integer types, logical right shift on unsigned integer types.

† For integer types, division by zero panics.

Here are examples of these operators being used.

```rust
assert_eq!(3 + 6, 9);
assert_eq!(5.5 - 1.25, 4.25);
assert_eq!(-5 * 14, -70);
assert_eq!(14 / 3, 4);
assert_eq!(100 % 7, 2);
assert_eq!(0b1010 & 0b1100, 0b1000);
assert_eq!(0b1010 | 0b1100, 0b1110);
assert_eq!(0b1010 ^ 0b1100, 0b110);
assert_eq!(13 << 3, 104);
assert_eq!(-10 >> 2, -3);
```

r[expr.cmp]
## Comparison operators

r[expr.cmp.syntax]
```grammar,expressions
ComparisonExpression ->
      Expression `==` Expression
    | Expression `!=` Expression
    | Expression `>` Expression
    | Expression `<` Expression
    | Expression `>=` Expression
    | Expression `<=` Expression
```

r[expr.cmp.intro]
Comparison operators are also defined both for primitive types and many types in the standard library.

r[expr.cmp.paren-chaining]
Parentheses are required when chaining comparison operators. For example, the expression `a == b == c` is invalid and may be written as `(a == b) == c`.

r[expr.cmp.trait]
Unlike arithmetic and logical operators, the traits for overloading these operators are used more generally to show how a type may be compared and will likely be assumed to define actual comparisons by functions that use these traits as bounds. Many functions and macros in the standard library can then use that assumption (although not to ensure safety).

r[expr.cmp.place]
Unlike the arithmetic and logical operators above, these operators implicitly take shared borrows of their operands, evaluating them in [place expression context][place expression]:

```rust
# let a = 1;
# let b = 1;
a == b;
// is equivalent to
::std::cmp::PartialEq::eq(&a, &b);
```

This means that the operands don't have to be moved out of.

r[expr.cmp.behavior]

| Symbol | Meaning                  | Overloading method         |
|--------|--------------------------|----------------------------|
| `==`   | Equal                    | `std::cmp::PartialEq::eq`  |
| `!=`   | Not equal                | `std::cmp::PartialEq::ne`  |
| `>`    | Greater than             | `std::cmp::PartialOrd::gt` |
| `<`    | Less than                | `std::cmp::PartialOrd::lt` |
| `>=`   | Greater than or equal to | `std::cmp::PartialOrd::ge` |
| `<=`   | Less than or equal to    | `std::cmp::PartialOrd::le` |

Here are examples of the comparison operators being used.

```rust
assert!(123 == 123);
assert!(23 != -12);
assert!(12.5 > 12.2);
assert!([1, 2, 3] < [1, 3, 4]);
assert!('A' <= 'B');
assert!("World" >= "Hello");
```

r[expr.bool-logic]
## Lazy boolean operators

r[expr.bool-logic.syntax]
```grammar,expressions
LazyBooleanExpression ->
      Expression `||` Expression
    | Expression `&&` Expression
```

r[expr.bool-logic.intro]
The operators `||` and `&&` may be applied to operands of boolean type. The `||` operator denotes logical 'or', and the `&&` operator denotes logical 'and'.

r[expr.bool-logic.conditional-evaluation]
They differ from `|` and `&` in that the right-hand operand is only evaluated when the left-hand operand does not already determine the result of the expression. That is, `||` only evaluates its right-hand operand when the left-hand operand evaluates to `false`, and `&&` only when it evaluates to `true`.

```rust
let x = false || true; // true
let y = false && panic!(); // false, doesn't evaluate `panic!()`
```

r[expr.as]
## Type cast expressions

r[expr.as.syntax]
```grammar,expressions
TypeCastExpression -> Expression `as` TypeNoBounds
```

r[expr.as.intro]
A type cast expression is denoted with the binary operator `as`.

r[expr.as.result]
Executing an `as` expression casts the value on the left-hand side to the type on the right-hand side.

An example of an `as` expression:

```rust
# fn sum(values: &[f64]) -> f64 { 0.0 }
# fn len(values: &[f64]) -> i32 { 0 }
fn average(values: &[f64]) -> f64 {
    let sum: f64 = sum(values);
    let size: f64 = len(values) as f64;
    sum / size
}
```

r[expr.as.coercions]
`as` can be used to explicitly perform [coercions](../type-coercions.md), as well as the following additional casts. Any cast that does not fit either a coercion rule or an entry in the table is a compiler error. Here `*T` means either `*const T` or `*mut T`. `m` stands for optional `mut` in reference types and `mut` or `const` in pointer types.

| Type of `e`           | `U`                   | Cast performed by `e as U`                            |
|-----------------------|-----------------------|-------------------------------------------------------|
| Integer or Float type | Integer or Float type | [Numeric cast][expr.as.numeric]                       |
| Enumeration           | Integer type          | [Enum cast][expr.as.enum]                             |
| `bool` or `char`      | Integer type          | [Primitive to integer cast][expr.as.bool-char-as-int] |
| `u8`                  | `char`                | [`u8` to `char` cast][expr.as.u8-as-char]             |
| `*T`                  | `*V` (when [compatible][expr.as.pointer]) | [Pointer to pointer cast][expr.as.pointer] |
| `*T` where `T: Sized` | Integer type          | [Pointer to address cast][expr.as.pointer-as-int]     |
| Integer type          | `*V` where `V: Sized` | [Address to pointer cast][expr.as.int-as-pointer]     |
| `&m₁ [T; n]`          | `*m₂ T` [^lessmut]    | Array to pointer cast                                 |
| `*m₁ [T; n]`          | `*m₂ T` [^lessmut]    | Array to pointer cast                                 |
| [Function item]       | [Function pointer]    | Function item to function pointer cast                |
| [Function item]       | `*V` where `V: Sized` | Function item to pointer cast                         |
| [Function item]       | Integer               | Function item to address cast                         |
| [Function pointer]    | `*V` where `V: Sized` | Function pointer to pointer cast                      |
| [Function pointer]    | Integer               | Function pointer to address cast                      |
| Closure [^no-capture] | Function pointer      | Closure to function pointer cast                      |

[^lessmut]: Only when `m₁` is `mut` or `m₂` is `const`. Casting `mut` reference/pointer to `const` pointer is allowed.

[^no-capture]: Only closures that do not capture (close over) any local variables can be cast to function pointers.

### Semantics

r[expr.as.numeric]
#### Numeric cast

r[expr.as.numeric.int-same-size]
* Casting between two integers of the same size (e.g. i32 -> u32) is a no-op (Rust uses 2's complement for negative values of fixed integers)

  ```rust
  assert_eq!(42i8 as u8, 42u8);
  assert_eq!(-1i8 as u8, 255u8);
  assert_eq!(255u8 as i8, -1i8);
  assert_eq!(-1i16 as u16, 65535u16);
  ```

r[expr.as.numeric.int-truncation]
* Casting from a larger integer to a smaller integer (e.g. u32 -> u8) will truncate

  ```rust
  assert_eq!(42u16 as u8, 42u8);
  assert_eq!(1234u16 as u8, 210u8);
  assert_eq!(0xabcdu16 as u8, 0xcdu8);

  assert_eq!(-42i16 as i8, -42i8);
  assert_eq!(1234u16 as i8, -46i8);
  assert_eq!(0xabcdi32 as i8, -51i8);
  ```

r[expr.as.numeric.int-extension]
* Casting from a smaller integer to a larger integer (e.g. u8 -> u32) will
    * zero-extend if the source is unsigned
    * sign-extend if the source is signed

  ```rust
  assert_eq!(42i8 as i16, 42i16);
  assert_eq!(-17i8 as i16, -17i16);
  assert_eq!(0b1000_1010u8 as u16, 0b0000_0000_1000_1010u16, "Zero-extend");
  assert_eq!(0b0000_1010i8 as i16, 0b0000_0000_0000_1010i16, "Sign-extend 0");
  assert_eq!(0b1000_1010u8 as i8 as i16, 0b1111_1111_1000_1010u16 as i16, "Sign-extend 1");
  ```

r[expr.as.numeric.float-as-int]
* Casting from a float to an integer will round the float towards zero
    * `NaN` will return `0`
    * Values larger than the maximum integer value, including `INFINITY`, will saturate to the maximum value of the integer type.
    * Values smaller than the minimum integer value, including `NEG_INFINITY`, will saturate to the minimum value of the integer type.

  ```rust
  assert_eq!(42.9f32 as i32, 42);
  assert_eq!(-42.9f32 as i32, -42);
  assert_eq!(42_000_000f32 as i32, 42_000_000);
  assert_eq!(std::f32::NAN as i32, 0);
  assert_eq!(1_000_000_000_000_000f32 as i32, 0x7fffffffi32);
  assert_eq!(std::f32::NEG_INFINITY as i32, -0x80000000i32);
  ```

r[expr.as.numeric.int-as-float]
* Casting from an integer to float will produce the closest possible float \*
    * if necessary, rounding is according to `roundTiesToEven` mode \*\*\*
    * on overflow, infinity (of the same sign as the input) is produced
    * note: with the current set of numeric types, overflow can only happen on `u128 as f32` for values greater or equal to `f32::MAX + (0.5 ULP)`

  ```rust
  assert_eq!(1337i32 as f32, 1337f32);
  assert_eq!(123_456_789i32 as f32, 123_456_790f32, "Rounded");
  assert_eq!(0xffffffff_ffffffff_ffffffff_ffffffff_u128 as f32, std::f32::INFINITY);
  ```

r[expr.as.numeric.float-widening]
* Casting from an f32 to an f64 is perfect and lossless

  ```rust
  assert_eq!(1_234.5f32 as f64, 1_234.5f64);
  assert_eq!(std::f32::INFINITY as f64, std::f64::INFINITY);
  assert!((std::f32::NAN as f64).is_nan());
  ```

r[expr.as.numeric.float-narrowing]
* Casting from an f64 to an f32 will produce the closest possible f32 \*\*
    * if necessary, rounding is according to `roundTiesToEven` mode \*\*\*
    * on overflow, infinity (of the same sign as the input) is produced

  ```rust
  assert_eq!(1_234.5f64 as f32, 1_234.5f32);
  assert_eq!(1_234_567_891.123f64 as f32, 1_234_567_890f32, "Rounded");
  assert_eq!(std::f64::INFINITY as f32, std::f32::INFINITY);
  assert!((std::f64::NAN as f32).is_nan());
  ```

\* if integer-to-float casts with this rounding mode and overflow behavior are not supported natively by the hardware, these casts will likely be slower than expected.

\*\* if f64-to-f32 casts with this rounding mode and overflow behavior are not supported natively by the hardware, these casts will likely be slower than expected.

\*\*\* as defined in IEEE 754-2008 &sect;4.3.1: pick the nearest floating point number, preferring the one with an even least significant digit if exactly halfway between two floating point numbers.

r[expr.as.enum]
#### Enum cast

r[expr.as.enum.discriminant]
Casts an enum to its discriminant, then uses a numeric cast if needed. Casting is limited to the following kinds of enumerations:

* [Unit-only enums]
* [Field-less enums] without [explicit discriminants], or where only unit-variants have explicit discriminants

```rust
enum Enum { A, B, C }
assert_eq!(Enum::A as i32, 0);
assert_eq!(Enum::B as i32, 1);
assert_eq!(Enum::C as i32, 2);
```

r[expr.as.enum.no-drop]
Casting is not allowed if the enum implements [`Drop`].

r[expr.as.bool-char-as-int]
#### Primitive to integer cast

* `false` casts to `0`, `true` casts to `1`
* `char` casts to the value of the code point, then uses a numeric cast if needed.

```rust
assert_eq!(false as i32, 0);
assert_eq!(true as i32, 1);
assert_eq!('A' as i32, 65);
assert_eq!('Ö' as i32, 214);
```

r[expr.as.u8-as-char]
#### `u8` to `char` cast

Casts to the `char` with the corresponding code point.

```rust
assert_eq!(65u8 as char, 'A');
assert_eq!(214u8 as char, 'Ö');
```

r[expr.as.pointer-as-int]
#### Pointer to address cast

Casting from a raw pointer to an integer produces the machine address of the referenced memory. If the integer type is smaller than the pointer type, the address may be truncated; using `usize` avoids this.

r[expr.as.int-as-pointer]
#### Address to pointer cast

Casting from an integer to a raw pointer interprets the integer as a memory address and produces a pointer referencing that memory.

> [!WARNING]
> This interacts with the Rust memory model, which is still under development.
> A pointer obtained from this cast may suffer additional restrictions even if it is bitwise equal to a valid pointer.
> Dereferencing such a pointer may be [undefined behavior] if aliasing rules are not followed.

A trivial example of sound address arithmetic:

```rust
let mut values: [i32; 2] = [1, 2];
let p1: *mut i32 = values.as_mut_ptr();
let first_address = p1 as usize;
let second_address = first_address + 4; // 4 == size_of::<i32>()
let p2 = second_address as *mut i32;
unsafe {
    *p2 += 1;
}
assert_eq!(values[1], 3);
```

r[expr.as.pointer]
#### Pointer-to-pointer cast

r[expr.as.pointer.behavior]
`*const T` / `*mut T` can be cast to `*const U` / `*mut U` with the following behavior:

r[expr.as.pointer.sized]
- If `T` and `U` are both sized, the pointer is returned unchanged.

  > [!EXAMPLE]
  > ```rust
  > let x: i32 = 42;
  > let p1: *const i32 = &x;
  > let p2: *const u8 = p1 as *const u8;
  > // The pointer address remains the same.
  > assert_eq!(p1 as usize, p2 as usize);
  > ```

r[expr.as.pointer.discard-metadata]
- If `T` is unsized and `U` is sized, the cast discards all metadata that completes the wide pointer `T` and produces a thin pointer `U` consisting of the data part of the unsized pointer.

  > [!EXAMPLE]
  > ```rust
  > let slice: &[i32] = &[1, 2, 3];
  > let ptr: *const [i32] = slice as *const [i32];
  > // Cast from wide pointer (*const [i32]) to thin pointer (*const i32)
  > // discarding the length metadata.
  > let data_ptr: *const i32 = ptr as *const i32;
  > assert_eq!(unsafe { *data_ptr }, 1);
  > ```

r[expr.as.pointer.unsized.unchanged]
- If `T` and `U` are both unsized, the pointer is also returned unchanged. In particular, the metadata is preserved exactly. The cast can only be performed if the metadata is compatible according to the below rules:

r[expr.as.pointer.unsized.slice]
- When `T` and `U` are unsized with slice metadata, they are always compatible. The metadata of a slice is the number of elements, so casting `*[u16] -> *[u8]` is legal but will result in reducing the number of bytes by half.

  > [!EXAMPLE]
  > ```rust
  > let slice: &[u16] = &[1, 2, 3];
  > let ptr: *const [u16] = slice as *const [u16];
  > let byte_ptr: *const [u8] = ptr as *const [u8];
  > assert_eq!(byte_ptr.len(), 3);
  > ```

r[expr.as.pointer.unsized.trait]
- When `T` and `U` are unsized with trait object metadata, the metadata is compatible only when all of the following holds:
  1. The principal trait must be the same.

     > [!EXAMPLE]
     > ```rust,compile_fail,E0606
     > trait Foo {}
     > trait Bar {}
     > impl Foo for i32 {}
     > impl Bar for i32 {}
     >
     > let x: i32 = 42;
     > let ptr_foo: *const dyn Foo = &x as *const dyn Foo;
     > // You can't cast to a different principal trait.
     > let ptr_bar: *const dyn Bar = ptr_foo as *const dyn Bar; // ERROR
     > ```


  2. Auto traits may be removed.

     > [!EXAMPLE]
     > ```rust
     > trait Foo {}
     > struct S;
     > impl Foo for S {}
     > unsafe impl Send for S {}
     >
     > let s = S;
     > let ptr_send: *const (dyn Foo + Send) = &s;
     > // Removing an auto trait.
     > let ptr_no_send: *const dyn Foo = ptr_send as *const dyn Foo;
     > ```


  3. Auto traits may be added only if they are a super trait of the principal trait.

     > [!EXAMPLE]
     > ```rust
     > trait Foo: Send {}
     > struct S;
     > impl Foo for S {}
     > unsafe impl Send for S {}
     >
     > let s = S;
     > let ptr_no_send: *const dyn Foo = &s;
     > // Adding an auto trait.
     > let ptr_send: *const (dyn Foo + Send) = ptr_no_send as *const (dyn Foo + Send);
     > ```
     >
     > ```rust,compile_fail,E0804
     > trait Foo {}
     > # struct S;
     > # impl Foo for S {}
     > # unsafe impl Send for S {}
     > #
     > # let s = S;
     > # let ptr_no_send: *const dyn Foo = &s;
     > // Same as above, except trait Foo does not have Send as a super trait.
     > let ptr_send: *const (dyn Foo + Send) = ptr_no_send as *const (dyn Foo + Send); // ERROR
     > ```


  4. Trailing lifetimes may only be shortened.

     > [!EXAMPLE]
     > ```rust
     > trait Foo {}
     >
     > fn shorten_lifetime<'long: 'short, 'short>(
     >     ptr: *const (dyn Foo + 'long),
     > ) -> *const (dyn Foo + 'short) {
     >     // Shortening the lifetime is allowed.
     >     ptr as *const (dyn Foo + 'short)
     > }
     > ```
     >
     > ```rust,compile_fail
     > trait Foo {}
     >
     > fn lengthen_lifetime<'long: 'short, 'short>(
     >     ptr: *const (dyn Foo + 'short),
     > ) -> *const (dyn Foo + 'long) {
     >     // It is not allowed to cast to a longer lifetime.
     >     ptr as *const (dyn Foo + 'long) // ERROR
     > }
     > ```

  5. Generics (including lifetimes) and associated types must match exactly.

     > [!EXAMPLE]
     > ```rust,compile_fail,E0606
     > trait Generic<T> {}
     > impl Generic<i32> for () {}
     > impl Generic<u32> for () {}
     >
     > let x = ();
     > let ptr_i32: *const dyn Generic<i32> = &x;
     > // You can't cast to a different generic parameter.
     > let ptr_u32: *const dyn Generic<u32> = ptr_i32 as *const dyn Generic<u32>; // ERROR
     > ```
     >
     > ```rust
     > trait HasType {
     >     type Output;
     > }
     >
     > trait Generic<'x, T> {}
     >
     > fn cast_via_associated<'a, 'b, A, B>(
     >     ptr: *const dyn Generic<'a, A::Output>,
     > ) -> *const dyn Generic<'b, B::Output>
     > where
     >     'a: 'b,
     >     'b: 'a,
     >     A: HasType,
     >     B: HasType<Output = A::Output>, // Forces equality
     > {
     >     ptr as *const dyn Generic<'b, B::Output>
     > }
     > ```



r[expr.as.pointer.unsized.compound]
- When `T` or `U` is a struct or tuple type whose last field is unsized, it has the same metadata and compatibility rules as its last field.

  > [!EXAMPLE]
  > ```rust
  > struct Wrapper(u32, [u8]);
  >
  > let slice: &[u8] = &[1, 2, 3];
  > let ptr: *const [u8] = slice;
  >
  > // The metadata (length 3) is preserved when casting to a struct
  > // where the last field is the unsized type `[u8]`.
  > let wrapper_ptr: *const Wrapper = ptr as *const Wrapper;
  >
  > // And preserved when casting back.
  > let ptr_back: *const [u8] = wrapper_ptr as *const [u8];
  > assert_eq!(ptr_back.len(), 3);
  > ```

r[expr.assign]
## Assignment expressions

r[expr.assign.syntax]
```grammar,expressions
AssignmentExpression -> Expression `=` Expression
```

r[expr.assign.intro]
An *assignment expression* moves a value into a specified place.

r[expr.assign.assignee]
An assignment expression consists of a [mutable] [assignee expression], the *assignee operand*, followed by an equals sign (`=`) and a [value expression], the *assigned value operand*.

r[expr.assign.behavior-basic]
In its most basic form, an assignee expression is a [place expression], and we discuss this case first.

r[expr.assign.behavior-destructuring]
The more general case of destructuring assignment is discussed below, but this case always decomposes into sequential assignments to place expressions, which may be considered the more fundamental case.

r[expr.assign.basic]
### Basic assignments

r[expr.assign.evaluation-order]
Evaluating assignment expressions begins by evaluating its operands. The assigned value operand is evaluated first, followed by the assignee expression.

r[expr.assign.destructuring-order]
For destructuring assignment, subexpressions of the assignee expression are evaluated left-to-right.

> [!NOTE]
> This is different than other expressions in that the right operand is evaluated before the left one.

r[expr.assign.drop-target]
It then has the effect of first [dropping] the value at the assigned place, unless the place is an uninitialized local variable or an uninitialized field of a local variable.

r[expr.assign.behavior]
Next it either [copies or moves] the assigned value to the assigned place.

r[expr.assign.result]
An assignment expression always produces [the unit value][unit].

Example:

```rust
let mut x = 0;
let y = 0;
x = y;
```

r[expr.assign.destructure]
### Destructuring assignments

r[expr.assign.destructure.intro]
Destructuring assignment is a counterpart to destructuring pattern matches for variable declaration, permitting assignment to complex values, such as tuples or structs. For instance, we may swap two mutable variables:

```rust
let (mut a, mut b) = (0, 1);
// Swap `a` and `b` using destructuring assignment.
(b, a) = (a, b);
```

r[expr.assign.destructure.assignee]
In contrast to destructuring declarations using `let`, patterns may not appear on the left-hand side of an assignment due to syntactic ambiguities. Instead, a group of expressions that correspond to patterns are designated to be [assignee expressions][assignee expression], and permitted on the left-hand side of an assignment. Assignee expressions are then desugared to pattern matches followed by sequential assignment.

r[expr.assign.destructure.irrefutable]
The desugared patterns must be irrefutable: in particular, this means that only slice patterns whose length is known at compile-time, and the trivial slice `[..]`, are permitted for destructuring assignment.

The desugaring method is straightforward, and is illustrated best by example.

```rust
# struct Struct { x: u32, y: u32 }
# let (mut a, mut b) = (0, 0);
(a, b) = (3, 4);

[a, b] = [3, 4];

Struct { x: a, y: b } = Struct { x: 3, y: 4};

// desugars to:

{
    let (_a, _b) = (3, 4);
    a = _a;
    b = _b;
}

{
    let [_a, _b] = [3, 4];
    a = _a;
    b = _b;
}

{
    let Struct { x: _a, y: _b } = Struct { x: 3, y: 4};
    a = _a;
    b = _b;
}
```

r[expr.assign.destructure.repeat-ident]
Identifiers are not forbidden from being used multiple times in a single assignee expression.

r[expr.assign.destructure.discard-value]
[Underscore expressions] and empty [range expressions] may be used to ignore certain values, without binding them.

r[expr.assign.destructure.default-binding]
Note that default binding modes do not apply for the desugared expression.

r[expr.assign.destructure.tmp-scopes]
> [!NOTE]
> The desugaring restricts the [temporary scope] of the assigned value operand (the RHS) of a destructuring assignment.
>
> In a basic assignment, the [temporary] is dropped at the end of the enclosing temporary scope. Below, that's the statement. Therefore, the assignment and use is allowed.
>
> ```rust
> # fn temp() {}
> fn f<T>(x: T) -> T { x }
> let x;
> (x = f(&temp()), x); // OK
> ```
>
> Conversely, in a destructuring assignment, the temporary is dropped at the end of the `let` statement in the desugaring. As that happens before we try to assign to `x`, below, it fails.
>
> ```rust,compile_fail,E0716
> # fn temp() {}
> # fn f<T>(x: T) -> T { x }
> # let x;
> [x] = [f(&temp())]; // ERROR
> ```
>
> This desugars to:
>
> ```rust,compile_fail,E0716
> # fn temp() {}
> # fn f<T>(x: T) -> T { x }
> # let x;
> {
>     let [_x] = [f(&temp())];
>     //                     ^
>     //      The temporary is dropped here.
>     x = _x; // ERROR
> }
> ```

r[expr.assign.destructure.tmp-ext]
> [!NOTE]
> Due to the desugaring, the assigned value operand (the RHS) of a destructuring assignment is an [extending expression] within a newly-introduced block.
>
> Below, because the [temporary scope] is extended to the end of this introduced block, the assignment is allowed.
>
> ```rust
> # fn temp() {}
> # let x;
> [x] = [&temp()]; // OK
> ```
>
> This desugars to:
>
> ```rust
> # fn temp() {}
> # let x;
> { let [_x] = [&temp()]; x = _x; } // OK
> ```
>
> However, if we try to use `x`, even within the same statement, we'll get an error because the [temporary] is dropped at the end of this introduced block.
>
> ```rust,compile_fail,E0716
> # fn temp() {}
> # let x;
> ([x] = [&temp()], x); // ERROR
> ```
>
> This desugars to:
>
> ```rust,compile_fail,E0716
> # fn temp() {}
> # let x;
> (
>     {
>         let [_x] = [&temp()];
>         x = _x;
>     }, // <-- The temporary is dropped here.
>     x, // ERROR
> );
> ```

r[expr.compound-assign]
## Compound assignment expressions

r[expr.compound-assign.syntax]
```grammar,expressions
CompoundAssignmentExpression ->
      Expression `+=` Expression
    | Expression `-=` Expression
    | Expression `*=` Expression
    | Expression `/=` Expression
    | Expression `%=` Expression
    | Expression `&=` Expression
    | Expression `|=` Expression
    | Expression `^=` Expression
    | Expression `<<=` Expression
    | Expression `>>=` Expression
```

r[expr.compound-assign.intro]
*Compound assignment expressions* combine arithmetic and logical binary operators with assignment expressions.

For example:

```rust
let mut x = 5;
x += 1;
assert!(x == 6);
```

The syntax of compound assignment is a [mutable] [place expression], the *assigned operand*, then one of the operators followed by an `=` as a single token (no whitespace), and then a [value expression], the *modifying operand*.

r[expr.compound-assign.place]
Unlike other place operands, the assigned place operand must be a place expression.

r[expr.compound-assign.no-value]
Attempting to use a value expression is a compiler error rather than promoting it to a temporary.

r[expr.compound-assign.operand-order]
Evaluation of compound assignment expressions depends on the types of the operands.

r[expr.compound-assign.primitives]
If the types of both operands are known, prior to monomorphization, to be primitive, the right hand side is evaluated first, the left hand side is evaluated next, and the place given by the evaluation of the left hand side is mutated by applying the operator to the values of both sides.

```rust
# use core::{num::Wrapping, ops::AddAssign};
#
trait Equate {}
impl<T> Equate for (T, T) {}

fn f1(x: (u8,)) {
    let mut order = vec![];
    // The RHS is evaluated first as both operands are of primitive
    // type.
    { order.push(2); x }.0 += { order.push(1); x }.0;
    assert!(order.is_sorted());
}

fn f2(x: (Wrapping<u8>,)) {
    let mut order = vec![];
    // The LHS is evaluated first as `Wrapping<_>` is not a primitive
    // type.
    { order.push(1); x }.0 += { order.push(2); (0u8,) }.0;
    assert!(order.is_sorted());
}

fn f3<T: AddAssign<u8> + Copy>(x: (T,)) where (T, u8): Equate {
    let mut order = vec![];
    // The LHS is evaluated first as one of the operands is a generic
    // parameter, even though that generic parameter can be unified
    // with a primitive type due to the where clause bound.
    { order.push(1); x }.0 += { order.push(2); (0u8,) }.0;
    assert!(order.is_sorted());
}

fn main() {
    f1((0u8,));
    f2((Wrapping(0u8),));
    // We supply a primitive type as the generic argument, but this
    // does not affect the evaluation order in `f3` when
    // monomorphized.
    f3::<u8>((0u8,));
}
```

> [!NOTE]
> This is unusual. Elsewhere left to right evaluation is the norm.
>
> See the [eval order test] for more examples.

r[expr.compound-assign.trait]
Otherwise, this expression is syntactic sugar for using the corresponding trait for the operator (see [expr.arith-logic.behavior]) and calling its method with the left hand side as the [receiver] and the right hand side as the next argument.

For example, the following two statements are equivalent:

```rust
# use std::ops::AddAssign;
fn f<T: AddAssign + Copy>(mut x: T, y: T) {
    x += y; // Statement 1.
    x.add_assign(y); // Statement 2.
}
```

> [!NOTE]
> Surprisingly, desugaring this further to a fully qualified method call is not equivalent, as there is special borrow checker behavior when the mutable reference to the first operand is taken via [autoref].
>
> ```rust
> # use std::ops::AddAssign;
> fn f<T: AddAssign + Copy>(mut x: T) {
>     // Here we used `x` as both the LHS and the RHS. Because the
>     // mutable borrow of the LHS needed to call the trait method
>     // is taken implicitly by autoref, this is OK.
>     x += x; //~ OK
>     x.add_assign(x); //~ OK
> }
> ```
>
> ```rust,compile_fail,E0503
> # use std::ops::AddAssign;
> fn f<T: AddAssign + Copy>(mut x: T) {
>     // We can't desugar the above to the below, as once we take the
>     // mutable borrow of `x` to pass the first argument, we can't
>     // pass `x` by value in the second argument because the mutable
>     // reference is still live.
>     <T as AddAssign>::add_assign(&mut x, x);
>     //~^ ERROR cannot use `x` because it was mutably borrowed
> }
> ```
>
> ```rust,compile_fail,E0503
> # use std::ops::AddAssign;
> fn f<T: AddAssign + Copy>(mut x: T) {
>     // As above.
>     (&mut x).add_assign(x);
>     //~^ ERROR cannot use `x` because it was mutably borrowed
> }
> ```

r[expr.compound-assign.result]
As with normal assignment expressions, compound assignment expressions always produce [the unit value][unit].

> [!WARNING]
> Avoid writing code that depends on the evaluation order of operands in compound assignments as it can be unusual and surprising.

[`Box`]: ../special-types-and-traits.md#boxt
[`Try`]: core::ops::Try
[autoref]: expr.method.candidate-receivers-refs
[copies or moves]: ../expressions.md#moved-and-copied-types
[dropping]: ../destructors.md
[eval order test]: https://github.com/rust-lang/rust/blob/1.58.0/src/test/ui/expr/compound-assignment/eval-order.rs
[explicit discriminants]: ../items/enumerations.md#explicit-discriminants
[extending expression]: destructors.scope.lifetime-extension.exprs
[field-less enums]: ../items/enumerations.md#field-less-enum
[grouped expression]: grouped-expr.md
[literal expression]: literal-expr.md#integer-literal-expressions
[logical and]: ../types/boolean.md#logical-and
[logical not]: ../types/boolean.md#logical-not
[logical or]: ../types/boolean.md#logical-or
[logical xor]: ../types/boolean.md#logical-xor
[moved from]: expr.move.movable-place
[mutable]: ../expressions.md#mutability
[place expression]: ../expressions.md#place-expressions-and-value-expressions
[assignee expression]: ../expressions.md#place-expressions-and-value-expressions
[undefined behavior]: ../behavior-considered-undefined.md
[unit]: ../types/tuple.md
[Unit-only enums]: ../items/enumerations.md#unit-only-enum
[value expression]: ../expressions.md#place-expressions-and-value-expressions
[temporary lifetime extension]: destructors.scope.lifetime-extension
[temporary scope]: destructors.scope.temporary
[temporary value]: ../expressions.md#temporaries
[float-float]: https://github.com/rust-lang/rust/issues/15536
[Function pointer]: ../types/function-pointer.md
[Function item]: ../types/function-item.md
[receiver]: expr.method.intro
[temporary]: expr.temporary
[undefined behavior]: ../behavior-considered-undefined.md
[Underscore expressions]: ./underscore-expr.md
[range expressions]: ./range-expr.md


---

r[expr.paren]
# Grouped expressions

r[expr.paren.syntax]
```grammar,expressions
GroupedExpression -> `(` Expression `)`
```

r[expr.paren.intro]
A *parenthesized expression* wraps a single expression, evaluating to that expression. The syntax for a parenthesized expression is a `(`, then an expression, called the *enclosed operand*, and then a `)`.

r[expr.paren.evaluation]
Parenthesized expressions evaluate to the value of the enclosed operand.

r[expr.paren.place-or-value]
A parenthesized expression is a [place expression][place] if the enclosed operand is a place expression, and is a value expression if the enclosed operand is a value expression.

r[expr.paren.override-precedence]
Parentheses can be used to explicitly modify the precedence order of subexpressions within an expression.

An example of a parenthesized expression:

```rust
let x: i32 = 2 + 3 * 4; // not parenthesized
let y: i32 = (2 + 3) * 4; // parenthesized
assert_eq!(x, 14);
assert_eq!(y, 20);
```

An example of a necessary use of parentheses is when calling a function pointer that is a member of a struct:

```rust
# struct A {
#    f: fn() -> &'static str
# }
# impl A {
#    fn f(&self) -> &'static str {
#        "The method f"
#    }
# }
# let a = A{f: || "The field f"};
#
assert_eq!( a.f (), "The method f");
assert_eq!((a.f)(), "The field f");
```

[place]: ../expressions.md#place-expressions-and-value-expressions


---

r[expr.array]
# Array and array index expressions

## Array expressions

r[expr.array.syntax]
```grammar,expressions
ArrayExpression -> `[` ArrayElements? `]`

ArrayElements ->
      Expression ( `,` Expression )* `,`?
    | Expression `;` Expression
```

r[expr.array.constructor]
*Array expressions* construct [arrays][array]. Array expressions come in two forms.

r[expr.array.array]
The first form lists out every value in the array.

r[expr.array.array-syntax]
The syntax for this form is a comma-separated list of expressions of uniform type enclosed in square brackets.

r[expr.array.array-behavior]
This produces an array containing each of these values in the order they are written.

r[expr.array.repeat]
The syntax for the second form is two expressions separated by a semicolon (`;`) enclosed in square brackets.

r[expr.array.repeat-operand]
The expression before the `;` is called the *repeat operand*.

r[expr.array.length-operand]
The expression after the `;` is called the *length operand*.

r[expr.array.length-restriction]
The length operand must either be an [inferred const] or be a [constant expression] of type `usize` (e.g. a [literal] or a [constant item]).

```rust
const C: usize = 1;
let _: [u8; C] = [0; 1]; // Literal.
let _: [u8; C] = [0; C]; // Constant item.
let _: [u8; C] = [0; _]; // Inferred const.
let _: [u8; C] = [0; (((_)))]; // Inferred const.
```

> [!NOTE]
> In an array expression, an [inferred const] is parsed as an [expression][Expression] but then semantically treated as a separate kind of [const generic argument].

r[expr.array.repeat-behavior]
An array expression of this form creates an array with the length of the value of the length operand with each element being a copy of the repeat operand. That is, `[a; b]` creates an array containing `b` copies of the value of `a`.

r[expr.array.repeat-copy]
If the length operand has a value greater than 1 then this requires the repeat operand to have a type that implements [`Copy`], to be a [const block expression], or to be a [path] to a constant item.

r[expr.array.repeat-const-item]
When the repeat operand is a const block or a path to a constant item, it is evaluated the number of times specified in the length operand.

r[expr.array.repeat-evaluation-zero]
If that value is `0`, then the const block or constant item is not evaluated at all.

r[expr.array.repeat-non-const]
For expressions that are neither a const block nor a path to a constant item, it is evaluated exactly once, and then the result is copied the length operand's value times.

```rust
[1, 2, 3, 4];
["a", "b", "c", "d"];
[0; 128];              // array with 128 zeros
[0u8, 0u8, 0u8, 0u8,];
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]; // 2D array
const EMPTY: Vec<i32> = Vec::new();
[EMPTY; 2];
```

r[expr.array.index]
## Array and slice indexing expressions

r[expr.array.index.syntax]
```grammar,expressions
IndexExpression -> Expression `[` Expression `]`
```

r[expr.array.index.array]
[Array] and [slice]-typed values can be indexed by writing a square-bracket-enclosed expression of type `usize` (the index) after them. When the array is mutable, the resulting [memory location] can be assigned to.

r[expr.array.index.trait]
For other types an index expression `a[b]` is equivalent to `*std::ops::Index::index(&a, b)`, or `*std::ops::IndexMut::index_mut(&mut a, b)` in a mutable place expression context, except that when the index expression undergoes [temporary lifetime extension], the indexed expression `a` also has its [temporary scope] extended. Just as with methods, Rust will also insert dereference operations on `a` repeatedly to find an implementation.

```rust
// The temporary holding the result of `vec![()]` is extended to
// live to the end of the block, so `x` may be used in subsequent
// statements.
let x = &vec![()][0];
# x;
```

```rust,compile_fail,E0716
// The temporary holding the result of `vec![()]` is dropped at the
// end of the statement, so it's an error to use `y` after.
let y = &*std::ops::Index::index(&vec![()], 0); // ERROR
# y;
```

r[expr.array.index.zero-index]
Indices are zero-based for arrays and slices.

r[expr.array.index.const]
Array access is a [constant expression], so bounds can be checked at compile-time with a constant index value. Otherwise a check will be performed at run-time that will put the thread in a [_panicked state_][panic] if it fails.

```rust,should_panic
// lint is deny by default.
#![warn(unconditional_panic)]

([1, 2, 3, 4])[2];        // Evaluates to 3

let b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
b[1][2];                  // multidimensional array indexing

let x = (["a", "b"])[10]; // warning: index out of bounds

let n = 10;
let y = (["a", "b"])[n];  // panics

let arr = ["a", "b"];
arr[10];                  // warning: index out of bounds
```

r[expr.array.index.trait-impl]
The array index expression can be implemented for types other than arrays and slices by implementing the [Index] and [IndexMut] traits.

[`Copy`]: ../special-types-and-traits.md#copy
[IndexMut]: std::ops::IndexMut
[Index]: std::ops::Index
[array]: ../types/array.md
[const generic argument]: items.generics.const.argument
[const block expression]: expr.block.const
[constant expression]: ../const_eval.md#constant-expressions
[constant item]: ../items/constant-items.md
[inferred const]: items.generics.const.inferred
[literal]: ../tokens.md#literals
[memory location]: ../expressions.md#place-expressions-and-value-expressions
[panic]: ../panic.md
[path]: path-expr.md
[slice]: ../types/slice.md
[temporary lifetime extension]: destructors.scope.lifetime-extension
[temporary scope]: destructors.scope.temporary


---

r[expr.tuple]
# Tuple and tuple indexing expressions

## Tuple expressions

r[expr.tuple.syntax]
```grammar,expressions
TupleExpression -> `(` TupleElements? `)`

TupleElements -> ( Expression `,` )+ Expression?
```

r[expr.tuple.result]
A *tuple expression* constructs [tuple values][tuple type].

r[expr.tuple.intro]
The syntax for tuple expressions is a parenthesized, comma separated list of expressions, called the *tuple initializer operands*.

r[expr.tuple.unary-tuple-restriction]
1-ary tuple expressions require a comma after their tuple initializer operand to be disambiguated with a [parenthetical expression].

r[expr.tuple.value]
Tuple expressions are a [value expression] that evaluate into a newly constructed value of a tuple type.

r[expr.tuple.type]
The number of tuple initializer operands is the arity of the constructed tuple.

r[expr.tuple.unit]
Tuple expressions without any tuple initializer operands produce the unit tuple.

r[expr.tuple.fields]
For other tuple expressions, the first written tuple initializer operand initializes the field `0` and subsequent operands initializes the next highest field. For example, in the tuple expression `('a', 'b', 'c')`, `'a'` initializes the value of the field `0`, `'b'` field `1`, and `'c'` field `2`.

Examples of tuple expressions and their types:

| Expression           | Type         |
| -------------------- | ------------ |
| `()`                 | `()` (unit)  |
| `(0.0, 4.5)`         | `(f64, f64)` |
| `("x".to_string(), )` | `(String, )`  |
| `("a", 4usize, true)`| `(&'static str, usize, bool)` |

r[expr.tuple-index]
## Tuple indexing expressions

r[expr.tuple-index.syntax]
```grammar,expressions
TupleIndexingExpression -> Expression `.` TUPLE_INDEX
```

r[expr.tuple-index.intro]
A *tuple indexing expression* accesses fields of [tuples][tuple type] and [tuple structs][tuple struct].

The syntax for a tuple index expression is an expression, called the *tuple operand*, then a `.`, then finally a tuple index.

r[expr.tuple-index.index-syntax]
The syntax for the *tuple index* is a [decimal literal] with no leading zeros, underscores, or suffix. For example `0` and `2` are valid tuple indices but not `01`, `0_`, nor `0i32`.

r[expr.tuple-index.required-type]
The type of the tuple operand must be a [tuple type] or a [tuple struct].

r[expr.tuple-index.index-name-operand]
The tuple index must be a name of a field of the type of the tuple operand.

r[expr.tuple-index.result]
Evaluation of tuple index expressions has no side effects beyond evaluation of its tuple operand. As a [place expression], it evaluates to the location of the field of the tuple operand with the same name as the tuple index.

Examples of tuple indexing expressions:

```rust
// Indexing a tuple
let pair = ("a string", 2);
assert_eq!(pair.1, 2);

// Indexing a tuple struct
# struct Point(f32, f32);
let point = Point(1.0, 0.0);
assert_eq!(point.0, 1.0);
assert_eq!(point.1, 0.0);
```

> [!NOTE]
> Unlike field access expressions, tuple index expressions can be the function operand of a [call expression] as it cannot be confused with a method call since method names cannot be numbers.

> [!NOTE]
> Although arrays and slices also have elements, you must use an [array or slice indexing expression] or a [slice pattern] to access their elements.

[array or slice indexing expression]: array-expr.md#array-and-slice-indexing-expressions
[call expression]: ./call-expr.md
[decimal literal]: ../tokens.md#integer-literals
[field access expressions]: ./field-expr.html#field-access-expressions
[operands]: ../expressions.md
[parenthetical expression]: grouped-expr.md
[place expression]: ../expressions.md#place-expressions-and-value-expressions
[slice pattern]: ../patterns.md#slice-patterns
[tuple type]: ../types/tuple.md
[tuple struct]: ../types/struct.md
[value expression]: ../expressions.md#place-expressions-and-value-expressions


---

r[expr.struct]
# Struct expressions

r[expr.struct.syntax]
```grammar,expressions
StructExpression ->
    PathInExpression `{` (StructExprFields | StructBase)? `}`

StructExprFields ->
    StructExprField (`,` StructExprField)* (`,` StructBase | `,`?)

StructExprField ->
    OuterAttribute*
    (
        IDENTIFIER
      | (IDENTIFIER | TUPLE_INDEX) `:` Expression
    )

StructBase -> `..` Expression
```

r[expr.struct.intro]
A *struct expression* creates a struct, enum, or union value. It consists of a path to a [struct], [enum variant], or [union] item followed by the values for the fields of the item.

The following are examples of struct expressions:

```rust
# struct Point { x: f64, y: f64 }
# struct NothingInMe { }
# mod game { pub struct User<'a> { pub name: &'a str, pub age: u32, pub score: usize } }
# enum Enum { Variant {} }
Point {x: 10.0, y: 20.0};
NothingInMe {};
let u = game::User {name: "Joe", age: 35, score: 100_000};
Enum::Variant {};
```

> [!NOTE]
> Tuple structs and tuple enum variants are typically instantiated using a [call expression][expr.call] referring to the [constructor in the value namespace][items.struct.tuple]. These are distinct from a struct expression using curly braces referring to the constructor in the type namespace.
>
> ```rust
> struct Position(i32, i32, i32);
> Position(0, 0, 0);  // Typical way of creating a tuple struct.
> let c = Position;  // `c` is a function that takes 3 arguments.
> let pos = c(8, 6, 7);  // Creates a `Position` value.
>
> enum Version { Triple(i32, i32, i32) };
> Version::Triple(0, 0, 0);
> let f = Version::Triple;
> let ver = f(8, 6, 7);
> ```
>
> The last segment of the call path cannot refer to a type alias:
>
> ```rust
> trait Tr { type T; }
> impl<T> Tr for T { type T = T; }
>
> struct Tuple();
> enum Enum { Tuple() }
>
> // <Unit as Tr>::T(); // causes an error -- `::T` is a type, not a value
> <Enum as Tr>::T::Tuple(); // OK
> ```
>
> ----
>
> Unit structs and unit enum variants are typically instantiated using a [path expression][expr.path] referring to the [constant in the value namespace][items.struct.unit].
>
> ```rust
> struct Gamma;
> // Gamma unit value, referring to the const in the value namespace.
> let a = Gamma;
> // Exact same value as `a`, but constructed using a struct expression
> // referring to the type namespace.
> let b = Gamma {};
>
> enum ColorSpace { Oklch }
> let c = ColorSpace::Oklch;
> let d = ColorSpace::Oklch {};
> ```

r[expr.struct.field]
## Field struct expression

r[expr.struct.field.intro]
A struct expression with fields enclosed in curly braces allows you to specify the value for each individual field in any order. The field name is separated from its value with a colon.

r[expr.struct.field.union-constraint]
A value of a [union] type can only be created using this syntax, and it must specify exactly one field.

r[expr.struct.update]
## Functional update syntax

r[expr.struct.update.intro]
A struct expression that constructs a value of a struct type can terminate with the syntax `..` followed by an expression to denote a functional update.

r[expr.struct.update.base-same-type]
The expression following `..` (the base) must have the same struct type as the new struct type being formed.

r[expr.struct.update.fields]
The entire expression uses the given values for the fields that were specified and moves or copies the remaining fields from the base expression.

r[expr.struct.update.visibility-constraint]
As with all struct expressions, all of the fields of the struct must be [visible], even those not explicitly named.

```rust
# struct Point3d { x: i32, y: i32, z: i32 }
let mut base = Point3d {x: 1, y: 2, z: 3};
let y_ref = &mut base.y;
Point3d {y: 0, z: 10, .. base}; // OK, only base.x is accessed
drop(y_ref);
```

r[expr.struct.brace-restricted-positions]
Struct expressions can't be used directly in a [loop] or [if] expression's head, or in the [scrutinee] of an [if let] or [match] expression. However, struct expressions can be used in these situations if they are within another expression, for example inside [parentheses].

r[expr.struct.tuple-field]
The field names can be decimal integer values to specify indices for constructing tuple structs. This can be used with base structs to fill out the remaining indices not specified:

```rust
struct Color(u8, u8, u8);
let c1 = Color(0, 0, 0);  // Typical way of creating a tuple struct.
let c2 = Color{0: 255, 1: 127, 2: 0};  // Specifying fields by index.
let c3 = Color{1: 0, ..c2};  // Fill out all other fields using a base struct.
```

r[expr.struct.field.named]
### Struct field init shorthand

When initializing a data structure (struct, enum, union) with named (but not numbered) fields, it is allowed to write `fieldname` as a shorthand for `fieldname: fieldname`. This allows a compact syntax with less duplication. For example:

```rust
# struct Point3d { x: i32, y: i32, z: i32 }
# let x = 0;
# let y_value = 0;
# let z = 0;
Point3d { x: x, y: y_value, z: z };
Point3d { x, y: y_value, z };
```

[enum variant]: ../items/enumerations.md
[if let]: if-expr.md#if-let-patterns
[if]: if-expr.md#if-expressions
[loop]: loop-expr.md
[match]: match-expr.md
[parentheses]: grouped-expr.md
[struct]: ../items/structs.md
[union]: ../items/unions.md
[visible]: ../visibility-and-privacy.md
[scrutinee]: ../glossary.md#scrutinee


---

r[expr.call]
# Call expressions

r[expr.call.syntax]
```grammar,expressions
CallExpression -> Expression `(` CallParams? `)`

CallParams -> Expression ( `,` Expression )* `,`?
```

r[expr.call.intro]
A *call expression* calls a function. The syntax of a call expression is an expression, called the *function operand*, followed by a parenthesized comma-separated list of expression, called the *argument operands*.

r[expr.call.convergence]
If the function eventually returns, then the expression completes.

r[expr.call.trait]
For [non-function types], the expression `f(...)` uses the method on one of the following traits based on the function operand:

- [`Fn`] or [`AsyncFn`] --- shared reference.
- [`FnMut`] or [`AsyncFnMut`] --- mutable reference.
- [`FnOnce`] or [`AsyncFnOnce`] --- value.

r[expr.call.autoref-deref]
An automatic borrow will be taken if needed. The function operand will also be [automatically dereferenced] as required.

Some examples of call expressions:

```rust
# fn add(x: i32, y: i32) -> i32 { 0 }
let three: i32 = add(1i32, 2i32);
let name: &'static str = (|| "Rust")();
```

r[expr.call.desugar]
## Disambiguating function calls

r[expr.call.desugar.fully-qualified]
All function calls are sugar for a more explicit [fully-qualified syntax].

r[expr.call.desugar.ambiguity]
Function calls may need to be fully qualified, depending on the ambiguity of a call in light of in-scope items.

> [!NOTE]
> In the past, the terms "Unambiguous Function Call Syntax", "Universal Function Call Syntax", or "UFCS", have been used in documentation, issues, RFCs, and other community writings. However, these terms lack descriptive power and potentially confuse the issue at hand. We mention them here for searchability's sake.

r[expr.call.desugar.limits]
Several situations often occur which result in ambiguities about the receiver or referent of method or associated function calls. These situations may include:

* Multiple in-scope traits define methods with the same name for the same types
* Auto-`deref` is undesirable; for example, distinguishing between methods on a smart pointer itself and the pointer's referent
* Methods which take no arguments, like [`default()`], and return properties of a type, like [`size_of()`]

r[expr.call.desugar.explicit-path]
To resolve the ambiguity, the programmer may refer to their desired method or function using more specific paths, types, or traits.

For example,

```rust
trait Pretty {
    fn print(&self);
}

trait Ugly {
    fn print(&self);
}

struct Foo;
impl Pretty for Foo {
    fn print(&self) {}
}

struct Bar;
impl Pretty for Bar {
    fn print(&self) {}
}
impl Ugly for Bar {
    fn print(&self) {}
}

fn main() {
    let f = Foo;
    let b = Bar;

    // we can do this because we only have one item called `print` for `Foo`s
    f.print();
    // more explicit, and, in the case of `Foo`, not necessary
    Foo::print(&f);
    // if you're not into the whole brevity thing
    <Foo as Pretty>::print(&f);

    // b.print(); // Error: multiple 'print' found
    // Bar::print(&b); // Still an error: multiple `print` found

    // necessary because of in-scope items defining `print`
    <Bar as Pretty>::print(&b);
}
```

Refer to [RFC 132] for further details and motivations.

[RFC 132]: https://github.com/rust-lang/rfcs/blob/master/text/0132-ufcs.md
[`default()`]: std::default::Default::default
[`size_of()`]: std::mem::size_of
[automatically dereferenced]: field-expr.md#automatic-dereferencing
[fully-qualified syntax]: ../paths.md#qualified-paths
[non-function types]: ../types/function-item.md


---

r[expr.method]
# Method-call expressions

r[expr.method.syntax]
```grammar,expressions
MethodCallExpression -> Expression `.` PathExprSegment `(`CallParams? `)`
```

r[expr.method.intro]
A _method call_ consists of an expression (the *receiver*) followed by a single dot, an expression path segment, and a parenthesized expression-list.

r[expr.method.target]
Method calls are resolved to associated [methods] on specific traits, either statically dispatching to a method if the exact `self`-type of the left-hand-side is known, or dynamically dispatching if the left-hand-side expression is an indirect [trait object](../types/trait-object.md).

```rust
let pi: Result<f32, _> = "3.14".parse();
let log_pi = pi.unwrap_or(1.0).log(2.72);
# assert!(1.14 < log_pi && log_pi < 1.15)
```

r[expr.method.autoref-deref]
When looking up a method call, the receiver may be automatically dereferenced or borrowed in order to call a method. This requires a more complex lookup process than for other functions, since there may be a number of possible methods to call. The following procedure is used:

r[expr.method.candidate-receivers]
The first step is to build a list of candidate receiver types. Obtain these by repeatedly [dereferencing][dereference] the receiver expression's type, adding each type encountered to the list, then finally attempting an array [unsized coercion] at the end, and adding the result type if that is successful.

r[expr.method.candidate-receivers-refs]
Then, for each candidate `T`, add `&T` and `&mut T` to the list immediately after `T`.

For instance, if the receiver has type `Box<[i32;2]>`, then the candidate types will be `Box<[i32;2]>`, `&Box<[i32;2]>`, `&mut Box<[i32;2]>`, `[i32; 2]` (by dereferencing), `&[i32; 2]`, `&mut [i32; 2]`, `[i32]` (by unsized coercion), `&[i32]`, and finally `&mut [i32]`.

r[expr.method.candidate-search]
Then, for each candidate type `T`, search for a [visible] method with a receiver of that type in the following places:

1. `T`'s inherent methods (methods implemented directly on `T`).
1. Any of the methods provided by a [visible] trait implemented by `T`. If `T` is a type parameter, methods provided by trait bounds on `T` are looked up first. Then all remaining methods in scope are looked up.

> [!NOTE]
> The lookup is done for each type in order, which can occasionally lead to surprising results. The below code will print "In trait impl!", because `&self` methods are looked up first, the trait method is found before the struct's `&mut self` method is found.
>
> ```rust
> struct Foo {}
>
> trait Bar {
>   fn bar(&self);
> }
>
> impl Foo {
>   fn bar(&mut self) {
>     println!("In struct impl!")
>   }
> }
>
> impl Bar for Foo {
>   fn bar(&self) {
>     println!("In trait impl!")
>   }
> }
>
> fn main() {
>   let mut f = Foo{};
>   f.bar();
> }
> ```

r[expr.method.ambiguous-target]
If this results in multiple possible candidates, then it is an error, and the receiver must be [converted][disambiguate call] to an appropriate receiver type to make the method call.

r[expr.method.receiver-constraints]
This process does not take into account the mutability or lifetime of the receiver, or whether a method is `unsafe`. Once a method is looked up, if it can't be called for one (or more) of those reasons, the result is a compiler error.

r[expr.method.ambiguous-search]
If a step is reached where there is more than one possible method, such as where generic methods or traits are considered the same, then it is a compiler error. These cases require a [disambiguating function call syntax] for method and function invocation.

r[expr.method.edition2021]
> [!EDITION-2021]
> Before the 2021 edition, during the search for visible methods, if the candidate receiver type is an [array type], methods provided by the standard library [`IntoIterator`] trait are ignored.
>
> The edition used for this purpose is determined by the token representing the method name.
>
> This special case may be removed in the future.

> [!WARNING]
> For [trait objects], if there is an inherent method of the same name as a trait method, it will give a compiler error when trying to call the method in a method call expression. Instead, you can call the method using [disambiguating function call syntax], in which case it calls the trait method, not the inherent method. There is no way to call the inherent method. Just don't define inherent methods on trait objects with the same name as a trait method and you'll be fine.

[visible]: ../visibility-and-privacy.md
[array type]: ../types/array.md
[trait objects]: ../types/trait-object.md
[disambiguate call]: call-expr.md#disambiguating-function-calls
[disambiguating function call syntax]: call-expr.md#disambiguating-function-calls
[dereference]: operator-expr.md#the-dereference-operator
[methods]: ../items/associated-items.md#methods
[unsized coercion]: ../type-coercions.md#unsized-coercions
[`IntoIterator`]: std::iter::IntoIterator


---

r[expr.field]
# Field access expressions

r[expr.field.syntax]
```grammar,expressions
FieldExpression -> Expression `.` IDENTIFIER
```

r[expr.field.intro]
A *field expression* is a [place expression] that evaluates to the location of a field of a [struct] or [union].

r[expr.field.mut]
When the operand is [mutable], the field expression is also mutable.

r[expr.field.form]
The syntax for a field expression is an expression, called the *container operand*, then a `.`, and finally an [identifier].

r[expr.field.not-method-call]
Field expressions cannot be followed by a parenthetical comma-separated list of expressions, as that is instead parsed as a [method call expression]. That is, they cannot be the function operand of a [call expression].

> [!NOTE]
> Wrap the field expression in a [parenthesized expression] to use it in a call expression.
>
> ```rust
> # struct HoldsCallable<F: Fn()> { callable: F }
> let holds_callable = HoldsCallable { callable: || () };
>
> // Invalid: Parsed as calling the method "callable"
> // holds_callable.callable();
>
> // Valid
> (holds_callable.callable)();
> ```

Examples:

<!-- ignore: needs lots of support code -->
```rust,ignore
mystruct.myfield;
foo().x;
(Struct {a: 10, b: 20}).a;
(mystruct.function_field)() // Call expression containing a field expression
```

r[expr.field.autoref-deref]
## Automatic dereferencing

If the type of the container operand implements [`Deref`] or [`DerefMut`][`Deref`] depending on whether the operand is [mutable], it is *automatically dereferenced* as many times as necessary to make the field access possible. This process is also called *autoderef* for short.

r[expr.field.borrow]
## Borrowing

The fields of a struct or a reference to a struct are treated as separate entities when borrowing. If the struct does not implement [`Drop`] and is stored in a local variable, this also applies to moving out of each of its fields. This also does not apply if automatic dereferencing is done through user-defined types other than [`Box`].

```rust
struct A { f1: String, f2: String, f3: String }
let mut x: A;
# x = A {
#     f1: "f1".to_string(),
#     f2: "f2".to_string(),
#     f3: "f3".to_string()
# };
let a: &mut String = &mut x.f1; // x.f1 borrowed mutably
let b: &String = &x.f2;         // x.f2 borrowed immutably
let c: &String = &x.f2;         // Can borrow again
let d: String = x.f3;           // Move out of x.f3
```

[`Box`]: ../special-types-and-traits.md#boxt
[`Deref`]: ../special-types-and-traits.md#deref-and-derefmut
[`drop`]: ../special-types-and-traits.md#drop
[identifier]: ../identifiers.md
[call expression]: call-expr.md
[method call expression]: method-call-expr.md
[mutable]: ../expressions.md#mutability
[parenthesized expression]: grouped-expr.md
[place expression]: ../expressions.md#place-expressions-and-value-expressions
[struct]: ../items/structs.md
[union]: ../items/unions.md


---

r[expr.closure]
# Closure expressions

r[expr.closure.syntax]
```grammar,expressions
ClosureExpression ->
    `async`?[^cl-async-edition]
    `move`?
    ( `||` | `|` ClosureParameters? `|` )
    (Expression | `->` TypeNoBounds BlockExpression)

ClosureParameters -> ClosureParam (`,` ClosureParam)* `,`?

ClosureParam -> OuterAttribute* PatternNoTopAlt ( `:` Type )?
```

[^cl-async-edition]: The `async` qualifier is not allowed in the 2015 edition.

r[expr.closure.intro]
A *closure expression*, also known as a lambda expression or a lambda, defines a [closure type] and evaluates to a value of that type. The syntax for a closure expression is an optional `async` keyword, an optional `move` keyword, then a pipe-symbol-delimited (`|`) comma-separated list of [patterns], called the *closure parameters* each optionally followed by a `:` and a type, then an optional `->` and type, called the *return type*, and then an expression, called the *closure body operand*.

r[expr.closure.param-type]
The optional type after each pattern is a type annotation for the pattern.

r[expr.closure.explicit-type-body]
If there is a return type, the closure body must be a [block].

r[expr.closure.parameter-restriction]
A closure expression denotes a function that maps a list of parameters onto the expression that follows the parameters. Just like a [`let` binding], the closure parameters are irrefutable [patterns], whose type annotation is optional and will be inferred from context if not given.

r[expr.closure.unique-type]
Each closure expression has a unique, anonymous type.

r[expr.closure.captures]
Significantly, closure expressions _capture their environment_, which regular [function definitions] do not.

r[expr.closure.capture-inference]
Without the `move` keyword, the closure expression [infers how it captures each variable from its environment](../types/closure.md#capture-modes), preferring to capture by shared reference, effectively borrowing all outer variables mentioned inside the closure's body.

r[expr.closure.capture-mut-ref]
If needed the compiler will infer that instead mutable references should be taken, or that the values should be moved or copied (depending on their type) from the environment.

r[expr.closure.capture-move]
A closure can be forced to capture its environment by copying or moving values by prefixing it with the `move` keyword. This is often used to ensure that the closure's lifetime is `'static`.

r[expr.closure.trait-impl]
## Closure trait implementations

Which traits the closure type implement depends on how variables are captured, the types of the captured variables, and the presence of `async`. See the [call traits and coercions] chapter for how and when a closure implements `Fn`, `FnMut`, and `FnOnce`. The closure type implements [`Send`] and [`Sync`] if the type of every captured variable also implements the trait.

r[expr.closure.async]
## Async closures

r[expr.closure.async.intro]
Closures marked with the `async` keyword indicate that they are asynchronous in an analogous way to an [async function][items.fn.async].

r[expr.closure.async.future]
Calling the async closure does not perform any work, but instead evaluates to a value that implements [`Future`] that corresponds to the computation of the body of the closure.

```rust
async fn takes_async_callback(f: impl AsyncFn(u64)) {
    f(0).await;
    f(1).await;
}

async fn example() {
    takes_async_callback(async |i| {
        core::future::ready(i).await;
        println!("done with {i}.");
    }).await;
}
```

r[expr.closure.async.edition2018]
> [!EDITION-2018]
> Async closures are only available beginning with Rust 2018.

## Example

In this example, we define a function `ten_times` that takes a higher-order function argument, and we then call it with a closure expression as an argument, followed by a closure expression that moves values from its environment.

```rust
fn ten_times<F>(f: F) where F: Fn(i32) {
    for index in 0..10 {
        f(index);
    }
}

ten_times(|j| println!("hello, {}", j));
// With type annotations
ten_times(|j: i32| -> () { println!("hello, {}", j) });

let word = "konnichiwa".to_owned();
ten_times(move |j| println!("{}, {}", word, j));
```

## Attributes on closure parameters

r[expr.closure.param-attributes]
Attributes on closure parameters follow the same rules and restrictions as [regular function parameters].

[`let` binding]: ../statements.md#let-statements
[`Send`]: ../special-types-and-traits.md#send
[`Sync`]: ../special-types-and-traits.md#sync
[block]: block-expr.md
[call traits and coercions]: ../types/closure.md#call-traits-and-coercions
[closure type]: ../types/closure.md
[function definitions]: ../items/functions.md
[patterns]: ../patterns.md
[regular function parameters]: ../items/functions.md#attributes-on-function-parameters


---

r[expr.loop]
# Loops and other breakable expressions

r[expr.loop.syntax]
```grammar,expressions
LoopExpression ->
    LoopLabel? (
        InfiniteLoopExpression
      | PredicateLoopExpression
      | IteratorLoopExpression
      | LabelBlockExpression
    )
```

r[expr.loop.intro]
Rust supports four loop expressions:

*   A [`loop` expression](#infinite-loops) denotes an infinite loop.
*   A [`while` expression](#predicate-loops) loops until a predicate is false.
*   A [`for` expression](#iterator-loops) extracts values from an iterator, looping until the iterator is empty.
*   A [labeled block expression][expr.loop.block-labels] runs a loop exactly once, but allows exiting the loop early with `break`.

r[expr.loop.break-label]
All four types of loop support [`break` expressions](#break-expressions), and [labels](#loop-labels).

r[expr.loop.continue-label]
All except labeled block expressions support [`continue` expressions](#continue-expressions).

r[expr.loop.explicit-result]
Only `loop` and labeled block expressions support [evaluation to non-trivial values](#break-and-loop-values).

r[expr.loop.infinite]
## Infinite loops

r[expr.loop.infinite.syntax]
```grammar,expressions
InfiniteLoopExpression -> `loop` BlockExpression
```

r[expr.loop.infinite.intro]
A `loop` expression repeats execution of its body continuously: `loop { println!("I live."); }`.

r[expr.loop.infinite.diverging]
A `loop` expression without an associated `break` expression is [diverging] and has type [`!`].

r[expr.loop.infinite.break]
A `loop` expression containing associated [`break` expression(s)](#break-expressions) may terminate, and must have type compatible with the value of the `break` expression(s).

r[expr.loop.while]
## Predicate loops

r[expr.loop.while.syntax]
```grammar,expressions
PredicateLoopExpression -> `while` Conditions BlockExpression
```

r[expr.loop.while.intro]
A `while` loop expression allows repeating the evaluation of a block while a set of conditions remain true.

r[expr.loop.while.condition]
Condition operands must be either an [Expression] with a [boolean type] or a conditional `let` match. If all of the condition operands evaluate to `true` and all of the `let` patterns successfully match their [scrutinee]s, then the loop body block executes.

r[expr.loop.while.repeat]
After the loop body successfully executes, the condition operands are re-evaluated to determine if the body should be executed again.

r[expr.loop.while.exit]
If any condition operand evaluates to `false` or any `let` pattern does not match its scrutinee, the body is not executed and execution continues after the `while` expression.

r[expr.loop.while.eval]
A `while` expression evaluates to `()`.

An example:

```rust
let mut i = 0;

while i < 10 {
    println!("hello");
    i = i + 1;
}
```

r[expr.loop.while.let]
### `while let` patterns

r[expr.loop.while.let.intro]
`let` patterns in a `while` condition allow binding new variables into scope when the pattern matches successfully. The following examples illustrate bindings using `let` patterns:

```rust
let mut x = vec![1, 2, 3];

while let Some(y) = x.pop() {
    println!("y = {}", y);
}

while let _ = 5 {
    println!("Irrefutable patterns are always true");
    break;
}
```

r[expr.loop.while.let.desugar]
A `while let` loop is equivalent to a `loop` expression containing a [`match` expression] as follows.

<!-- ignore: expansion example -->
```rust,ignore
'label: while let PATS = EXPR {
    /* loop body */
}
```

is equivalent to

<!-- ignore: expansion example -->
```rust,ignore
'label: loop {
    match EXPR {
        PATS => { /* loop body */ },
        _ => break,
    }
}
```

r[expr.loop.while.let.or-pattern]
Multiple patterns may be specified with the `|` operator. This has the same semantics as with `|` in `match` expressions:

```rust
let mut vals = vec![2, 3, 1, 2, 2];
while let Some(v @ 1) | Some(v @ 2) = vals.pop() {
    // Prints 2, 2, then 1
    println!("{}", v);
}
```

r[expr.loop.while.chains]
### `while` condition chains

r[expr.loop.while.chains.intro]
Multiple condition operands can be separated with `&&`. These have the same semantics and restrictions as [`if` condition chains].

The following is an example of chaining multiple expressions, mixing `let` bindings and boolean expressions, and with expressions able to reference pattern bindings from previous expressions:

```rust
fn main() {
    let outer_opt = Some(Some(1i32));

    while let Some(inner_opt) = outer_opt
        && let Some(number) = inner_opt
        && number == 1
    {
        println!("Peek a boo");
        break;
    }
}
```

r[expr.loop.for]
## Iterator loops

r[expr.loop.for.syntax]
```grammar,expressions
IteratorLoopExpression ->
    `for` Pattern `in` Expression _except [StructExpression]_ BlockExpression
```
<!-- TODO: The exception above isn't accurate, see https://github.com/rust-lang/reference/issues/569 -->

r[expr.loop.for.intro]
A `for` expression is a syntactic construct for looping over elements provided by an implementation of `std::iter::IntoIterator`.

r[expr.loop.for.condition]
If the iterator yields a value, that value is matched against the irrefutable pattern, the body of the loop is executed, and then control returns to the head of the `for` loop. If the iterator is empty, the `for` expression completes.

An example of a `for` loop over the contents of an array:

```rust
let v = &["apples", "cake", "coffee"];

for text in v {
    println!("I like {}.", text);
}
```

An example of a for loop over a series of integers:

```rust
let mut sum = 0;
for n in 1..11 {
    sum += n;
}
assert_eq!(sum, 55);
```

r[expr.loop.for.desugar]
A `for` loop is equivalent to a `loop` expression containing a [`match` expression] as follows:

<!-- ignore: expansion example -->
```rust,ignore
'label: for PATTERN in iter_expr {
    /* loop body */
}
```

is equivalent to

<!-- ignore: expansion example -->
```rust,ignore
{
    let result = match IntoIterator::into_iter(iter_expr) {
        mut iter => 'label: loop {
            let mut next;
            match Iterator::next(&mut iter) {
                Option::Some(val) => next = val,
                Option::None => break,
            };
            let PATTERN = next;
            let () = { /* loop body */ };
        },
    };
    result
}
```

r[expr.loop.for.lang-items]
`IntoIterator`, `Iterator`, and `Option` are always the standard library items here, not whatever those names resolve to in the current scope.

The variable names `next`, `iter`, and `val` are for exposition only, they do not actually have names the user can type.

> [!NOTE]
> The outer `match` is used to ensure that any [temporary values] in `iter_expr` don't get dropped before the loop is finished. `next` is declared before being assigned because it results in types being inferred correctly more often.

r[expr.loop.label]
## Loop labels

r[expr.loop.label.syntax]
```grammar,expressions
LoopLabel -> LIFETIME_OR_LABEL `:`
```

r[expr.loop.label.intro]
A loop expression may optionally have a _label_. The label is written as a lifetime preceding the loop expression, as in `'foo: loop { break 'foo; }`, `'bar: while false {}`, `'humbug: for _ in 0..0 {}`.

r[expr.loop.label.control-flow]
If a label is present, then labeled `break` and `continue` expressions nested within this loop may exit out of this loop or return control to its head. See [break expressions](#break-expressions) and [continue expressions](#continue-expressions).

r[expr.loop.label.ref]
Labels follow the hygiene and shadowing rules of local variables. For example, this code will print "outer loop":

```rust
'a: loop {
    'a: loop {
        break 'a;
    }
    print!("outer loop");
    break 'a;
}
```

`'_` is not a valid loop label.

r[expr.loop.break]
## `break` expressions

r[expr.loop.break.syntax]
```grammar,expressions
BreakExpression -> `break` LIFETIME_OR_LABEL? Expression?
```

r[expr.loop.break.intro]
When `break` is encountered, execution of the associated loop body is immediately terminated, for example:

```rust
let mut last = 0;
for x in 1..100 {
    if x > 12 {
        break;
    }
    last = x;
}
assert_eq!(last, 12);
```

r[expr.loop.break.diverging]
A `break` expression is [diverging] and has a type of [`!`].

r[expr.loop.break.label]
A `break` expression is normally associated with the innermost `loop`, `for` or `while` loop enclosing the `break` expression, but a [label](#loop-labels) can be used to specify which enclosing loop is affected. Example:

```rust
'outer: loop {
    while true {
        break 'outer;
    }
}
```

r[expr.loop.break.value]
A `break` expression is only permitted in the body of a loop, and has one of the forms `break`, `break 'label` or ([see below](#break-and-loop-values)) `break EXPR` or `break 'label EXPR`.

r[expr.loop.break-value.implicit-value]
In a [`loop` with break expressions][expr.loop.break-value] or a [labeled block expression], a `break` without an expression is equivalent to `break ()`.

r[expr.loop.block-labels]
## Labeled block expressions

r[expr.loop.block-labels.syntax]
```grammar,expressions
LabelBlockExpression -> BlockExpression
```

r[expr.loop.block-labels.intro]
Labeled block expressions are exactly like block expressions, except that they allow using `break` expressions within the block.

r[expr.loop.block-labels.break]
Unlike loops, `break` expressions within a labeled block expression *must* have a label (i.e. the label is not optional).

r[expr.loop.block-labels.label-required]
Similarly, labeled block expressions *must* begin with a label.

```rust
# fn do_thing() {}
# fn condition_not_met() -> bool { true }
# fn do_next_thing() {}
# fn do_last_thing() {}
let result = 'block: {
    do_thing();
    if condition_not_met() {
        break 'block 1;
    }
    do_next_thing();
    if condition_not_met() {
        break 'block 2;
    }
    do_last_thing();
    3
};
```

r[expr.loop.block-labels.type]
The type of a labeled block expression is the [least upper bound] of all of the break operands and the final operand. If the final operand is omitted, the type of the final operand defaults to the [unit type], unless the block [diverges][expr.block.diverging], in which case it is the [never type].

> [!EXAMPLE]
> ```rust
> fn example(condition: bool) {
>     let s = String::from("owned");
>
>     let _: &str = 'block: {
>         if condition {
>             break 'block &s;  // &String coerced to &str via Deref
>         }
>         break 'block "literal";  // &'static str coerced to &str
>     };
> }
> ```

r[expr.loop.continue]
## `continue` expressions

r[expr.loop.continue.syntax]
```grammar,expressions
ContinueExpression -> `continue` LIFETIME_OR_LABEL?
```

r[expr.loop.continue.intro]
When `continue` is encountered, the current iteration of the associated loop body is immediately terminated, returning control to the loop *head*.

r[expr.loop.continue.diverging]
A `continue` expression is [diverging] and has a type of [`!`].

r[expr.loop.continue.while]
In the case of a `while` loop, the head is the conditional operands controlling the loop.

r[expr.loop.continue.for]
In the case of a `for` loop, the head is the call-expression controlling the loop.

r[expr.loop.continue.label]
Like `break`, `continue` is normally associated with the innermost enclosing loop, but `continue 'label` may be used to specify the loop affected.

r[expr.loop.continue.in-loop-only]
A `continue` expression is only permitted in the body of a loop.

r[expr.loop.break-value]
## `break` and loop values

r[expr.loop.break-value.intro]
When associated with a `loop`, a break expression may be used to return a value from that loop, via one of the forms `break EXPR` or `break 'label EXPR`, where `EXPR` is an expression whose result is returned from the `loop`. For example:

```rust
let (mut a, mut b) = (1, 1);
let result = loop {
    if b > 10 {
        break b;
    }
    let c = a + b;
    a = b;
    b = c;
};
// first number in Fibonacci sequence over 10:
assert_eq!(result, 13);
```

r[expr.loop.break-value.type]
The type of a `loop` with associated `break` expressions is the [least upper bound] of all of the break operands.

> [!EXAMPLE]
> ```rust
> fn example(condition: bool) {
>     let s = String::from("owned");
>
>     let _: &str = loop {
>         if condition {
>             break &s; // &String coerced to &str via Deref
>         }
>         break "literal"; // &'static str coerced to &str
>     };
> }
> ```

r[expr.loop.break-value.diverging]
A `loop` with associated `break` expressions does not [diverge] if any of the break operands do not diverge. If all of the `break` operands diverge, then the `loop` expression also diverges.

> [!EXAMPLE]
> ```rust
> fn diverging_loop_with_break(condition: bool) -> ! {
>     // This loop is diverging because all `break` operands are diverging.
>     loop {
>         if condition {
>             break loop {};
>         } else {
>             break panic!();
>         }
>     }
> }
> ```
>
> ```rust,compile_fail,E0308
> fn loop_with_non_diverging_break(condition: bool) -> ! {
>     // The type of this loop is i32 even though one of the breaks is
>     // diverging.
>     loop {
>         if condition {
>             break loop {};
>         } else {
>             break 123i32;
>         }
>     } // ERROR: expected `!`, found `i32`
> }
> ```

[`!`]: type.never
[`if` condition chains]: if-expr.md#chains-of-conditions
[`if` expressions]: if-expr.md
[`match` expression]: match-expr.md
[boolean type]: ../types/boolean.md
[diverge]: divergence
[diverging]: divergence
[labeled block expression]: expr.loop.block-labels
[least upper bound]: coerce.least-upper-bound
[never type]: type.never
[scrutinee]: ../glossary.md#scrutinee
[temporary values]: ../expressions.md#temporaries
[unit type]: type.tuple.unit


---

r[expr.range]
# Range expressions

r[expr.range.syntax]
```grammar,expressions
RangeExpression ->
      RangeExpr
    | RangeFromExpr
    | RangeToExpr
    | RangeFullExpr
    | RangeInclusiveExpr
    | RangeToInclusiveExpr

RangeExpr -> Expression `..` Expression

RangeFromExpr -> Expression `..`

RangeToExpr -> `..` Expression

RangeFullExpr -> `..`

RangeInclusiveExpr -> Expression `..=` Expression

RangeToInclusiveExpr -> `..=` Expression
```

r[expr.range.behavior]
The `..` and `..=` operators will construct an object of one of the `std::ops::Range` (or `core::ops::Range`) variants, according to the following table:

| Production             | Syntax        | Type                         | Range                 |
|------------------------|---------------|------------------------------|-----------------------|
| [RangeExpr]            | start`..`end  | [std::ops::Range]            | start &le; x &lt; end |
| [RangeFromExpr]        | start`..`     | [std::ops::RangeFrom]        | start &le; x          |
| [RangeToExpr]          | `..`end       | [std::ops::RangeTo]          |            x &lt; end |
| [RangeFullExpr]        | `..`          | [std::ops::RangeFull]        |            -          |
| [RangeInclusiveExpr]   | start`..=`end | [std::ops::RangeInclusive]   | start &le; x &le; end |
| [RangeToInclusiveExpr] | `..=`end      | [std::ops::RangeToInclusive] |            x &le; end |

Examples:

```rust
1..2;   // std::ops::Range
3..;    // std::ops::RangeFrom
..4;    // std::ops::RangeTo
..;     // std::ops::RangeFull
5..=6;  // std::ops::RangeInclusive
..=7;   // std::ops::RangeToInclusive
```

r[expr.range.equivalence]
The following expressions are equivalent.

```rust
let x = std::ops::Range {start: 0, end: 10};
let y = 0..10;

assert_eq!(x, y);
```

r[expr.range.for]
Ranges can be used in `for` loops:

```rust
for i in 1..11 {
    println!("{}", i);
}
```


---

r[expr.if]
# `if` expressions

r[expr.if.syntax]
```grammar,expressions
IfExpression ->
    `if` Conditions BlockExpression
    (`else` ( BlockExpression | IfExpression ) )?

Conditions ->
      Expression _except [StructExpression]_
    | LetChain

LetChain -> LetChainCondition ( `&&` LetChainCondition )*

LetChainCondition ->
      Expression _except [ExcludedConditions]_
    | OuterAttribute* `let` Pattern `=` Scrutinee _except [ExcludedConditions]_

@root ExcludedConditions ->
      StructExpression
    | LazyBooleanExpression
    | RangeExpr
    | RangeFromExpr
    | RangeInclusiveExpr
    | AssignmentExpression
    | CompoundAssignmentExpression
```
<!-- TODO: The struct exception above needs clarification, see https://github.com/rust-lang/reference/issues/1808
     The chain grammar could use some work, see https://github.com/rust-lang/reference/issues/1811
-->

r[expr.if.intro]
The syntax of an `if` expression is a sequence of one or more condition operands separated by `&&`, followed by a consequent block, any number of `else if` conditions and blocks, and an optional trailing `else` block.

r[expr.if.condition]
Condition operands must be either an [Expression] with a [boolean type] or a conditional `let` match.

r[expr.if.condition-true]
If all of the condition operands evaluate to `true` and all of the `let` patterns successfully match their [scrutinee]s, the consequent block is executed and any subsequent `else if` or `else` block is skipped.

r[expr.if.else-if]
If any condition operand evaluates to `false` or any `let` pattern does not match its scrutinee, the consequent block is skipped and any subsequent `else if` condition is evaluated.

r[expr.if.else]
If all `if` and `else if` conditions evaluate to `false` then any `else` block is executed.

r[expr.if.result]
An `if` expression evaluates to the same value as the executed block, or `()` if no block is evaluated.

r[expr.if.type]
An `if` expression must have the same type in all situations.

```rust
# let x = 3;
if x == 4 {
    println!("x is four");
} else if x == 3 {
    println!("x is three");
} else {
    println!("x is something else");
}

// `if` can be used as an expression.
let y = if 12 * 15 > 150 {
    "Bigger"
} else {
    "Smaller"
};
assert_eq!(y, "Bigger");
```

r[expr.if.diverging]
An `if` expression [diverges] if either the condition expression diverges or if all arms diverge.

```rust,no_run
fn diverging_condition() -> ! {
    // Diverges because the condition expression diverges
    if loop {} {
        ()
    } else {
        ()
    };
    // The semicolon above is important: The type of the `if` expression is
    // `()`, despite being diverging. When the final body expression is
    // elided, the type of the body is inferred to ! because the function body
    // diverges. Without the semicolon, the `if` would be the tail expression
    // with type `()`, which would fail to match the return type `!`.
}

fn diverging_arms() -> ! {
    // Diverges because all arms diverge
    if true {
        loop {}
    } else {
        loop {}
    }
}
```

r[expr.if.let]
## `if let` patterns

r[expr.if.let.intro]
`let` patterns in an `if` condition allow binding new variables into scope when the pattern matches successfully.

The following examples illustrate bindings using `let` patterns:

```rust
let dish = ("Ham", "Eggs");

// This body will be skipped because the pattern is refuted.
if let ("Bacon", b) = dish {
    println!("Bacon is served with {}", b);
} else {
    // This block is evaluated instead.
    println!("No bacon will be served");
}

// This body will execute.
if let ("Ham", b) = dish {
    println!("Ham is served with {}", b);
}

if let _ = 5 {
    println!("Irrefutable patterns are always true");
}
```

r[expr.if.let.or-pattern]
Multiple patterns may be specified with the `|` operator. This has the same semantics as with `|` in [`match` expressions]:

```rust
enum E {
    X(u8),
    Y(u8),
    Z(u8),
}
let v = E::Y(12);
if let E::X(n) | E::Y(n) = v {
    assert_eq!(n, 12);
}
```

r[expr.if.chains]
## Chains of conditions

r[expr.if.chains.intro]
Multiple condition operands can be separated with `&&`.

r[expr.if.chains.order]
Similar to a `&&` [LazyBooleanExpression], each operand is evaluated from left-to-right until an operand evaluates as `false` or a `let` match fails, in which case the subsequent operands are not evaluated.

r[expr.if.chains.bindings]
The bindings of each pattern are put into scope to be available for the next condition operand and the consequent block.

The following is an example of chaining multiple expressions, mixing `let` bindings and boolean expressions, and with expressions able to reference pattern bindings from previous expressions:

```rust
fn single() {
    let outer_opt = Some(Some(1i32));

    if let Some(inner_opt) = outer_opt
        && let Some(number) = inner_opt
        && number == 1
    {
        println!("Peek a boo");
    }
}
```

The above is equivalent to the following without using chains of conditions:

```rust
fn nested() {
    let outer_opt = Some(Some(1i32));

    if let Some(inner_opt) = outer_opt {
        if let Some(number) = inner_opt {
            if number == 1 {
                println!("Peek a boo");
            }
        }
    }
}
```

r[expr.if.chains.or]
If any condition operand is a `let` pattern, then none of the condition operands can be a `||` [lazy boolean operator expression][expr.bool-logic] due to ambiguity and precedence with the `let` scrutinee. If a `||` expression is needed, then parentheses can be used. For example:

```rust
# let foo = Some(123);
# let condition1 = true;
# let condition2 = false;
// Parentheses are required here.
if let Some(x) = foo && (condition1 || condition2) { /*...*/ }
```

r[expr.if.edition2024]
> [!EDITION-2024]
> Before the 2024 edition, let chains are not supported. That is, the [LetChain] grammar is not allowed in an `if` expression.

[`match` expressions]: match-expr.md
[boolean type]: ../types/boolean.md
[diverges]: divergence
[scrutinee]: ../glossary.md#scrutinee


---

r[expr.match]
# `match` expressions

r[expr.match.syntax]
```grammar,expressions
MatchExpression ->
    `match` Scrutinee `{`
        InnerAttribute*
        MatchArms?
    `}`

Scrutinee -> Expression _except [StructExpression]_

MatchArms ->
    ( MatchArm `=>` ( ExpressionWithoutBlock `,` | ExpressionWithBlock `,`? ) )*
    MatchArm `=>` Expression `,`?

MatchArm -> OuterAttribute* Pattern MatchArmGuard?

MatchArmGuard -> `if` MatchConditions

MatchConditions ->
     MatchGuardChain
   | Expression

MatchGuardChain -> MatchGuardCondition ( `&&` MatchGuardCondition )*

MatchGuardCondition ->
     Expression _except [ExcludedMatchConditions]_
   | OuterAttribute* `let` Pattern `=` MatchGuardScrutinee

MatchGuardScrutinee -> Expression _except [ExcludedMatchConditions]_

@root ExcludedMatchConditions ->
      LazyBooleanExpression
    | RangeExpr
    | RangeFromExpr
    | RangeInclusiveExpr
    | AssignmentExpression
    | CompoundAssignmentExpression
```
<!-- TODO: The exception above isn't accurate, see https://github.com/rust-lang/reference/issues/569 -->

r[expr.match.intro]
A *`match` expression* branches on a pattern. The exact form of matching that occurs depends on the [pattern].

r[expr.match.scrutinee]
A `match` expression has a *[scrutinee] expression*, which is the value to compare to the patterns.

r[expr.match.scrutinee-constraint]
The scrutinee expression and the patterns must have the same type.

r[expr.match.scrutinee-behavior]
A `match` behaves differently depending on whether or not the scrutinee expression is a [place expression or value expression][place expression].

r[expr.match.scrutinee-value]
If the scrutinee expression is a [value expression], it is first evaluated into a temporary location, and the resulting value is sequentially compared to the patterns in the arms until a match is found. The first arm with a matching pattern is chosen as the branch target of the `match`, any variables bound by the pattern are assigned to local variables in the arm's block, and control enters the block.

r[expr.match.scrutinee-place]
When the scrutinee expression is a [place expression], the match does not allocate a temporary location; however, a by-value binding may copy or move from the memory location. When possible, it is preferable to match on place expressions, as the lifetime of these matches inherits the lifetime of the place expression rather than being restricted to the inside of the match.

An example of a `match` expression:

```rust
let x = 1;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3 => println!("three"),
    4 => println!("four"),
    5 => println!("five"),
    _ => println!("something else"),
}
```

r[expr.match.pattern-vars]
Variables bound within the pattern are scoped to the match guard and the arm's expression.

r[expr.match.pattern-var-binding]
The [binding mode] (move, copy, or reference) depends on the pattern.

r[expr.match.or-pattern]
Multiple match patterns may be joined with the `|` operator. Each pattern will be tested in left-to-right sequence until a successful match is found.

```rust
let x = 9;
let message = match x {
    0 | 1  => "not many",
    2 ..= 9 => "a few",
    _      => "lots"
};

assert_eq!(message, "a few");

// Demonstration of pattern match order.
struct S(i32, i32);

match S(1, 2) {
    S(z @ 1, _) | S(_, z @ 2) => assert_eq!(z, 1),
    _ => panic!(),
}
```

> [!NOTE]
> The `2..=9` is a [Range Pattern], not a [Range Expression]. Thus, only those types of ranges supported by range patterns can be used in match arms.

r[expr.match.or-patterns-restriction]
Every binding in each `|` separated pattern must appear in all of the patterns in the arm.

r[expr.match.binding-restriction]
Every binding of the same name must have the same type, and have the same binding mode.

r[expr.match.type]
The type of the overall `match` expression is the [least upper bound] of the individual match arms.

r[expr.match.empty]
If there are no match arms, then the `match` expression is [diverging] and the type is [`!`].

> [!EXAMPLE]
> ```rust
> # fn make<T>() -> T { loop {} }
> enum Empty {}
>
> fn diverging_match_no_arms() -> ! {
>     let e: Empty = make();
>     match e {}
> }
> ```


r[expr.match.diverging]
If either the scrutinee expression or all of the match arms diverge, then the entire `match` expression also diverges.

r[expr.match.guard]
## Match guards

r[expr.match.guard.intro]
Match arms can accept _match guards_ to further refine the criteria for matching a case.

r[expr.match.guard.condition]
Pattern guards appear after the pattern following the `if` keyword and consist of an [Expression] with a [boolean type][type.bool] or a conditional `let` match.

r[expr.match.guard.behavior]
When the pattern matches successfully, the pattern guard is executed. If all of the guard condition operands evaluate to `true` and all of the `let` patterns successfully match their [scrutinee]s, the match arm is successfully matched against and the arm body is executed.

r[expr.match.guard.next]
Otherwise, the next pattern, including other matches with the `|` operator in the same arm, is tested.

```rust
# let maybe_digit = Some(0);
# fn process_digit(i: i32) { }
# fn process_other(i: i32) { }
let message = match maybe_digit {
    Some(x) if x < 10 => process_digit(x),
    Some(x) => process_other(x),
    None => panic!(),
};
```

> [!NOTE]
> Multiple matches using the `|` operator can cause the pattern guard and the side effects it has to execute multiple times. For example:
>
> ```rust
> # use std::cell::Cell;
> let i : Cell<i32> = Cell::new(0);
> match 1 {
>     1 | _ if { i.set(i.get() + 1); false } => {}
>     _ => {}
> }
> assert_eq!(i.get(), 2);
> ```

r[expr.match.guard.bound-variables]
A pattern guard may refer to the variables bound within the pattern they follow.

r[expr.match.guard.shared-ref]
Before evaluating the guard, a shared reference is taken to the part of the scrutinee the variable matches on. While evaluating the guard, this shared reference is then used when accessing the variable.

r[expr.match.guard.value]
Only when the guard evaluates successfully is the value moved, or copied, from the scrutinee into the variable. This allows shared borrows to be used inside guards without moving out of the scrutinee in case guard fails to match.

r[expr.match.guard.no-mutation]
Moreover, by holding a shared reference while evaluating the guard, mutation inside guards is also prevented.

r[expr.match.guard.let]
Guards can use `let` patterns to conditionally match a scrutinee and to bind new variables into scope when the pattern matches successfully.

> [!EXAMPLE]
> In this example, the guard condition `let Some(first_char) = name.chars().next()` is evaluated. If the `let` pattern successfully matches (i.e. the string has at least one character), the arm's body is executed. Otherwise, pattern matching continues to the next arm.
>
> The `let` pattern creates a new binding (`first_char`), which can be used alongside the original pattern bindings (`name`) in the arm's body.
> ```rust
> # enum Command {
> #     Run(String),
> #     Stop,
> # }
> let cmd = Command::Run("example".to_string());
>
> match cmd {
>     Command::Run(name) if let Some(first_char) = name.chars().next() => {
>         // Both `name` and `first_char` are available here
>         println!("Running: {name} (starts with '{first_char}')");
>     }
>     Command::Run(name) => {
>         println!("{name} is empty");
>     }
>     _ => {}
> }
> ```

r[expr.match.guard.chains]
## Match guard chains

r[expr.match.guard.chains.intro]
Multiple guard condition operands can be separated with `&&`.

> [!EXAMPLE]
> ```rust
> # let foo = Some([123]);
> # let already_checked = false;
> match foo {
>     Some(xs) if let [single] = xs && !already_checked => { dbg!(single); }
>     _ => {}
> }
> ```

r[expr.match.guard.chains.order]
Similar to a `&&` [LazyBooleanExpression], each operand is evaluated from left-to-right until an operand evaluates as `false` or a `let` match fails, in which case the subsequent operands are not evaluated.

r[expr.match.guard.chains.bindings]
The bindings of each `let` pattern are put into scope to be available for the next condition operand and the match arm body.

r[expr.match.guard.chains.or]
If any guard condition operand is a `let` pattern, then none of the condition operands can be a `||` [lazy boolean operator expression][expr.bool-logic] due to ambiguity and precedence with the `let` scrutinee.

> [!EXAMPLE]
> If a `||` expression is needed, then parentheses can be used. For example:
>
> ```rust
> # let foo = Some([123]);
> match foo {
>     // Parentheses are required here.
>     Some(xs) if let [x] = xs && (x < -100 || x > 20) => {}
>     _ => {}
> }
> ```

r[expr.match.attributes]
## Attributes on match arms

r[expr.match.attributes.outer]
Outer attributes are allowed on match arms. The only attributes that have meaning on match arms are [`cfg`] and the [lint check attributes].

r[expr.match.attributes.inner]
[Inner attributes] are allowed directly after the opening brace of the match expression in the same expression contexts as [attributes on block expressions].

[`!`]: type.never
[`cfg`]: ../conditional-compilation.md
[attributes on block expressions]: block-expr.md#attributes-on-block-expressions
[binding mode]: ../patterns.md#binding-modes
[diverging]: divergence
[Inner attributes]: ../attributes.md
[least upper bound]: coerce.least-upper-bound
[lint check attributes]: ../attributes/diagnostics.md#lint-check-attributes
[pattern]: ../patterns.md
[place expression]: ../expressions.md#place-expressions-and-value-expressions
[Range Expression]: range-expr.md
[Range Pattern]: ../patterns.md#range-patterns
[scrutinee]: ../glossary.md#scrutinee
[value expression]: ../expressions.md#place-expressions-and-value-expressions


---

r[expr.return]
# `return` expressions

r[expr.return.syntax]
```grammar,expressions
ReturnExpression -> `return` Expression?
```

r[expr.return.intro]
Return expressions are denoted with the keyword `return`.

r[expr.return.behavior]
Evaluating a `return` expression moves its argument into the designated output location for the current function call, destroys the current function activation frame, and transfers control to the caller frame.

r[expr.return.diverging]
A `return` expression is [diverging] and has a type of [`!`].

An example of a `return` expression:

```rust
fn max(a: i32, b: i32) -> i32 {
    if a > b {
        return a;
    }
    return b;
}
```

[`!`]: type.never
[diverging]: divergence


---

r[expr.await]
# Await expressions

r[expr.await.syntax]
```grammar,expressions
AwaitExpression -> Expression `.` `await`
```

r[expr.await.intro]
An `await` expression is a syntactic construct for suspending a computation provided by an implementation of `std::future::IntoFuture` until the given future is ready to produce a value.

r[expr.await.construct]
The syntax for an await expression is an expression with a type that implements the [`IntoFuture`] trait, called the *future operand*, then the token `.`, and then the `await` keyword.

r[expr.await.allowed-positions]
Await expressions are legal only within an [async context], like an [`async fn`], [`async` closure], or [`async` block].

r[expr.await.effects]
More specifically, an await expression has the following effect.

1. Create a future by calling [`IntoFuture::into_future`] on the future operand.
2. Evaluate the future to a [future] `tmp`;
3. Pin `tmp` using [`Pin::new_unchecked`];
4. This pinned future is then polled by calling the [`Future::poll`] method and passing it the current [task context](#task-context);
5. If the call to `poll` returns [`Poll::Pending`], then the future returns `Poll::Pending`, suspending its state so that, when the surrounding async context is re-polled, execution returns to step 3;
6. Otherwise the call to `poll` must have returned [`Poll::Ready`], in which case the value contained in the [`Poll::Ready`] variant is used as the result of the `await` expression itself.

r[expr.await.edition2018]
> [!EDITION-2018]
> Await expressions are only available beginning with Rust 2018.

r[expr.await.task]
## Task context

The task context refers to the [`Context`] which was supplied to the current [async context] when the async context itself was polled. Because `await` expressions are only legal in an async context, there must be some task context available.

r[expr.await.desugar]
## Approximate desugaring

Effectively, an await expression is roughly equivalent to the following non-normative desugaring:

<!-- ignore: example expansion -->
```rust,ignore
match operand.into_future() {
    mut pinned => loop {
        let mut pin = unsafe { Pin::new_unchecked(&mut pinned) };
        match Pin::future::poll(Pin::borrow(&mut pin), &mut current_context) {
            Poll::Ready(r) => break r,
            Poll::Pending => yield Poll::Pending,
        }
    }
}
```

where the `yield` pseudo-code returns `Poll::Pending` and, when re-invoked, resumes execution from that point. The variable `current_context` refers to the context taken from the async environment.

[`async fn`]: ../items/functions.md#async-functions
[`async` closure]: closure-expr.md#async-closures
[`async` block]: block-expr.md#async-blocks
[`Context`]: std::task::Context
[`future::poll`]: std::future::Future::poll
[`pin::new_unchecked`]: std::pin::Pin::new_unchecked
[`poll::Pending`]: std::task::Poll::Pending
[`poll::Ready`]: std::task::Poll::Ready
[async context]: ../expressions/block-expr.md#async-context
[future]: std::future::Future
[`IntoFuture`]: std::future::IntoFuture
[`IntoFuture::into_future`]: std::future::IntoFuture::into_future


---

r[expr.placeholder]
# `_` expressions

r[expr.placeholder.syntax]
```grammar,expressions
UnderscoreExpression -> `_`
```

r[expr.placeholder.intro]
Underscore expressions, denoted with the symbol `_`, are used to signify a placeholder in a destructuring assignment.

r[expr.placeholder.lhs-assignment-only]
They may only appear in the left-hand side of an assignment.

r[expr.placeholder.pattern]
Note that this is distinct from the [wildcard pattern](../patterns.md#wildcard-pattern).

Examples of `_` expressions:

```rust
let p = (1, 2);
let mut a = 0;
(_, a) = p;

struct Position {
    x: u32,
    y: u32,
}

Position { x: a, y: _ } = Position{ x: 2, y: 3 };

// unused result, assignment to `_` used to declare intent and remove a warning
_ = 2 + 2;
// triggers unused_must_use warning
// 2 + 2;

// equivalent technique using a wildcard pattern in a let-binding
let _ = 2 + 2;
```
