# Lexical structure

<!-- Editor Note: Oh, there's nothing here -->


---

r[input]
# Input format

r[input.syntax]
```grammar,lexer
CHAR -> [U+0000-U+D7FF U+E000-U+10FFFF] // a Unicode scalar value

ASCII -> [U+0000-U+007F]

NUL -> U+0000

EOF -> !CHAR  // End of file or input
```

r[input.intro]
This chapter describes how a source file is interpreted as a sequence of tokens.

See [Crates and source files] for a description of how programs are organised into files.

r[input.encoding]
## Source encoding

r[input.encoding.utf8]
Each source file is interpreted as a sequence of Unicode characters encoded in UTF-8.

r[input.encoding.invalid]
It is an error if the file is not valid UTF-8.

r[input.byte-order-mark]
## Byte order mark removal

If the first character in the sequence is `U+FEFF` ([BYTE ORDER MARK]), it is removed.

r[input.crlf]
## CRLF normalization

Each pair of characters `U+000D` (CR) immediately followed by `U+000A` (LF) is replaced by a single `U+000A` (LF). This happens once, not repeatedly, so after the normalization, there can still exist `U+000D` (CR) immediately followed by `U+000A` (LF) in the input (e.g. if the raw input contained "CR CR LF LF").

Other occurrences of the character `U+000D` (CR) are left in place (they are treated as [whitespace]).

r[input.shebang]
## Shebang removal

r[input.shebang.removal]
If a [shebang] is present, it is removed from the input sequence (and is therefore ignored).

r[input.tokenization]
## Tokenization

The resulting sequence of characters is then converted into tokens as described in the remainder of this chapter.

> [!NOTE]
> The standard library [`include!`] macro applies the following transformations to the file it reads:
>
> - Byte order mark removal.
> - CRLF normalization.
> - Shebang removal when invoked in an item context (as opposed to expression or statement contexts).
>
> The [`include_str!`] and [`include_bytes!`] macros do not apply these transformations.

[BYTE ORDER MARK]: https://en.wikipedia.org/wiki/Byte_order_mark#UTF-8
[Crates and source files]: crates-and-source-files.md
[shebang]: shebang.md
[whitespace]: whitespace.md


---

r[shebang]
# Shebang

r[shebang.intro]
A *[shebang]* is an optional line that is typically used in Unix-like systems to specify an interpreter for executing the file.

> [!EXAMPLE]
> <!-- ignore: tests don't like shebang -->
> ```rust,ignore
> #!/usr/bin/env rustx
>
> fn main() {
>     println!("Hello!");
> }
> ```

r[shebang.syntax]
```grammar,lexer
@root SHEBANG ->
    `#!` !((WHITESPACE | LINE_COMMENT | BLOCK_COMMENT)* `[`)
    ~LF* (LF | EOF)
```

r[shebang.syntax-description]
The shebang starts with the characters `#!` and extends through the first `U+000A` (LF) or through EOF if no LF is present. If the `#!` characters are followed by `[` (ignoring any intervening [comments] or [whitespace]), the line is not considered a shebang (to avoid ambiguity with an [inner attribute]).

r[shebang.position]
The shebang may appear immediately at the start of the file or after the optional [byte order mark].

[byte order mark]: https://en.wikipedia.org/wiki/Byte_order_mark#UTF-8
[comments]: comments.md
[inner attribute]: attributes.md
[shebang]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[whitespace]: whitespace.md


---

r[lex.keywords]
# Keywords

Rust divides keywords into three categories:

