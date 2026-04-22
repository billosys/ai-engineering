---
# === CORE IDENTIFICATION ===
concept: API Type Safety Guidelines
slug: api-type-safety-guidelines

# === CLASSIFICATION ===
category: api-design
subcategory: type-safety
tier: intermediate

# === PROVENANCE ===
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "07-type-safety"
chapter_number: 7
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C-NEWTYPE"
  - "C-CUSTOM-TYPE"
  - "C-BITFLAG"
  - "C-BUILDER"
  - "Rust API type safety"
  - "builder pattern guidelines"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - api-guidelines-overview
extends: []
related:
  - api-predictability-guidelines
  - api-flexibility-guidelines
  - api-future-proofing-guidelines
  - api-interoperability-guidelines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use newtypes to distinguish values of the same underlying type?"
  - "Why should I avoid bool and Option parameters in public APIs?"
  - "When should I use bitflags instead of enums for flag sets?"
  - "How do I implement the builder pattern in Rust?"
  - "What is the difference between consuming and non-consuming builders?"
  - "When should a builder method take &mut self vs self?"
  - "How does the type system prevent bugs like the Mars Climate Orbiter failure?"
---

# Quick Definition

Rust APIs should leverage the type system to prevent misuse at compile time. Four guidelines govern this: use newtypes to give static meaning to primitive types (C-NEWTYPE), use custom types instead of bool/Option for arguments (C-CUSTOM-TYPE), use the `bitflags` crate for flag sets instead of enums (C-BITFLAG), and use the builder pattern for complex value construction (C-BUILDER).

# Core Definition

The Rust API Guidelines define four type safety conventions that ensure APIs are hard to misuse.

**C-NEWTYPE**: "Newtypes can statically distinguish between different interpretations of an underlying type." A `f64` used for miles vs kilometers should be wrapped in distinct newtypes (`Miles(pub f64)` and `Kilometers(pub f64)`) so the compiler prevents accidental confusion -- the source references the Mars Climate Orbiter as a real-world example of what this prevents.

**C-CUSTOM-TYPE**: "Core types like `bool`, `u8` and `Option` have many possible interpretations. Use a deliberate type (whether enum, struct, or tuple) to convey interpretation and invariants." Prefer `Widget::new(Small, Round)` over `Widget::new(true, false)`.

**C-BITFLAG**: When an API input is "the presence or absence of a set of flags" rather than a single choice, use the `bitflags` crate to provide a typesafe representation instead of raw integer flags or enums.

**C-BUILDER**: "Some data structures are complicated to construct" due to large numbers of inputs, compound data, optional configuration, or choice between flavors. The builder pattern addresses this by introducing a separate builder type with chainable configuration methods and terminal construction methods.

# Prerequisites

- **API Guidelines Overview** -- understanding the overall framework and checklist approach of the Rust API Guidelines

# Key Properties

1. **Static distinction via newtypes**: Wrapper types around primitives enforce correct usage at compile time with zero runtime cost
2. **Meaningful argument types**: Custom enums/structs for parameters make call sites self-documenting and extensible
3. **Bitflags for flag combinations**: The `bitflags` crate enables typesafe combining of multiple boolean options via bitwise OR
4. **Non-consuming builders (preferred)**: Terminal methods take `&self`, configuration methods take/return `&mut self` -- supports both one-liners and complex configuration
5. **Consuming builders**: Terminal methods take `self`, configuration methods take/return owned `self` -- needed when construction transfers ownership (e.g., `io::Write`)
6. **Builder naming**: Choose meaningful names over `TBuilder` -- e.g., `Command` is the builder for a child process, `ParseOptions` builds a `Url`
7. **Builder constructor minimalism**: Builder constructors should take only the data required to make the target value
8. **Extensibility**: Custom types make it easy to add variants later (e.g., adding `ExtraLarge` to a size enum)

# Construction / Recognition

## Newtype pattern (C-NEWTYPE):
```rust
struct Miles(pub f64);
struct Kilometers(pub f64);

impl Miles {
    fn to_kilometers(self) -> Kilometers { /* ... */ }
}

fn are_we_there_yet(distance_travelled: Miles) -> bool { /* ... */ }
```

## Custom types for arguments (C-CUSTOM-TYPE):
```rust
// Prefer this:
let w = Widget::new(Small, Round);

// Over this:
let w = Widget::new(true, false);
```

## Bitflags (C-BITFLAG):
```rust
use bitflags::bitflags;

bitflags! {
    struct Flags: u32 {
        const FLAG_A = 0b00000001;
        const FLAG_B = 0b00000010;
        const FLAG_C = 0b00000100;
    }
}

fn f(settings: Flags) {
    if settings.contains(Flags::FLAG_A) { /* ... */ }
}

f(Flags::FLAG_A | Flags::FLAG_C);
```

## Non-consuming builder (C-BUILDER, preferred):
```rust
impl Command {
    pub fn new(program: String) -> Command { /* ... */ }
    pub fn arg(&mut self, arg: String) -> &mut Command {
        self.args.push(arg);
        self
    }
    pub fn spawn(&self) -> io::Result<Child> { /* ... */ }
}

// One-liner:
Command::new("/bin/cat").arg("file.txt").spawn();

// Complex configuration:
let mut cmd = Command::new("/bin/ls");
if size_sorted { cmd.arg("-S"); }
cmd.arg(".");
cmd.spawn();
```

