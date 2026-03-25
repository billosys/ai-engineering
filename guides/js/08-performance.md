# Performance

Measurement discipline, data structure choices, allocation patterns, lazy evaluation, caching, and — critically — what NOT to micro-optimize. The most damaging performance anti-pattern in AI-generated code is premature optimization. This guide establishes "measure first" before any optimization technique. Grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: Don't Optimize Without Measuring — Profile First, Optimize Second

**Strength**: MUST

**Summary**: Never optimize code based on intuition. Measure first, identify the bottleneck, then optimize only that path.

```js
// Good — measure before optimizing
const start = performance.now();
const result = processData(largeDataSet);
const elapsed = performance.now() - start;
console.log(`processData: ${elapsed.toFixed(2)}ms`);

// Then optimize ONLY if processData is actually the bottleneck
```

**The performance discipline**:
1. Write clear, idiomatic code first
2. Measure with real workloads (not toy data)
3. Identify the actual bottleneck (it's rarely where you think)
4. Optimize only the bottleneck
5. Measure again to confirm the improvement

**Rationale**: Engines are highly optimizing. Code that "looks slow" often isn't, and code that "looks fast" often isn't either. Premature optimization trades readability for negligible gains in non-bottleneck code. The guides in this series (01–07) define what "clear, idiomatic code" looks like — this guide covers what to do when idiomatic code isn't fast enough.

---

## ID-02: `Deno.bench()` for Microbenchmarks

**Strength**: SHOULD

**Summary**: Use Deno's built-in benchmark runner for comparing implementation alternatives.

```js
// bench.js — run with: deno bench bench.js

// Create data outside the bench function to measure lookup, not allocation
const map = new Map([["a", 1], ["b", 2], ["c", 3]]);
const obj = { a: 1, b: 2, c: 3 };

Deno.bench("Map lookup", () => {
  map.get("b");
});

Deno.bench("Object lookup", () => {
  obj.b;
});

// Group related benchmarks
const memberSet = new Set([1, 2, 3, 4, 5]);
const memberArr = [1, 2, 3, 4, 5];

Deno.bench({
  name: "Set.has()",
  group: "membership",
  fn() {
    memberSet.has(3);
  },
});

Deno.bench({
  name: "Array.includes()",
  group: "membership",
  baseline: true,
  fn() {
    const a = [1, 2, 3, 4, 5];
    a.includes(3);
  },
});
```

**Rationale**: `Deno.bench()` handles warmup iterations, statistical sampling, and comparison output. It is the correct tool for answering "which approach is faster for this specific operation?" — far more reliable than manual `performance.now()` loops.

---

## ID-03: `performance.now()` for Timing Critical Sections

**Strength**: SHOULD

**Summary**: Use `performance.now()` for wall-clock timing of specific code paths in production or debugging.

```js
// Good — timing a specific operation
async function loadAndProcess(path) {
  const t0 = performance.now();
  const raw = await Deno.readTextFile(path);
  const t1 = performance.now();
  const result = processData(raw);
  const t2 = performance.now();

  console.log(`Read: ${(t1 - t0).toFixed(2)}ms, Process: ${(t2 - t1).toFixed(2)}ms`);
  return result;
}

// Good — reusable timer utility
function time(label, fn) {
  const start = performance.now();
  const result = fn();
  console.log(`${label}: ${(performance.now() - start).toFixed(2)}ms`);
  return result;
}

const data = time("parse", () => JSON.parse(raw));
```

**Rationale**: `performance.now()` provides sub-millisecond precision. Use it for identifying which phase of a multi-step operation is the bottleneck. For comparative benchmarks, prefer `Deno.bench()` (ID-02) which handles statistical noise.

---

## ID-04: Beware Microbenchmark Traps

**Strength**: SHOULD

**Summary**: Microbenchmarks are unreliable unless you account for JIT warmup, dead code elimination, and call-site polymorphism.

```js
// Bad — JIT hasn't warmed up; first run is interpreter speed
const start = performance.now();
doWork();
console.log(performance.now() - start); // misleadingly slow

// Good — warm up first, then measure
for (let i = 0; i < 1000; i++) doWork(); // warmup
const start = performance.now();
for (let i = 0; i < 10000; i++) doWork(); // measured
console.log((performance.now() - start) / 10000);

// Bad — dead code elimination: engine may skip work with no observable effect
const start = performance.now();
for (let i = 0; i < 1e6; i++) {
  Math.sqrt(i); // result unused — engine may eliminate entirely
}

// Good — use the result to prevent elimination
let sum = 0;
for (let i = 0; i < 1e6; i++) {
  sum += Math.sqrt(i);
}
```

**Key traps**:
- **JIT warmup**: First executions run in the interpreter; subsequent runs are JIT-compiled and much faster
- **Dead code elimination**: Engines remove computations whose results are never used
- **Monomorphic vs megamorphic**: A function called with one type is faster than one called with many types
- **GC pauses**: Garbage collection can occur during measurement, skewing results

**Rationale**: `Deno.bench()` handles warmup and statistical analysis automatically. If you must use manual timing, account for these traps explicitly. Always use the result of computation to prevent elimination.

---

## ID-05: `Map` over Plain Objects for Dynamic Key Collections

**Strength**: SHOULD

**Summary**: `Map` provides O(1) lookup for any key type, no prototype pollution, and a `.size` property. Use it when keys are dynamic or non-string.

```js
// Good — Map for dynamic key-value collection
const frequency = new Map();
for (const word of words) {
  frequency.set(word, (frequency.get(word) ?? 0) + 1);
}

// Bad — object keys coerce to strings; "constructor" is a trap
const frequency = {};
for (const word of words) {
  frequency[word] = (frequency[word] ?? 0) + 1;
  // "constructor" and "toString" collide with Object.prototype
}
```

**When objects are fine**: Fixed, known, string-keyed records with a small number of properties (configuration objects, DTOs). For 3-5 known keys, there is no meaningful performance difference.

**Rationale**: `Map` accepts any key type without coercion, has O(1) `.has()`/`.get()`/`.set()`, exposes `.size` directly, and has no inherited keys from `Object.prototype`. Use it when the key set is dynamic or potentially large (Exploring JS Ch. 33; JS Definitive Guide, §11.1).

**See also**: `01-core-idioms.md` ID-16, `05-type-discipline.md` ID-26

---

## ID-06: `Set` over Arrays for Membership Testing

**Strength**: SHOULD

**Summary**: `Set.has()` is O(1); `Array.includes()` is O(n). For repeated membership checks, the difference compounds.

```js
// Good — O(1) per lookup
const banned = new Set(["spam", "phishing", "malware"]);
const clean = items.filter((item) => !banned.has(item.category));

// Bad — O(n) per lookup, O(n*m) total
const banned = ["spam", "phishing", "malware"];
const clean = items.filter((item) => !banned.includes(item.category));

// Good — deduplication
const unique = [...new Set(items)];
```

**Crossover point**: For very small collections (< 5 elements), `Array.includes()` can be faster due to lower overhead. For any collection that grows or is checked repeatedly, `Set` wins decisively.

**Rationale**: `Set` uses a hash-based internal structure. `Array.includes()` performs a linear scan. The difference is negligible for 3 elements but dramatic for 1000 (Exploring JS Ch. 33; JS Definitive Guide, §11.1).

---

## ID-07: `WeakMap` for Object-Keyed Caches That Don't Prevent GC

**Strength**: SHOULD

**Summary**: A `Map` cache keyed by objects prevents garbage collection. A `WeakMap` lets entries be collected when the key has no other references.

```js
// Good — WeakMap: entries are GC'd with the key
const layoutCache = new WeakMap();
function getLayout(element) {
  if (layoutCache.has(element)) return layoutCache.get(element);
  const layout = computeExpensiveLayout(element);
  layoutCache.set(element, layout);
  return layout;
}
// When element is removed from DOM and dereferenced, cache entry is collected

// Bad — Map: element stays alive as long as cache exists
const layoutCache = new Map();
// Same code, but element is never GC'd even after removal from DOM
```

**Rationale**: `WeakMap` holds keys weakly — when the only reference to a key is the `WeakMap` itself, both key and value are eligible for GC. `WeakMap` has no `.size`, no iteration, and no `.clear()` — these limitations exist because contents can change non-deterministically due to GC (Exploring JS Ch. 37; JS Definitive Guide, §11.1.3).

---

## ID-08: TypedArrays for Numeric/Binary Data

**Strength**: CONSIDER

**Summary**: TypedArrays are ~4x faster and ~8x more memory-efficient than regular Arrays for numeric data.

```js
// Good — TypedArray for numeric computation
const data = new Float64Array(1_000_000); // contiguous, unboxed, zero-initialized

// Sieve of Eratosthenes — Uint8Array vs Array
function sieve(n) {
  const isPrime = new Uint8Array(n + 1); // 1 byte each, not a JS object per slot
  isPrime.fill(1);
  isPrime[0] = isPrime[1] = 0;
  for (let i = 2; i * i <= n; i++) {
    if (isPrime[i]) {
      for (let j = i * i; j <= n; j += i) isPrime[j] = 0;
    }
  }
  return isPrime;
}

// Bad — regular Array for large numeric data
const data = new Array(1_000_000).fill(0); // boxed values, possible holes
```

**Rationale**: Regular arrays store each element as a boxed JS value with type tags and pointer indirection. TypedArrays store elements in a contiguous `ArrayBuffer` with no boxing. Flanagan gives a concrete benchmark: a sieve with `Uint8Array` runs "more than four times faster and uses eight times less memory" (Exploring JS Ch. 36; JS Definitive Guide, §11.2).

**See also**: `05-type-discipline.md` ID-27

---

## ID-09: Avoid Sparse Arrays — Holes Are Slower

**Strength**: SHOULD

**Summary**: Sparse arrays (arrays with holes) force engines into slower dictionary-mode representations and produce surprising iteration behavior.

```js
// Bad — creates holes (sparse)
const a = new Array(1000); // 1000 holes, not 1000 undefined values
a[999] = "last";           // indices 0-998 are holes

// Bad — delete creates a hole
const b = [1, 2, 3];
delete b[1]; // b is now [1, empty, 3] — sparse

// Good — dense initialization
const a = Array.from({ length: 1000 }, () => 0); // dense, all zeros
const b = new Uint32Array(1000);                  // dense, typed

// Good — use undefined, not delete, if you need to "clear" an element
b[1] = undefined; // still dense, element exists
```

**Why holes are problematic**:
- Engines optimize dense arrays as contiguous memory; holes force fallback to hash-map representation
- `forEach()` and `map()` behave differently on holes: `forEach` skips them, `map` preserves them
- A hole is not the same as `undefined`: `0 in [,]` is `false`; `0 in [undefined]` is `true`

**Rationale**: Rauschmayer: "engines optimize dense arrays for speed." Flanagan: "sparse arrays are typically slower." Avoid `new Array(n)` (creates holes) and `delete arr[i]` (creates holes). Use `Array.from()` or TypedArrays for dense initialization (Exploring JS Ch. 34; JS Definitive Guide, §7.3).

---

## ID-10: `push`/`pop` Are O(1); `shift`/`unshift` Are O(n)

**Strength**: SHOULD

**Summary**: Work from the end of an array (stack pattern) when possible. Front operations re-index every element.

```js
// Good — stack: both ends O(1)
const stack = [];
stack.push(item);   // O(1) amortized
stack.pop();         // O(1)

// Bad for large arrays — queue via shift is O(n)
const queue = [];
queue.push(item);    // O(1)
queue.shift();       // O(n) — every element re-indexed

// Good for high-throughput queues — index-pointer approach
class FastQueue {
  #data = [];
  #head = 0;
  enqueue(item) { this.#data.push(item); }
  dequeue() { return this.#data[this.#head++]; }
  get size() { return this.#data.length - this.#head; }
  // Note: for production use, periodically compact with
  // this.#data = this.#data.slice(this.#head); this.#head = 0;
  // to prevent unbounded memory growth from the abandoned head portion
}
```

**Also O(n)**: `unshift()` (prepend), `splice()` at arbitrary positions.

**Rationale**: `shift()` and `unshift()` must move every element in the array. For small arrays this is negligible; for arrays of 10,000+ elements it becomes measurable. Engines may optimize some cases, but the algorithmic complexity is inherent (Exploring JS Ch. 34; JS Definitive Guide, §7.8.4).

---

## ID-11: Pre-Allocate When Size Is Known

**Strength**: CONSIDER

**Summary**: When the output size is known in advance, pre-allocate to avoid repeated array resizing.

```js
// Good — pre-allocate dense array
const result = Array.from({ length: n }, (_, i) => compute(i));

// Good — pre-allocate TypedArray
const buffer = new Float64Array(sampleCount);
for (let i = 0; i < sampleCount; i++) {
  buffer[i] = generateSample(i);
}

// Less efficient — push in a loop (array grows incrementally)
const result = [];
for (let i = 0; i < n; i++) {
  result.push(compute(i));
}
```

**Rationale**: Arrays grow by reallocating and copying when capacity is exceeded. Pre-allocation avoids this overhead. For small arrays, the difference is negligible. For large arrays (10,000+), it can matter. `Array.from()` with a mapping function is the idiomatic dense pre-allocation pattern (Exploring JS Ch. 34).

---

## ID-12: Chain vs Intermediate Arrays — `.flatMap()` and `.reduce()` Can Avoid Double Allocation

**Strength**: CONSIDER

**Summary**: `.filter().map()` allocates two arrays. `.flatMap()` or a single `.reduce()` can do the same work in one pass.

```js
// Two passes, two allocations
const result = items
  .filter((x) => x.active)
  .map((x) => x.name);

// One pass, readable — but allocates a small array per element
const result = items.flatMap((x) =>
  x.active ? [x.name] : [],
);

// One pass, one allocation — genuinely minimal allocations
const result = items.reduce((acc, x) => {
  if (x.active) acc.push(x.name);
  return acc;
}, []);
```

**Trade-off note**: `.flatMap()` is one pass but allocates a `[value]` or `[]` array per element — it is the readability winner for combined filter+transform, not necessarily the allocation winner. `.reduce()` with a single accumulator array is the true minimal-allocation approach. For typical arrays (< 1000 elements), `.filter().map()` is clearest and the allocation cost is negligible.

**Rationale**: `.flatMap()` applies the callback and flattens in a single pass — it's readable and avoids the intermediate filtered array. `.reduce()` is the lowest-allocation option when that matters. The readability of `.filter().map()` is often worth the extra allocation (Exploring JS Ch. 34; JS Definitive Guide, §7.8.2).

---

## ID-13: Short-Circuiting Methods — Use `.find()` / `.some()` over `.filter()`

**Strength**: SHOULD

**Summary**: `.find()`, `.findIndex()`, `.some()`, and `.every()` stop at the first match. `.filter()` always scans the entire array.

```js
// Good — stops at first match
const admin = users.find((u) => u.role === "admin");
const hasErrors = results.some((r) => r.status === "error");
const allValid = inputs.every((i) => i.length > 0);

// Bad — scans entire array to find one element
const admin = users.filter((u) => u.role === "admin")[0];

// Bad — scans entire array to check existence
const hasErrors = results.filter((r) => r.status === "error").length > 0;
```

**Rationale**: `.filter()[0]` allocates a full array and examines every element even when only the first match is needed. `.find()` stops immediately. `.some()` and `.every()` short-circuit on the first decisive result. These methods express intent more clearly AND perform better (Exploring JS Ch. 34; JS Definitive Guide, §7.8.1).

**See also**: `06-functions-closures.md` ID-21, ID-22

---

## ID-14: Generators for Lazy Sequences — Process On Demand

**Strength**: SHOULD

**Summary**: Generators compute values one at a time. Combined with lazy pipeline operators, they avoid materializing intermediate arrays.

```js
// Good — lazy: only computes what's consumed
function* filter(pred, iterable) {
  for (const x of iterable) if (pred(x)) yield x;
}
function* map(fn, iterable) {
  for (const x of iterable) yield fn(x);
}
function* take(n, iterable) {
  for (const x of iterable) {
    if (n-- <= 0) return;
    yield x;
  }
}

// Only the first 5 matching items are ever computed
const result = [...take(5, map(transform, filter(isValid, hugeDataSet)))];

// Bad — eager: computes and allocates everything, then throws most away
const result = hugeDataSet.filter(isValid).map(transform).slice(0, 5);
```

**Rationale**: The eager version allocates two intermediate arrays (filter result, map result) and processes every element, even though only 5 are needed. The generator pipeline computes at most 5 items and allocates nothing between stages. Use generators for large or unbounded data sources (Exploring JS Ch. 38; JS Definitive Guide, §12.3).

**See also**: `06-functions-closures.md` ID-05

---

## ID-15: Iterator Helpers for Lazy Pipelines

**Strength**: CONSIDER

**Summary**: ES2025 iterator helpers (`.map()`, `.filter()`, `.take()`, `.drop()`) add lazy pipeline support to all iterators. Supported in Deno — verify with `deno eval "[1,2,3].values().map(x=>x*2).toArray()"` if unsure.

```js
// Good — lazy pipeline on any iterable, no intermediate arrays
function* naturals() { let n = 0; while (true) yield n++; }

const firstFiveEvenSquares = naturals()
  .filter((n) => n % 2 === 0)
  .map((n) => n * n)
  .take(5)
  .toArray();
// [0, 4, 16, 36, 64]

// Good — lazy pipeline from a Set (Sets have no native .map/.filter)
const positives = new Set(
  new Set([-5, 2, 6, -3]).values()
    .filter((x) => x >= 0),
);

// Good — bridge from Array to lazy pipeline
[1, 2, 3, 4, 5].values()
  .filter((x) => x % 2 === 0)
  .map((x) => x * 10)
  .toArray(); // [20, 40]
```

**Rationale**: Iterator helpers add `.map()`, `.filter()`, `.flatMap()`, `.drop()`, `.take()`, `.reduce()`, `.find()`, `.some()`, `.every()`, `.forEach()`, and `.toArray()` to `Iterator.prototype`. All transform methods are lazy — no intermediate arrays. `.take(n)` and `.drop(n)` enable safe consumption of infinite generators (Exploring JS Ch. 37).

---

## ID-16: `for-of` vs `.forEach()` vs `for` — Readability Wins

**Strength**: SHOULD

**Summary**: Choose the iteration form that best expresses intent. Don't convert idiomatic `.map()` to `for` loops for "performance" without profiling evidence.

```js
// Good — .map() for transformation (expresses intent)
const names = users.map((u) => u.name);

// Good — for-of for side effects and control flow
for (const user of users) {
  if (user.banned) continue;
  notify(user);
}

// Bad — converting .map() to for loop "for performance" without evidence
const names = [];
for (let i = 0; i < users.length; i++) {
  names.push(users[i].name);
}
```

**When raw `for` is justified**: Tight numerical loops (100,000+ iterations) where profiling shows the overhead of `.map()` or `for-of` matters. This is rare in application code.

**Rationale**: Engines heavily optimize all three forms. The differences are negligible for typical workloads. Readability and intent-communication are the default priority. Only switch to a lower-level form when profiling identifies a specific hot path (Exploring JS Ch. 34).

**See also**: `01-core-idioms.md` ID-25, `06-functions-closures.md` ID-24

---

## ID-17: Early Exit with `break`/`return` in `for-of`

**Strength**: SHOULD

**Summary**: `.forEach()` cannot break. `for-of` can. Use `for-of` when early termination is possible.

```js
// Good — stops processing as soon as target is found
function findFirst(items, predicate) {
  for (const item of items) {
    if (predicate(item)) return item;
  }
  return undefined;
}

// Bad — .forEach processes every element even after "finding" the answer
let found = null;
items.forEach((item) => {
  if (found) return; // only exits the callback, not the loop
  if (predicate(item)) found = item;
});
```

**Rationale**: `.forEach()` has no early-termination mechanism — `return` only exits the callback, not the loop. For searches, validations, and any operation that can terminate early, `for-of` with `break` or `return` avoids unnecessary work (JS Definitive Guide, §7.8.1; Exploring JS Ch. 34).

---

## ID-18: Keep Object Shapes Consistent

**Strength**: SHOULD

**Summary**: Initialize all properties in the same order every time. Don't add or remove properties after construction.

```js
// Good — consistent shape: always the same properties in the same order
function createPoint(x, y, z = 0) {
  return { x, y, z };
}

// Bad — shape varies depending on input
function createPoint(x, y, z) {
  const p = { x, y };
  if (z !== undefined) p.z = z; // different shape than points without z
  return p;
}

// Bad — adding properties later changes shape
const p = { x: 0, y: 0 };
p.z = 0; // shape mutation
```

**Rationale**: Engines optimize objects with consistent property structures — objects that always have the same properties in the same order share compiled code and fast property access paths. Divergent structures cause the engine to fall back to slower generic paths. The fix is simple: always initialize all properties, using default values for optional ones (Deep JS Ch. 10; JS Definitive Guide, §6.1).

---

## ID-19: Avoid `delete` — Use `undefined` or Destructure-Out

**Strength**: SHOULD

**Summary**: `delete obj.prop` changes the object's shape, degrading performance. Set to `undefined` or create a new object without the property.

```js
// Bad — shape mutation, potential deoptimization
delete obj.temp;

// Good — shape preserved, property logically cleared
obj.temp = undefined;

// Good — new object without the property (non-destructive)
const { temp, ...clean } = obj;
```

**Rationale**: `delete` forces the engine to transition the object to a different internal structure, potentially falling back to a slower dictionary-mode representation. Setting to `undefined` preserves the structure. Destructuring with rest creates a clean new object (Deep JS Ch. 8, 10).

**See also**: `04-values-references.md` ID-14

---

## ID-20: Cache Deep Property Lookups in Local Variables

**Strength**: CONSIDER

**Summary**: Property lookup walks the prototype chain. In hot loops, cache inherited or deeply nested values in a local variable.

```js
// Good — cache deeply nested property before the loop
const transform = config.pipeline.transform;
for (const item of items) {
  result.push(transform(item));
}

// Bad — deeply nested lookup on every iteration
for (const item of items) {
  result.push(config.pipeline.transform(item)); // 3-level chain per iteration
}
```

**Note on built-in lookups**: Caching `Math.sqrt` or `Math.floor` into locals is a frequently cited optimization, but modern engines inline-cache these stable built-in lookups aggressively — the benefit is minimal. The pattern genuinely helps for deeply nested property chains (like `config.pipeline.transform`) and dynamically resolved properties where inline caches miss.

**Rationale**: Property lookup traverses the prototype chain outward until the name is found. Local variables are resolved in one step. For stable built-in lookups, engines already optimize this. For deep chains and dynamic property access, local caching is a reliable win (Deep JS Ch. 4, 5).

---

## ID-21: `Object.keys()`/`Object.entries()` Allocate Arrays

**Strength**: CONSIDER

**Summary**: These methods create a new array on every call. In hot paths, cache the result or use `for-in` with `Object.hasOwn()`.

```js
// Good — cache once, iterate many times
const keys = Object.keys(config);
for (let i = 0; i < 1000; i++) {
  for (const k of keys) {
    process(k, config[k]);
  }
}

// Bad — allocates a new array on every outer iteration
for (let i = 0; i < 1000; i++) {
  for (const k of Object.keys(config)) { // new array each time
    process(k, config[k]);
  }
}

// Alternative — for-in with hasOwn (zero allocation per iteration)
for (const k in config) {
  if (Object.hasOwn(config, k)) {
    process(k, config[k]);
  }
}
```

**Rationale**: `Object.keys()`, `Object.values()`, and `Object.entries()` each allocate a fresh array. For code called infrequently, this is fine. In hot inner loops, the allocation cost compounds. Cache the result or use `for-in` (Deep JS Ch. 13; Exploring JS Ch. 30).

---

## ID-22: Template Literals vs Concatenation — Equivalent in Practice

**Strength**: SHOULD

**Summary**: There is no meaningful performance difference between template literals and `+` concatenation. Choose based on readability.

```js
// Both are fine — choose the more readable option
const msg = `Hello, ${name}! You have ${count} items.`;
const msg = "Hello, " + name + "! You have " + count + " items.";

// For large string assembly, use array + join regardless of syntax
const parts = [];
for (const item of items) {
  parts.push(`<li>${item.name}</li>`);
}
const html = parts.join("\n");
```

**Rationale**: Template literals compile to equivalent concatenation. The engine handles both the same way. The only performance consideration for strings is tight-loop assembly, where array + `.join()` avoids repeated intermediate string allocation regardless of which syntax is used (Exploring JS Ch. 23; JS Definitive Guide, §3.3.4).

---

## ID-23: Collect String Pieces in an Array, `.join()` at the End

**Strength**: SHOULD

**Summary**: For building large strings from many fragments, collect in an array and `.join()` once.

```js
// Good — one final allocation
function buildCSV(rows) {
  const lines = [];
  for (const row of rows) {
    lines.push(row.join(","));
  }
  return lines.join("\n");
}

// Risky in large loops — repeated intermediate strings
function buildCSV(rows) {
  let csv = "";
  for (const row of rows) {
    csv += row.join(",") + "\n"; // new string on every iteration
  }
  return csv;
}
```

**Rationale**: Strings are immutable — every `+=` creates a new string. For small concatenations, engines optimize this well. For thousands of iterations, the intermediate allocations accumulate. Array + `.join()` produces the final string in one allocation (Exploring JS Ch. 22).

---

## ID-24: Avoid Allocations in Hot Loops

**Strength**: SHOULD

**Summary**: Hoist object/array creation out of loops when the same structure is reused.

```js
// Bad — allocates a new options object on every iteration
for (const item of items) {
  const result = process({ ...defaults, id: item.id }); // new object per iteration
}

// Good — reuse one object, mutate only the changing field
const options = { ...defaults };
for (const item of items) {
  options.id = item.id;
  const result = process(options);
}

// Bad — regex created inside loop AND .match() allocates a result array
for (const line of lines) {
  if (line.match(/^ERROR:/)) errorCount++; // allocates regex + match result array
}

// Good — regex hoisted AND .test() returns boolean (no array allocation)
const errorPattern = /^ERROR:/;
for (const line of lines) {
  if (errorPattern.test(line)) errorCount++; // no allocation per iteration
}
```

**Two wins in the regex example**: (1) Hoisting the regex avoids creating a new `RegExp` on each iteration (though engines may intern regex literals). (2) Switching from `.match()` (which allocates a result array) to `.test()` (which returns a boolean) eliminates per-iteration allocation — this is often the bigger win.

**Rationale**: Every object literal, array literal, regex literal, and spread inside a loop allocates. The allocations themselves are fast, but they create GC pressure that compounds in hot loops. Hoist invariant allocations above the loop. Prefer `.test()` over `.match()` when you only need a boolean (Exploring JS Ch. 34).

---

## ID-25: `structuredClone()` Is Not Free — Copy Only When Needed

**Strength**: SHOULD

**Summary**: Deep copying is expensive. Use shallow copies (spread) for flat data and `structuredClone()` only when nested independence is required.

```js
// Good — shallow copy is sufficient for flat data
const copy = { ...config };

// Good — structuredClone for nested data that will be independently mutated
const independent = structuredClone(deeplyNested);

// Bad — deep-copying when spread would suffice
const copy = structuredClone({ name: "Alice", age: 30 }); // no nesting — wasteful
```

**Rationale**: `structuredClone()` recursively walks the entire object graph, handling circular references, `Date`, `Map`, `Set`, and more. This is substantially more expensive than a spread. Match the copy depth to the mutation depth — most data is flat enough for spread (Exploring JS Ch. 17; Deep JS Ch. 7).

**See also**: `04-values-references.md` ID-09

---

## ID-26: Object Pooling for High-Churn Short-Lived Objects

**Strength**: CONSIDER

**Summary**: For objects created and discarded millions of times (particles, matrix cells), reuse from a pool instead of allocating.

```js
// Good — simple object pool
class Pool {
  #free = [];
  #factory;

  constructor(factory) { this.#factory = factory; }

  acquire() {
    return this.#free.length > 0 ? this.#free.pop() : this.#factory();
  }

  release(obj) {
    this.#free.push(obj);
  }
}

const vecPool = new Pool(() => ({ x: 0, y: 0, z: 0 }));

// Hot loop — reuse instead of allocate
for (const particle of particles) {
  const v = vecPool.acquire();
  v.x = particle.vx; v.y = particle.vy; v.z = particle.vz;
  applyForce(v);
  vecPool.release(v);
}
```

**When it matters**: Only for extreme high-churn scenarios (game loops, simulations, real-time audio). For typical application code, the GC handles short-lived objects efficiently.

**Rationale**: Object pooling trades memory management complexity for reduced GC pressure. It is a CONSIDER-level pattern because it adds complexity and is only worthwhile when profiling identifies allocation/GC as the bottleneck (JS Definitive Guide, §3.1; Exploring JS Ch. 14).

---

## ID-27: Memoize Expensive Pure Functions with Closure + `Map`

**Strength**: SHOULD

**Summary**: Cache results of expensive computations keyed by their arguments.

```js
// Good — single-argument memoization (most common case, simplest and fastest)
function memoize(fn) {
  const cache = new Map();
  return function (arg) {
    if (cache.has(arg)) return cache.get(arg);
    const result = fn.call(this, arg);
    cache.set(arg, result);
    return result;
  };
}

const expensiveCalc = memoize((n) => {
  let result = 0;
  for (let i = 0; i < n; i++) result += Math.sqrt(i);
  return result;
});

expensiveCalc(1_000_000); // computed
expensiveCalc(1_000_000); // cached

// Multi-argument fallback — JSON.stringify as key
function memoizeMulti(fn) {
  const cache = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}
```

**Requirements**: The function must be pure (same input → same output, no side effects). For single-argument functions with primitive args, `cache.has(arg)` is both faster and more correct than `JSON.stringify`. The `JSON.stringify` key strategy works for multi-arg primitives but fails for object arguments (all produce `"[object Object]"`), `undefined` (silently omitted by JSON), and functions.

**Rationale**: Memoization is a memory-for-speed trade-off. It is most effective for expensive computations called repeatedly with the same arguments. The closure holds the cache privately (JS Definitive Guide, §8.8.4; Exploring JS Ch. 13).

**See also**: `06-functions-closures.md` ID-28

---

## ID-28: Bounded Caches — LRU or Size-Limited to Prevent Memory Leaks

**Strength**: SHOULD

**Summary**: Unbounded caches grow forever. Implement a size limit with LRU eviction.

```js
function memoizeLRU(fn, maxSize = 100) {
  const cache = new Map();
  return function (...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) {
      const value = cache.get(key);
      cache.delete(key);
      cache.set(key, value); // move to end (most recently used)
      return value;
    }
    if (cache.size >= maxSize) {
      cache.delete(cache.keys().next().value); // evict oldest
    }
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}
```

**Rationale**: `Map` preserves insertion order, making LRU eviction trivial — the first key is the oldest. Without a size limit, a memoized function called with many distinct argument sets leaks memory indefinitely (Exploring JS Ch. 33).

---

## ID-29: `WeakMap` for Memoizing Per-Object Computations

**Strength**: SHOULD

**Summary**: When the cache key is an object, use `WeakMap` so entries are automatically collected when the key is GC'd.

```js
const styleCache = new WeakMap();

function computeStyles(element) {
  if (styleCache.has(element)) return styleCache.get(element);
  const styles = deriveStyles(element); // expensive
  styleCache.set(element, styles);
  return styles;
}
// When element is collected, the cache entry vanishes automatically
```

**Rationale**: A `Map` keyed by objects creates strong references that prevent GC. `WeakMap` lets the cache clean itself up as objects become unreachable — no manual eviction needed. Only objects (and non-registered symbols) can be `WeakMap` keys (Exploring JS Ch. 37; JS Definitive Guide, §11.1.3).

---

## ID-30: ESM Named Exports Enable Tree Shaking

**Strength**: SHOULD

**Summary**: Named exports let bundlers eliminate unused code. Default-exported objects bundle everything.

```js
// Good — individually tree-shakeable
export function formatDate(d) { /* ... */ }
export function parseDate(s) { /* ... */ }

// Bad — all-or-nothing
export default { formatDate, parseDate };

// Bad — side effect at module level prevents tree shaking
console.log("utils loaded");
export function formatDate(d) { /* ... */ }
```

**Rationale**: Tree shaking depends on static analysis of `import`/`export`. Named exports are individually removable; a default-exported object is a single unit. Module-level side effects force inclusion even if no exports are used (Exploring JS Ch. 49; JS Definitive Guide, §17.5).

**See also**: `01-core-idioms.md` ID-07, `02-api-design.md` ID-07, ID-09

---

## ID-31: Side-Effect-Free Modules — Don't Execute Logic at Import Time

**Strength**: SHOULD

**Summary**: Module top-level code runs once on first import. Keep it declaration-only — no I/O, no global mutations.

```js
// Good — pure declarations
const DEFAULT_TIMEOUT = 5000;
export function createClient(options) {
  return new Client({ timeout: DEFAULT_TIMEOUT, ...options });
}

// Bad — side effect runs on import
const db = await connect("localhost:5432"); // blocks all importers
export function query(sql) { return db.execute(sql); }

// Bad — global mutation on import
globalThis.myLib = { version: "1.0" };
```

**Rationale**: Side effects at module level defeat tree shaking, make testing difficult, and create import-order dependencies. Let callers trigger initialization explicitly (Exploring JS Ch. 29).

**See also**: `02-api-design.md` ID-09

---

## ID-32: Don't Hand-Unroll Loops

**Strength**: MUST

**Summary**: The engine's JIT compiler unrolls loops far better than hand-written unrolled code. Don't sacrifice readability.

```js
// Bad — hand-unrolled "optimization"
function sum(arr) {
  let total = 0;
  const len = arr.length;
  let i = 0;
  for (; i < len - 3; i += 4) {
    total += arr[i] + arr[i+1] + arr[i+2] + arr[i+3];
  }
  for (; i < len; i++) total += arr[i];
  return total;
}

// Good — clear, idiomatic, JIT-friendly
function sum(arr) {
  let total = 0;
  for (const n of arr) total += n;
  return total;
}
```

**Rationale**: Hand-unrolled loops are harder to read, harder to maintain, and rarely faster than what the JIT produces from idiomatic code. Engines are designed to optimize common patterns — write the pattern the engine expects, not a clever alternative.

---

## ID-33: Don't Convert Idiomatic Code to "Faster" Unreadable Code Without Evidence

**Strength**: MUST

**Summary**: Readability is the default priority. Never trade clarity for hypothetical performance without profiling data from a real workload.

```js
// Bad — "clever" bit manipulation instead of Math.floor
const n = ~~(x / y);
const n = (x / y) | 0;

// Good — clear intent, engine optimizes it
const n = Math.floor(x / y);

// Bad — manual loop instead of .map() "for performance"
const names = [];
for (let i = 0; i < users.length; i++) names.push(users[i].name);

// Good — intent is clear
const names = users.map((u) => u.name);
```

**Rationale**: Bit tricks like `~~x` and `x | 0` truncate to 32-bit integers, which silently destroys values larger than 2^31. They obscure intent, introduce bugs for large numbers, and are not meaningfully faster than `Math.floor()` or `Math.trunc()`. Always prefer the clear, correct version.

---

## ID-34: Don't Cache `array.length` in `for` Loops

**Strength**: SHOULD

**Summary**: Engines already optimize `array.length` access. Caching it manually adds noise without benefit.

```js
// Unnecessary — engine caches this
for (let i = 0, len = arr.length; i < len; i++) { /* ... */ }

// Good — idiomatic and equally fast
for (let i = 0; i < arr.length; i++) { /* ... */ }

// Better — for-of when you don't need the index
for (const item of arr) { /* ... */ }
```

**Rationale**: In the early 2000s, caching `.length` was a real optimization because engines re-read it from the object on every iteration. Modern engines recognize this pattern and optimize it. The manual cache is now pure noise.

---

## ID-35: Proxies Have Overhead — Don't Use in Hot Paths Without Measurement

**Strength**: CONSIDER

**Summary**: Proxy traps add a function-call overhead on every intercepted operation. Keep Proxies away from tight loops.

```js
// Bad — Proxy in hot loop
const proxied = new Proxy(data, validationHandler);
for (const item of largeArray) {
  total += proxied[item.key]; // get trap fires on every access
}

// Good — validate once, then use plain object in hot path
validateData(data); // one-time check
for (const item of largeArray) {
  total += data[item.key]; // direct access, no trap overhead
}
```

**Rationale**: Rauschmayer explicitly notes: "Proxies slow down code; performance may be a consideration." Even an empty handler (transparent proxy) adds indirection. Proxy invariant checking is also not free. Use Proxies for development tooling, validation boundaries, and infrequently accessed paths — not inner loops (Deep JS Ch. 20; JS Definitive Guide, §14.7).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Profile first, optimize second | MUST | Don't optimize without measuring |
| 02 | `Deno.bench()` for microbenchmarks | SHOULD | Handles warmup, sampling, comparison |
| 03 | `performance.now()` for timing | SHOULD | Sub-millisecond precision for sections |
| 04 | Microbenchmark traps | SHOULD | JIT warmup, dead code elimination, GC pauses |
| 05 | `Map` for dynamic collections | SHOULD | O(1), any key type, no prototype pollution |
| 06 | `Set` for membership testing | SHOULD | O(1) `.has()` vs O(n) `.includes()` |
| 07 | `WeakMap` for GC-safe caches | SHOULD | Entries collected when keys are unreachable |
| 08 | TypedArrays for numeric data | CONSIDER | ~4x faster, ~8x less memory |
| 09 | Avoid sparse arrays | SHOULD | Holes force slower engine paths |
| 10 | `push`/`pop` O(1) vs `shift`/`unshift` O(n) | SHOULD | Work from the end when possible |
| 11 | Pre-allocate when size is known | CONSIDER | Avoid incremental array resizing |
| 12 | `.flatMap()` over `.filter().map()` | CONSIDER | One pass vs two; readability first |
| 13 | Short-circuiting methods | SHOULD | `.find()`/`.some()` stop early; `.filter()` doesn't |
| 14 | Generators for lazy evaluation | SHOULD | No intermediate arrays; process on demand |
| 15 | Iterator helpers | CONSIDER | Lazy `.map()`/`.filter()`/`.take()` on any iterator |
| 16 | Iteration form — readability wins | SHOULD | Don't convert `.map()` to `for` without evidence |
| 17 | Early exit with `break`/`return` | SHOULD | `.forEach()` cannot break; `for-of` can |
| 18 | Consistent object shapes | SHOULD | Same properties, same order — hidden classes |
| 19 | Avoid `delete` | SHOULD | Shape mutation degrades performance |
| 20 | Cache deep property lookups | CONSIDER | Locals resolve in one step; chain walks are slower |
| 21 | `Object.keys()` allocates arrays | CONSIDER | Cache result or use `for-in` in hot paths |
| 22 | Template literals ≈ concatenation | SHOULD | No meaningful difference; readability first |
| 23 | Array + `.join()` for large strings | SHOULD | One allocation vs repeated intermediates |
| 24 | Hoist allocations out of hot loops | SHOULD | Spread, regex, object literals inside loops = GC pressure |
| 25 | `structuredClone()` is not free | SHOULD | Use spread for flat data; deep copy only when needed |
| 26 | Object pooling | CONSIDER | Only for extreme high-churn (games, simulations) |
| 27 | Memoize expensive pure functions | SHOULD | Closure + `Map`; must be pure |
| 28 | Bounded caches (LRU) | SHOULD | Unbounded caches leak memory |
| 29 | `WeakMap` for per-object memoization | SHOULD | Auto-evicts when key is GC'd |
| 30 | Named exports for tree shaking | SHOULD | Individually removable; default objects are not |
| 31 | No side effects at module level | SHOULD | Defeats tree shaking and testing |
| 32 | Don't hand-unroll loops | MUST | JIT does it better; readability first |
| 33 | Don't trade clarity for speed without evidence | MUST | Bit tricks hide bugs; idiomatic code is optimized |
| 34 | Don't cache `array.length` | SHOULD | Engines optimize this; manual cache is noise |
| 35 | Proxies have overhead | CONSIDER | Keep off hot paths; validate once, access directly |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `Map`/`Set` (ID-16), `for-of` vs `.forEach()` (ID-25), named exports (ID-07), `structuredClone()` (ID-23)
- **API Design**: See `02-api-design.md` for module interface design (ID-06–10), tree shaking (ID-07, ID-08)
- **Error Handling**: See `03-error-handling.md` for validation patterns (ID-23, ID-24) — validate at boundaries, trust within
- **Values & References**: See `04-values-references.md` for `structuredClone()` (ID-09), spread (ID-06), `Object.freeze()` (ID-16–19), `delete` avoidance (ID-19 here cross-refs ID-14 there)
- **Type Discipline**: See `05-type-discipline.md` for TypedArrays (ID-27) and `Map`/`Set` as typed collections (ID-26)
- **Functions & Closures**: See `06-functions-closures.md` for generators (ID-05), closures (ID-06–09), and higher-order functions (ID-20–24)
- **Async & Concurrency**: See `07-async-concurrency.md` for parallel vs sequential `await` (ID-13, ID-18), Workers (ID-30), streams (ID-27–29)
- **Anti-Patterns**: See `09-anti-patterns.md` for ID-17, 34 (performance-related anti-patterns)

---

## External References

- [Deno — Benchmarking](https://docs.deno.com/runtime/fundamentals/testing/#benchmarking)
- [MDN — performance.now()](https://developer.mozilla.org/en-US/docs/Web/API/Performance/now)
- [MDN — Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [MDN — WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