* [strict](#strict-keywords)
* [reserved](#reserved-keywords)
* [weak](#weak-keywords)

r[lex.keywords.strict]
## Strict keywords

r[lex.keywords.strict.intro]
These keywords can only be used in their correct contexts. They cannot be used as the names of:

* [Items]
* [Variables] and function parameters
* Fields and [variants]
* [Type parameters]
* Lifetime parameters or [loop labels]
* [Macros] or [attributes]
* [Macro placeholders]
* [Crates]

r[lex.keywords.strict.list]
The following keywords are in all editions:

- `_`
- `as`
- `async`
- `await`
- `break`
- `const`
- `continue`
- `crate`
- `dyn`
- `else`
- `enum`
- `extern`
- `false`
- `fn`
- `for`
- `if`
- `impl`
- `in`
- `let`
- `loop`
- `match`
- `mod`
- `move`
- `mut`
- `pub`
- `ref`
- `return`
- `self`
- `Self`
- `static`
- `struct`
- `super`
- `trait`
- `true`
- `type`
- `unsafe`
- `use`
- `where`
- `while`

r[lex.keywords.strict.edition2018]
> [!EDITION-2018]
> The following keywords were added in the 2018 edition:
>
> - `async`
> - `await`
> - `dyn`

r[lex.keywords.reserved]
## Reserved keywords

r[lex.keywords.reserved.intro]
These keywords aren't used yet, but they are reserved for future use. They have the same restrictions as strict keywords. The reasoning behind this is to make current programs forward compatible with future versions of Rust by forbidding them to use these keywords.

r[lex.keywords.reserved.list]
- `abstract`
- `become`
- `box`
- `do`
- `final`
- `gen`
- `macro`
- `override`
- `priv`
- `try`
- `typeof`
- `unsized`
- `virtual`
- `yield`

r[lex.keywords.reserved.edition2018]
> [!EDITION-2018]
> The `try` keyword was added as a reserved keyword in the 2018 edition.

r[lex.keywords.reserved.edition2024]
> [!EDITION-2024]
> The `gen` keyword was added as a reserved keyword in the 2024 edition.

r[lex.keywords.weak]
## Weak keywords

r[lex.keywords.weak.intro]
These keywords have special meaning only in certain contexts. For example, it is possible to declare a variable or method with the name `union`.

- `'static`
- `macro_rules`
- `raw`
- `safe`
- `union`

r[lex.keywords.weak.macro_rules]
* `macro_rules` is used to create custom [macros].

r[lex.keywords.weak.union]
* `union` is used to declare a [union] and is only a keyword when used in a union declaration.

r[lex.keywords.weak.lifetime-static]
* `'static` is used for the static lifetime and cannot be used as a [generic lifetime parameter] or [loop label]

  ```compile_fail
  // error[E0262]: invalid lifetime parameter name: `'static`
  fn invalid_lifetime_parameter<'static>(s: &'static str) -> &'static str { s }
  ```

r[lex.keywords.weak.safe]
* `safe` is used for functions and statics, which has meaning in [external blocks].

r[lex.keywords.weak.raw]
* `raw` is used for [raw borrow operators], and is only a keyword when matching a raw borrow operator form (such as `&raw const expr` or `&raw mut expr`).

r[lex.keywords.weak.dyn.edition2018]
> [!EDITION-2018]
> In the 2015 edition, [`dyn`] is a keyword when used in a type position followed by a path that does not start with `::` or `<`, a lifetime, a question mark, a `for` keyword or an opening parenthesis.
>
> Beginning in the 2018 edition, `dyn` has been promoted to a strict keyword.

[items]: items.md
[Variables]: variables.md
[Type parameters]: types/parameters.md
[loop labels]: expressions/loop-expr.md#loop-labels
[Macros]: macros.md
[attributes]: attributes.md
[Macro placeholders]: macros-by-example.md
[Crates]: crates-and-source-files.md
[union]: items/unions.md
[variants]: items/enumerations.md
[`dyn`]: types/trait-object.md
[loop label]: expressions/loop-expr.md#loop-labels
[generic lifetime parameter]: items/generics.md
[external blocks]: items/external-blocks.md
[raw borrow operators]: expressions/operator-expr.md#raw-borrow-operators


---

r[ident]
# Identifiers

r[ident.syntax]
```grammar,lexer
IDENTIFIER_OR_KEYWORD -> ( XID_Start | `_` ) XID_Continue*

XID_Start -> <`XID_Start` defined by Unicode>

XID_Continue -> <`XID_Continue` defined by Unicode>

RAW_IDENTIFIER -> `r#` IDENTIFIER_OR_KEYWORD

NON_KEYWORD_IDENTIFIER -> IDENTIFIER_OR_KEYWORD _except a [strict][lex.keywords.strict] or [reserved][lex.keywords.reserved] keyword_

IDENTIFIER -> NON_KEYWORD_IDENTIFIER | RAW_IDENTIFIER

RESERVED_RAW_IDENTIFIER ->
    `r#` (`_` | `crate` | `self` | `Self` | `super`) !XID_Continue
```

<!-- When updating the version, update the UAX links, too. -->
r[ident.unicode]
Identifiers follow the specification in [Unicode Standard Annex #31][UAX31] for Unicode version 17.0, with the additions described below. Some examples of identifiers:

* `foo`
* `_identifier`
* `r#true`
* `Москва`
* `東京`

r[ident.profile]
The profile used from UAX #31 is:

* Start := [`XID_Start`], plus the underscore character (U+005F)
* Continue := [`XID_Continue`]
* Medial := empty

> [!NOTE]
> Identifiers starting with an underscore are typically used to indicate an identifier that is intentionally unused, and will silence the unused warning in `rustc`.

r[ident.keyword]
Identifiers may not be a [strict] or [reserved] keyword without the `r#` prefix described below in [raw identifiers](#raw-identifiers).

r[ident.zero-width-chars]
Zero width non-joiner (ZWNJ U+200C) and zero width joiner (ZWJ U+200D) characters are not allowed in identifiers.

r[ident.ascii-limitations]
Identifiers are restricted to the ASCII subset of [`XID_Start`] and [`XID_Continue`] in the following situations:

* [`extern crate`] declarations (except the [AsClause] identifier)
* External crate names referenced in a [path]
* [Module] names loaded from the filesystem without a [`path` attribute]
* [`no_mangle`] attributed items
* Item names in [external blocks]

r[ident.normalization]
## Normalization

Identifiers are normalized using Normalization Form C (NFC) as defined in [Unicode Standard Annex #15][UAX15]. Two identifiers are equal if their NFC forms are equal.

[Procedural][proc-macro] and [declarative][mbe] macros receive normalized identifiers in their input.

r[ident.raw]
## Raw identifiers

r[ident.raw.intro]
A raw identifier is like a normal identifier, but prefixed by `r#`. (Note that the `r#` prefix is not included as part of the actual identifier.)

r[ident.raw.allowed]
Unlike a normal identifier, a raw identifier may be any strict or reserved keyword except the ones listed above for `RAW_IDENTIFIER`.

r[ident.raw.reserved]
It is an error to use the [RESERVED_RAW_IDENTIFIER] token.

[`extern crate`]: items/extern-crates.md
[`no_mangle`]: abi.md#the-no_mangle-attribute
[`path` attribute]: items/modules.md#the-path-attribute
[`XID_Continue`]: http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Continue%3A%5D&abb=on&g=&i=
[`XID_Start`]:  http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Start%3A%5D&abb=on&g=&i=
[external blocks]: items/external-blocks.md
[mbe]: macros-by-example.md
[module]: items/modules.md
[path]: paths.md
[proc-macro]: procedural-macros.md
[reserved]: keywords.md#reserved-keywords
[strict]: keywords.md#strict-keywords
[UAX15]: https://www.unicode.org/reports/tr15/tr15-57.html
[UAX31]: https://www.unicode.org/reports/tr31/tr31-43.html


---

r[comments]
# Comments

r[comments.syntax]
```grammar,lexer
@root COMMENT ->
      LINE_COMMENT
    | INNER_LINE_DOC
    | OUTER_LINE_DOC
    | INNER_BLOCK_DOC
    | OUTER_BLOCK_DOC
    | BLOCK_COMMENT

LINE_COMMENT ->
      `//` (~[`/` `!` LF] | `//`) ~LF*
    | `//` EOF
    | `//` _immediately followed by LF_

BLOCK_COMMENT ->
    `/*` ^
      ( BLOCK_COMMENT_OR_DOC | (!`*/` CHAR) )*
    `*/`

INNER_LINE_DOC ->
    `//!` ^ LINE_DOC_COMMENT_CONTENT (LF | EOF)

LINE_DOC_COMMENT_CONTENT -> (!CR ~LF)*

INNER_BLOCK_DOC ->
    `/*!` ^ ( BLOCK_COMMENT_OR_DOC | BLOCK_CHAR )* `*/`

OUTER_LINE_DOC ->
    `///` ^ LINE_DOC_COMMENT_CONTENT (LF | EOF)

OUTER_BLOCK_DOC ->
    `/**` ![`*` `/`]
      ^
      ( ~`*` | BLOCK_COMMENT_OR_DOC )
      ( BLOCK_COMMENT_OR_DOC | BLOCK_CHAR )*
    `*/`

BLOCK_CHAR -> (!(`*/` | CR) CHAR)

BLOCK_COMMENT_OR_DOC ->
      INNER_BLOCK_DOC
    | OUTER_BLOCK_DOC
    | BLOCK_COMMENT
```

r[comments.normal]
## Non-doc comments

Comments follow the general C++ style of line (`//`) and block (`/* ... */`) comment forms. Nested block comments are supported.

r[comments.normal.tokenization]
Non-doc comments are interpreted as a form of whitespace.

r[comments.doc]
## Doc comments

r[comments.doc.syntax]
Line doc comments beginning with exactly _three_ slashes (`///`), and block doc comments (`/** ... */`), both outer doc comments, are interpreted as a special syntax for [`doc` attributes].

r[comments.doc.attributes]
That is, they are equivalent to writing `#[doc="..."]` around the body of the comment, i.e., `/// Foo` turns into `#[doc=" Foo"]` and `/** Bar */` turns into `#[doc=" Bar "]`. They must therefore appear before something that accepts an outer attribute.

r[comments.doc.inner-syntax]
Line comments beginning with `//!` and block comments `/*! ... */` are doc comments that apply to the parent of the comment, rather than the item that follows.

r[comments.doc.inner-attributes]
That is, they are equivalent to writing `#![doc="..."]` around the body of the comment. `//!` comments are usually used to document modules that occupy a source file.

r[comments.doc.bare-crs]
The character `U+000D` (CR) is not allowed in doc comments.

> [!NOTE]
> It is conventional for doc comments to contain Markdown, as expected by `rustdoc`. However, the comment syntax does not respect any internal Markdown. ``/** `glob = "*/*.rs";` */`` terminates the comment at the first `*/`, and the remaining code would cause a syntax error. This slightly limits the content of block doc comments compared to line doc comments.

> [!NOTE]
> The sequence `U+000D` (CR) immediately followed by `U+000A` (LF) would have been previously transformed into a single `U+000A` (LF).

## Examples

```rust
//! A doc comment that applies to the implicit anonymous module of this crate

pub mod outer_module {

    //!  - Inner line doc
    //!! - Still an inner line doc (but with a bang at the beginning)

    /*!  - Inner block doc */
    /*!! - Still an inner block doc (but with a bang at the beginning) */

    //   - Only a comment
    ///  - Outer line doc (exactly 3 slashes)
    //// - Only a comment

    /*   - Only a comment */
    /**  - Outer block doc (exactly) 2 asterisks */
    /*** - Only a comment */

    pub mod inner_module {}

    pub mod nested_comments {
        /* In Rust /* we can /* nest comments */ */ */

        // All three types of block comments can contain or be nested inside
        // any other type:

        /*   /* */  /** */  /*! */  */
        /*!  /* */  /** */  /*! */  */
        /**  /* */  /** */  /*! */  */
        pub mod dummy_item {}
    }

    pub mod degenerate_cases {
        // empty inner line doc
        //!

        // empty inner block doc
        /*!*/

        // empty line comment
        //

        // empty outer line doc
        ///

        // empty block comment
        /**/

        pub mod dummy_item {}

        // empty 2-asterisk block isn't a doc block, it is a block comment
        /***/

    }

    /* The next one isn't allowed because outer doc comments
       require an item that will receive the doc */

    /// Where is my item?
#   mod boo {}
}
```

[`doc` attributes]: ../rustdoc/the-doc-attribute.html


---

r[lex.whitespace]
# Whitespace

r[whitespace.syntax]
```grammar,lexer
WHITESPACE ->
      U+0009 // Horizontal tab, `'\t'`
    | U+000A // Line feed, `'\n'`
    | U+000B // Vertical tab
    | U+000C // Form feed
    | U+000D // Carriage return, `'\r'`
    | U+0020 // Space, `' '`
    | U+0085 // Next line
    | U+200E // Left-to-right mark
    | U+200F // Right-to-left mark
    | U+2028 // Line separator
    | U+2029 // Paragraph separator

TAB -> U+0009 // Horizontal tab, `'\t'`

LF -> U+000A  // Line feed, `'\n'`

CR -> U+000D  // Carriage return, `'\r'`
```

r[lex.whitespace.intro]
Whitespace is any non-empty string containing only characters that have the [`Pattern_White_Space`] Unicode property.

r[lex.whitespace.token-sep]
Rust is a "free-form" language, meaning that all forms of whitespace serve only to separate _tokens_ in the grammar, and have no semantic significance.

r[lex.whitespace.replacement]
A Rust program has identical meaning if each whitespace element is replaced with any other legal whitespace element, such as a single space character.

[`Pattern_White_Space`]: https://www.unicode.org/reports/tr31/


---

r[lex.token]
# Tokens

r[lex.token.syntax]
```grammar,lexer
Token ->
      RESERVED_TOKEN
    | RAW_IDENTIFIER
    | CHAR_LITERAL
    | STRING_LITERAL
    | RAW_STRING_LITERAL
    | BYTE_LITERAL
    | BYTE_STRING_LITERAL
    | RAW_BYTE_STRING_LITERAL
    | C_STRING_LITERAL
    | RAW_C_STRING_LITERAL
    | FLOAT_LITERAL
    | INTEGER_LITERAL
    | LIFETIME_TOKEN
    | PUNCTUATION
    | IDENTIFIER_OR_KEYWORD
```

r[lex.token.intro]
Tokens are primitive productions in the grammar defined by regular (non-recursive) languages.  Rust source input can be broken down into the following kinds of tokens:

* [Keywords]
* [Identifiers][identifier]
* [Literals](#literals)
* [Lifetimes](#lifetimes-and-loop-labels)
* [Punctuation](#punctuation)
* [Delimiters](#delimiters)

Within this documentation's grammar, "simple" tokens are given in [string table production] form, and appear in `monospace` font.

[string table production]: notation.md#string-table-productions

r[lex.token.literal]
## Literals

Literals are tokens used in [literal expressions].

### Examples

#### Characters and strings

|                                              | Example         | `#`&nbsp;sets[^nsets] | Characters  | Escapes             |
|----------------------------------------------|-----------------|------------|-------------|---------------------|
| [Character](#character-literals)             | `'H'`           | 0          | All Unicode | [Quote](#quote-escapes) & [ASCII](#ascii-escapes) & [Unicode](#unicode-escapes) |
| [String](#string-literals)                   | `"hello"`       | 0          | All Unicode | [Quote](#quote-escapes) & [ASCII](#ascii-escapes) & [Unicode](#unicode-escapes) |
| [Raw string](#raw-string-literals)           | `r#"hello"#`    | <256       | All Unicode | `N/A`                                                      |
| [Byte](#byte-literals)                       | `b'H'`          | 0          | All ASCII   | [Quote](#quote-escapes) & [Byte](#byte-escapes)                               |
| [Byte string](#byte-string-literals)         | `b"hello"`      | 0          | All ASCII   | [Quote](#quote-escapes) & [Byte](#byte-escapes)                               |
| [Raw byte string](#raw-byte-string-literals) | `br#"hello"#`   | <256       | All ASCII   | `N/A`                                                      |
| [C string](#c-string-literals)               | `c"hello"`      | 0          | All Unicode | [Quote](#quote-escapes) & [Byte](#byte-escapes) & [Unicode](#unicode-escapes)   |
| [Raw C string](#raw-c-string-literals)       | `cr#"hello"#`   | <256       | All Unicode | `N/A`                                                                           |

[^nsets]: The number of `#`s on each side of the same literal must be equivalent.


#### ASCII escapes

|   | Name |
|---|------|
| `\x41` | 7-bit character code (exactly 2 hex digits, up to 0x7F) |
| `\n` | Newline |
| `\r` | Carriage return |
| `\t` | Tab |
| `\\` | Backslash |
| `\0` | Null |

#### Byte escapes

|   | Name |
|---|------|
| `\x7F` | 8-bit character code (exactly 2 hex digits) |
| `\n` | Newline |
| `\r` | Carriage return |
| `\t` | Tab |
| `\\` | Backslash |
| `\0` | Null |

#### Unicode escapes

|   | Name |
|---|------|
| `\u{7FFF}` | 24-bit Unicode character code (up to 6 hex digits) |

#### Quote escapes

|   | Name |
|---|------|
| `\'` | Single quote |
| `\"` | Double quote |

#### Numbers

| [Number literals](#number-literals)[^nl] | Example | Exponentiation |
|----------------------------------------|---------|----------------|
| Decimal integer | `98_222` | `N/A` |
| Hex integer | `0xff` | `N/A` |
| Octal integer | `0o77` | `N/A` |
| Binary integer | `0b1111_0000` | `N/A` |
| Floating-point | `123.0E+77` | `Optional` |

[^nl]: All number literals allow `_` as a visual separator: `1_234.0E+18f64`

r[lex.token.literal.suffix]
#### Suffixes

r[lex.token.literal.literal.suffix.intro]
A suffix is a sequence of characters following (without intervening whitespace) the primary part of a literal of the same form as a non-raw identifier or keyword.

r[lex.token.literal.suffix.syntax]
```grammar,lexer
SUFFIX ->
      `_` ^ XID_Continue+
    | XID_Start XID_Continue*
```

r[lex.token.literal.suffix.validity]
Any kind of literal (string, integer, etc.) with any suffix is valid as a token.

A literal token with any suffix can be passed to a macro without producing an error. The macro itself will decide how to interpret such a token and whether to produce an error or not. In particular, the `literal` fragment specifier for by-example macros matches literal tokens with arbitrary suffixes.

```rust
macro_rules! blackhole { ($tt:tt) => () }
macro_rules! blackhole_lit { ($l:literal) => () }

blackhole!("string"suffix); // OK
blackhole_lit!(1suffix); // OK
```

r[lex.token.literal.suffix.parse]
However, suffixes on literal tokens which are interpreted as literal expressions or patterns are restricted. Any suffixes are rejected on non-numeric literal tokens, and numeric literal tokens are accepted only with suffixes from the list below.

| Integer | Floating-point |
|---------|----------------|
| `u8`, `i8`, `u16`, `i16`, `u32`, `i32`, `u64`, `i64`, `u128`, `i128`, `usize`, `isize` | `f32`, `f64` |

### Character and string literals

r[lex.token.literal.char]
#### Character literals

r[lex.token.literal.char.syntax]
```grammar,lexer
CHAR_LITERAL ->
    `'`
        ( ~[`'` `\` LF CR TAB] | QUOTE_ESCAPE | ASCII_ESCAPE | UNICODE_ESCAPE )
    `'` SUFFIX?

QUOTE_ESCAPE -> `\'` | `\"`

ASCII_ESCAPE ->
      `\x` OCT_DIGIT HEX_DIGIT
    | `\n` | `\r` | `\t` | `\\` | `\0`

UNICODE_ESCAPE ->
    `\u{` ( HEX_DIGIT `_`* ){1..=6} _valid hex char value_ `}`[^valid-hex-char]
```

[^valid-hex-char]: See [lex.token.literal.char-escape.unicode].

r[lex.token.literal.char.intro]
A _character literal_ is a single Unicode character enclosed within two `U+0027` (single-quote) characters, with the exception of `U+0027` itself, which must be _escaped_ by a preceding `U+005C` character (`\`).

r[lex.token.literal.str]
#### String literals

r[lex.token.literal.str.syntax]
```grammar,lexer
STRING_LITERAL ->
    `"` (
        ~[`"` `\` CR]
      | QUOTE_ESCAPE
      | ASCII_ESCAPE
      | UNICODE_ESCAPE
      | STRING_CONTINUE
    )* `"` SUFFIX?

STRING_CONTINUE -> `\` LF
```

r[lex.token.literal.str.intro]
A _string literal_ is a sequence of any Unicode characters enclosed within two `U+0022` (double-quote) characters, with the exception of `U+0022` itself, which must be _escaped_ by a preceding `U+005C` character (`\`).

r[lex.token.literal.str.linefeed]
Line-breaks, represented by the  character `U+000A` (LF), are allowed in string literals. The character `U+000D` (CR) may not appear in a string literal. When an unescaped `U+005C` character (`\`) occurs immediately before a line break, the line break does not appear in the string represented by the token. See [String continuation escapes] for details.

r[lex.token.literal.char-escape]
#### Character escapes

r[lex.token.literal.char-escape.intro]
Some additional _escapes_ are available in either character or non-raw string literals. An escape starts with a `U+005C` (`\`) and continues with one of the following forms:

r[lex.token.literal.char-escape.ascii]
* A _7-bit code point escape_ starts with `U+0078` (`x`) and is followed by exactly two _hex digits_ with value up to `0x7F`. It denotes the ASCII character with value equal to the provided hex value. Higher values are not permitted because it is ambiguous whether they mean Unicode code points or byte values.

r[lex.token.literal.char-escape.unicode]
* A _24-bit code point escape_ starts with `U+0075` (`u`) and is followed by up to six _hex digits_ surrounded by braces `U+007B` (`{`) and `U+007D` (`}`). It denotes the Unicode code point equal to the provided hex value. The value must be a valid Unicode scalar value.

r[lex.token.literal.char-escape.whitespace]
* A _whitespace escape_ is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the Unicode values `U+000A` (LF), `U+000D` (CR) or `U+0009` (HT) respectively.

r[lex.token.literal.char-escape.null]
* The _null escape_ is the character `U+0030` (`0`) and denotes the Unicode value `U+0000` (NUL).

r[lex.token.literal.char-escape.slash]
* The _backslash escape_ is the character `U+005C` (`\`) which must be escaped in order to denote itself.

r[lex.token.literal.str-raw]
#### Raw string literals

r[lex.token.literal.str-raw.syntax]
```grammar,lexer
RAW_STRING_LITERAL ->
      `r` `"` ^ RAW_STRING_CONTENT `"` SUFFIX?
    | `r` `#`{n:1..=255} ^ `"` RAW_STRING_CONTENT_HASHED `"` `#`{n} SUFFIX?

RAW_STRING_CONTENT -> (!`"` ~CR )*

RAW_STRING_CONTENT_HASHED -> (!(`"` `#`{n}) ~CR )*
```

r[lex.token.literal.str-raw.intro]
Raw string literals do not process any escapes. They start with the character `U+0072` (`r`), followed by fewer than 256 of the character `U+0023` (`#`) and a `U+0022` (double-quote) character.

r[lex.token.literal.str-raw.body]
The _raw string body_ can contain any sequence of Unicode characters other than `U+000D` (CR). It is terminated only by another `U+0022` (double-quote) character, followed by the same number of `U+0023` (`#`) characters that preceded the opening `U+0022` (double-quote) character.

r[lex.token.literal.str-raw.content]
All Unicode characters contained in the raw string body represent themselves, the characters `U+0022` (double-quote) (except when followed by at least as many `U+0023` (`#`) characters as were used to start the raw string literal) or `U+005C` (`\`) do not have any special meaning.

Examples for string literals:

```rust
"foo"; r"foo";                     // foo
"\"foo\""; r#""foo""#;             // "foo"

"foo #\"# bar";
r##"foo #"# bar"##;                // foo #"# bar

"\x52"; "R"; r"R";                 // R
"\\x52"; r"\x52";                  // \x52
```

### Byte and byte string literals

r[lex.token.byte]
#### Byte literals

r[lex.token.byte.syntax]
```grammar,lexer
BYTE_LITERAL ->
    `b'` ^ ( ASCII_FOR_CHAR | BYTE_ESCAPE )  `'` SUFFIX?

ASCII_FOR_CHAR -> ![`'` `\` LF CR TAB] ASCII

BYTE_ESCAPE ->
      `\x` HEX_DIGIT HEX_DIGIT
    | `\n` | `\r` | `\t` | `\\` | `\0` | `\'` | `\"`
```

r[lex.token.byte.intro]
A _byte literal_ is a single ASCII character (in the `U+0000` to `U+007F` range) or a single _escape_ preceded by the characters `U+0062` (`b`) and `U+0027` (single-quote), and followed by the character `U+0027`. If the character `U+0027` is present within the literal, it must be _escaped_ by a preceding `U+005C` (`\`) character. It is equivalent to a `u8` unsigned 8-bit integer _number literal_.

r[lex.token.str-byte]
#### Byte string literals

r[lex.token.str-byte.syntax]
```grammar,lexer
BYTE_STRING_LITERAL ->
    `b"` ^ ( ASCII_FOR_STRING | BYTE_ESCAPE | STRING_CONTINUE )* `"` SUFFIX?

ASCII_FOR_STRING -> ![`"` `\` CR] ASCII
```

r[lex.token.str-byte.intro]
A non-raw _byte string literal_ is a sequence of ASCII characters and _escapes_, preceded by the characters `U+0062` (`b`) and `U+0022` (double-quote), and followed by the character `U+0022`. If the character `U+0022` is present within the literal, it must be _escaped_ by a preceding `U+005C` (`\`) character. Alternatively, a byte string literal can be a _raw byte string literal_, defined below.

r[lex.token.str-byte.linefeed]
Line-breaks, represented by the  character `U+000A` (LF), are allowed in byte string literals. The character `U+000D` (CR) may not appear in a byte string literal. When an unescaped `U+005C` character (`\`) occurs immediately before a line break, the line break does not appear in the string represented by the token. See [String continuation escapes] for details.

r[lex.token.str-byte.escape]
Some additional _escapes_ are available in either byte or non-raw byte string literals. An escape starts with a `U+005C` (`\`) and continues with one of the following forms:

r[lex.token.str-byte.escape-byte]
* A _byte escape_ escape starts with `U+0078` (`x`) and is followed by exactly two _hex digits_. It denotes the byte equal to the provided hex value.

r[lex.token.str-byte.escape-whitespace]
* A _whitespace escape_ is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the bytes values `0x0A` (ASCII LF), `0x0D` (ASCII CR) or `0x09` (ASCII HT) respectively.

r[lex.token.str-byte.escape-null]
* The _null escape_ is the character `U+0030` (`0`) and denotes the byte value `0x00` (ASCII NUL).

r[lex.token.str-byte.escape-slash]
* The _backslash escape_ is the character `U+005C` (`\`) which must be escaped in order to denote its ASCII encoding `0x5C`.

r[lex.token.str-byte-raw]
#### Raw byte string literals

r[lex.token.str-byte-raw.syntax]
```grammar,lexer
RAW_BYTE_STRING_LITERAL ->
      `br` `"` ^ RAW_BYTE_STRING_CONTENT `"` SUFFIX?
    | `br` `#`{n:1..=255} ^ `"` RAW_BYTE_STRING_CONTENT_HASHED `"` `#`{n} SUFFIX?

RAW_BYTE_STRING_CONTENT -> (!`"` ASCII_FOR_RAW )*

RAW_BYTE_STRING_CONTENT_HASHED -> (!(`"` `#`{n}) ASCII_FOR_RAW )*

ASCII_FOR_RAW -> !CR ASCII
```

r[lex.token.str-byte-raw.intro]
Raw byte string literals do not process any escapes. They start with the character `U+0062` (`b`), followed by `U+0072` (`r`), followed by fewer than 256 of the character `U+0023` (`#`), and a `U+0022` (double-quote) character.

r[lex.token.str-byte-raw.body]
The _raw string body_ can contain any sequence of ASCII characters other than `U+000D` (CR). It is terminated only by another `U+0022` (double-quote) character, followed by the same number of `U+0023` (`#`) characters that preceded the opening `U+0022` (double-quote) character. A raw byte string literal can not contain any non-ASCII byte.

r[lex.token.literal.str-byte-raw.content]
All characters contained in the raw string body represent their ASCII encoding, the characters `U+0022` (double-quote) (except when followed by at least as many `U+0023` (`#`) characters as were used to start the raw string literal) or `U+005C` (`\`) do not have any special meaning.

Examples for byte string literals:

```rust
b"foo"; br"foo";                     // foo
b"\"foo\""; br#""foo""#;             // "foo"

b"foo #\"# bar";
br##"foo #"# bar"##;                 // foo #"# bar

b"\x52"; b"R"; br"R";                // R
b"\\x52"; br"\x52";                  // \x52
```

### C string and raw C string literals

r[lex.token.str-c]
#### C string literals

r[lex.token.str-c.syntax]
```grammar,lexer
C_STRING_LITERAL ->
    `c"` ^ (
        ~[`"` `\` CR NUL]
      | BYTE_ESCAPE _except `\0` or `\x00`_
      | UNICODE_ESCAPE _except `\u{0}`, `\u{00}`, …, `\u{000000}`_
      | STRING_CONTINUE
    )* `"` SUFFIX?
```

r[lex.token.str-c.intro]
A _C string literal_ is a sequence of Unicode characters and _escapes_, preceded by the characters `U+0063` (`c`) and `U+0022` (double-quote), and followed by the character `U+0022`. If the character `U+0022` is present within the literal, it must be _escaped_ by a preceding `U+005C` (`\`) character. Alternatively, a C string literal can be a _raw C string literal_, defined below.

[CStr]: core::ffi::CStr

r[lex.token.str-c.null]
C strings are implicitly terminated by byte `0x00`, so the C string literal `c""` is equivalent to manually constructing a `&CStr` from the byte string literal `b"\x00"`. Other than the implicit terminator, byte `0x00` is not permitted within a C string.

r[lex.token.str-c.linefeed]
Line-breaks, represented by the  character `U+000A` (LF), are allowed in C string literals. The character `U+000D` (CR) may not appear in a C string literal. When an unescaped `U+005C` character (`\`) occurs immediately before a line break, the line break does not appear in the string represented by the token. See [String continuation escapes] for details.

r[lex.token.str-c.escape]
Some additional _escapes_ are available in non-raw C string literals. An escape starts with a `U+005C` (`\`) and continues with one of the following forms:

r[lex.token.str-c.escape-byte]
* A _byte escape_ escape starts with `U+0078` (`x`) and is followed by exactly two _hex digits_. It denotes the byte equal to the provided hex value.

r[lex.token.str-c.escape-unicode]
* A _24-bit code point escape_ starts with `U+0075` (`u`) and is followed by up to six _hex digits_ surrounded by braces `U+007B` (`{`) and `U+007D` (`}`). It denotes the Unicode code point equal to the provided hex value, encoded as UTF-8.

r[lex.token.str-c.escape-whitespace]
* A _whitespace escape_ is one of the characters `U+006E` (`n`), `U+0072` (`r`), or `U+0074` (`t`), denoting the bytes values `0x0A` (ASCII LF), `0x0D` (ASCII CR) or `0x09` (ASCII HT) respectively.

r[lex.token.str-c.escape-slash]
* The _backslash escape_ is the character `U+005C` (`\`) which must be escaped in order to denote its ASCII encoding `0x5C`.

r[lex.token.str-c.char-unicode]
A C string represents bytes with no defined encoding, but a C string literal may contain Unicode characters above `U+007F`. Such characters will be replaced with the bytes of that character's UTF-8 representation.

The following C string literals are equivalent:

```rust
c"æ";        // LATIN SMALL LETTER AE (U+00E6)
c"\u{00E6}";
c"\xC3\xA6";
```

r[lex.token.str-c.edition2021]
> [!EDITION-2021]
> C string literals are accepted in the 2021 edition or later. In earlier editions the token `c""` is lexed as `c ""`.

r[lex.token.str-c-raw]
#### Raw C string literals

r[lex.token.str-c-raw.syntax]
```grammar,lexer
RAW_C_STRING_LITERAL ->
      `cr` `"` ^ RAW_C_STRING_CONTENT `"` SUFFIX?
    | `cr` `#`{n:1..=255} ^ `"` RAW_C_STRING_CONTENT_HASHED `"` `#`{n} SUFFIX?

RAW_C_STRING_CONTENT -> (!`"` ~[CR NUL] )*

RAW_C_STRING_CONTENT_HASHED -> (!(`"` `#`{n}) ~[CR NUL] )*
```

r[lex.token.str-c-raw.intro]
Raw C string literals do not process any escapes. They start with the character `U+0063` (`c`), followed by `U+0072` (`r`), followed by fewer than 256 of the character `U+0023` (`#`), and a `U+0022` (double-quote) character.

r[lex.token.str-c-raw.body]
The _raw C string body_ can contain any sequence of Unicode characters other than `U+0000` (NUL) and `U+000D` (CR). It is terminated only by another `U+0022` (double-quote) character, followed by the same number of `U+0023` (`#`) characters that preceded the opening `U+0022` (double-quote) character.

r[lex.token.str-c-raw.content]
All characters contained in the raw C string body represent themselves in UTF-8 encoding. The characters `U+0022` (double-quote) (except when followed by at least as many `U+0023` (`#`) characters as were used to start the raw C string literal) or `U+005C` (`\`) do not have any special meaning.

r[lex.token.str-c-raw.edition2021]
> [!EDITION-2021]
> Raw C string literals are accepted in the 2021 edition or later. In earlier editions the token `cr""` is lexed as `cr ""`, and `cr#""#` is lexed as `cr #""#` (which is non-grammatical).

#### Examples for C string and raw C string literals

```rust
c"foo"; cr"foo";                     // foo
c"\"foo\""; cr#""foo""#;             // "foo"

c"foo #\"# bar";
cr##"foo #"# bar"##;                 // foo #"# bar

c"\x52"; c"R"; cr"R";                // R
c"\\x52"; cr"\x52";                  // \x52
```

r[lex.token.literal.num]
### Number literals

A _number literal_ is either an _integer literal_ or a _floating-point literal_. The grammar for recognizing the two kinds of literals is mixed.

r[lex.token.literal.int]
#### Integer literals

r[lex.token.literal.int.syntax]
```grammar,lexer
INTEGER_LITERAL ->
    ( BIN_LITERAL | OCT_LITERAL | HEX_LITERAL | DEC_LITERAL )
    ^ !RESERVED_FLOAT SUFFIX?

DEC_LITERAL -> DEC_DIGIT (DEC_DIGIT|`_`)*

BIN_LITERAL -> `0b` ^ `_`* BIN_DIGIT (BIN_DIGIT|`_`)* ![`e` `E` `2`-`9`]

OCT_LITERAL -> `0o` ^ `_`* OCT_DIGIT (OCT_DIGIT|`_`)* ![`e` `E` `8`-`9`]

HEX_LITERAL -> `0x` ^ `_`* HEX_DIGIT (HEX_DIGIT|`_`)*

BIN_DIGIT -> [`0`-`1`]

OCT_DIGIT -> [`0`-`7`]

DEC_DIGIT -> [`0`-`9`]

HEX_DIGIT -> [`0`-`9` `a`-`f` `A`-`F`]

RESERVED_FLOAT -> `.` !(`.` | `_` | XID_Start)
```

r[lex.token.literal.int.kind]
An _integer literal_ has one of four forms:

r[lex.token.literal.int.kind-dec]
* A _decimal literal_ starts with a *decimal digit* and continues with any mixture of *decimal digits* and _underscores_.

r[lex.token.literal.int.kind-hex]
* A _hex literal_ starts with the character sequence `U+0030` `U+0078` (`0x`) and continues as any mixture (with at least one digit) of hex digits and underscores.

r[lex.token.literal.int.kind-oct]
* An _octal literal_ starts with the character sequence `U+0030` `U+006F` (`0o`) and continues as any mixture (with at least one digit) of octal digits and underscores.

r[lex.token.literal.int.kind-bin]
* A _binary literal_ starts with the character sequence `U+0030` `U+0062` (`0b`) and continues as any mixture (with at least one digit) of binary digits and underscores.

r[lex.token.literal.int.suffix]
Like any literal, an integer literal may be followed (immediately, without any spaces) by a suffix as described above. The suffix may not begin with `e` or `E`, as that would be interpreted as the exponent of a floating-point literal. See [Integer literal expressions] for the effect of these suffixes.

Examples of integer literals which are accepted as literal expressions:

```rust
# #![allow(overflowing_literals)]
123;
123i32;
123u32;
123_u32;

0xff;
0xff_u8;
0x01_f32; // integer 7986, not floating-point 1.0
0x01_e3;  // integer 483, not floating-point 1000.0

0o70;
0o70_i16;

0b1111_1111_1001_0000;
0b1111_1111_1001_0000i64;
0b________1;

0usize;

// These are too big for their type, but are accepted as literal expressions.
128_i8;
256_u8;

// This is an integer literal, accepted as a floating-point literal expression.
5f32;
```

Note that `-1i8`, for example, is analyzed as two tokens: `-` followed by `1i8`.

Examples of integer literals which are not accepted as literal expressions:

```rust
# #[cfg(false)] {
0invalidSuffix;
123AFB43;
0b010a;
0xAB_CD_EF_GH;
0b1111_f32;
# }
```

r[lex.token.literal.int.invalid]
##### Invalid integer literals

r[lex.token.literal.int.invalid.intro]
Certain integer literal forms are invalid. To avoid ambiguity, the tokenizer rejects them rather than splitting them into separate tokens.

```rust,compile_fail
0b0102;  // This is not `0b010` followed by `2`.
0o1279;  // This is not `0o127` followed by `9`.
0x80.0;  // This is not `0x80` followed by `.` and `0`.
0b101e;  // This is not a suffixed literal or `0b101` followed by `e`.
0b;      // This is not an integer literal or `0` followed by `b`.
0b_;     // This is not an integer literal or `0` followed by `b_`.
2em;     // This is not a suffixed literal or `2` followed by `em`.
2.0em;   // This is not a suffixed literal or `2.0` followed by `em`.
```

r[lex.token.literal.int.out-of-range]
It is an error to have an unsuffixed binary or octal literal followed without intervening whitespace by a decimal digit outside the range for its radix.

r[lex.token.literal.int.period]
It is an error to have an unsuffixed binary, octal, or hexadecimal literal followed without intervening whitespace by a period character (subject to the same restrictions on what may follow the period as in floating-point literals).

r[lex.token.literal.int.exp]
It is an error to have an unsuffixed binary or octal literal followed without intervening whitespace by the character `e` or `E`.

r[lex.token.literal.int.empty-with-radix]
It is an error for a radix prefix to not be followed, after any optional leading underscores, by at least one valid digit for its radix.

r[lex.token.literal.int.tuple-field]
#### Tuple index

r[lex.token.literal.int.tuple-field.syntax]
```grammar,lexer
TUPLE_INDEX -> DEC_LITERAL | BIN_LITERAL | OCT_LITERAL | HEX_LITERAL
```

r[lex.token.literal.int.tuple-field.intro]
A tuple index is used to refer to the fields of [tuples], [tuple structs], and [tuple enum variants].

r[lex.token.literal.int.tuple-field.eq]
Tuple indices are compared with the literal token directly. Tuple indices start with `0` and each successive index increments the value by `1` as a decimal value. Thus, only decimal values will match, and the value must not have any extra `0` prefix characters.

Tuple indices may not include any suffixes (such as `usize`).

```rust,compile_fail
let example = ("dog", "cat", "horse");
let dog = example.0;
let cat = example.1;
// The following examples are invalid.
let cat = example.01;  // ERROR no field named `01`
let horse = example.0b10;  // ERROR no field named `0b10`
let unicorn = example.0usize; // ERROR suffixes on a tuple index are invalid
let underscore = example.0_0; // ERROR no field `0_0` on type `(&str, &str, &str)`
```

r[lex.token.literal.float]
#### Floating-point literals

r[lex.token.literal.float.syntax]
```grammar,lexer
FLOAT_LITERAL ->
      DEC_LITERAL (`.` DEC_LITERAL)? FLOAT_EXPONENT SUFFIX?
    | DEC_LITERAL `.` DEC_LITERAL SUFFIX?
    | DEC_LITERAL `.` !(`.` | `_` | XID_Start)

FLOAT_EXPONENT ->
    (`e`|`E`) ^ (`+`|`-`)? `_`* DEC_DIGIT (DEC_DIGIT|`_`)*
```

r[lex.token.literal.float.form]
A _floating-point literal_ has one of two forms:

* A _decimal literal_ followed by a period character `U+002E` (`.`). This is optionally followed by another decimal literal, with an optional _exponent_.
* A single _decimal literal_ followed by an _exponent_.

r[lex.token.literal.float.suffix]
Like integer literals, a floating-point literal may be followed by a suffix, so long as the pre-suffix part does not end with `U+002E` (`.`). The suffix may not begin with `e` or `E` if the literal does not include an exponent. See [Floating-point literal expressions] for the effect of these suffixes.

Examples of floating-point literals which are accepted as literal expressions:

```rust
123.0f64;
0.1f64;
0.1f32;
12E+99_f64;
let x: f64 = 2.;
```

This last example is different because it is not possible to use the suffix syntax with a floating point literal ending in a period. `2.f64` would attempt to call a method named `f64` on `2`.

Note that `-1.0`, for example, is analyzed as two tokens: `-` followed by `1.0`.

Examples of floating-point literals which are not accepted as literal expressions:

```rust
# #[cfg(false)] {
2.0f80;
2e5f80;
2e5e6;
2.0e5e6;
1.3e10u64;
# }
```

r[lex.token.literal.float.invalid-exponent]
It is an error for a floating-point literal to have an exponent with no digits.

```rust,compile_fail
2e;   // This is not a floating-point literal or `2` followed by `e`.
2.0e; // This is not a floating-point literal or `2.0` followed by `e`.
```

r[lex.token.life]
## Lifetimes and loop labels

r[lex.token.life.syntax]
```grammar,lexer
LIFETIME_TOKEN ->
      RAW_LIFETIME
    | `'` IDENTIFIER_OR_KEYWORD !`'`

LIFETIME_OR_LABEL ->
      RAW_LIFETIME
    | `'` NON_KEYWORD_IDENTIFIER !`'`

RAW_LIFETIME ->
    `'r#` ^ IDENTIFIER_OR_KEYWORD !`'`

RESERVED_RAW_LIFETIME -> `'r#` (`_` | `crate` | `self` | `Self` | `super`) !(`'` | XID_Continue)
```

r[lex.token.life.intro]
Lifetime parameters and [loop labels] use LIFETIME_OR_LABEL tokens. Any LIFETIME_TOKEN will be accepted by the lexer, and for example, can be used in macros.

r[lex.token.life.raw.intro]
A raw lifetime is like a normal lifetime, but its identifier is prefixed by `r#`. (Note that the `r#` prefix is not included as part of the actual lifetime.)

r[lex.token.life.raw.allowed]
Unlike a normal lifetime, a raw lifetime may be any strict or reserved keyword except the ones listed above for `RAW_LIFETIME`.

r[lex.token.life.raw.reserved]
It is an error to use the [RESERVED_RAW_LIFETIME] token.

r[lex.token.life.raw.edition2021]
> [!EDITION-2021]
> Raw lifetimes are accepted in the 2021 edition or later. In earlier editions the token `'r#lt` is lexed as `'r # lt`.

r[lex.token.punct]
## Punctuation

r[lex.token.punct.intro]
Punctuation tokens are used as operators, separators, and other parts of the grammar.

r[lex.token.punct.syntax]
```grammar,lexer
PUNCTUATION ->
      `...`
    | `..=`
    | `<<=`
    | `>>=`
    | `!=`
    | `%=`
    | `&&`
    | `&=`
    | `*=`
    | `+=`
    | `-=`
    | `->`
    | `..`
    | `/=`
    | `::`
    | `<-`
    | `<<`
    | `<=`
    | `==`
    | `=>`
    | `>=`
    | `>>`
    | `^=`
    | `|=`
    | `||`
    | `!`
    | `#`
    | `$`
    | `%`
    | `&`
    | `(`
    | `)`
    | `*`
    | `+`
    | `,`
    | `-`
    | `.`
    | `/`
    | `:`
    | `;`
    | `<`
    | `=`
    | `>`
    | `?`
    | `@`
    | `[`
    | `]`
    | `^`
    | `{`
    | `|`
    | `}`
    | `~`
```

> [!NOTE]
> See the [syntax index] for links to how punctuation characters are used.

r[lex.token.delim]
## Delimiters

Bracket punctuation is used in various parts of the grammar. An open bracket must always be paired with a close bracket. Brackets and the tokens within them are referred to as "token trees" in [macros].  The three types of brackets are:

| Bracket | Type            |
|---------|-----------------|
| `{` `}` | Curly braces    |
| `[` `]` | Square brackets |
| `(` `)` | Parentheses     |

r[lex.token.reserved]
## Reserved tokens

r[lex.token.reserved.intro]
Several token forms are reserved for future use or to avoid confusion. It is an error for the source input to match one of these forms.

r[lex.token.reserved.syntax]
```grammar,lexer
RESERVED_TOKEN ->
      RESERVED_GUARDED_STRING_LITERAL
    | RESERVED_POUNDS
    | RESERVED_RAW_IDENTIFIER
    | RESERVED_RAW_LIFETIME
    | RESERVED_TOKEN_DOUBLE_QUOTE
    | RESERVED_TOKEN_LIFETIME
    | RESERVED_TOKEN_POUND
    | RESERVED_TOKEN_SINGLE_QUOTE
```

r[lex.token.reserved-prefix]
## Reserved prefixes

r[lex.token.reserved-prefix.syntax]
```grammar,lexer
RESERVED_TOKEN_DOUBLE_QUOTE ->
    IDENTIFIER_OR_KEYWORD _except `b` or `c` or `r` or `br` or `cr`_ `"`

RESERVED_TOKEN_SINGLE_QUOTE ->
    IDENTIFIER_OR_KEYWORD _except `b`_ `'`

RESERVED_TOKEN_POUND ->
    IDENTIFIER_OR_KEYWORD _except `r` or `br` or `cr`_ `#`

RESERVED_TOKEN_LIFETIME ->
    `'` IDENTIFIER_OR_KEYWORD _except `r`_ `#`
```

r[lex.token.reserved-prefix.intro]
Some lexical forms known as _reserved prefixes_ are reserved for future use.

r[lex.token.reserved-prefix.id]
Source input which would otherwise be lexically interpreted as a non-raw identifier (or a keyword) which is immediately followed by a `#`, `'`, or `"` character (without intervening whitespace) is identified as a reserved prefix.

r[lex.token.reserved-prefix.raw-token]
Note that raw identifiers, raw string literals, and raw byte string literals may contain a `#` character but are not interpreted as containing a reserved prefix.

r[lex.token.reserved-prefix.strings]
Similarly the `r`, `b`, `br`, `c`, and `cr` prefixes used in raw string literals, byte literals, byte string literals, raw byte string literals, C string literals, and raw C string literals are not interpreted as reserved prefixes.

r[lex.token.reserved-prefix.life]
Source input which would otherwise be lexically interpreted as a non-raw lifetime (or a keyword) which is immediately followed by a `#` character (without intervening whitespace) is identified as a reserved lifetime prefix.

r[lex.token.reserved-prefix.edition2021]
> [!EDITION-2021]
> Starting with the 2021 edition, reserved prefixes are reported as an error by the lexer (in particular, they cannot be passed to macros).
>
> Before the 2021 edition, reserved prefixes are accepted by the lexer and interpreted as multiple tokens (for example, one token for the identifier or keyword, followed by a `#` token).
>
> Examples accepted in all editions:
> ```rust
> macro_rules! lexes {($($_:tt)*) => {}}
> lexes!{a #foo}
> lexes!{continue 'foo}
> lexes!{match "..." {}}
> lexes!{r#let#foo}         // three tokens: r#let # foo
> lexes!{'prefix #lt}
> ```
>
> Examples accepted before the 2021 edition but rejected later:
> ```rust,edition2018
> macro_rules! lexes {($($_:tt)*) => {}}
> lexes!{a#foo}
> lexes!{continue'foo}
> lexes!{match"..." {}}
> lexes!{'prefix#lt}
> ```

r[lex.token.reserved-guards]
## Reserved guards

r[lex.token.reserved-guards.syntax]
```grammar,lexer
RESERVED_GUARDED_STRING_LITERAL -> `#`+ STRING_LITERAL

RESERVED_POUNDS -> `#`{2..}
```

r[lex.token.reserved-guards.intro]
The reserved guards are syntax reserved for future use, and will generate a compile error if used.

r[lex.token.reserved-guards.string-literal]
The *reserved guarded string literal* is a token of one or more `U+0023` (`#`) immediately followed by a [STRING_LITERAL].

r[lex.token.reserved-guards.pounds]
The *reserved pounds* is a token of two or more `U+0023` (`#`).

r[lex.token.reserved-guards.edition2024]
> [!EDITION-2024]
> Before the 2024 edition, reserved guards are accepted by the lexer and interpreted as multiple tokens. For example, the `#"foo"#` form is interpreted as three tokens. `##` is interpreted as two tokens.

[Floating-point literal expressions]: expressions/literal-expr.md#floating-point-literal-expressions
[identifier]: identifiers.md
[Integer literal expressions]: expressions/literal-expr.md#integer-literal-expressions
[keywords]: keywords.md
[literal expressions]: expressions/literal-expr.md
[loop labels]: expressions/loop-expr.md#loop-labels
[macros]: macros-by-example.md
[String continuation escapes]: expressions/literal-expr.md#string-continuation-escapes
[syntax index]: syntax-index.md#operators-and-punctuation
[tuple structs]: items/structs.md
[tuple enum variants]: items/enumerations.md
[tuples]: types/tuple.md
