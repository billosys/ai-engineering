---
# === CORE IDENTIFICATION ===
concept: Lint Declaration
slug: lint-declaration

# === CLASSIFICATION ===
category: lint-development
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "03-lint-basics"
chapter_number: 3
pdf_page: null
section: "Lint declaration"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "declare_clippy_lint!"
  - "lint definition"
  - "declare_clippy_lint macro"
  - "lint declaration macro"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adding-a-lint
  - clippy-lint-levels
extends: []
related:
  - lint-registration
  - lint-pass
  - clippy-lint-groups
  - clippy-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I declare a new Clippy lint?"
  - "What is the declare_clippy_lint! macro?"
  - "What are the required parts of a lint declaration?"
  - "How do I document a lint?"
  - "What does the clippy::version attribute do?"
---

# Quick Definition

`declare_clippy_lint!` is the macro used to formally define a Clippy lint, specifying its name, category (which determines default lint level), description, version, and documentation. It produces the lint constant and documentation that appears in the Clippy lint list.

# Core Definition

The source describes lint declaration as updating the auto-generated `declare_clippy_lint!` macro to have a real description. The macro has four essential components:

1. **Documentation** (lines prefixed with `///`): Structured doc comments following a `What it does` / `Why is this bad?` / `Example` format
2. **Version attribute** (`#[clippy::version = "..."]`): The Rust version in which the lint was developed
3. **Lint name** (e.g., `FOO_FUNCTIONS`): The ALL_CAPS constant name, following lint naming conventions
4. **Category** (e.g., `pedantic`): Determines the default lint level (pedantic maps to Allow)
5. **Description string**: A brief text explaining what is wrong with the matched code

The full macro structure:

```rust
declare_clippy_lint! {
    /// ### What it does
    /// Checks for ... (describe what the lint matches).
    ///
    /// ### Why is this bad?
    /// Supply the reason for linting the code.
    ///
    /// ### Example
    /// ```rust,ignore
    /// // A short example of code that triggers the lint
    /// ```
    ///
    /// Use instead:
    /// ```rust,ignore
    /// // A short example of improved code that doesn't trigger the lint
    /// ```
    #[clippy::version = "1.29.0"]
    pub FOO_FUNCTIONS,
    pedantic,
    "function named `foo`, which is not a descriptive name"
}
```

After declaration, the lint pass struct is declared with `declare_lint_pass!`:
```rust
declare_lint_pass!(FooFunctions => [FOO_FUNCTIONS]);
```

This macro generates the struct and links it to the declared lint(s). For lints with configuration, the struct must be defined manually using `impl_lint_pass!` instead.

# Prerequisites

- **adding-a-lint** -- Lint declaration is one step in the overall lint creation process.
- **clippy-lint-levels** -- The category field maps to a default lint level (e.g., pedantic -> Allow, style -> Warn).

# Key Properties

1. `declare_clippy_lint!` is the only way to declare a Clippy lint
2. The documentation section uses three required headings: `What it does`, `Why is this bad?`, `Example`
3. For `restriction` group lints, replace "Why is this bad?" with "Why restrict this?" to avoid awkward phrasing
4. The `#[clippy::version]` attribute should be the current Rust version without `-nightly` suffix (retrieved via `rustc -vV`)
5. The lint name must be in ALL_CAPS (e.g., `FOO_FUNCTIONS`) and follow lint naming conventions
6. The category determines the default lint level via category-to-level mapping
7. The description string should explain what is wrong with the code in a concise phrase
8. `declare_lint_pass!` generates the pass struct; `impl_lint_pass!` is used when the struct needs custom fields (e.g., configuration)
9. The documentation is rendered on the Clippy lint list website and can be previewed with `cargo dev serve`
10. A single `declare_lint_pass!` can link multiple lint names to one struct: `declare_lint_pass!(MyPass => [LINT_A, LINT_B])`

# Construction / Recognition

## To Write a Lint Declaration:
1. Start with the generated boilerplate from `cargo dev new_lint`
2. Fill in the `What it does` section: describe what code patterns the lint detects
3. Fill in the `Why is this bad?` section: explain why the pattern is problematic (or `Why restrict this?` for restriction lints)
4. Fill in the `Example` section with a bad code example and a "Use instead" good example
5. Set `#[clippy::version]` to the current Rust release version (run `rustc -vV` to check)
6. Set the lint name to an ALL_CAPS identifier that follows naming conventions
7. Choose the category: `correctness`, `suspicious`, `style`, `complexity`, `pedantic`, `restriction`, `nursery`, `cargo`
8. Write a concise description string

## To Add Configuration to a Declared Lint:
1. Replace `declare_lint_pass!` with a manual struct definition and `impl_lint_pass!`:
   ```rust
   pub struct StructName { configuration_ident: Type }
   impl_lint_pass!(StructName => [LINT_NAME]);
   ```
2. Add a constructor that reads from `Conf`:
   ```rust
   impl StructName {
       pub fn new(conf: &'static Conf) -> Self {
           Self { configuration_ident: conf.configuration_ident }
       }
   }
   ```
3. Add the configuration entry to `clippy_config::conf`
4. Update registration to pass configuration: `store.register_*_pass(move || Box::new(module::StructName::new(conf)));`

## To Recognize a Lint Declaration:
1. Look for `declare_clippy_lint! { ... }` blocks
2. The ALL_CAPS name after `pub` is the lint constant
3. The word after the comma is the category
4. The string at the end is the description