## Consuming builder (C-BUILDER):
```rust
impl TaskBuilder {
    pub fn named(mut self, name: String) -> TaskBuilder {
        self.name = Some(name);
        self
    }
    pub fn spawn<F>(self, f: F) where F: FnOnce() + Send { /* ... */ }
}

// Must re-assign to retain ownership:
let mut task = TaskBuilder::new();
task = task.named("my_task_2");
task.spawn(|| { /* ... */ });
```

# Context & Application

These four guidelines represent Rust's approach to leveraging the type system as a first line of defense against API misuse. The newtype pattern (C-NEWTYPE) is foundational -- it appears again in the dependability chapter (C-VALIDATE) for static enforcement and in the future proofing chapter (C-NEWTYPE-HIDE) for encapsulation. The builder pattern (C-BUILDER) is one of the most widely used patterns in the Rust ecosystem, appearing in the standard library (`Command`, `thread::Builder`) and in many popular crates. The preference for non-consuming builders reflects a practical design philosophy: "making easy things easy and hard things possible."

# Examples

**Example 1** (Ch. 7, C-NEWTYPE): The Mars Climate Orbiter catastrophe is cited as motivation -- a function expecting miles cannot accidentally receive kilometers when newtypes enforce the distinction at compile time.

**Example 2** (Ch. 7, C-CUSTOM-TYPE): "Using custom types makes it easier to expand the options later on, for example by adding an `ExtraLarge` variant." Enums are open to extension while booleans are not.

**Example 3** (Ch. 7, C-BITFLAG): The `bitflags!` macro creates a struct wrapping a `u32` with named constants, supporting `|` for combination and `.contains()` for testing.

**Example 4** (Ch. 7, C-BUILDER): `std::process::Command` is the canonical non-consuming builder. The builder constructor takes only the program name (required data), and optional configuration like arguments and working directory are added via chained methods.

**Example 5** (Ch. 7, C-BUILDER): For consuming builders, "client code works as follows: `task = task.named('my_task_2'); // must re-assign to retain ownership`." This is more verbose but necessary when the terminal method must take ownership.

# Relationships

## Builds Upon
- **API Guidelines Overview** -- these guidelines are part of the overall API Guidelines checklist

## Enables
- Compile-time prevention of API misuse
- Self-documenting function signatures
- Complex object construction without constructor explosion

## Related
- **api-predictability-guidelines** -- type safety and predictability work together to prevent misuse
- **api-flexibility-guidelines** -- builders provide flexible construction APIs
- **api-future-proofing-guidelines** -- newtypes and custom types support future API evolution
- **api-interoperability-guidelines** -- type-safe APIs must also interoperate with standard traits

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `bool` parameters for function arguments.
  **Correction**: "Core types like `bool`, `u8` and `Option` have many possible interpretations. Use a deliberate type (whether enum, struct, or tuple) to convey interpretation and invariants." (C-CUSTOM-TYPE)

- **Error**: Using an enum when an API input is a set of combinable flags.
  **Correction**: "An `enum` allows an API to request exactly one choice from among many." For flag sets, use the `bitflags` crate instead. (C-BITFLAG)

- **Error**: Making the builder constructor take all configuration parameters.
  **Correction**: "The builder constructor should take as parameters only the data required to make a `T`." Optional configuration belongs on chainable methods. (C-BUILDER)

- **Error**: Using `&mut self` configuration methods with a consuming terminal method.
  **Correction**: "If the other builder methods take/return a mutable borrow, the complex configuration case will work well, but one-liner configuration becomes impossible." For consuming builders, use owned `self` throughout. (C-BUILDER)

# Common Confusions

- **Confusion**: Thinking newtypes add runtime overhead.
  **Clarification**: Newtypes are zero-cost abstractions -- they are erased at compile time and add no runtime cost. The C-NEWTYPE guideline calls them a "no-cost way to wrap existing types with a distinguished name."

- **Confusion**: Thinking consuming builders are always inferior to non-consuming builders.
  **Clarification**: Consuming builders are necessary "sometimes builders must transfer ownership when constructing the final type `T`" -- for example when the builder holds an `io::Write` that must be moved into the constructed value.

- **Confusion**: Thinking the builder type must be named `TBuilder`.
  **Clarification**: "When possible, choose a better name: e.g. `Command` is the builder for a child process, `Url` can be created from a `ParseOptions`."

# Source Reference

Chapter 7: Type Safety -- guidelines C-NEWTYPE (newtypes provide static distinctions), C-CUSTOM-TYPE (arguments convey meaning through types), C-BITFLAG (types for flag sets are bitflags), C-BUILDER (builders enable construction of complex values). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 7 of the Rust API Guidelines
- Confidence rationale: HIGH -- the source provides detailed code examples and clear rationale for each guideline
- Uncertainties: None -- guidelines are well-established and stable
- Cross-reference status: api-guidelines-overview referenced but not yet in this extraction set; will be created by another agent
