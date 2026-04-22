---
# === CORE IDENTIFICATION ===
concept: Rust Compiler Query System and Incremental Compilation
slug: rustc-compiler-query-system

# === CLASSIFICATION ===
category: compiler-internals
subcategory: architecture
tier: intermediate

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Queries"
chapter_number: 10
pdf_page: null
section: "Query System, Query Evaluation Model, Incremental Compilation, Red-Green Algorithm, Salsa"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "query system"
  - "demand-driven compilation"
  - "incremental compilation"
  - "red-green algorithm"
  - "try-mark-green"
  - "query providers"
  - "query memoization"
  - "dependency graph"
  - "dep-graph"
  - "Fingerprint"
  - "HashStable"
  - "DefPath"
  - "Salsa"
  - "query modifiers"
  - "eval_always"
  - "no_hash"
  - "cache_on_disk"
  - "Steal queries"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rustc-compiler-overview
extends: []
related:
  - rustc-compiler-overview
  - rustc-compiler-bootstrapping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the query system in rustc and why does it exist?"
  - "How does demand-driven compilation differ from pass-based compilation?"
  - "How does incremental compilation work in rustc?"
  - "What is the red-green algorithm and try-mark-green?"
  - "What are query providers and how are they registered?"
  - "How do queries interact with external crate metadata?"
  - "How do I add a new query to the compiler?"
  - "What are query modifiers (eval_always, no_hash, cache_on_disk)?"
  - "What is the projection query pattern?"
  - "How does the dependency graph enable incremental compilation?"
  - "What are Fingerprints and HashStable?"
  - "What is Salsa and how does it relate to rustc?"
  - "What happens when a query cycle is detected?"
  - "What are Steal queries and when should they be used?"
  - "How are DefPaths used for cross-session stability?"
---

# Quick Definition

Rustc's query system replaces traditional sequential compiler passes with a set of memoized, demand-driven functions that compute information about the source code. Instead of running parsing, then type-checking, then codegen in order, the compiler defines queries like `type_of(DefId)` that compute results on-demand and cache them. This enables **incremental compilation**: on recompilation, the system uses the **red-green algorithm** to determine which cached results are still valid (green) and which have changed (red), re-executing only the minimum necessary queries. Query results are persisted to disk alongside a dependency DAG that tracks which queries depend on which other queries.

# Core Definition

The query system is "the key to rustc's demand-driven organization." Each query is conceptually a pure function that maps a key to a result. For example, `type_of` takes a `DefId` and returns the type of that item. Queries are invoked as methods on `TyCtxt`: `let ty = tcx.type_of(some_def_id)`.

## Query Execution and Memoization

When a query is invoked, the system checks its cache. If a result exists, it is cloned and returned (so return types should be cheaply cloneable -- "insert an `Rc` if necessary"). If not cached, the system calls the query's **provider** function, which computes the result and may itself invoke other queries.

Providers are **defined per-crate** and registered as function pointers in the `Providers` struct (for local crate queries) and `ExternProviders` struct (for external crate queries). These are "not Rust traits, but plain structs with function pointer fields." Most external providers go through `rustc_metadata`, which loads information from `.rmeta` files. Whether a query targets the local or external crate is determined by the key's `DefId`, not the query kind.

## Incremental Compilation: The Red-Green Algorithm

After each compilation, the compiler saves query results and the **query DAG** (a directed acyclic graph of which queries invoked which other queries). On the next compilation, each query is assigned a **color**:

- **Green**: Result is the same as the previous compilation -- can be reused
- **Red**: Result has changed -- dependents must be re-executed

The core algorithm is **try-mark-green**: Given a query Q that hasn't been executed yet, it recursively checks Q's dependencies. If all dependencies are green, Q must also be green (without re-executing it). If any dependency is red, Q is re-executed and its new result is compared to the old one. Crucially, "even if some inputs to a query changes, it may be that it still produces the same result" -- if so, Q is still marked green, preventing unnecessary re-execution of Q's dependents. This eliminates false positives that would cascade through the dependency graph.

The dependency DAG preserves **ordering** of query invocations because "once a subquery comes back as red, we can no longer be sure that Q will continue along the same path as before" -- different inputs might cause the query to take different branches.

## Persistence and Stability

Between sessions, the compiler must bridge the gap between different ID assignments. `DefId`s (numeric IDs) are unstable across sessions -- adding a function can shift all subsequent IDs. The solution is `DefPath` (path-based identifiers like `std::collections::HashMap`) and `DefPathHash` (128-bit hash of the DefPath). On-disk caches store `DefPathHash` values, which are mapped back to current-session `DefId`s via hash table lookup.

Result comparison uses **Fingerprints**: 128-bit hashes computed via the `HashStable` infrastructure. Instead of comparing full results (which would require loading them from disk), the system compares fingerprints. This introduces a small collision risk, mitigated by using "a high-quality hash function and a 128 bit wide hash value."

## Query Modifiers