# Context & Application

Lint declarations serve dual purposes: they define the lint constant used in code and generate the user-facing documentation. The structured doc comment format (`What it does` / `Why is this bad?` / `Example`) is rendered on the [Clippy lint list](https://rust-lang.github.io/rust-clippy/master/index.html), making it the primary reference for users.

The category-to-level mapping determines the lint's default behavior:
- `correctness` -> Deny (these catch real bugs)
- `suspicious`, `style`, `complexity` -> Warn
- `pedantic`, `restriction`, `nursery`, `cargo` -> Allow

**Configuration support**: Some lints accept configuration through `clippy.toml`. This requires replacing the generated `declare_lint_pass!` with a manual struct definition using `impl_lint_pass!`, adding configuration fields, and reading values from `Conf` in a constructor. Configuration is searched for in `CLIPPY_CONF_DIR`, `CARGO_MANIFEST_DIR`, or the current directory.

**Testing configuration**: Default values are tested in `tests/ui`; configured values are tested separately in `tests/ui-toml` with a `clippy.toml` file alongside the test.

# Examples

**Example 1**: Basic lint declaration:
```rust
declare_clippy_lint! {
    /// ### What it does
    /// Checks for functions named `foo`.
    ///
    /// ### Why is this bad?
    /// `foo` is not a descriptive name.
    ///
    /// ### Example
    /// ```rust,ignore
    /// fn foo() { }
    /// ```
    /// Use instead:
    /// ```rust,ignore
    /// fn descriptive_name() { }
    /// ```
    #[clippy::version = "1.29.0"]
    pub FOO_FUNCTIONS,
    pedantic,
    "function named `foo`, which is not a descriptive name"
}
```

**Example 2**: Lint pass declaration linking lint to struct:
```rust
declare_lint_pass!(FooFunctions => [FOO_FUNCTIONS]);
impl EarlyLintPass for FooFunctions {}
```

**Example 3**: Manual struct with configuration (replacing `declare_lint_pass!`):
```rust
pub struct StructName {
    configuration_ident: Type,
}

impl_lint_pass!(StructName => [LINT_NAME]);

impl StructName {
    pub fn new(conf: &'static Conf) -> Self {
        Self {
            configuration_ident: conf.configuration_ident,
        }
    }
}
```

# Relationships

## Builds Upon
- **adding-a-lint** -- Lint declaration is a step in the lint creation workflow
- **clippy-lint-levels** -- The category determines the lint's default level

## Enables
- **lint-registration** -- The declared lint must be registered to be active
- **lint-pass** -- The `declare_lint_pass!` macro generates the struct that implements a pass

## Related
- **clippy-lint-groups** -- Categories correspond to lint groups visible to users
- **clippy-configuration** -- Configurable lints replace `declare_lint_pass!` with `impl_lint_pass!` and a custom struct
- **clippy-lint-naming** -- The lint name in the declaration must follow naming conventions

# Common Errors

- **Error**: Forgetting to update the `#[clippy::version]` attribute to the current version.
  **Correction**: Run `rustc -vV` in the rust-clippy directory and use the version listed under `release` (without the `-nightly` suffix).

- **Error**: Using `declare_lint_pass!` when the lint needs configuration fields.
  **Correction**: Define the struct manually and use `impl_lint_pass!` instead, adding the configuration fields and a constructor.

- **Error**: Leaving the generated placeholder documentation in the `declare_clippy_lint!` macro.
  **Correction**: Fill in all three sections (`What it does`, `Why is this bad?`, `Example`) with real content before submitting a PR.

# Common Confusions

- **Confusion**: Thinking `declare_clippy_lint!` and `declare_lint_pass!` are the same macro.
  **Clarification**: `declare_clippy_lint!` declares the lint itself (name, category, docs). `declare_lint_pass!` declares the struct that implements the lint pass and links it to one or more lints.

- **Confusion**: Believing the category in the declaration is just a label.
  **Clarification**: The category determines the default lint level. Choosing `pedantic` means the lint is Allow by default; choosing `correctness` means it is Deny by default. This has real impact on users.

- **Confusion**: Assuming every lint needs its own `declare_lint_pass!`.
  **Clarification**: Multiple lints can share a single pass struct: `declare_lint_pass!(MyPass => [LINT_A, LINT_B, LINT_C])`. This is common in type-specific lint groups.

# Source Reference

Chapter 3: Lint Basics, sections "Lint declaration", "The declare_clippy_lint macro", "Documentation", and "Adding configuration to a lint". The declaration macro is shown in the "Adding a new lint" walkthrough and again in the "Define New Lints" chapter with additional detail.

# Verification Notes

- Macro structure: Directly reproduced from the source with all four components
- Doc format: Source specifies `What it does` / `Why is this bad?` / `Example` with explicit note about `Why restrict this?` for restriction lints
- Version attribute: Source says "retrieved by running `rustc -vV`" and "use the version without the -nightly suffix"
- declare_lint_pass vs impl_lint_pass: Source shows both patterns with configuration example
- Category mapping: Referenced but detailed mapping is in another chapter (linked as `category_level_mapping`)
- Confidence: HIGH -- the macro format is shown multiple times with detailed explanation of each component
- Cross-references: All slugs verified against planned extractions across agents
