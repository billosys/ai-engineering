---
# === CORE IDENTIFICATION ===
concept: Rustdoc Internals
slug: rustdoc-internals

# === CLASSIFICATION ===
category: compiler-internals
subcategory: documentation-tooling
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Rustdoc internals"
chapter_number: 11
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustdoc implementation"
  - "rustdoc passes"
  - "rustdoc clean AST"
  - "rustdoc search index"
  - "rustdoc HTML rendering"
  - "rustdoc-html test suite"
  - "rustdoc-json test suite"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiler-hir
  - compiler-syntax-and-ast
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does rustdoc convert a Rust crate into HTML documentation?"
  - "What is the 'clean' AST and how does it relate to the HIR?"
  - "What passes does rustdoc run over the cleaned AST?"
  - "How does rustdoc's search index work and what format does it use?"
  - "How does rustdoc handle cross-crate inlining of documentation?"
  - "What is the relationship between DocContext, run_global_ctxt, and the rendering pipeline?"
  - "How are rustdoc tests (rustdoc-html, rustdoc-js, rustdoc-gui, rustdoc-json) organized?"
  - "What role does TyCtxt play in rustdoc's HTML generation?"
---

# Quick Definition

Rustdoc is Rust's documentation generator, implemented as a compiler tool that transforms crate source into HTML (or JSON) documentation. Its pipeline has two major phases: (1) converting the compiler's HIR and type information into a "clean" AST -- a simplified, documentation-oriented intermediate representation -- and (2) rendering that clean AST into HTML pages. Between these phases, a series of passes run over the clean AST to resolve intra-doc links, strip private items, collect trait implementations, and run lints.

# Core Definition

Rustdoc's pipeline begins in `core.rs` with `DocContext` (a state container) and `run_global_ctxt` (which invokes `rustc` to compile the crate up to the point where rustdoc can take over). The crate crawling process uses `visit_ast::RustdocVisitor` to walk the `rustc_middle::hir::Crate`, handling `#[doc(inline)]`, `#[doc(no_inline)]`, import globs/cycles, re-exports, and `#[macro_export]`. This produces an intermediate `visit_ast::Module`.

Next, `clean_doc_module` converts HIR items into the "clean" AST -- a documentation-oriented representation defined in `clean/mod.rs`. Each `clean_*` function accepts an HIR or `ty` data structure and outputs the corresponding clean type. Cross-crate inlining is performed at this stage, converting `rustc_middle` data structures into clean AST. The primary output is a `clean::types::Crate` containing a tree of `Item`s.

Several passes then run over the cleaned AST (in `librustdoc/passes`): `collect-intra-doc-links` resolves link syntax, `collect-trait-impls` gathers implementations, `strip-hidden` and `strip-private` remove non-public items (skippable via `--document-private-items`), `propagate-doc-cfg` distributes `#[doc(cfg(...))]`, and `run-lints` checks for bare URLs, invalid HTML, and code block syntax errors.

For rendering, `formats::renderer::run_format` drives the `FormatRenderer` trait (implemented by `Context` for HTML). The `init` method generates static files and the search index, `item` generates per-item HTML pages via Askama templates and `write!()` calls, and `after_krate` generates global resources like `all.html`. Hand-written documentation is processed through `html/markdown.rs`, which interfaces with a Markdown parser and applies syntax highlighting to Rust code blocks.

Notably, rustdoc now has access to `TyCtxt` during HTML generation, enabling queries into the compiler's type information. However, the clean AST remains necessary because (a) docs can be generated for crates that do not pass type checking (e.g., multi-platform libstd docs), and (b) cross-crate inlining requires generating docs from `rustc_middle` metadata, which lacks HIR.

# Prerequisites

Understanding of the HIR, the query system, and basic Rust compiler architecture. Familiarity with the AST-to-HIR pipeline is helpful for understanding the "clean" layer.

# Key Properties

1. **Two-phase pipeline**: Crate-to-clean (crawling and converting HIR/types to documentation-oriented IR) followed by clean-to-HTML (rendering pages from the clean AST)
2. **Clean AST as a common format**: Acts as the output format for both HIR-based and `rustc_middle`-based (cross-crate) documentation sources
3. **Pass-based transformation**: Multiple passes run on the cleaned AST for intra-doc link resolution, privacy stripping, trait impl collection, `cfg` propagation, and linting
4. **Search index**: A compact JSON format using parallel arrays, VLQ hex encoding, and roaring bitmaps for space-efficient representation of item names, types, function signatures, and descriptions
5. **Name-based search**: Uses edit distance (like a regex-style NFA) plus substring matching, path checking, and type filtering for ranking results
6. **Type-based search**: Two-phase approach with a bloom filter for quick rejection followed by recursive type unification for precise matching
7. **Doctest extraction**: Rustdoc can run doctests by performing a simplified crate walk to extract hand-written documentation, scanning for Rust code blocks, and passing them to the test runner
8. **TyCtxt access during rendering**: The rendering phase can query the compiler's type context directly, though the clean AST still serves as the primary data source

# Construction / Recognition

## Rustdoc's main pipeline:
1. `run_global_ctxt` compiles the crate and creates a `DocContext`
2. `visit_ast::RustdocVisitor` crawls the HIR, resolving re-exports and inlining
3. `clean_doc_module` converts HIR items to the clean AST
4. Passes run over the clean AST (link resolution, stripping, linting)
5. `run_format` drives HTML rendering via `Context`
6. Per-item pages are generated via `print_item` and Askama templates
7. Markdown processing and syntax highlighting happen in `html/markdown.rs`

