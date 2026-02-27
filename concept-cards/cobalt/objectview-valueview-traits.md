---
# === CORE IDENTIFICATION ===
concept: ObjectView and ValueView Traits
slug: objectview-valueview-traits

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
section: "liquid::ObjectView / liquid::ValueView"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ObjectView trait"
  - "ValueView trait"
  - "Liquid view traits"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-value-system
  - liquid-template-language
extends:
  - liquid-value-system
related:
  - liquid-parser
  - liquid-template-object
  - cobalt-config-struct
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Liquid Rust crate relate to Ruby Liquid?"
  - "What must I understand before using the Cobalt Rust API?"
  - "What distinguishes Cobalt's Liquid from Ruby Liquid?"
---

# Quick Definition
`ValueView` and `ObjectView` are Rust traits in the `liquid` crate that provide borrowed, read-only access to Liquid values and objects, enabling custom Rust types to be exposed to Liquid templates without requiring conversion to owned `Value`/`Object` types.

# Core Definition
The `ValueView` trait is the primary accessor trait for all Liquid values. It defines methods for querying a value's type (`type_name`), state (`query_state`), string representation (`to_kstr`), owned conversion (`to_value`), and type-specific downcasting (`as_scalar`, `as_array`, `as_object`). The `ObjectView` trait extends `ValueView` and provides map-like access methods: `size()`, `keys()`, `values()`, `iter()`, `contains_key()`, and `get()`. `ObjectView` is the trait bound used by `Template::render()` for the `globals` parameter (`&dyn ObjectView`), meaning any Rust type implementing `ObjectView` can be used as template data without conversion to `liquid::Object`. Standard implementations exist for `HashMap<K, V>`, `BTreeMap<K, V>`, and `&O where O: ObjectView`. A derive macro is available for automatically implementing both traits on custom structs (source: liquid rustdoc, `trait.ObjectView.html`, `trait.ValueView.html`).

# Prerequisites
- Understanding of the Liquid value system (see `liquid-value-system`)
- Understanding of Rust traits, trait objects, and dynamic dispatch
- Understanding of Liquid template language concepts (see `liquid-template-language`)

# Key Properties
## ValueView Trait
1. **`type_name(&self) -> &'static str`**: Returns the Liquid type name (e.g., "string", "number", "array", "object", "nil").
2. **`query_state(&self, state: State) -> bool`**: Queries whether the value matches a particular state (e.g., truthy, default, blank, empty).
3. **`to_kstr(&self) -> KStringCow<'_>`**: Returns the string representation of the value.
4. **`to_value(&self) -> Value`**: Converts the borrowed view to an owned `Value`.
5. **`as_scalar(&self) -> Option<&dyn ScalarView>`**: Downcasts to scalar, if applicable.
6. **`as_array(&self) -> Option<&dyn ArrayView>`**: Downcasts to array, if applicable.
7. **`as_object(&self) -> Option<&dyn ObjectView>`**: Downcasts to object, if applicable.
8. **`source(&self) -> DisplayCow<'_>`**: Returns a debug-friendly source representation.

## ObjectView Trait (extends ValueView)
9. **`as_value(&self) -> &dyn ValueView`**: Upcasts to `ValueView`.
10. **`size(&self) -> i64`**: Returns the number of key-value pairs.
11. **`keys(&self) -> Box<dyn Iterator<Item = KStringCow<'_>>>`**: Iterates over keys.
12. **`values(&self) -> Box<dyn Iterator<Item = &dyn ValueView>>`**: Iterates over values.
13. **`iter(&self) -> Box<dyn Iterator<Item = (KStringCow<'_>, &dyn ValueView)>>`**: Iterates over key-value pairs.
14. **`contains_key(&self, index: &str) -> bool`**: Checks if a key exists.
15. **`get(&self, index: &str) -> Option<&dyn ValueView>`**: Retrieves a value by key.

