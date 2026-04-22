# Performance Guidelines

Patterns for measuring, diagnosing, and improving Rust program performance. Covers methodology (benchmark and profile before optimizing), build configuration (release profile knobs, allocators, LTO, PGO), compile-time performance, heap allocation reduction, hashing, type-size optimization, iterator and inlining tuning, I/O discipline, and async/parallel throughput. Draws heavily on *The Rust Performance Book* (nnethercote et al.) and the Pragmatic Rust M-* guidelines.


## PF-01: Benchmark Before Optimizing

**Strength**: MUST

**Summary**: Establish reproducible benchmarks with representative workloads before changing code in the name of performance. "Mediocre benchmarking is far better than no benchmarking."

```rust
// benches/hot_path.rs  — Criterion harness
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_parse(c: &mut Criterion) {
    let input = include_str!("../testdata/sample.json");
    c.bench_function("parse/sample", |b| {
        b.iter(|| parse(black_box(input)));
    });
}

criterion_group!(benches, bench_parse);
criterion_main!(benches);
```

```toml
# Cargo.toml
[dev-dependencies]
criterion = "0.5"

[[bench]]
name = "hot_path"
harness = false
```

**Rationale**: Wall-time suffers high variance; tiny memory-layout shifts produce ephemeral noise. Criterion and Divan give you statistical distributions; Hyperfine is a general-purpose CLI alternative; Cachegrind/iai-callgrind give lower-variance instruction counts for CI. Benchmark every change in isolation — compound changes mask regressions and interactions.

**See also**: PF-05 (profiling), M-HOTPATH

---

## PF-02: Run Clippy's Perf Lints First

**Strength**: MUST

**Summary**: Clippy catches common performance anti-patterns automatically. Treat its perf lints as the zero-cost first pass before manual optimization.

```rust
// Examples Clippy catches automatically:

// ❌ `ptr_arg` — inflexible and forces extra indirection
fn sum(xs: &mut Vec<i32>) -> i32 { xs.iter().sum() }

// ✅ Clippy's suggested fix
fn sum(xs: &mut [i32]) -> i32 { xs.iter().sum() }

// ❌ `redundant_clone`, `unnecessary_to_owned`, `inefficient_to_string`
let s: String = "hi".to_string().clone();

// ✅
let s: String = "hi".to_string();
```

```toml
# clippy.toml — lock in faster alternatives after a switch
disallowed-types = [
    "std::collections::HashMap",   # we use FxHashMap
    "std::collections::HashSet",   # we use FxHashSet
]
```

**Rationale**: Anything Clippy flags is strictly easier to fix than anything you would find manually. The `disallowed_types` lint is crucial after switching to FxHash or parking_lot — it prevents new code from silently reintroducing the slow default.

**See also**: PF-13 (hashing), Pragmatic Rust M-PERF-LINTS

---

## PF-03: Profile to Find Hot Paths

**Strength**: MUST

**Summary**: Before optimizing, profile a release build with debug info to identify where time is actually spent. Optimizing without profiling is a coin toss.

```toml
# Cargo.toml — minimum profilable release build
[profile.release]
debug = "line-tables-only"   # source mappings for perf/samply/flamegraph
# strip = false              # keep symbols on binaries you profile
```

```bash
# Linux — CPU profile via samply (cross-platform, Firefox Profiler output)
cargo install samply
samply record ./target/release/myapp

# Linux — perf + flamegraph
cargo install flamegraph
cargo flamegraph --release --bin myapp

# Linux — instruction counts (lower variance than wall-time)
valgrind --tool=cachegrind ./target/release/myapp

# Linux — allocations
valgrind --tool=dhat ./target/release/myapp

# macOS — Instruments via samply or Xcode
# Windows — Intel VTune or samply
```

```bash
# Force frame pointers when stack traces are wrong
RUSTFLAGS="-C force-frame-pointers=yes" cargo build --release

# Demangle v0 symbol names when a profiler shows `_RNv...`
RUSTFLAGS="-C symbol-mangling-version=v0" cargo build --release
# or: samply/perf | rustfilt
```

**Rationale**: Different profilers answer different questions — samply/perf for CPU time, Cachegrind for instruction counts and cache behavior, DHAT for allocations, heaptrack for peak memory, Coz for "what if I speed this up?" causal analysis. Use more than one. Shipped stdlib binaries lack debug info; build your own stdlib with `debuginfo-level=1` in `bootstrap.toml` when you need stdlib symbols.

**See also**: PF-05 (Profiling Playbook), Performance Book §4

---

## PF-04: The Optimization Loop

**Strength**: SHOULD

**Summary**: Profile → hypothesize → change *one thing* → benchmark → keep or revert. Never optimize blind; never bundle changes.

```text
1. Benchmark baseline                  (cargo bench / hyperfine)
2. Profile                             (samply, perf, Cachegrind, DHAT)
3. Identify the hottest ≤3 functions or allocation sites
4. Form a hypothesis                   ("this Vec reallocates in a loop")
5. Make ONE change
6. Re-run the benchmark
7. Keep if improved; revert if not
8. Goto 2
```

**Rationale**: The biggest wins come from algorithms and data structures, not micro-optimization. Bundling changes masks which one helped. Two ways to speed up a hot function: (a) make it faster, or (b) call it less often — option (b) is usually easier. Eliminate "silly slowdowns" before attempting "clever speedups."

**See also**: PF-01, Performance Book §17 "General Tips"

---

## PF-05: Release Build vs Dev Build

**Strength**: MUST

**Summary**: Always measure release builds. Dev builds are 10–100× slower, omit optimizations, and include debug assertions — benchmark numbers from `cargo run` or `cargo test` are meaningless.

```bash
# ❌ BAD: dev-build numbers
cargo run                    # unoptimized + debuginfo
cargo bench                  # ok — uses bench profile (opt-level 3)

# ✅ GOOD: release builds for real performance work
cargo run --release
cargo build --release
```

```text
Compiling myapp v0.1.0
    Finished dev [unoptimized + debuginfo]    ← never benchmark this
    Finished release [optimized]              ← this one
```

**Rationale**: Dev builds exist for iteration speed and debugability. They skip inlining, constant folding, vectorization, and monomorphization cleanup. A microbenchmark showing dev-build regressions tells you nothing about production.

---

## PF-06: Release Profile — Maximize Runtime Speed

**Strength**: SHOULD