## Search index format:
The search index is a JSON file with parallel arrays: `n` (names), `t` (item types), `q` (parent modules), `i` (parent types), `f` (function signatures in VLQ hex), `p` (type dictionary), `c`/`e` (roaring bitmaps for deprecation and empty descriptions), and `D` (description shard list).

# Context & Application

Rustdoc serves as both a documentation generator and a doctest runner. Its architecture demonstrates how compiler internals can be reused for tooling -- it leverages the full compilation pipeline up to HIR/type information, then diverges into its own clean AST and rendering system.

Understanding rustdoc internals is important for:
- Contributing documentation improvements to the Rust project
- Understanding how cross-crate documentation inlining works
- Debugging issues with intra-doc links or `#[doc(cfg)]` propagation
- Writing or debugging the search functionality
- Contributing to the rustdoc-json output format (unstable)

# Examples

**Example 1** (Ch. 11, "From crate to clean"): The `clean_lifetime` function illustrates the pattern of converting HIR types to clean types:
```rust,ignore
fn clean_lifetime<'tcx>(lifetime: &hir::Lifetime, cx: &mut DocContext<'tcx>) -> Lifetime {
    if let Some(
        rbv::ResolvedArg::EarlyBound(did)
        | rbv::ResolvedArg::LateBound(_, _, did)
        | rbv::ResolvedArg::Free(_, did),
    ) = cx.tcx.named_bound_var(lifetime.hir_id)
        && let Some(lt) = cx.args.get(&did).and_then(|arg| arg.as_lt())
    {
        return lt.clone();
    }
    Lifetime(lifetime.ident.name)
}
```

**Example 2** (Ch. 11, "Search index"): A search index entry for a crate with a function and struct:
```json
[ "crate_name", {
    "n": ["function_name", "Data"],
    "t": "HF",
    "q": [[0, "crate_name"]],
    "i": [2, 0],
    "p": [[1, "i32"], [1, "str"], [5, "Data", 0]],
    "f": "{{gb}{d}}`"
}]
```
This defines `function_name` with signature `Data, i32 -> str` and a struct `Data`.

**Example 3** (Ch. 11, "Testing"): Testing the generated HTML with HtmlDocCk directives:
```rust,ignore
//@ has file/type.Alias.html
//@ has - '//*[@class="rust item-decl"]//code' 'type Alias = Option<i32>;'
pub type Alias = Option<i32>;
```

**Example 4** (Ch. 11): Testing locally by running a local HTTP server:
```console
$ ./x doc library
$ python3 -m http.server -d build/[YOUR ARCH]/doc
```

# Relationships

## Builds Upon
- **compiler-hir** -- rustdoc crawls the HIR to build its clean AST
- **compiler-syntax-and-ast** -- the parsed AST feeds into the HIR that rustdoc processes

## Enables
(none within this extraction set -- rustdoc is an end-user tool)

## Related
- **compiler-hir** -- the clean AST mirrors many HIR structures but with documentation-oriented simplifications

## Contrasts With
(none within this source)

# Common Errors

- **Error**: Assuming rustdoc only works with type-checked code.
  **Correction**: Rustdoc can generate docs for crates that do not pass type checking, such as multi-platform configurations of `libstd`. This is why the clean AST exists as a common format for both HIR and `rustc_middle` data sources.

- **Error**: Expecting negated HtmlDocCk checks (`//@ !has`) to reliably catch regressions.
  **Correction**: Negative checks are fragile because changes to the HTML structure can silently invalidate the XPath, causing the check to pass vacuously. Always pair negated checks with analogous positive checks.

- **Error**: Thinking the search index is a standard human-readable JSON format.
  **Correction**: The search index uses highly compressed formats (VLQ hex, roaring bitmaps, parallel arrays) optimized for DEFLATE compression and in-memory efficiency, not human readability.

# Common Confusions

- **Confusion**: The clean AST is the same as the compiler's AST or HIR.
  **Clarification**: The clean AST is rustdoc's own intermediate representation, purpose-built for documentation. It strips away compiler-specific details and adds documentation-specific data like collected doc comments and `#[doc]` attributes.

- **Confusion**: Rustdoc generates documentation purely from source text.
  **Clarification**: Rustdoc leverages the full compilation pipeline (parsing, macro expansion, name resolution, type checking) and can query `TyCtxt` even during HTML generation. It uses compiler data structures extensively.

- **Confusion**: The search index stores descriptions inline with all other data.
  **Clarification**: Descriptions are stored in separate shards and loaded on demand after the initial search completes. This "sandwich workload" design (download index, search, download descriptions) optimizes perceived latency.

# Source Reference

Chapter 11 of the Rust Compiler Dev Guide (1159 lines). Covers rustdoc's two-phase pipeline (crate-to-clean, clean-to-HTML), the passes system, the search index format (parallel arrays, VLQ hex, roaring bitmaps, type-based search), testing infrastructure (rustdoc-html with HtmlDocCk/XPath, rustdoc-js for search, rustdoc-gui with puppeteer, rustdoc-json with jsondocck), and re-export handling.

# Verification Notes

- Definition source: Directly extracted from Chapter 11 "Rustdoc internals", "Rustdoc search", and associated test suite sections
- Key Properties: All derived from explicit descriptions in the source text
- Confidence rationale: HIGH -- official compiler team documentation describing the current rustdoc architecture
- Uncertainties: Some details may shift as the clean AST is gradually soft-deprecated in favor of direct TyCtxt queries
- Cross-reference status: Related cards reference HIR and AST from this extraction set