## Standard Implementations
16. **`Object` (BTreeMap-based)**: The standard `liquid::Object` type implements `ObjectView`.
17. **`HashMap<K, V>`**: Implements `ObjectView` when `K: ObjectIndex` and `V: ValueView`.
18. **`BTreeMap<K, V>`**: Implements `ObjectView` when `K: ObjectIndex` and `V: ValueView`.
19. **`&O where O: ObjectView`**: References to `ObjectView` implementors also implement `ObjectView`.

# Construction / Recognition
## Using with Template::render():
```rust
// Using liquid::Object (implements ObjectView)
let globals = liquid::object!({ "name": "World" });
let output = template.render(&globals).unwrap();

// Using HashMap (implements ObjectView)
use std::collections::HashMap;
let mut globals = HashMap::new();
globals.insert("name".to_string(), liquid_core::Value::scalar("World"));
let output = template.render(&globals).unwrap();
```

## Custom struct with derive:
```rust
use liquid::ObjectView;
use liquid::ValueView;

#[derive(ObjectView, ValueView)]
struct MyGlobals {
    title: String,
    count: i64,
}
```

# Context & Application
- **Typical contexts**: Providing template data from custom Rust structs, implementing zero-copy template rendering, creating custom Liquid filters and tags.
- **When to use ObjectView**: When you want to pass data to `Template::render()` or implement custom types accessible in templates.
- **When to use ValueView**: When implementing values that can be accessed by template expressions, filters, and tags.
- **Performance benefit**: Using traits allows templates to borrow data from existing Rust structs without copying into `liquid::Object`.

# Examples
**Example 1** (source: liquid rustdoc, Template::render): Standard ObjectView usage

```rust
let template = liquid::ParserBuilder::with_stdlib()
    .build().unwrap()
    .parse("Hello, {{ name }}!").unwrap();

let globals = liquid::object!({ "name": "Cobalt" });
let output = template.render(&globals).unwrap();
// output: "Hello, Cobalt!"
```

**Example 2** (source: liquid rustdoc, trait.ObjectView): ObjectView methods

The `ObjectView` trait provides map-like read access:
- `globals.get("name")` returns `Some(&dyn ValueView)` for the "name" key.
- `globals.size()` returns the number of entries.
- `globals.keys()` iterates over the key names.
- `globals.contains_key("name")` checks for key existence.

# Relationships
## Builds Upon
- `liquid-value-system`: The traits provide borrowed access to the value types.

## Enables
- `liquid-template-object`: Templates accept `&dyn ObjectView` for rendering.
- Zero-copy template rendering from custom Rust types.
- Custom filter and tag implementations.

## Related
- `liquid-parser`: The parser creates templates that use these traits at render time.
- `cobalt-config-struct`: Cobalt's internal data types implement these traits to expose site data to templates.

## Contrasts With
- Ruby Liquid: Ruby does not have a trait system; it uses duck typing. The Rust traits provide compile-time guarantees about what data is accessible in templates.
- `Value` enum: `Value` is owned; `ValueView`/`ObjectView` are borrowed trait objects. This is a Rust-specific distinction.

# Common Errors
1. **Not implementing both traits**: `ObjectView` requires `ValueView`; you must implement both (or derive both).
2. **Key type mismatch**: For `HashMap`/`BTreeMap` to implement `ObjectView`, the key type must implement `ObjectIndex` (typically `String` or `KString`).

# Common Confusions
1. **`ObjectView` vs. `Object`**: `ObjectView` is a trait (borrowed access); `Object` is an owned type (the map itself). `Object` implements `ObjectView`.
2. **`ValueView` vs. `Value`**: Same pattern; `ValueView` is the trait, `Value` is the owned enum.
3. **Dynamic dispatch**: Template rendering uses `&dyn ObjectView` (trait object), which involves dynamic dispatch at runtime.

# Source Reference
- liquid rustdoc: `liquid::ObjectView` trait, `liquid::ValueView` trait.
- liquid_core source: `src/liquid_core/model/object/mod.rs`, `src/liquid_core/model/value/view.rs`.

# Verification Notes
- Trait method signatures confirmed from `sources-html/liquid/trait.ObjectView.html`. Foreign type implementations (HashMap, BTreeMap) confirmed from the same source. ValueView methods confirmed from grep of `sources-html/liquid/trait.ValueView.html`.
