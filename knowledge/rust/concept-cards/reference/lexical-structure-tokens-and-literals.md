---
concept: Lexical Structure - Tokens and Literals
slug: lexical-structure-tokens-and-literals
category: language-specification
subcategory: lexical-structure
tier: foundational
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: null
section: "Tokens / Literals / Lifetimes / Punctuation / Delimiters / Reserved tokens"
extraction_confidence: high
aliases:
  - "Rust tokens"
  - "literal types"
  - "string literals"
  - "raw string literals"
  - "byte literals"
  - "C string literals"
  - "integer literals"
  - "floating-point literals"
  - "lifetime tokens"
  - "punctuation tokens"
  - "reserved prefixes"
prerequisites:
  - rust-reference-overview
  - lexical-structure-input-and-keywords
extends: []
related:
  - reference-macros-by-example
  - reference-procedural-macros
contrasts_with: []
answers_questions:
  - "What are the different kinds of tokens in Rust?"
  - "What literal types does Rust support?"
  - "How do raw string literals work?"
  - "What are C string literals and when were they introduced?"
  - "What escape sequences are available in character and string literals?"
  - "How do integer and floating-point literal suffixes work?"
  - "What are lifetime tokens and raw lifetimes?"
  - "What tokens are reserved for future use?"
  - "How do tuple index tokens work?"
---

# Quick Definition

Rust source input is broken into tokens: keywords, identifiers, literals (characters, strings, bytes, C strings, integers, floats -- each with raw and escaped variants), lifetimes, punctuation, and delimiters. Literals support multiple escape sequences (ASCII, Unicode, byte, quote) and type suffixes. The lexer also defines reserved token forms that prevent certain character sequences from being split into separate tokens, ensuring forward compatibility.

# Core Definition

## Token Categories

Tokens are primitive productions defined by regular (non-recursive) languages. Rust tokens fall into six categories: keywords, identifiers, literals, lifetimes, punctuation, and delimiters.

## Character and String Literals

Rust provides eight literal string/character forms across three encoding families:

**Unicode family**: Character literals (`'H'`) hold a single Unicode character. String literals (`"hello"`) hold a sequence of Unicode characters. Raw string literals (`r#"hello"#`) disable escape processing, delimited by matching counts of `#` characters (up to 255). All three support ASCII escapes (`\x41`, `\n`, `\r`, `\t`, `\\`, `\0`), Unicode escapes (`\u{7FFF}` -- up to 6 hex digits), and quote escapes (`\'`, `\"`). Raw strings support no escapes.

**Byte family**: Byte literals (`b'H'`) hold a single ASCII character as `u8`. Byte string literals (`b"hello"`) hold ASCII sequences. Raw byte string literals (`br#"hello"#`) disable escapes. These support byte escapes (`\x7F` -- full 8-bit range), whitespace escapes, and quote escapes, but not Unicode escapes.

**C string family** (2021 edition+): C string literals (`c"hello"`) produce `&CStr` values with an implicit null terminator. Raw C string literals (`cr#"hello"#`) disable escapes. C strings allow both byte escapes and Unicode escapes, but `\0` and `\x00` are prohibited (the null terminator is implicit). Unicode characters above U+007F in C strings are encoded as UTF-8 bytes. Before the 2021 edition, `c""` is lexed as two tokens: identifier `c` and string `""`.

**String continuation**: In non-raw string, byte string, and C string literals, a backslash immediately before a line break causes the line break (and leading whitespace on the next line) to be omitted from the string value.

**CR restriction**: The character U+000D (CR) may not appear in any string or character literal (standalone CR in source files is preserved by CRLF normalization but forbidden within literals).

## Number Literals

**Integer literals** come in four forms: decimal (`98_222`), hex (`0xff`), octal (`0o77`), and binary (`0b1111_0000`). All allow `_` as visual separators. Valid integer suffixes are: `u8`, `i8`, `u16`, `i16`, `u32`, `i32`, `u64`, `i64`, `u128`, `i128`, `usize`, `isize`. Negative numbers like `-1i8` are two tokens: `-` and `1i8`.

**Floating-point literals** have two forms: a decimal with a period and optional exponent (`123.0E+77`), or a decimal with an exponent only (`12E+99_f64`). Valid float suffixes are `f32` and `f64`. A trailing period without further digits (`2.`) is valid but cannot take a suffix (`2.f64` would attempt to call method `f64` on `2`).

**Literal suffixes**: Any literal with any suffix is a valid token and can be passed to macros. However, when interpreted as literal expressions, only the type suffixes listed above are accepted; non-numeric literals reject all suffixes.