Queries support modifiers that affect incremental behavior:
- **`eval_always`**: Re-executed unconditionally; used for queries that read external input or whose results depend on the entire source
- **`no_hash`**: Skips fingerprint computation; dependents are always re-executed; useful when the result almost certainly changes with any input change
- **`cache_on_disk`**: Results are persisted to disk for cross-session reuse
- **`separate_provide_extern`**: When combined with `cache_on_disk`, only caches local keys (external values come from crate metadata)

# Prerequisites

Understanding of the Rust compiler's overall architecture and intermediate representations (see `rustc-compiler-overview`). Familiarity with graph theory concepts (DAGs, graph coloring). Basic understanding of memoization and caching.

# Key Properties

1. **Pure function requirement**: Query providers must be pure -- same key always yields same result; only parameters are the key and `TyCtxt`
2. **Immutable results**: Query key and result must be immutable values; results should be cheaply cloneable
3. **DAG structure**: Query invocations form a directed acyclic graph; cycles are detected and reported as errors
4. **Ordered dependency tracking**: The DAG tracks not just which queries were called but the order, to ensure correctness when re-evaluating
5. **Two-graph model**: At runtime, an immutable old dep-graph (from disk) and a new dep-graph (being built) coexist; green nodes are copied from old to new
6. **Cache promotion**: Before persisting the new result cache, the compiler loads all green dep-nodes' results into memory to prevent unnecessary cache shrinkage
7. **`Steal<T>` mechanism**: Some expensive results (e.g., function MIR) can be "stolen" from the cache for ownership transfer; all readers must be eagerly run first
8. **Provider registration**: Each `rustc_*` crate exposes a `provide` function that fills in the `Providers` struct during initialization
9. **Cross-crate queries**: Require both a local provider and an external provider in `rustc_metadata`, plus encoding/decoding in crate metadata
10. **Projection query pattern**: A monolithic query (e.g., `index_hir`) combined with projection queries (e.g., `hir_owner`) creates change-propagation firewalls -- even if the monolith changes, individual projections may remain green

# Construction / Recognition

## To Add a New Query:

1. Add an entry to `rustc_queries!` in `compiler/rustc_middle/src/query/mod.rs`:
```rust
rustc_queries! {
    /// Records the type of every item.
    query type_of(key: DefId) -> Ty<'tcx> {
        desc { |tcx| "computing the type of `{}`", tcx.def_path_str(key) }
        cache_on_disk
        separate_provide_extern
    }
}
```

2. Implement the provider function in the owning crate:
```rust
fn fubar<'tcx>(tcx: TyCtxt<'tcx>, key: LocalDefId) -> Fubar<'tcx> { ... }
```

3. Register it in the crate's `provide` function:
```rust
pub fn provide(providers: &mut query::Providers) {
    *providers = query::Providers {
        fubar,
        ..*providers
    };
}
```

4. For cross-crate queries, also add an external provider in `rustc_metadata` via `provide_extern`.

## Query Definition Anatomy:

```rust
query type_of(key: DefId) -> Ty<'tcx> { ... }
//    ^^^^^^^      ^^^^^     ^^^^^^^^   ^^^
//    name         key type  result     modifiers
```

## The try-mark-green Algorithm (Simplified):

1. Was Q executed in the previous session? If not, re-execute (red).
2. Load `reads(Q)` -- the queries Q depended on last time.
3. For each dependency R (in original order):
   - If R is green, continue.
   - If R is unknown, recursively try-mark-green on R.
   - If R turns red, re-execute Q and compare its result hash.
4. If all dependencies are green, mark Q as green without re-executing.

# Context & Application

- **Compiler contributors**: Every new analysis or transformation should be implemented as a query for incremental compilation support
- **Performance optimization**: The projection query pattern (`eval_always` + `no_hash` monolith with projection queries) creates change-propagation firewalls that prevent unnecessary recomputation
- **Debugging incremental issues**: Use `-Z dump-dep-graph` to dump the dependency graph, `RUST_DEP_GRAPH_FILTER` to filter it, and `RUST_FORBID_DEP_GRAPH_EDGE` to trace incorrect edges
- **Testing dependencies**: Use `#[rustc_if_this_changed]` and `#[rustc_then_this_would_need]` annotations in UI tests to verify expected dependency paths
- **Tool integration**: The Salsa library implements similar concepts and is used by rust-analyzer; not currently used in rustc itself but shares the same theoretical foundation

# Examples

**Example 1**: Query invocation DAG showing execution order and caching:
```
         (2)                                     (1)
  list_of_all_hir_items <--------------------- type_check_crate()
                                                       |
    (5)             (4)              (3)               |
  Hir(foo) <--- type_of(foo) <--- type_check_item(foo) <--+
                                      |                    |
                    +-----------------+                    |
                    |                                      |
    (7)             v  (6)              (8)                |
  Hir(bar) <--- type_of(bar) <--- type_check_item(bar) <--+

// type_of(bar) computed for type_check_item(foo) is cached
// and reused by type_check_item(bar)
```