**Summary**: In the release profile, set `codegen-units = 1`, `lto = "fat"`, `panic = "abort"` (when `catch_unwind` isn't needed), and consider `-C target-cpu=native` for binaries that don't need to be portable.

```toml
# Cargo.toml
[profile.release]
codegen-units = 1       # fewer units → more cross-function optimization
lto = "fat"             # whole-program link-time optimization
panic = "abort"         # smaller binary, tiny speedup; disables catch_unwind
# opt-level = 3         # already the default for release
```

```bash
# Build machine-specific code (AVX/BMI2/etc.) — not portable
RUSTFLAGS="-C target-cpu=native" cargo build --release
```

**Rationale**: `codegen-units = 1` lets LLVM see the whole crate at once; fat LTO extends that across dependencies. Both trade compile time for runtime. `panic = "abort"` saves unwinding code but forbids catching panics across FFI. `target-cpu=native` enables CPU-specific vectorization but pins the binary to the build machine's architecture. Values for `lto`: `false` (default = thin local), `"thin"`, `"fat"`, `"off"` (fully disabled — usually worse).

**See also**: PF-07 (binary size), PF-08 (allocators), Performance Book §2

---

## PF-07: Release Profile — Minimize Binary Size

**Strength**: CONSIDER

**Summary**: For size-constrained builds (WASM, embedded, container images), lower `opt-level` to `"s"` or `"z"`, enable LTO, `panic = "abort"`, and strip symbols.

```toml
[profile.release]
opt-level = "z"         # smallest; "s" also OK and permits loop vectorization
codegen-units = 1
lto = "fat"
panic = "abort"
strip = "symbols"       # discard debug symbols + names
```

**Rationale**: `opt-level = "z"` aggressively minimizes size; `"s"` is slightly larger but keeps loop vectorization. `strip = "symbols"` makes post-mortem debugging and profiling harder — don't use it on builds you might need to profile. See the `min-sized-rust` repo for advanced techniques (nightly `build-std`, custom panic handler, etc.).

---

## PF-08: Consider an Alternative Allocator

**Strength**: SHOULD

**Summary**: For allocation-heavy applications, swap the global allocator for mimalloc or jemalloc. 10–25% speedups are common on allocation-bound workloads, with no code changes.

```toml
# Cargo.toml
[dependencies]
mimalloc = { version = "0.1", default-features = false }
# or:
# tikv-jemallocator = "0.5"
```

```rust
// main.rs — mimalloc
use mimalloc::MiMalloc;

#[global_allocator]
static GLOBAL: MiMalloc = MiMalloc;

fn main() { /* ... */ }
```

```rust
// main.rs — jemalloc (Linux THP tuning via MALLOC_CONF if desired)
#[global_allocator]
static GLOBAL: tikv_jemallocator::Jemalloc = tikv_jemallocator::Jemalloc;
```

**Rationale**: The system allocator varies wildly by platform (glibc malloc, jemalloc, Windows HeapAlloc). mimalloc and jemalloc are optimized for multithreaded server workloads. Gains vary — benchmark both, on the target platform. Library crates should *not* set a global allocator; only top-level binaries should.

**See also**: M-MIMALLOC-APP

---

## PF-09: Profile-Guided Optimization and BOLT

**Strength**: CONSIDER

**Summary**: PGO compiles, runs with profiling instrumentation, then recompiles using the collected profile. Typical wins are 5–15%. BOLT applies similar optimizations at the linker level.

```bash
cargo install cargo-pgo

# 1. Build instrumented binary
cargo pgo build
# 2. Run it on representative workloads
./target/.../myapp <realistic-inputs>
# 3. Rebuild using the collected profile
cargo pgo optimize
# Optional: post-link optimization with BOLT
cargo pgo bolt build --with-pgo
```

**Rationale**: PGO targets what the compiler can't know statically — which branches are hot, which functions to inline, where to lay out code. It is "not supported for binaries hosted on crates.io and distributed via `cargo install`," so it's most applicable to services and first-party deployments. Requires a realistic profiling run; bad profiles produce bad binaries.

**See also**: PF-06, Performance Book §2

---

## PF-10: Speed Up Compile Times — Build Configuration

**Strength**: SHOULD

**Summary**: For the dev loop, use a faster linker (lld, mold, wild), disable debug info if not debugging, and split workspaces to increase build parallelism.

```toml
# .cargo/config.toml — faster linker, no runtime trade-off
[target.x86_64-unknown-linux-gnu]
linker = "clang"
rustflags = ["-C", "link-arg=-fuse-ld=mold"]

[target.aarch64-apple-darwin]
# lld is default since Rust 1.90

# Cargo.toml — dev build that compiles faster
[profile.dev]
debug = false            # 20-40% faster dev builds; lose gdb/lldb info
# opt-level = 1          # optional: slight runtime speedup, moderate compile cost
```

```bash
# Nightly: experimental parallel frontend and Cranelift backend
RUSTFLAGS="-Z threads=8" cargo +nightly build
cargo +nightly build -Z codegen-backend
# config.toml: [profile.dev] codegen-backend = "cranelift"

# cargo check is ~2-5x faster than cargo build; use it as the inner loop
cargo check
cargo clippy
```

**Rationale**: Linker swap is the only lever here with pure upside — mold/wild/lld are strictly faster than bfd. `cargo check` skips codegen entirely. Cranelift (nightly) emits lower-quality code but compiles much faster, so it's good for dev but not production.

**See also**: PF-11

---

## PF-11: Speed Up Compile Times — Code Changes

**Strength**: CONSIDER

**Summary**: Diagnose compile-time bottlenecks with `cargo build --timings`, `cargo llvm-lines`, and `-Zmacro-stats`. Fix LLVM IR bloat by shrinking generic function bodies or extracting non-generic inner functions.

```rust
// ❌ Large generic body → monomorphized N times → lots of LLVM IR
pub fn read<P: AsRef<Path>>(path: P) -> io::Result<Vec<u8>> {
    let mut file = File::open(path.as_ref())?;
    let size = file.metadata().map(|m| m.len()).unwrap_or(0);
    let mut bytes = Vec::with_capacity(size as usize);
    io::default_read_to_end(&mut file, &mut bytes)?;
    Ok(bytes)
}

// ✅ std::fs::read pattern — generic outer, non-generic inner
pub fn read<P: AsRef<Path>>(path: P) -> io::Result<Vec<u8>> {
    fn inner(path: &Path) -> io::Result<Vec<u8>> {
        let mut file = File::open(path)?;
        let size = file.metadata().map(|m| m.len()).unwrap_or(0);
        let mut bytes = Vec::with_capacity(size as usize);
        io::default_read_to_end(&mut file, &mut bytes)?;
        Ok(bytes)
    }
    inner(path.as_ref())
}
```

```bash
# Crate-level serialization analysis — opens an HTML Gantt chart
cargo build --timings

# Per-function LLVM IR output — find monomorphization bloat
cargo install cargo-llvm-lines
cargo llvm-lines --release | head -30

# Macro-generated code volume (nightly)
RUSTFLAGS="-Zmacro-stats" cargo +nightly build
cargo install cargo-expand && cargo expand crate::mymodule
```

**Rationale**: Generic functions are monomorphized per concrete type — a 50-line generic body can become tens of thousands of lines of LLVM IR across instantiations. The "non-generic inner function" pattern keeps the outer function a thin conversion shim and instantiates the real work only once. Replacing `Option::map`/`Result::map_err` with `match` in heavily generic code also measurably reduces IR. Proc-macro-heavy crates (derive-everything, tracing attributes) can dwarf hand-written code volume — measure before blaming the compiler.

**See also**: PF-10, Performance Book §18

---

## PF-12: Avoid `clone()` in Hot Paths

**Strength**: SHOULD

**Summary**: `clone` on a `String`, `Vec`, `HashMap`, or any heap-owning type allocates. In hot loops, prefer references, `Rc`/`Arc`, or restructure ownership.

```rust
// ❌ BAD: clones every iteration
fn process(items: &[Item]) {
    for item in items {
        let owned = item.clone();
        handle(owned);
    }
}

// ✅ Borrow when possible
fn process(items: &[Item]) {
    for item in items {
        handle(item);
    }
}

// ✅ Arc::clone is O(1) — a refcount bump, no data copy
use std::sync::Arc;
fn fan_out(data: Arc<Data>) {
    for _ in 0..N {
        let data = Arc::clone(&data);      // not a deep clone
        tokio::spawn(async move { use_it(&data) });
    }
}

// ✅ clone_from reuses an existing allocation when v already has capacity
let mut v1: Vec<u32> = Vec::with_capacity(99);
let v2: Vec<u32> = vec![1, 2, 3];
v1.clone_from(&v2);                        // reuses v1's buffer
assert_eq!(v1.capacity(), 99);
```

**Rationale**: Cloning to "appease the borrow checker" is a smell — the fix is usually to restructure the data flow (split borrows, take a reference, move ownership earlier). `Rc::clone` and `Arc::clone` are cheap; writing `x.clone()` on an `Rc` works but obscures intent — use `Rc::clone(&x)`. `clone_from` is strictly more efficient than `a = b.clone()` because it can reuse `a`'s buffer.

**See also**: PF-17 (Cow), PF-19 (`&str`/`&[T]` parameters), M-CLONE

---

## PF-13: Reduce Heap Allocations

**Strength**: SHOULD

**Summary**: Allocations involve a global lock, data-structure manipulation, and sometimes a syscall. Reuse buffers, pre-allocate capacity, hoist allocations out of loops, and batch.

```rust
// ❌ Allocates a fresh Vec every call
fn collect_names(items: &[Item]) -> Vec<String> {
    let mut out = Vec::new();
    for it in items {
        out.push(it.name.to_uppercase());   // and a String per item
    }
    out
}

// ✅ Pre-allocate exact capacity
fn collect_names(items: &[Item]) -> Vec<String> {
    let mut out = Vec::with_capacity(items.len());
    for it in items {
        out.push(it.name.to_uppercase());
    }
    out
}

// ✅ Iterator with size_hint → collect pre-allocates correctly
fn collect_names(items: &[Item]) -> Vec<String> {
    items.iter().map(|it| it.name.to_uppercase()).collect()
}

// ✅ Reuse a "workhorse" buffer across iterations
let mut buf = String::with_capacity(128);
for it in items {
    use std::fmt::Write;
    buf.clear();                            // keeps capacity
    write!(buf, "processing {}", it.id).unwrap();
    log_line(&buf);
}

// ✅ Read lines without allocating per line
use std::io::{BufRead, BufReader, stdin};
let mut line = String::new();
let mut r = BufReader::new(stdin().lock());
while r.read_line(&mut line)? != 0 {
    process(&line);
    line.clear();
}
// Contrast with `r.lines()` which allocates a fresh String per line.
```

**Rationale**: `Vec` grows on a quasi-doubling schedule (0 → 4 → 8 → 16 → …). Known sizes should bypass this with `with_capacity`. Buffer reuse trades code clarity for performance — the workhorse buffer "obscures the fact that each iteration's usage is unrelated," which is a conscious trade-off. `BufRead::lines` is ergonomic but allocation-heavy; `read_line` + `clear` cuts allocations to near zero.

**See also**: PF-14 (SmallVec), PF-17 (Cow), PF-19, Performance Book §7

---

## PF-14: Small-Capacity Collections and Arenas

**Strength**: CONSIDER

**Summary**: For collections that are usually small or have a known upper bound, use `SmallVec`, `ArrayVec`, `smallstr`, or bump arenas to skip heap allocation entirely.

```rust
// SmallVec — up to N inline, falls back to heap
use smallvec::{smallvec, SmallVec};
let v: SmallVec<[u32; 8]> = smallvec![1, 2, 3];       // zero allocations
let v: SmallVec<[u32; 8]> = (0..100).collect();       // spills to heap at 9

// ArrayVec — fixed max, NEVER allocates; push returns Err when full
use arrayvec::ArrayVec;
let mut v: ArrayVec<u32, 8> = ArrayVec::new();
v.try_push(1).unwrap();

// bumpalo — arena for many short-lived allocations
use bumpalo::Bump;
let arena = Bump::new();
let items: &mut [i32] = arena.alloc_slice_copy(&[1, 2, 3]);
let s: &str = arena.alloc_str("hello");
// Everything freed together when `arena` drops.

// smartstring — SSO for strings ≤ 23 ASCII bytes on 64-bit
use smartstring::alias::String as SString;
let s: SString = "short".into();      // inline, no heap

// String interning — deduplicate repeated strings
use string_interner::StringInterner;
let mut interner = StringInterner::default();
let sym = interner.get_or_intern("recurring-token");
```

**Rationale**: Heap allocations don't get cheaper with size; a million 1-byte allocations are worse than one million-byte allocation. Arenas (bumpalo, typed_arena) turn N deallocations into one. SmallVec is slightly slower per access (must check inline-vs-heap), so the win comes from skipping allocations — profile to confirm. For `SmallVec<[T; N]>`, keep `N` small; large `N` or large `T` makes the value larger than `Vec` itself.

**See also**: PF-13, Performance Book §7

---

## PF-15: Pre-Allocate Collection Capacity

**Strength**: SHOULD

**Summary**: When the final size is known or has a tight upper bound, use `with_capacity` or `reserve` to replace N small allocations with one.

```rust
// ❌ Grows from 0 → 4 → 8 → 16 → 32: four allocations for 20 items
let mut v = Vec::new();
for i in 0..20 { v.push(i); }

// ✅ Single allocation
let mut v = Vec::with_capacity(20);
for i in 0..20 { v.push(i); }

// ✅ When merging into an existing collection
let mut v: Vec<i32> = existing;
v.reserve(extra.len());
v.extend(extra);

// ✅ HashMap also supports with_capacity
use std::collections::HashMap;
let mut m = HashMap::with_capacity(1000);

// ✅ Custom iterators: implement size_hint so collect() pre-allocates
impl Iterator for MyIter {
    type Item = T;
    fn next(&mut self) -> Option<T> { /* ... */ todo!() }
    fn size_hint(&self) -> (usize, Option<usize>) { (self.remaining, Some(self.remaining)) }
}
```

**Rationale**: `Vec` grows by roughly doubling, so growing to size N requires log₂(N) reallocations. Pre-allocation eliminates all of them. Standard iterator adapters propagate `size_hint` through the chain, so `collect` on an `ExactSizeIterator` pre-allocates correctly — implement `size_hint` on your own iterators to enable this.

---

## PF-16: Avoid `format!` in Hot Paths

**Strength**: SHOULD

**Summary**: `format!` always allocates a fresh `String`. In loops, reuse a buffer with `write!`; for `Display` implementations, write directly to the formatter.

```rust
// ❌ Allocates on every iteration
for i in 0..1000 {
    let msg = format!("processing {}", i);
    handler.send(msg);
}

// ✅ Reuse one buffer
use std::fmt::Write;
let mut msg = String::with_capacity(32);
for i in 0..1000 {
    msg.clear();
    write!(msg, "processing {}", i).unwrap();
    handler.send(&msg);
}

// ✅ Defer formatting entirely — pass format_args! where possible
fn log_it(args: std::fmt::Arguments<'_>) { /* ... */ }
log_it(format_args!("processing {}", 42));    // no allocation at all

// ✅ Implement Display instead of returning String
use std::fmt;
impl fmt::Display for Event {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}@{}", self.name, self.time)    // writes into caller's buffer
    }
}
```

**Rationale**: Formatting machinery is not the bottleneck — allocation is. `format_args!` constructs a lazy `Arguments` value that can be written into any `Write` target without allocating. Returning `String` from a `Display`-like helper wastes the optimization — implement `Display` directly.

---

## PF-17: `Cow<'_, T>` for Conditional Allocation

**Strength**: SHOULD

**Summary**: Use `Cow` when most values are borrowed but a minority need ownership (e.g., escaping, normalization, defaulting).

```rust
use std::borrow::Cow;

// ❌ Always allocates, even on the fast path
fn escape(s: &str) -> String {
    if s.contains('&') { s.replace('&', "&amp;") } else { s.to_string() }
}

// ✅ Borrowed when unchanged, owned only when needed
fn escape(s: &str) -> Cow<'_, str> {
    if s.contains('&') {
        Cow::Owned(s.replace('&', "&amp;"))
    } else {
        Cow::Borrowed(s)
    }
}

// ✅ Also works for &[T]/Vec<T>, &Path/PathBuf
fn normalize_values(values: &[i32]) -> Cow<'_, [i32]> {
    if values.iter().all(|&v| v >= 0) {
        Cow::Borrowed(values)
    } else {
        Cow::Owned(values.iter().map(|v| v.max(&0).copied().unwrap_or(0)).collect())
    }
}

// ✅ Mixed-origin collection — literals and computed strings together
let mut errors: Vec<Cow<'static, str>> = vec![];
errors.push(Cow::Borrowed("something went wrong"));
errors.push(Cow::Owned(format!("failed at line {}", 42)));

// ✅ Clone-on-write mutation via Cow::to_mut
let mut s: Cow<str> = Cow::Borrowed("read-only");
if need_to_edit { s.to_mut().push_str(" + edit"); }   // only now does it allocate
```

**Rationale**: `Cow<'a, str>` derefs to `&str` for reads, so most call sites look identical to `String` or `&str`. The win is skipping allocation on the hot path while preserving a path for ownership when needed. `Cow` is "fiddly" — the lifetime in the return position sometimes fights generics; default to it only where measurements justify the complexity.

**See also**: PF-12, Performance Book §7

---

## PF-18: Return `impl Iterator`, Not `Vec<T>`

**Strength**: SHOULD

**Summary**: When the caller will likely iterate the result, return `impl Iterator<Item = T>`. Returning `Vec<T>` forces an allocation the caller may not need.

```rust
// ❌ Forces allocation even if the caller just iterates once
pub fn skip_blanks(lines: &[String]) -> Vec<&str> {
    lines.iter().filter(|l| !l.is_empty()).map(String::as_str).collect()
}

// ✅ No allocation; composes with more adapters
pub fn skip_blanks<'a>(lines: &'a [String]) -> impl Iterator<Item = &'a str> + 'a {
    lines.iter().filter(|l| !l.is_empty()).map(String::as_str)
}

// Caller decides whether to collect
let non_empty: Vec<&str> = skip_blanks(&lines).collect();
for l in skip_blanks(&lines) { process(l); }       // no Vec allocated
```

**Rationale**: `impl Iterator` keeps the return type opaque and lazy. It composes: `a.skip_blanks().filter(..).take(10)` never materializes the intermediate `Vec`. When the caller *does* want a `Vec`, one `.collect()` call with a correct `size_hint` is as efficient as building the `Vec` inside.

**See also**: PF-20 (iterator methods)

---

## PF-19: Accept `&str` and `&[T]`, Not `String`/`Vec<T>`

**Strength**: MUST

**Summary**: Function parameters that only read their input should take `&str`/`&[T]`. Taking owned types forces callers to allocate.

```rust
// ❌ Caller must convert &str → String
fn greet(name: String) { println!("Hello, {name}"); }
greet("world".to_string());                         // allocation at every call site

// ✅ Works with &str, &String, Box<str>, String, literal
fn greet(name: &str) { println!("Hello, {name}"); }
greet("world");
greet(&format!("user {}", id));                     // only one allocation, not two

// Same for collections
fn sum(xs: &[i32]) -> i32 { xs.iter().sum() }
sum(&[1, 2, 3]);
sum(&vec![1, 2, 3]);                                // coerces

// AsRef<Path> is the idiomatic shorthand for "anything path-like"
fn open(path: impl AsRef<std::path::Path>) -> std::io::Result<std::fs::File> {
    std::fs::File::open(path.as_ref())              // see PF-11 — inner fn pattern
}
```

**Rationale**: `&str`/`&[T]` are the lingua franca for borrowed data and coerce from a strict superset of owned types (deref coercion handles `&String → &str`, `&Vec<T> → &[T]`). Taking `String` in a public API burdens every caller with an allocation and signals "I will consume this," which you usually don't mean to. Clippy's `ptr_arg` lint enforces this.

**See also**: PF-11 (generic outer, non-generic inner), Pragmatic Rust ptr_arg

---

## PF-20: Use Iterator Adapters, Not Index Loops

**Strength**: SHOULD

**Summary**: Iterators let the compiler elide bounds checks and sometimes auto-vectorize. Prefer `iter()`, `map`, `filter_map`, `chunks_exact` over manual indexing.

```rust
// ❌ Bounds check on every access
fn sum_positive(xs: &[i32]) -> i32 {
    let mut s = 0;
    for i in 0..xs.len() {
        if xs[i] > 0 { s += xs[i]; }
    }
    s
}

// ✅ Iterator — no bounds checks, composes cleanly
fn sum_positive(xs: &[i32]) -> i32 {
    xs.iter().filter(|&&n| n > 0).sum()
}

// ✅ filter_map fuses filter + map in one pass
let lens: Vec<usize> = lines.iter()
    .filter_map(|l| (!l.is_empty()).then(|| l.len()))
    .collect();

// ✅ chunks_exact is faster than chunks — compiler knows the exact size
for chunk in xs.chunks_exact(4) {
    let [a, b, c, d] = chunk.try_into().unwrap();   // no runtime size check
    process4(a, b, c, d);
}
for tail in xs.chunks_exact(4).remainder() {
    process1(*tail);
}

// ✅ iter().copied() on small Copy types — LLVM often generates better code
let sum: u32 = xs.iter().copied().sum();            // values, not refs
```

**Rationale**: `iter()` proves to LLVM that indices stay in range, so redundant bounds checks disappear. `chunks_exact` is a stronger proof: every chunk is *exactly* N elements, which enables unrolling and vectorization. On hot paths, `filter + map` fused as `filter_map` avoids per-element overhead; `chain` can cost more than it looks because every step branches on which sub-iterator is active.

**See also**: PF-21 (bounds checks), Performance Book §10

---

## PF-21: Eliminate Redundant Bounds Checks

**Strength**: CONSIDER

**Summary**: When indexing is necessary, structure the code so the compiler can prove indices in range — slice once before the loop, or use an assertion.

```rust
// ✅ Slice first, then index the slice
fn process_range(xs: &[u8], start: usize, end: usize) {
    let s = &xs[start..end];                        // bounds check once
    for i in 0..s.len() {
        use_it(s[i]);                               // no per-iter bounds check
    }
}

// ✅ Hoist an assertion so later accesses are free
fn dot(a: &[f64], b: &[f64]) -> f64 {
    assert_eq!(a.len(), b.len());
    let mut s = 0.0;
    for i in 0..a.len() {
        s += a[i] * b[i];                           // LLVM elides b's bounds check
    }
    s
}

// ⚠️ Last resort: unsafe get_unchecked — you own the invariant now
// SAFETY: i < xs.len() is guaranteed by the outer loop bound.
let v = unsafe { *xs.get_unchecked(i) };
```

**Rationale**: Bounds checks matter less often than people think — profile first. When they do, the safe remedies are usually enough. `get_unchecked` should be a last resort: one mistake is UB, and the speedup is often ≤5%. See the "Bounds Check Cookbook" in the Performance Book references.

**See also**: PF-20

---

## PF-22: Inlining — `#[inline]`, `#[inline(always)]`, `#[cold]`

**Strength**: CONSIDER

**Summary**: The compiler inlines generics and small functions automatically. Add `#[inline]` on non-generic cross-crate hot functions; use `#[inline(always)]` sparingly; mark error paths `#[cold]` to improve the hot path.

```rust
// ✅ Cross-crate inlining: a small non-generic function
impl Vector3 {
    #[inline]
    pub fn dot(self, other: Self) -> f64 {
        self.x * other.x + self.y * other.y + self.z * other.z
    }
}

// ✅ #[cold] on error paths tells the optimizer "this is rare"
#[cold]
fn report_unexpected(state: State) -> ! {
    panic!("unexpected state: {state:?}");
}

// ✅ Split function for mixed hot/cold call sites
#[inline(always)] fn inlined_work() { /* body */ }
#[inline(never)]  fn outlined_work() { inlined_work(); }
// Use inlined_work() in the hot loop, outlined_work() elsewhere.

// ❌ Don't #[inline(always)] large functions or many-callsite helpers
// — causes code bloat and icache pressure with no proportional speedup.
```

**Rationale**: Generic functions are always eligible for cross-crate inlining because they're instantiated per caller. Non-generic functions need `#[inline]` to be available cross-crate. Inlining is non-transitive — `f` calling `g` requires both marked to inline together. `#[cold]` moves branch-prediction hints: the hot path runs straighter; the cold path may be moved out of line entirely. Verify with Cachegrind — inlined functions show `.` (no counts) on their first/last lines.

**See also**: PF-06 (LTO enables cross-crate inlining), Performance Book §5

---

## PF-23: Choose the Right Collection

**Strength**: SHOULD

**Summary**: Pick the data structure based on access pattern, not familiarity. `Vec` is the default; reach for `VecDeque`, `BTreeMap`, `HashMap`, or `IndexMap` deliberately.

```rust
// Vec<T>: cache-friendly, O(1) push/pop at end, O(n) insert/remove at front/middle
let mut v = Vec::new();
v.push(x);                    // O(1) amortized
v.swap_remove(idx);           // O(1) — use when order doesn't matter
v.remove(idx);                // O(n) — avoid in hot paths

// VecDeque<T>: ring buffer; O(1) push/pop at both ends
use std::collections::VecDeque;
let mut q = VecDeque::new();
q.push_back(x); q.push_front(y);

// HashMap<K,V>: O(1) average; unordered; SipHash by default
// BTreeMap<K,V>: O(log n); sorted iteration; stable order
// IndexMap<K,V> (indexmap crate): O(1) average; insertion-ordered
use indexmap::IndexMap;
let mut cfg: IndexMap<String, Value> = IndexMap::new();
// cfg.iter() yields in insertion order — useful for config round-trips

// For very small N, a linear search over Vec beats HashMap due to cache effects
fn lookup_small<'a>(xs: &'a [(String, Value)], k: &str) -> Option<&'a Value> {
    xs.iter().find(|(key, _)| key == k).map(|(_, v)| v)
    // N < ~20 → Vec wins against HashMap hashing overhead
}
```

**Rationale**: `Vec` is cache-friendly because it's contiguous; hash tables chase pointers. For N under ~20, linear search in a `Vec<(K, V)>` usually beats a `HashMap` lookup. `BTreeMap` gives sorted iteration and range queries; `IndexMap` preserves insertion order, which matters for config serialization and deterministic output.

**See also**: PF-24 (stdlib methods), PF-13

---

## PF-24: Know Your Standard Library Methods

**Strength**: SHOULD

**Summary**: The stdlib has specialized methods that outperform hand-rolled versions: `swap_remove`, `retain`, `entry`, `ok_or_else`, `make_mut`, `extend`.

```rust
// swap_remove — O(1) when order doesn't matter
let mut v = vec![1, 2, 3, 4, 5];
v.swap_remove(1);                       // ~= [1, 5, 3, 4]; remove() would be O(n)

// retain — efficient multi-remove in one pass
v.retain(|&x| x % 2 == 0);              // also on String, HashMap, HashSet

// entry — one lookup instead of two for insert-or-update
use std::collections::HashMap;
let mut counts: HashMap<&str, u32> = HashMap::new();
for word in words {
    *counts.entry(word).or_insert(0) += 1;
}

// Lazy variants — defer expensive fallbacks
let v = opt.ok_or_else(|| format!("missing {}", name))?;    // not ok_or(format!())
let v = opt.unwrap_or_else(compute_default);                // not unwrap_or(compute_default())
let v = res.map_or_else(|e| log_error(e), |ok| ok);

// Arc::make_mut — clone-on-write only when shared
use std::sync::Arc;
let mut a: Arc<Config> = Arc::new(Config::default());
Arc::make_mut(&mut a).port = 8080;      // in-place if refcount==1, else clone

// vec![0; n] — OS-accelerated zero-fill, faster than resize/extend/unsafe
let buf = vec![0u8; 1 << 20];

// extend instead of collect-then-append
existing.extend(iter);                  // not: let v: Vec<_> = iter.collect(); existing.append(&mut v);

// parking_lot — sometimes faster Mutex/RwLock, but measure first
// use parking_lot::Mutex;               // stdlib has caught up on some platforms
```

**Rationale**: These methods exist because the naïve version has a known cost. `ok_or(format!(..))` allocates even when the value is `Some`; `ok_or_else` defers the work. `Vec::remove` shifts everything; `swap_remove` doesn't. `entry` fuses lookup + insert into one hash+probe. `Arc::make_mut` implements COW for free on unshared data. parking_lot used to be a universal win but the stdlib has caught up on Linux/macOS — benchmark before switching.

**See also**: PF-20, Performance Book §9

---

## PF-25: Switch Hashers When Profiling Shows Hashing Is Hot

**Strength**: CONSIDER

**Summary**: The default `SipHash-1-3` is collision-resistant but slow for short keys. When profiling shows hashing is hot and HashDoS isn't a concern, swap in `FxHashMap`, `ahash`, or `fnv`.

```rust
// ✅ rustc-hash — fastest for integer and small-key workloads
use rustc_hash::{FxHashMap, FxHashSet};
let mut m: FxHashMap<u64, Value> = FxHashMap::default();

// ✅ ahash — uses AES hardware instructions when available
use ahash::AHashMap;
let mut m: AHashMap<String, Value> = AHashMap::default();

// ✅ fnv — higher quality than FxHash, slightly slower
use fnv::FnvHashMap;

// ✅ Custom BuildHasher with stdlib HashMap
use std::collections::HashMap;
use std::hash::BuildHasherDefault;
type FxMap<K, V> = HashMap<K, V, BuildHasherDefault<rustc_hash::FxHasher>>;

// ✅ nohash — for already-random integer keys (UUIDs, hashes, random IDs)
use nohash_hasher::IntMap;
let mut m: IntMap<u64, Value> = IntMap::default();
```

```toml
# clippy.toml — prevent accidental reintroduction of stdlib HashMap
disallowed-types = ["std::collections::HashMap", "std::collections::HashSet"]
```

**Rationale**: SipHash protects against HashDoS — attacker-crafted inputs that collide, turning O(1) lookups into O(n). For internal maps where keys come from trusted sources, a faster hasher is safe and can measurably speed the program up. rustc itself saw 4–84% slowdowns when switching *back* to SipHash. Benchmark multiple alternatives; results vary: rustc found FxHash beat ahash in its own workload despite ahash using AES. The `hashbrown` crate powers stdlib's HashMap under the hood; you rarely need it directly unless you want its raw entry API.

**See also**: PF-02 (clippy disallowed_types), Performance Book §6

---

## PF-26: Optimize Type Sizes for Hot Types

**Strength**: CONSIDER

**Summary**: Shrinking frequently-instantiated types reduces cache pressure and `memcpy` overhead. Above 128 bytes, Rust uses `memcpy` for moves.

```rust
// Measure: nightly only
// $ RUSTFLAGS=-Zprint-type-sizes cargo +nightly build --release
// (see also the top-type-sizes crate for a compact view)

// ❌ Enum sized to its largest variant — most uses waste 1KB
enum Op {
    Nop,
    Set(u32, u32),
    BigBlob([u8; 1024]),            // enum is 1024 + tag bytes
}

// ✅ Box the rare large variant
enum Op {
    Nop,
    Set(u32, u32),
    BigBlob(Box<[u8; 1024]>),       // now just a pointer per BigBlob
}

// ✅ Boxed slice — 2 words instead of Vec's 3 (no capacity)
let v: Vec<u32> = compute();
let frozen: Box<[u32]> = v.into_boxed_slice();     // len + ptr only
let back: Vec<u32> = frozen.into_vec();            // no realloc

// ✅ ThinVec — single-word metadata; great inside hot enums
use thin_vec::ThinVec;
struct Node { children: ThinVec<Node> }            // empty children: 1 word, no alloc

// ✅ Use the smallest integer that fits the domain
struct IndexedItem { idx: u32, name: String }     // not usize if < 4B items

// ✅ Niche optimization: Option<NonZeroU32> is 4 bytes (not 8)
use std::num::NonZeroU32;
struct Handle(NonZeroU32);                         // Option<Handle> fits in 4 bytes

// ✅ Prevent regressions
#[cfg(target_arch = "x86_64")]
static_assertions::assert_eq_size!(HotPathFrame, [u8; 64]);
```

**Rationale**: The Rust compiler automatically reorders struct/enum fields to minimize padding (unless `#[repr(C)]`) — don't hand-order them. The real wins come from structural changes: boxing rare variants, using smaller integers, switching `Vec` to `Box<[T]>` or `ThinVec`, and niche-optimized `Option`. DHAT's copy-profiling mode (`--mode=copy`) highlights hot `memcpy` calls from oversized types. Cross-reference TD-20 (`NonZero*`) and TD-21 (`repr`) for the type-design perspective.

**See also**: TD-20, TD-21, Performance Book §8

---

## PF-27: Buffer Your I/O

**Strength**: MUST

**Summary**: Rust's file and socket I/O is unbuffered. Wrap readers with `BufReader`, writers with `BufWriter`, lock stdout manually for repeated writes, and flush explicitly.

```rust
use std::io::{self, BufRead, BufReader, BufWriter, Read, Write};
use std::fs::File;

// ❌ One syscall per line
let mut f = File::create("out.txt")?;
for line in &lines {
    writeln!(f, "{line}")?;
}

// ✅ Batches syscalls behind an 8 KiB buffer
let mut f = BufWriter::new(File::create("out.txt")?);
for line in &lines {
    writeln!(f, "{line}")?;
}
f.flush()?;                         // explicit — surfaces errors; drop would swallow them

// ❌ println! locks stdout each call
for line in &lines { println!("{line}"); }

// ✅ Lock once, write many — combine with BufWriter for CLI tools
let stdout = io::stdout();
let mut out = BufWriter::new(stdout.lock());
for line in &lines {
    writeln!(out, "{line}")?;
}
out.flush()?;

// ✅ write_all, not repeated write() calls (which may be partial)
out.write_all(payload)?;

// ✅ Read raw bytes when UTF-8 validation is wasted work
let mut r = BufReader::new(File::open("log.bin")?);
let mut buf = Vec::new();
while r.read_until(b'\n', &mut buf)? != 0 {
    process_bytes(&buf);
    buf.clear();
}
```

**Rationale**: Every raw `write` or `read` can become a syscall. `BufWriter` batches them into buffer-sized chunks (default 8 KiB); `BufReader` reads ahead. `write` returns how many bytes it wrote — short writes are legal, so use `write_all` unless you really need the partial count. `BufWriter`'s drop silently swallows flush errors; an explicit `flush()?` is required to surface them. Reading into `String` incurs UTF-8 validation; for ASCII or binary data, `read_until` + `&[u8]` skips it.

**See also**: PF-13 (read_line + clear), Performance Book §12

---

## PF-28: Parallelize with Rayon — When the Work Is Worth It

**Strength**: CONSIDER

**Summary**: `rayon` turns data-parallel iterators into thread-parallel ones for essentially zero code cost. Use it when per-item work is substantial and you have many items; avoid it for tight inner loops and contended shared state.

```rust
use rayon::prelude::*;

// ✅ Embarrassingly parallel: heavy per-item CPU work
let results: Vec<Output> = inputs.par_iter()
    .map(|i| expensive_transform(i))
    .collect();

// ✅ Parallel reduction
let total: u64 = items.par_iter().map(|it| it.size).sum();

// ✅ Parallel filter + collect
let hits: Vec<&Record> = records.par_iter()
    .filter(|r| matches_query(r, &query))
    .collect();

// ❌ Tiny per-item work: parallelism overhead dominates
let sum: u32 = (0..1000).into_par_iter().sum();     // sequential wins here

// ❌ Shared mutable state: contention kills scaling
let counter = std::sync::Mutex::new(0);
items.par_iter().for_each(|_| *counter.lock().unwrap() += 1);   // serializes

// ✅ Reduce into thread-local state, then combine
let total = items.par_iter()
    .map(|_| 1u32)
    .reduce(|| 0, |a, b| a + b);
```

**Rationale**: Rayon uses a work-stealing thread pool, so chunking and scheduling are automatic. The cost is ~microsecond per task-boundary crossing — if the per-item work is nanoseconds, sequential code wins. Contention on shared mutexes serializes the parallel work and can produce worse wall-time than the sequential version. For I/O-bound work, rayon is the wrong tool — use `tokio::spawn` or `rayon::spawn_fifo` with care.

**See also**: PF-29, PF-30

---

## PF-29: Yield in Long Async Tasks

**Strength**: MUST

**Summary**: CPU-bound async code without `.await` points starves other tasks on the same runtime thread. Insert `yield_now().await` every 10–100 microseconds of work.

```rust
use tokio::task;

// ❌ Starves the runtime
async fn process_all(items: Vec<Item>) {
    for item in items {
        expensive_computation(&item);       // no await, no yield
    }
}

// ✅ Yield each batch
async fn process_all(items: Vec<Item>) {
    for chunk in items.chunks(100) {
        for item in chunk {
            expensive_computation(item);
        }
        task::yield_now().await;            // cooperative pre-emption
    }
}

// ✅ Best: respect the runtime's cooperative budget
async fn process_all(items: Vec<Item>) {
    for item in &items {
        expensive_computation(item);
        // unstable API illustrative of pattern:
        // if !tokio::runtime::Handle::current().has_budget_remaining() {
        //     task::yield_now().await;
        // }
    }
}

// ✅ Offload truly heavy CPU work to a blocking thread
let handle = task::spawn_blocking(|| heavy_sync_work());
let result = handle.await?;

// ✅ For CPU-heavy data pipelines, dispatch through rayon instead
// (bridge with tokio::sync::oneshot)
```

**Rationale**: Tokio (and most async runtimes) are cooperatively scheduled. Between `.await` points, nothing else on that thread runs. Yielding every 10–100µs keeps tail latencies low; yielding every iteration adds switching overhead (~100 ns per yield). Code with natural `.await` points (database queries, RPCs) yields implicitly — explicit yields are only needed in CPU-bound stretches. For truly heavy CPU work, move it off the async runtime with `spawn_blocking` or a dedicated thread pool.

**See also**: PF-30, M-YIELD-POINTS, Guide 07 (concurrency)

---

## PF-30: Design for Throughput, Not Single-Item Latency

**Strength**: SHOULD

**Summary**: Server workloads scale via throughput (items/second, not ms/item). Batch, partition work upfront, avoid hot-spinning, and let threads stay on-core.

```rust
use tokio::sync::mpsc::Receiver;
use tokio::time::{sleep, Duration};

// ❌ Hot spin wastes CPU and causes cache thrash
async fn drain_slow(mut rx: Receiver<Item>) {
    loop {
        if let Ok(item) = rx.try_recv() {
            handle_one(item).await;
        }
        sleep(Duration::from_micros(1)).await;     // busy-wait
    }
}

// ✅ Batch so amortized overhead is low
async fn drain_batched(mut rx: Receiver<Item>) {
    let mut batch: Vec<Item> = Vec::with_capacity(128);
    while let Some(first) = rx.recv().await {
        batch.push(first);
        while batch.len() < 128 {
            match rx.try_recv() {
                Ok(item) => batch.push(item),
                Err(_)   => break,
            }
        }
        handle_batch(&batch).await;
        batch.clear();
    }
}

// ✅ Partition upfront — each worker owns its slice, no stealing
async fn process_partitioned(items: Vec<Item>, workers: usize) {
    let chunks: Vec<Vec<Item>> = partition(items, workers);
    let handles: Vec<_> = chunks.into_iter().map(|chunk| {
        tokio::spawn(async move {
            for item in chunk { handle_one(item).await; }
        })
    }).collect();
    for h in handles { h.await.unwrap(); }
}
```

**Rationale**: Items-per-cycle and items-per-second are what scale; single-request latency matters but is cheaper to address with capacity. Hot-spinning wastes cycles that could serve other requests. Batching amortizes per-operation overhead (locks, syscalls, bounds checks) across N items. Partitioning upfront avoids the contention of work-stealing on small items. The Pragmatic Rust M-THROUGHPUT guideline is explicit: "you can scale for throughput, but not for latency."

**See also**: PF-28, PF-29, M-THROUGHPUT

---

## PF-31: Compute at Compile Time with `const`

**Strength**: CONSIDER

**Summary**: `const fn` and `const` items execute at compile time. Prefer `const` for true constants, `static` for shared data with a unique address, and `&'static str` tables over runtime-allocated data.

```rust
// ✅ Constant value — inlined everywhere it's used
const MAX_USERS: usize = 10_000;
const BUFFER_SIZE: usize = 4 * 1024;

// ✅ const fn — executed at compile time when inputs are const
const fn table(n: usize) -> [u32; 8] {
    let mut t = [0u32; 8];
    let mut i = 0;
    while i < 8 { t[i] = (n + i) as u32; i += 1; }
    t
}
const LOOKUP: [u32; 8] = table(100);

// ✅ static — single address, 'static lifetime, for shared read-only data
static GREETINGS: &[&str] = &["hello", "bonjour", "hola"];
static ERROR_MESSAGES: &[(u32, &str)] = &[
    (404, "not found"),
    (500, "server error"),
];

// ✅ &'static str literals cost nothing — no allocation
fn error_for(code: u32) -> &'static str {
    match code {
        404 => "not found",
        500 => "server error",
        _   => "unknown",
    }
}

// ✅ include_bytes!/include_str! — embed files at compile time
static SCHEMA: &str = include_str!("../schemas/v1.json");

// ❌ Runtime-built "constant" — reallocates on every call
fn greeting() -> String { String::from("hello") }
```

**Rationale**: `const` values are inlined at each use — no runtime storage, no allocation. `static` values have a fixed address and are ideal for lookup tables. `const fn` has grown dramatically: loops, mutation, trait dispatch via `const` traits (nightly), and floating-point are all available. `&'static str` tables beat `Vec<String>` for built-in data. `include_str!`/`include_bytes!` embeds external data with zero runtime cost.

**See also**: Guide 01 (idioms — const vs static)


## Profiling Playbook

Concrete steps when the answer to "is it fast enough?" is "no."

```text
╭─ 1. FIX THE OBVIOUS ──────────────────────────────────────────────╮
│  • Are you measuring a release build?  (PF-05)                    │
│  • Has `cargo clippy` passed all perf lints?  (PF-02)             │
│  • Is `[profile.release]` reasonable?  (PF-06)                    │
╰───────────────────────────────────────────────────────────────────╯
╭─ 2. ESTABLISH A BENCHMARK ────────────────────────────────────────╮
│  • Representative input (not a microbenchmark of nothing)         │
│  • Criterion for library work                                     │
│  • Hyperfine for end-to-end                                       │
│  • Record the baseline number                                     │
╰───────────────────────────────────────────────────────────────────╯
╭─ 3. CPU PROFILE ──────────────────────────────────────────────────╮
│  • [profile.release] debug = "line-tables-only"                   │
│  • samply record ./target/release/myapp    (or cargo flamegraph)  │
│  • Identify hottest ≤3 functions                                  │
│  • On Linux, add `perf stat` for IPC / cache-miss rate            │
╰───────────────────────────────────────────────────────────────────╯
╭─ 4. ALLOCATION PROFILE ───────────────────────────────────────────╮
│  • valgrind --tool=dhat ./target/release/myapp                    │
│  • Or dhat-rs as a test harness for CI                            │
│  • Hot allocation sites → apply PF-13..PF-17                      │
│  • If memcpy is hot → apply PF-26                                 │
╰───────────────────────────────────────────────────────────────────╯
╭─ 5. TARGETED INTERVENTION ────────────────────────────────────────╮
│  Hot path is ...                                                  │
│    ... hashing-bound   → PF-25                                    │
│    ... iteration-bound → PF-20, PF-21                             │
│    ... clone-heavy     → PF-12, PF-17                             │
│    ... allocation-heavy→ PF-13, PF-14, PF-15, PF-16               │
│    ... I/O-bound       → PF-27                                    │
│    ... async-bound     → PF-29, PF-30                             │
│    ... CPU-bound large → PF-28 (rayon) + PF-06 (fat LTO)          │
│    ... call-overhead   → PF-22 (inlining)                         │
│    ... type too big    → PF-26                                    │
╰───────────────────────────────────────────────────────────────────╯
╭─ 6. MEASURE AGAIN ────────────────────────────────────────────────╮
│  • One change at a time (PF-04)                                   │
│  • Revert if no improvement                                       │
│  • Keep the benchmark committed — it's regression protection      │
╰───────────────────────────────────────────────────────────────────╯
╭─ 7. LAST-MILE KNOBS ──────────────────────────────────────────────╮
│  • codegen-units = 1, lto = "fat"       (PF-06)                   │
│  • target-cpu=native                    (PF-06)                   │
│  • mimalloc / jemalloc                  (PF-08)                   │
│  • PGO + BOLT                           (PF-09)                   │
╰───────────────────────────────────────────────────────────────────╯
```


## Release Profile Template

A reference `Cargo.toml` showing the common knobs with rationale comments. Copy and uncomment what you need — defaults are chosen conservatively.

```toml
# ─── Runtime-speed release profile ──────────────────────────────────
[profile.release]
opt-level      = 3          # default; maximum runtime speed
lto            = "fat"      # whole-program inlining — slower compile, faster binary
codegen-units  = 1          # single unit → best cross-function optimization
panic          = "abort"    # smaller binary, tiny speedup; drops catch_unwind
strip          = "none"     # keep symbols for profiling; set to "symbols" for releases
# debug        = false      # default; set to "line-tables-only" to profile

# ─── Profile-friendly release (CI, staging, troubleshooting prod) ──
[profile.release-with-profiling]
inherits       = "release"
debug          = "line-tables-only"   # source line mapping for samply/perf/flamegraph
strip          = "none"

# ─── Size-optimized release (WASM, embedded, small containers) ─────
[profile.release-small]
inherits       = "release"
opt-level      = "z"        # "s" also OK and allows loop vectorization
lto            = "fat"
codegen-units  = 1
panic          = "abort"
strip          = "symbols"  # drop symbols; harder to debug

# ─── Faster dev loop (compile time > runtime for local iteration) ──
[profile.dev]
debug          = false      # 20-40% faster dev builds; lose gdb/lldb line info
# opt-level    = 1          # uncomment for slightly faster dev-build runtime

# ─── Bench profile — always inherits release unless overridden ─────
[profile.bench]
debug          = "line-tables-only"   # so flamegraphs of benches are readable
# inherits release implicitly

# ─── Deps in dev: optimize third-party code, skip optimizing ours ──
# Compiles most deps optimized, keeps your-crate fast to rebuild.
[profile.dev.package."*"]
opt-level      = 3

# ─── RUSTFLAGS — .cargo/config.toml, not Cargo.toml ────────────────
# [target.x86_64-unknown-linux-gnu]
# linker       = "clang"
# rustflags    = [
#   "-C", "link-arg=-fuse-ld=mold",       # faster linker
#   "-C", "target-cpu=native",            # non-portable machine-specific codegen
#   "-C", "force-frame-pointers=yes",     # better profiler stack traces
# ]
```

A few conscious choices worth calling out:

- `lto = "fat"` is the biggest lever after `opt-level = 3`. Compile time roughly doubles; runtime gains are usually 5–20%.
- `codegen-units = 1` compounds with fat LTO. Split this with `lto = "thin"` and `codegen-units = 16` for a compile-time/runtime compromise.
- `panic = "abort"` is only safe if no code relies on `std::panic::catch_unwind` for isolation (e.g., some FFI boundaries, some plugin systems, most test frameworks).
- Leave `strip` as `"none"` on profilable builds. `strip = "symbols"` removes both DWARF and function names — you lose both debugging and profiling.
- Profile-inheriting custom profiles (`inherits = "release"`) let you keep a standard `cargo build --release` fast while having `cargo build --profile release-with-profiling` when needed.


## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| PF-01 Benchmark before optimizing | MUST | Mediocre benchmarks beat none |
| PF-02 Run Clippy's perf lints | MUST | Free wins before manual work |
| PF-03 Profile to find hot paths | MUST | `debug = "line-tables-only"` + samply/perf/DHAT |
| PF-04 The optimization loop | SHOULD | One change at a time; revert if no improvement |
| PF-05 Release vs dev | MUST | Dev builds are 10–100× slower; never benchmark them |
| PF-06 Release profile — speed | SHOULD | `codegen-units=1`, `lto="fat"`, `panic="abort"` |
| PF-07 Release profile — size | CONSIDER | `opt-level="z"`, `strip="symbols"` |
| PF-08 Alternative allocator | SHOULD | mimalloc/jemalloc, 10–25% on alloc-heavy apps |
| PF-09 PGO / BOLT | CONSIDER | 5–15% wins; requires realistic profiling runs |
| PF-10 Compile times — build config | SHOULD | mold/lld, `cargo check`, `debug=false` in dev |
| PF-11 Compile times — code | CONSIDER | `cargo llvm-lines`, non-generic inner function |
| PF-12 Avoid `clone` in hot paths | SHOULD | Borrow; `Arc::clone` is free; use `clone_from` |
| PF-13 Reduce heap allocations | SHOULD | Reuse buffers; pre-allocate; `read_line + clear` |
| PF-14 Small-capacity collections | CONSIDER | SmallVec/ArrayVec/bumpalo for short-lived data |
| PF-15 Pre-allocate capacity | SHOULD | `with_capacity`; implement `size_hint` |
| PF-16 Avoid `format!` in hot paths | SHOULD | Reuse `String` buffer; use `write!`/`format_args!` |
| PF-17 `Cow` for conditional allocation | SHOULD | Borrowed fast path, owned when mutated |
| PF-18 Return `impl Iterator` | SHOULD | Let callers decide whether to allocate |
| PF-19 Accept `&str`/`&[T]` | MUST | Don't force caller allocations |
| PF-20 Iterators over index loops | SHOULD | Bounds checks elided; `chunks_exact` |
| PF-21 Eliminate redundant bounds checks | CONSIDER | Pre-slice or assert; `get_unchecked` is last resort |
| PF-22 Inlining attributes | CONSIDER | `#[inline]` cross-crate; `#[cold]` for rare paths |
| PF-23 Choose the right collection | SHOULD | `Vec` default; `IndexMap` preserves order |
| PF-24 Stdlib specialized methods | SHOULD | `swap_remove`, `entry`, `ok_or_else`, `make_mut` |
| PF-25 Switch hashers when hot | CONSIDER | FxHash/ahash; gate with `disallowed_types` |
| PF-26 Optimize type sizes | CONSIDER | Box rare large variants; `ThinVec`; `Box<[T]>` |
| PF-27 Buffer your I/O | MUST | `BufReader`/`BufWriter`; explicit `flush()?` |
| PF-28 Rayon for data parallelism | CONSIDER | Worth it when per-item work is substantial |
| PF-29 Yield in long async tasks | MUST | Every 10–100 µs of CPU-bound work |
| PF-30 Design for throughput | SHOULD | Batch, partition, avoid hot-spinning |
| PF-31 Compute at compile time | CONSIDER | `const`, `static`, `include_str!`, `&'static str` |


## Related Guidelines

- **Ownership and Borrowing**: See `04-ownership-borrowing.md` for when `Rc`/`Arc` and borrowing replace `clone`, and how to structure data to avoid fighting the borrow checker.
- **Type Design**: See `05-type-design.md` for TD-20 (`NonZero*`), TD-21 (`repr`), and the type-level perspective on layout; PF-26 is the performance view of those ideas.
- **Unsafe and FFI**: See `09-unsafe-ffi.md` for the soundness obligations when reaching for `get_unchecked`, `MaybeUninit`, or `#[repr(C)]` as performance tools.
- **Anti-Patterns**: See `11-anti-patterns.md` for common performance anti-patterns (unnecessary cloning, `collect` chains, `HashMap` without a hint).
- **Project Structure**: See `12-project-structure.md` for workspace layouts that speed up compilation (PF-10, PF-11).


## External References

- [The Rust Performance Book](https://nnethercote.github.io/perf-book/) — Nicholas Nethercote et al., the primary source for this guide
- [The Rustonomicon — Data Representation](https://doc.rust-lang.org/nomicon/data.html) — type layout, alignment, niches
- [Cargo Reference — Profiles](https://doc.rust-lang.org/cargo/reference/profiles.html) — all profile settings in detail
- [`rustc` book — codegen options](https://doc.rust-lang.org/rustc/codegen-options/index.html) — `-C target-cpu`, `-C opt-level`, `-C lto`, frame pointers
- [Criterion.rs](https://bheisler.github.io/criterion.rs/book/) and [Divan](https://github.com/nvzqz/divan) — benchmarking frameworks
- [samply](https://github.com/mstange/samply) — cross-platform sampling profiler
- [cargo-flamegraph](https://github.com/flamegraph-rs/flamegraph) — flame graphs via perf/DTrace
- [cargo-pgo](https://github.com/Kobzol/cargo-pgo) — profile-guided optimization and BOLT wrapper
- [cargo-llvm-lines](https://github.com/dtolnay/cargo-llvm-lines) and [cargo-show-asm](https://github.com/pacak/cargo-show-asm) — inspect codegen
- [min-sized-rust](https://github.com/johnthagen/min-sized-rust) — binary size minimization
- [mimalloc](https://crates.io/crates/mimalloc), [tikv-jemallocator](https://crates.io/crates/tikv-jemallocator) — alternative allocators
- [rustc-hash](https://crates.io/crates/rustc-hash), [ahash](https://crates.io/crates/ahash), [hashbrown](https://crates.io/crates/hashbrown) — faster hashers
- [smallvec](https://crates.io/crates/smallvec), [arrayvec](https://crates.io/crates/arrayvec), [bumpalo](https://crates.io/crates/bumpalo), [thin-vec](https://crates.io/crates/thin-vec) — specialized containers
- [rayon](https://crates.io/crates/rayon) — data-parallel iterators
- Pragmatic Rust Guidelines: M-HOTPATH, M-THROUGHPUT, M-YIELD-POINTS, M-MIMALLOC-APP
