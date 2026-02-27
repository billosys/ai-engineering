---
# === CORE IDENTIFICATION ===
concept: Liquid Value System
slug: liquid-value-system

# === CLASSIFICATION ===
category: rust-api
tier: advanced

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid API Reference"
chapter_number: null
pdf_page: null
section: "liquid_core::model::Value / liquid::Object"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Liquid types"
  - "Value enum"
  - "Liquid Object"
  - "Liquid data model"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
extends: []
related:
  - liquid-parser
  - liquid-template-object
  - objectview-valueview-traits
  - template-variables
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Liquid Rust crate relate to Ruby Liquid?"
  - "What distinguishes Cobalt's Liquid from Ruby Liquid?"
  - "What must I understand before using the Cobalt Rust API?"
---

# Quick Definition
The Liquid Rust crate's value system consists of the `Value` enum (with variants for Scalar, Array, Object, Nil, and State), the `Object` type alias (a map from string keys to `Value`), the `Scalar` type, and the `object!` macro for constructing objects using literal syntax.

# Core Definition
The `liquid_core::model::Value` enum represents all possible values in Liquid templates. Its variants include `Scalar` (strings, integers, floats, booleans, date-times), `Array` (a `Vec<Value>`), `Object` (a key-value map), and `Nil` (absence of a value). The `liquid::Object` type is a type alias for a map structure (`BTreeMap<KString, Value>` or similar) that serves as the standard container for template global variables. The `liquid::object!` macro provides JSON-like literal syntax for constructing `Object` instances. The `Scalar` type encompasses multiple primitive types: strings (`KString`), integers (`i64`), floats (`f64`), booleans (`bool`), and date-time values. This value system is the Rust equivalent of Ruby Liquid's dynamic typing, but expressed through Rust's static type system using enums and traits (source: liquid_core rustdoc, `model::Value`; liquid rustdoc, `Object`, `object!` macro).

# Prerequisites
- Understanding of Liquid template language and its data model (see `liquid-template-language`)
- Rust programming fundamentals (enums, type aliases, macros)

# Key Properties
1. **`Value` enum**: The core data type with variants:
   - `Scalar(Scalar)`: Primitive values (string, integer, float, boolean, date-time)
   - `Array(Vec<Value>)`: Ordered list of values
   - `Object(Object)`: Key-value map
   - `Nil`: Represents the absence of a value
2. **`Object` type**: A type alias for `BTreeMap<KString, Value>` that maps string keys to Liquid values. This is the primary type used for template global variables.
3. **`Scalar` type**: Encapsulates primitive types within a single type.
4. **`object!` macro**: Constructs `Object` instances with a JSON-like literal syntax.
5. **`to_object` function**: `liquid::to_object` converts a serializable Rust type `T` into a `liquid_core::model::Object` via Serde.
6. **`Value` is owned**: `Value` is an owned data type; for borrowed access, the `ValueView` and `ObjectView` traits are used.

# Construction / Recognition
## Creating objects with the `object!` macro:
```rust
let globals = liquid::object!({
    "name": "World",
    "num": 4f64,
    "tags": ["rust", "liquid"],
    "active": true
});
```

## Creating an empty object:
```rust
let globals = liquid::Object::new();
```

## Creating values manually:
```rust
use liquid_core::model::Value;

let scalar = Value::scalar("hello");
let number = Value::scalar(42i64);
let array = Value::Array(vec![Value::scalar("a"), Value::scalar("b")]);
let nil = Value::Nil;
```

## Using `to_object` with Serde:
```rust
#[derive(Serialize)]
struct PageData {
    title: String,
    count: i64,
}

let data = PageData { title: "Hello".into(), count: 5 };
let obj = liquid::to_object(&data).unwrap();
```

# Context & Application
- **Typical contexts**: Constructing template global variables, passing data to templates for rendering, implementing custom filters that manipulate values.
- **When to use `object!` macro**: For quick, inline construction of template data with literal values.
- **When to use `to_object`**: When converting structured Rust data (e.g., from a config file or database) into Liquid-compatible objects.
- **When to use `Value` directly**: When implementing custom filters or tags that need to manipulate individual values.

# Examples
**Example 1** (source: liquid rustdoc, crate overview): Using the `object!` macro

```rust
let globals = liquid::object!({
    "num": 4f64
});
let output = template.render(&globals).unwrap();
```

**Example 2** (source: liquid rustdoc, Parser::parse): Using `Object::new()`

```rust
let globals = liquid::Object::new();
let output = template.render(&globals).unwrap();
```

# Relationships
## Builds Upon
- `liquid-template-language`: The value system represents the data model used in Liquid templates.

## Enables
- `liquid-template-object`: Templates are rendered with `Object` or `ObjectView` implementors as globals.
- `objectview-valueview-traits`: The trait-based borrowed view of the value system.
- Custom filter and tag implementations that manipulate values.

## Related
- `liquid-parser`: The parser compiles templates that operate on these value types.
- `template-variables`: Template variables in Cobalt are exposed through this value system.

## Contrasts With
- Ruby Liquid values: Ruby Liquid uses native Ruby types (Hash, Array, String, Integer, etc.); the Rust version uses explicit enum variants. The `object!` macro provides similar ergonomics to Ruby hash literals.

# Common Errors
1. **Type mismatches**: Liquid values are dynamically typed at runtime; passing an integer where a string is expected may cause filter errors.
2. **Forgetting the `f64` suffix for floats**: In the `object!` macro, `4` is an integer; use `4f64` for floating-point.

# Common Confusions
1. **`Value` vs. `ValueView`**: `Value` is the owned enum; `ValueView` is the borrowed trait. Templates accept `&dyn ObjectView` (borrowed), while `Object` holds owned `Value` instances.
2. **`Object` as a type alias**: `liquid::Object` is not a separate struct but a type alias for a map type. It implements `ObjectView`.
3. **`KString` vs. `String`**: The Liquid crate uses `KString` (from the `kstring` crate) for interned/optimized strings rather than standard `String`.

# Source Reference
- liquid_core rustdoc: `liquid_core::model::Value` enum.
- liquid rustdoc: `liquid::Object`, `liquid::object!` macro, `liquid::to_object`.

# Verification Notes
- Value enum variants confirmed from `sources-html/liquid_core/model/enum.Value.html`. Object type and object! macro confirmed from `sources-html/liquid/struct.Object.html` and `sources-html/liquid/index.html`.