**Example 2**: The projection query pattern as a change-propagation firewall:
```
  +------------+
  | monolithic |  <--- projection(x) <--- foo(a)   [x changed: red -> re-execute foo]
  |   query    |  <--- projection(y) <--- bar(b)   [y unchanged: green -> skip bar]
  | (no_hash,  |  <--- projection(z) <--- baz(c)   [z unchanged: green -> skip baz]
  | eval_always)|
  +------------+
```

**Example 3**: Testing dependency graph edges:
```rust
#[rustc_if_this_changed]
fn foo() { }

#[rustc_then_this_would_need(TypeckTables)] //~ ERROR OK
fn bar() { foo(); }

#[rustc_then_this_would_need(TypeckTables)] //~ ERROR no path
fn baz() { }
```

**Example 4**: Debugging the dependency graph:
```bash
# Dump all edges reaching TypeckTables nodes for functions containing "bar"
RUST_DEP_GRAPH_FILTER='-> TypeckTables & bar' rustc ...

# Find edges between Hir(foo) and TypeckTables(bar)
RUST_DEP_GRAPH_FILTER='Hir & foo -> TypeckTables & bar' rustc ...

# Trigger a bug! when an incorrect edge is created
RUST_FORBID_DEP_GRAPH_EDGE='Hir&foo -> Collect&bar' rustc ...
```

# Relationships

## Builds Upon
- **rustc-compiler-overview** -- the query system implements the demand-driven architecture described in the overview

## Enables
- All downstream compiler work benefits from the query system's memoization and incremental compilation capabilities

## Related
- **rustc-compiler-overview** -- provides the architectural context in which the query system operates
- **rustc-feature-lifecycle** -- feature gating and stability attributes are checked within query providers

## Contrasts With
- None within this source, though the system is contrasted with traditional "pass-based" compilation throughout

# Common Errors

- **Error**: Creating a query with mutable or non-deterministic results.
  **Correction**: "The key and result must be immutable values" and "the provider function must be a pure function in the sense that for the same key it must always yield the same result." Non-deterministic providers break incremental compilation soundness.

- **Error**: Adding new uses of `Steal<T>` without team approval.
  **Correction**: "New uses of `Steal` should **not** be added without alerting `@rust-lang/compiler`." Steal queries require manual coordination to ensure all readers run before the result is stolen.

- **Error**: Visiting dependencies out of order during incremental checking.
  **Correction**: Dependencies must be visited in the same order as the original compilation because "once a subquery comes back as red, we can no longer be sure that Q will continue along the same path as before."

# Common Confusions

- **Confusion**: The query system replaces all sequential compilation.
  **Clarification**: "The compiler wasn't originally built to use a query system; the query system has been retrofitted." Only steps between HIR and LLVM-IR are currently query-driven. Lexing, parsing, name resolution, and macro expansion are still done all-at-once. LLVM isn't querified either.

- **Confusion**: If an input changes, all transitive dependents must be re-executed.
  **Clarification**: The red-green algorithm prevents this. "Even if some inputs to a query changes, it may be that it still produces the same result." When a re-executed query produces the same result, it is marked green, stopping the propagation of changes to its dependents.

- **Confusion**: Salsa is used in the Rust compiler.
  **Clarification**: "Although Salsa is inspired by (among other things) rustc's query system, it is not used directly in rustc." Salsa is used in rust-analyzer and chalk, but "there are no medium or long-term concrete plans to integrate it into the compiler."

- **Confusion**: `DefId` is stable across compilation sessions.
  **Clarification**: `DefId` is a numeric ID that "depends on the contents of the source code being compiled" and can shift when code is added or removed. Cross-session stability uses `DefPath` (path-based, e.g., `std::collections::HashMap`) or `DefPathHash` (128-bit hash of DefPath).

- **Confusion**: `no_hash` means the query result is not cached.
  **Clarification**: `no_hash` only skips fingerprint computation. The result is still cached and memoized within a session. But without a fingerprint, "the system has to unconditionally assume that the result of the query has changed" in incremental mode, making all dependents re-execute.

# Source Reference

Chapter 10: Queries (1646 lines). Covers the query system design and invocation, query providers and registration, adding new queries, cross-crate query metadata interaction, the query evaluation model (DAG, memoization, cycles, Steal queries), incremental compilation (red-green algorithm, try-mark-green, persistence, DefPath stability, Fingerprints, HashStable, query modifiers, projection query pattern, shortcomings), dependency graph debugging and testing, and the Salsa library.

# Verification Notes

- Definition source: Direct quotes from "Queries: demand-driven compilation", "The Query Evaluation Model in detail", "Incremental compilation", and "Incremental compilation in detail" sections
- Key Properties: All items directly supported by source text with algorithm descriptions, code patterns, and architectural explanations
- Confidence rationale: HIGH -- canonical design documentation for rustc's most distinctive architectural feature, with detailed algorithmic descriptions
- Uncertainties: Some implementation details note they are "as of" specific dates and may have evolved; the Salsa section describes an external project whose API may differ from what's shown
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