**Invalid integer forms**: The lexer rejects certain ambiguous forms as single error tokens rather than splitting them: `0b0102` (not `0b010` + `2`), `0o1279` (not `0o127` + `9`), `0x80.0`, `0b101e`, `0b` (bare prefix), `2em`.

**Tuple indices** use the same grammar as number literals but are compared literally: only decimal values starting from 0 match, extra leading zeros are rejected (`example.01` fails), suffixes are not allowed, and non-decimal forms (`0b10`) do not match.

## Lifetimes and Punctuation

**Lifetime tokens** consist of `'` followed by an identifier or keyword (e.g., `'a`, `'static`). **Raw lifetimes** (`'r#keyword`, 2021 edition+) allow using keywords as lifetime names, except `_`, `crate`, `self`, `Self`, and `super`. In earlier editions, `'r#lt` is lexed as three tokens: `'r`, `#`, `lt`.

**Punctuation** includes all operator and separator characters, from single characters (`+`, `-`, `*`, etc.) to multi-character sequences (`...`, `..=`, `<<=`, `>>=`, `=>`, `->`, `::`, etc.).

**Delimiters** are the three bracket pairs: `{}` (curly braces), `[]` (square brackets), `()` (parentheses). An open bracket must always be paired with a close bracket. Brackets and their contents form "token trees" used in macros.

## Reserved Tokens

Several token forms are reserved for future use: reserved guarded string literals (`#+"string"`), reserved pounds (`##` or more), reserved raw identifiers, reserved raw lifetimes, and reserved prefixes. **Reserved prefixes** are identifiers immediately followed (without whitespace) by `#`, `'`, or `"` -- starting in the 2021 edition these are errors rather than being split into separate tokens. The prefixes `r`, `b`, `br`, `c`, and `cr` used for raw strings and byte/C string literals are exempt.

# Prerequisites

- **rust-reference-overview** -- grammar notation for reading formal productions
- **lexical-structure-input-and-keywords** -- keywords and identifiers referenced by token definitions

# Key Properties

1. Tokens are defined by regular (non-recursive) languages -- they are the primitive lexical units
2. Eight literal string/character forms span three encoding families (Unicode, byte, C string) with raw variants
3. Raw strings use matching `#` counts (up to 255) to delimit content with no escape processing
4. C string literals implicitly terminate with `\0`; explicit null bytes are forbidden within them
5. Integer literals allow `_` separators anywhere after the first digit; negative signs are separate tokens
6. Floating-point literals cannot have a suffix when ending in `.` (ambiguity with method calls)
7. Any suffix on any literal is a valid token for macros, but only recognized type suffixes are valid in expressions
8. The lexer rejects ambiguous numeric forms as single error tokens rather than splitting them
9. Tuple indices must be simple decimal values starting from 0 with no leading zeros or suffixes
10. Reserved prefixes (identifier immediately before `#`, `'`, or `"`) are errors from the 2021 edition onward, ensuring future syntax extensions do not break existing code

# Construction / Recognition

## Choosing the Right String Literal Form

1. For normal Unicode strings with escapes: `"..."` (string literal)
2. For strings with many backslashes or quotes: `r#"..."#` (raw string, add `#`s as needed)
3. For single-byte ASCII values: `b'x'` (byte literal)
4. For ASCII byte sequences: `b"..."` (byte string literal)
5. For null-terminated C-compatible strings: `c"..."` (C string literal, 2021+ edition)
6. For any raw variant: prefix with `r` (or `br`, `cr`) and use `#` delimiters

## Writing Number Literals

1. Use `_` freely for readability: `1_000_000`, `0xFF_FF`
2. Remember negative signs are separate tokens: `-1` is `-` then `1`
3. Use suffixes to specify type: `42u64`, `3.14f32`
4. A bare `2.` is a valid float literal but cannot take a suffix

# Context & Application

The token system defines what the parser receives after lexical analysis. This has direct implications for macro authors: `macro_rules!` macros and procedural macros see different token representations (covered in the macros cards). The distinction matters because multi-character operators, lifetimes, and metavariable substitutions are handled differently between the two macro systems.

The reserved prefix system is a forward-compatibility mechanism: by reserving `identifier"..."` forms, Rust can introduce new literal types in future editions (as it did with C strings in the 2021 edition) without breaking existing code. The `c"..."` literal type demonstrates this pattern in action.

The tuple index rules are surprisingly strict: `example.0b10` fails not because binary indexing is nonsensical, but because tuple indices are compared as literal text against decimal values. This avoids ambiguity in the grammar.

# Examples

**Example 1** (String Literal Equivalences):
```rust
"foo"; r"foo";                     // foo
"\"foo\""; r#""foo""#;             // "foo"
"foo #\"# bar";
r##"foo #"# bar"##;                // foo #"# bar
"\x52"; "R"; r"R";                 // R
"\\x52"; r"\x52";                  // \x52
```

**Example 2** (C String Literals, 2021+ edition):
```rust
c"ae";           // LATIN SMALL LETTER AE (U+00E6) -- stored as UTF-8 bytes
c"\u{00E6}";    // Same content via Unicode escape
c"\xC3\xA6";   // Same content via explicit UTF-8 byte escapes
// All three produce identical CStr values with implicit \0 terminator
```

**Example 3** (Integer Literal Forms):
```rust
123;                        // decimal
0xff;                       // hex
0o77;                       // octal
0b1111_0000;               // binary with separator
0xff_u8;                   // hex with type suffix
0x01_f32;                  // integer 7986, NOT float 1.0
5f32;                      // integer literal, accepted as float expression
```

**Example 4** (Tuple Index Strictness):
```rust
let example = ("dog", "cat", "horse");
let dog = example.0;       // OK
// let cat = example.01;   // ERROR: no field named `01`
// let horse = example.0b10; // ERROR: no field named `0b10`
```

# Relationships

## Builds Upon
- **rust-reference-overview** -- grammar notation
- **lexical-structure-input-and-keywords** -- keywords and identifiers

## Enables
- **reference-macros-by-example** -- `tt` fragment specifier matches token trees; `literal` matches literals with arbitrary suffixes
- **reference-procedural-macros** -- procedural macros operate on token streams composed of these tokens

## Related
- **lexical-structure-input-and-keywords** -- companion card for keywords, identifiers, comments, whitespace

## Contrasts With
(none)

# Common Errors

- **Error**: Writing `0x01_f32` expecting a floating-point value of 1.0.
  **Correction**: This is the integer 7986 (0x01F32 in hex) with no suffix (the `_f32` is not a valid hex suffix -- `f32` characters happen to be valid hex digits). Integer literal suffixes cannot start with `e` or `E` to avoid confusion with float exponents, but hex digits `a`-`f` are consumed as part of the hex literal itself.

- **Error**: Using `\0` or `\x00` inside a C string literal.
  **Correction**: C string literals have an implicit null terminator. Explicit null bytes are forbidden within the string body. Use byte escapes for other values: `c"\x01"` is valid but `c"\x00"` is not.

# Common Confusions

- **Confusion**: Thinking raw strings `r#"..."#` can use any number of `#` characters.
  **Clarification**: Raw strings support fewer than 256 `#` characters. In practice this is not a real limitation, but the specification explicitly caps it at 255.

- **Confusion**: Thinking `-1i8` is a single literal token.
  **Clarification**: Negative numbers in Rust are always two tokens: the unary minus operator `-` and the literal `1i8`. This is a lexer-level distinction that matters for macros and for understanding how literal expressions are parsed.

- **Confusion**: Assuming `2.f64` is a valid floating-point literal with suffix.
  **Clarification**: When a float literal ends with `.` and no further digits, it cannot take a suffix. `2.f64` is parsed as attempting to call a method `f64` on the integer `2`. Use `2.0f64` or `2_f64` instead.

# Source Reference

Chapter 2 (Lexical Structure): Tokens -- six token categories, formal grammar. Literals -- character/string/byte/C-string literal forms (8 variants), escape sequences (ASCII, byte, Unicode, quote), string continuation, number literals (integer and float forms), literal suffixes, invalid forms, tuple indices. Lifetimes -- lifetime tokens, raw lifetimes (2021+ edition). Punctuation -- operator and separator characters. Delimiters -- bracket pairs and token trees. Reserved tokens -- reserved prefixes, guarded string literals, reserved pounds.

# Verification Notes

- Definition source: Direct synthesis from Ch. 2, sections on tokens (40 lines), literals (450+ lines including all variants), lifetimes (35 lines), punctuation (65 lines), delimiters (10 lines), reserved tokens (100 lines)
- Key Properties: All items directly from grammar productions and normative text
- Confidence rationale: HIGH -- formal grammar productions leave no ambiguity
- Uncertainties: Reserved token forms may gain meaning in future editions
- Cross-reference status: All slugs reference cards in this Reference extraction set
