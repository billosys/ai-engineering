# Anti-Patterns

A dedicated catalog of what NOT to do in JavaScript — cross-cutting mistakes that span multiple guides, patterns disproportionately common in AI-generated code, and subtle traps that need deeper treatment than an inline "Bad" example can provide. Every entry includes a fix with a cross-reference to the guide that teaches the positive pattern. Grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: Using `==` Instead of `===`

**Strength**: MUST-AVOID

**Summary**: `==` applies a multi-step coercion cascade that produces surprising results. Use `===` except for the `== null` idiom.

```js
// Anti-pattern — coercion surprises
"" == 0;            // true — string converts to number
"0" == false;       // true — both become 0
2 == true;          // false — true becomes 1, not "truthy match"
[] == false;        // true — [] → "" → 0, false → 0
null == 0;          // false — but null == undefined is true
"\t\n" == 0;        // true — whitespace string converts to 0

// Fix — strict equality, no coercion
"" === 0;           // false
"0" === false;      // false
value === null || value === undefined;  // explicit

// The one accepted exception:
if (value == null) { /* checks both null and undefined */ }
```

**Why it's wrong**: The `==` algorithm converts booleans to numbers first, then strings to numbers, then objects to primitives via `ToPrimitive`. The result is predictable by the spec but surprising to humans. `2 == true` is `false` because `true` becomes `1`, not because `2` isn't truthy — this trips even experienced developers (Exploring JS Ch. 13; Deep JS Ch. 14; Eloquent JS Ch. 1).

**Fix**: `01-core-idioms.md` ID-02. Biome's `noDoubleEquals` rule catches this automatically.

---

## ID-02: Trusting `typeof` for All Type Checks

**Strength**: SHOULD-AVOID

**Summary**: `typeof` returns misleading results for `null`, arrays, and `NaN`. Use specific checks for each.

```js
// Anti-pattern — typeof lies
typeof null;        // "object" — historical bug
typeof [];          // "object" — arrays are objects
typeof NaN;         // "number" — NaN is a numeric value
typeof /regex/;     // "object" — can't distinguish from plain objects

// Fix — use the right check for each type
value === null;               // null check
Array.isArray(value);         // array check
Number.isNaN(value);          // NaN check
value instanceof RegExp;      // regex check
value !== null && typeof value === "object";  // true object check
```

**Why it's wrong**: `typeof` returns only 8 strings. There is no `"null"`, `"array"`, or `"NaN"`. Code that uses `typeof` as a universal type guard will misclassify these values, leading to bugs that are invisible in testing because `typeof null === "object"` looks like a valid object (Exploring JS Ch. 13; JS Definitive Guide, §4.13.3).

**Fix**: `05-type-discipline.md` ID-01, ID-02, ID-04.

---

## ID-03: Using `||` for Defaults When `0`, `""`, or `false` Are Valid

**Strength**: MUST-AVOID

**Summary**: `||` returns the right-hand side for any falsy value, silently discarding `0`, `""`, `false`, and `NaN`.

```js
// Anti-pattern — || swallows legitimate values
function setVolume(level) {
  const vol = level || 50;  // 0 becomes 50!
}
function setTitle(title) {
  const t = title || "Untitled";  // "" becomes "Untitled"!
}

// Fix — ?? only triggers on null/undefined
function setVolume(level) {
  const vol = level ?? 50;  // 0 is preserved
}
function setTitle(title) {
  const t = title ?? "Untitled";  // "" is preserved
}
```

**Why it's wrong**: `||` uses boolean coercion: 8 values are falsy (`false`, `0`, `-0`, `0n`, `NaN`, `""`, `null`, `undefined`). When `0` is a valid volume level or `""` is a valid empty title, `||` silently replaces them with the default. This is one of the most common bugs in AI-generated code (Exploring JS Ch. 14; JS Definitive Guide, §4.13.2).

**Fix**: `01-core-idioms.md` ID-03.

---

## ID-04: Global `isNaN()` vs `Number.isNaN()`

**Strength**: SHOULD-AVOID

**Summary**: The global `isNaN()` coerces its argument to a number first, producing false positives.

```js
// Anti-pattern
isNaN("hello");     // true — "hello" coerces to NaN, then isNaN checks
isNaN(undefined);   // true — undefined coerces to NaN
isNaN({});          // true — {} coerces to NaN

// Fix — no coercion
Number.isNaN("hello");    // false — "hello" is not NaN
Number.isNaN(undefined);  // false
Number.isNaN(NaN);        // true — the only true positive

// Also remember: NaN === NaN is false
[1, NaN, 3].indexOf(NaN);    // -1 (uses ===)
[1, NaN, 3].includes(NaN);   // true (uses SameValueZero)
```

**Why it's wrong**: `isNaN()` answers "does this coerce to NaN?" not "is this NaN?" Any non-numeric string, object, or undefined passes the check, making it useless as a type guard. NaN propagates silently through arithmetic — a single NaN input corrupts an entire calculation chain with no exception thrown (Exploring JS Ch. 18; JS Definitive Guide, §3.2.3).

**Fix**: `05-type-discipline.md` ID-04, ID-11.

---

## ID-05: `parseInt` Without a Radix

**Strength**: SHOULD-AVOID

**Summary**: `parseInt` without a radix infers the base from the string prefix. Always pass `10`.

```js
// Anti-pattern — radix inference and silent truncation
parseInt("0x1F");       // 31 — hex inferred from "0x" prefix
parseInt("123abc");     // 123 — silently ignores trailing characters
parseInt("  42  ");     // 42 — silently trims whitespace

// Fix — explicit radix
parseInt("08", 10);     // always 8
parseInt("1F", 16);     // 31 — explicit hex

// Better for strict parsing: Number()
Number("123abc");       // NaN — rejects trailing characters
Number("123");          // 123
```

**Why it's wrong**: Without a radix, `parseInt` silently parses with an inferred base. `parseInt("123abc")` returns `123` without signaling that the input was malformed. If the full string must be numeric, `Number()` is the correct choice — it returns `NaN` for any non-numeric content (Exploring JS Ch. 18; JS Definitive Guide, §3.9.2).

**Fix**: `05-type-discipline.md` ID-08.

---

## ID-06: Constructor Wrappers — `new String()`, `new Number()`, `new Boolean()`

**Strength**: SHOULD-AVOID

**Summary**: Calling primitive constructors with `new` creates wrapper objects, not primitives. `new Boolean(false)` is truthy.

```js
// Anti-pattern — wrapper objects
const flag = new Boolean(false);
if (flag) {
  console.log("this runs!"); // objects are always truthy
}
typeof new String("abc");    // "object", not "string"
new Number(42) === 42;       // false — object !== primitive

// Fix — call without new for type conversion
const flag = Boolean(false);     // primitive false
const num = Number("42");        // primitive 42
const str = String(123);         // primitive "123"
```

**Why it's wrong**: `new Boolean(false)` creates an object that wraps `false`. Since all objects are truthy, `if (new Boolean(false))` executes — the opposite of what the code intends. `typeof` returns `"object"` and `===` fails between wrapper and primitive. These are genuine traps, not theoretical concerns (Exploring JS Ch. 13; JS Definitive Guide, §3.9.2).

**Fix**: `05-type-discipline.md` ID-07.

---

## ID-07: Method Extraction Loses `this`

**Strength**: MUST-AVOID

**Summary**: Storing a method in a variable or passing it as a callback disconnects it from its receiver. `this` becomes `undefined` in strict mode.

```js
// Anti-pattern — this is lost
class Handler {
  name = "Handler";
  handle(event) { console.log(`${this.name}: ${event}`); }
}
const h = new Handler();
const fn = h.handle;
fn("click");  // TypeError: Cannot read properties of undefined

// Anti-pattern — event listener
button.addEventListener("click", h.handle);  // this is the button, not h

// Fix — bind or arrow wrapper
button.addEventListener("click", h.handle.bind(h));
button.addEventListener("click", (e) => h.handle(e));

// Fix — arrow class field (permanently bound)
class Handler {
  name = "Handler";
  handle = (event) => { console.log(`${this.name}: ${event}`); };
}
```

**Why it's wrong**: `this` is determined by the call site, not the definition site. When `obj.method` is stored in a variable, the object reference is lost — the function is called with default binding (`undefined` in strict mode). The bug is invisible at extraction and surfaces at call time, often in a different module (Exploring JS Ch. 30; JS Definitive Guide, §8.2).

**Fix**: `06-functions-closures.md` ID-18.

---

## ID-08: Regular Functions as Callbacks When `this` Matters

**Strength**: SHOULD-AVOID

**Summary**: Ordinary functions as callbacks inside methods lose `this` in strict mode. Use arrow functions.

```js
// Anti-pattern — this is undefined inside the callback
class Processor {
  items = [];
  processAll() {
    this.items.forEach(function (item) {
      this.process(item);  // TypeError: this is undefined
    });
  }
  process(item) { /* ... */ }
}

// Fix — arrow function inherits this from the method
class Processor {
  items = [];
  processAll() {
    this.items.forEach((item) => {
      this.process(item);  // works — this is the Processor instance
    });
  }
  process(item) { /* ... */ }
}
```

**Why it's wrong**: In strict mode (which ESM enables automatically), a plain function callback receives `this === undefined`. This is the narrower form of the method-extraction bug — it occurs inside methods that use `.forEach()`, `.map()`, `setTimeout()`, or any other callback-accepting API (Exploring JS Ch. 30; JS Definitive Guide, §8.1.3).

**Fix**: `06-functions-closures.md` ID-02, ID-03.

---

## ID-09: Arrow Functions as Object Methods

**Strength**: SHOULD-AVOID

**Summary**: Arrow functions as object methods inherit `this` from the enclosing scope, not from the object.

```js
// Anti-pattern — this is not the object
const counter = {
  count: 0,
  increment: () => { this.count++; },  // this is undefined (module scope)
};
counter.increment();  // TypeError or silently increments nothing

// Fix — method shorthand
const counter = {
  count: 0,
  increment() { this.count++; },  // this is counter
};
```

**Why it's wrong**: Arrow functions capture `this` lexically from the enclosing scope at definition time. If the object literal is at module top level, `this` is `undefined`. Unlike regular methods, `call()`, `apply()`, and `bind()` cannot override an arrow's `this`. Arrow functions solve the callback problem (ID-08) but create the inverse bug when used as methods (Exploring JS Ch. 27; JS Definitive Guide, §8.1.3).

**Fix**: `06-functions-closures.md` ID-04.

---

## ID-10: `var` in Loops with Closures

**Strength**: MUST-AVOID

**Summary**: `var` creates one binding per function scope. Closures in a loop all share the same variable and see its final value.

```js
// Anti-pattern — all callbacks log 3
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// Output: 3, 3, 3

// Fix — let creates a fresh binding per iteration
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// Output: 0, 1, 2
```

**Why it's wrong**: `var` is function-scoped. The single `i` binding is shared across all iterations. Each closure captures the same binding, not a snapshot of the value. By the time the callbacks execute, the loop has finished and `i` is `3`. This is the classic closure-in-loop bug and is disproportionately common in AI-generated code (Exploring JS Ch. 13; Deep JS Ch. 4; JS Definitive Guide, §3.10.1).

**Fix**: `06-functions-closures.md` ID-07. Biome's `noVar` rule catches `var` usage.

---

## ID-11: Accidental Globals — Missing `const`/`let`

**Strength**: MUST-AVOID

**Summary**: Assigning to an undeclared variable in non-strict mode silently creates a global property.

```js
// Anti-pattern — accidental global (non-strict, non-module)
function calculate(items) {
  total = 0;  // missing const/let — creates globalThis.total
  for (const item of items) {
    total += item.value;
  }
  return total;
}

// Fix — always declare
function calculate(items) {
  let total = 0;
  for (const item of items) {
    total += item.value;
  }
  return total;
}
```

**Why it's wrong**: In non-strict mode, assignment to an undeclared name creates a property on `globalThis`. This pollutes the global namespace, creates action-at-a-distance bugs, and persists beyond the function call. The global object is, as Rauschmayer puts it, "a mistake that JavaScript can't get rid of" (Exploring JS Ch. 14; Deep JS Ch. 5).

**In our target environment** (Deno + ESM), this is caught automatically — ESM is always strict mode, so undeclared assignment throws `ReferenceError`. The entry earns MUST-AVOID because the pattern still bites in `eval()`, REPL sessions, and any non-module `<script>` context. Understanding it explains a class of legacy bugs and why strict mode exists.

**Fix**: `01-core-idioms.md` ID-01. ESM strict mode provides implicit protection.

---

## ID-12: Shadowing Outer Variables Accidentally

**Strength**: SHOULD-AVOID

**Summary**: Declaring a variable with the same name as an outer-scope variable hides the outer one silently.

```js
// Anti-pattern 1 — shadow hides outer, adjustment lost
let result = computeInitial();
if (needsAdjustment) {
  const result = computeAdjusted();  // NEW variable — outer result unchanged
  console.log(result);               // the adjusted value (local)
}
console.log(result);  // still the initial value — adjustment was silently lost

// Anti-pattern 2 — shadow + TDZ self-reference (different bug)
let result = computeInitial();
if (needsAdjustment) {
  const result = adjust(result);  // ReferenceError! the inner `result` is in TDZ
  // The `result` in adjust(result) refers to the inner binding, not the outer one
}

// Fix — use distinct names
let result = computeInitial();
if (needsAdjustment) {
  const adjusted = adjust(result);  // reads outer result, stores in new name
  result = adjusted;
}
```

**Two distinct bugs here**:

1. **Shadow hides outer** (Anti-pattern 1): The inner `const result` creates a new binding. The programmer intends to update the outer variable but instead creates an independent local that is discarded when the block exits.
2. **Shadow + TDZ** (Anti-pattern 2): When the inner binding's initializer references `result`, it refers to the inner `const result` which is still in its Temporal Dead Zone — not the outer `result`. This throws `ReferenceError`.

Both are prevented by using distinct variable names (Exploring JS Ch. 13; JS Definitive Guide, §3.10.1).

**Fix**: `06-functions-closures.md` ID-14. Biome's `noShadowRestrictedNames` rule catches some cases.

---

## ID-13: Relying on `var` Hoisting for Variable Access Before Declaration

**Strength**: SHOULD-AVOID

**Summary**: `var` declarations hoist to the top of their function scope and initialize as `undefined`. Accessing them before the assignment silently returns `undefined` instead of throwing.

```js
// Anti-pattern — silent undefined from hoisting
function process() {
  console.log(data);  // undefined — no error, no warning
  var data = loadData();
  return data;
}

// Fix — let/const: TDZ catches early access
function process() {
  console.log(data);  // ReferenceError — caught immediately
  const data = loadData();
  return data;
}
```

**Why it's wrong**: `var` hoisting silently provides `undefined` instead of throwing an error, making the bug invisible. With `let`/`const`, the Temporal Dead Zone throws `ReferenceError` — a loud failure at the exact line of the mistake (Exploring JS Ch. 13; JS Definitive Guide, §3.10.2).

**Fix**: `01-core-idioms.md` ID-01, `06-functions-closures.md` ID-12.

---

## ID-14: Mutating Function Arguments

**Strength**: MUST-AVOID

**Summary**: Objects and arrays are passed by identity. Mutating a parameter mutates the caller's data.

```js
// Anti-pattern — destroys the caller's array
function logAll(arr) {
  while (arr.length > 0) {
    console.log(arr.shift());  // mutates arr
  }
}
const items = ["a", "b", "c"];
logAll(items);
items;  // [] — destroyed!

// Fix — defensive copy at entry
function logAll(arr) {
  for (const item of [...arr]) {
    console.log(item);
  }
}
```

**Why it's wrong**: The caller does not expect passing an argument to destroy it. `const` on the caller's side does not protect against this — `const` prevents reassignment, not mutation. The symptom appears far from the cause, making these bugs difficult to diagnose (Deep JS Ch. 6; Exploring JS Ch. 14).

**Fix**: `04-values-references.md` ID-12, ID-13.

---

## ID-15: Assuming `const` Means Immutable

**Strength**: SHOULD-AVOID

**Summary**: `const` freezes the binding (variable cannot be reassigned). The value itself remains fully mutable.

```js
// Anti-pattern — expecting const to prevent mutation
const config = { debug: false };
config.debug = true;     // succeeds — const doesn't prevent this
config.newProp = "added"; // also succeeds

const arr = [1, 2, 3];
arr.push(4);             // [1, 2, 3, 4] — succeeds

// Fix — use Object.freeze() for true immutability
const config = Object.freeze({ debug: false });
config.debug = true;     // TypeError in strict mode
```

**Why it's wrong**: This is one of the most common JavaScript misconceptions, consistently flagged by all four sources. `const` means "constant binding" not "constant value." It prevents `config = {}` but not `config.debug = true` (Exploring JS Ch. 11; Deep JS Ch. 8; JS Definitive Guide, §3.10.1).

**Fix**: `04-values-references.md` ID-04, ID-16.

---

## ID-16: Shallow Copy Surprise — Spread Doesn't Copy Nested Objects

**Strength**: SHOULD-AVOID

**Summary**: `{...obj}` and `[...arr]` are shallow. Nested objects are shared references.

```js
// Anti-pattern — shallow copy shares nested refs
const original = { user: { name: "Alice" }, tags: ["admin"] };
const copy = { ...original };
copy.user.name = "Bob";
original.user.name;  // "Bob" — original mutated!

// Fix — structuredClone for deep independence
const copy = structuredClone(original);
copy.user.name = "Bob";
original.user.name;  // "Alice" — independent
```

**Why it's wrong**: Spread creates a new top-level object but every nested object or array is the same reference as in the original. Mutating a nested property through the copy also mutates the original. This is the single most common source of "my copy changed the original" bugs (Deep JS Ch. 7; Exploring JS Ch. 30).

**Fix**: `04-values-references.md` ID-06, ID-08, ID-09.

---

## ID-17: `.sort()` Mutates in Place and Defaults to String Comparison

**Strength**: SHOULD-AVOID

**Summary**: `.sort()` mutates the original array AND defaults to lexicographic (string) comparison — two footguns in one method call.

```js
// Anti-pattern — original is mutated
const original = [3, 1, 2];
const sorted = original.sort();
sorted === original;  // true — same reference!
original;            // [1, 2, 3] — mutated

// Also: default sort is lexicographic, not numeric
[10, 9, 2].sort();   // [10, 2, 9] — string comparison!

// Fix — non-destructive sort (ES2023)
const sorted = original.toSorted((a, b) => a - b);
original;  // [3, 1, 2] — unchanged

// Pre-ES2023 fix
const sorted = [...original].sort((a, b) => a - b);
```

**Two distinct bugs here**:

1. **Mutation**: `.sort()` returns the same mutated reference. `const sorted = arr.sort()` mutates `arr` AND aliases `sorted` to it — the original is destroyed.
2. **Default comparator**: Without a comparator, `.sort()` converts elements to strings and sorts lexicographically. `[10, 9, 2].sort()` produces `[10, 2, 9]` because `"10" < "2"` in string comparison. This is disproportionately common in AI-generated code — always provide a numeric comparator: `(a, b) => a - b`.

(Exploring JS Ch. 34; JS Definitive Guide, §7.8.6). Biome's `useArraySortCompare` rule catches the missing comparator.

**Fix**: `04-values-references.md` ID-15.

---

## ID-18: Sequential `await` on Independent Operations

**Strength**: MUST-AVOID

**Summary**: Consecutive `await` calls on unrelated operations serialize them, doubling total latency. This is disproportionately common in AI-generated code.

```js
// Anti-pattern — sequential, total time = sum of both
const users = await fetch("/api/users").then((r) => r.json());
const posts = await fetch("/api/posts").then((r) => r.json());

// Fix — parallel, total time = max of both
const [users, posts] = await Promise.all([
  fetch("/api/users").then((r) => r.json()),
  fetch("/api/posts").then((r) => r.json()),
]);
```

**Why it's wrong**: Flanagan: "unnecessarily sequential: the fetch of the second URL will not begin until the first fetch is complete." For two independent 500ms network requests, sequential takes ~1000ms; parallel takes ~500ms. Use sequential `await` only when the second operation depends on the first's result (JS Definitive Guide, §13.3.3; Exploring JS Ch. 42).

**Fix**: `07-async-concurrency.md` ID-13. See also `03-error-handling.md` ID-21.

---

## ID-19: `.map(async fn)` Without `Promise.all()`

**Strength**: MUST-AVOID

**Summary**: `Array.map()` with an async callback returns `Promise[]`, not resolved values. This is disproportionately common in AI-generated code.

```js
// Anti-pattern — results is an array of Promises
const results = items.map(async (item) => {
  return await fetchData(item.id);
});
console.log(results[0]);  // Promise { <pending> }

// Fix — wrap with Promise.all()
const results = await Promise.all(
  items.map(async (item) => fetchData(item.id)),
);
console.log(results[0]);  // the actual resolved value
```

**Why it's wrong**: `.map()` does not know about Promises. It returns whatever the callback returns — in this case, a Promise for each element. The outer `await` receives an array, not the resolved values. This is a direct consequence of "awaiting is shallow": `await` inside the `.map()` callback pauses only that callback, not the outer function (Exploring JS Ch. 42; JS Definitive Guide, §13.3.3).

**Fix**: `07-async-concurrency.md` ID-21. See also `03-error-handling.md` ID-22.

---

## ID-20: Fire-and-Forget Promises — Unhandled Rejections

**Strength**: MUST-AVOID

**Summary**: Calling an async function without `await` and without `.catch()` silently loses rejections. In Deno, this terminates the process.

```js
// Anti-pattern — rejection has nowhere to go
async function handleRequest(req) {
  logRequest(req);          // async, unawaited — rejection lost
  return await getData();
}

// Fix — await it
async function handleRequest(req) {
  await logRequest(req);
  return await getData();
}

// Fix — explicit catch for intentional fire-and-forget
async function handleRequest(req) {
  logRequest(req).catch((err) => console.error("Log failed:", err));
  return await getData();
}
```

**Why it's wrong**: An unawaited async call creates a floating Promise with no rejection handler. In modern Deno and Node.js, unhandled rejections terminate the process by default. Even where they don't terminate, they produce silent failures (Exploring JS Ch. 42; JS Definitive Guide, §13.2.4).

**Fix**: `03-error-handling.md` ID-20.

---

## ID-21: Synchronous Throws in Promise-Returning Functions

**Strength**: SHOULD-AVOID

**Summary**: A function that returns a Promise must not throw synchronously. Sync throws escape the Promise chain — callers' `.catch()` never sees them.

```js
// Anti-pattern — sync throw escapes the Promise chain
function fetchData(url) {
  validateUrl(url);              // throws synchronously — escapes .catch()
  return fetch(url).then((r) => r.json());
}
fetchData(badUrl).catch(handleError);  // validateUrl's throw is NOT caught here

// Fix — async function: sync throws become rejections
async function fetchData(url) {
  validateUrl(url);              // throw becomes rejection — caught by .catch()
  const r = await fetch(url);
  return r.json();
}

// Anti-pattern — dual-mode API (callback + Promise)
function readConfig(path, callback) {
  const promise = Deno.readTextFile(path).then(JSON.parse);
  if (callback) {
    promise.then((data) => callback(null, data)).catch((err) => callback(err));
  }
  return promise;
}

// Fix — Promise-only API
async function readConfig(path) {
  const raw = await Deno.readTextFile(path);
  return JSON.parse(raw);
}
```

**Why it's wrong**: Two anti-patterns share a root cause — mixing error models. (1) Synchronous throws in Promise-returning functions escape the chain because callers set up `.catch()`, not `try/catch` around the call. (2) Dual-mode APIs (accepting both a callback and returning a Promise) double the surface area and confuse error handling. In both cases, pick one model: `async` functions handle both cases correctly (Exploring JS Ch. 43; JS Definitive Guide, §13.2).

**Fix**: `03-error-handling.md` ID-18.

---

## ID-22: `.then()` Nesting Instead of Chaining

**Strength**: SHOULD-AVOID

**Summary**: Nesting `.then()` inside `.then()` recreates callback hell. Chain flat.

```js
// Anti-pattern — pyramid of doom with Promises
fetchUser(id).then((user) => {
  fetchPosts(user.id).then((posts) => {
    fetchComments(posts[0].id).then((comments) => {
      render(comments);
    });
  });
});

// Fix — flat chain (note: examples are illustrative; guard empty arrays in production)
fetchUser(id)
  .then((user) => fetchPosts(user.id))
  .then((posts) => fetchComments(posts[0].id))
  .then((comments) => render(comments));

// Better — async/await
const user = await fetchUser(id);
const posts = await fetchPosts(user.id);
const comments = await fetchComments(posts[0].id);
render(comments);
```

**Why it's wrong**: Nested `.then()` calls lose error propagation (the outer chain doesn't see inner rejections) and recreate the indentation pyramid that Promises were designed to eliminate. Promise flattening makes chaining work — returning a Promise from `.then()` automatically resolves it before the next `.then()` fires (Exploring JS Ch. 43; JS Definitive Guide, §13.2).

**Fix**: `03-error-handling.md` ID-14, `07-async-concurrency.md` ID-10.

---

## ID-23: `fetch()` Without `signal`

**Strength**: SHOULD-AVOID

**Summary**: A `fetch()` without an `AbortSignal` cannot be cancelled. Uncancellable requests waste resources.

```js
// Anti-pattern — uncancellable
const data = await fetch("/api/data").then((r) => r.json());

// Fix — pass a signal
const controller = new AbortController();
const data = await fetch("/api/data", { signal: controller.signal })
  .then((r) => r.json());

// Fix — with timeout
const data = await fetch("/api/data", {
  signal: AbortSignal.timeout(5000),
}).then((r) => r.json());
```

**Why it's wrong**: Without a signal, `fetch()` continues consuming bandwidth and server resources even after the result is discarded (user navigated away, timeout expired, component unmounted). In production code, every `fetch()` should accept a signal for coordinated cancellation (Web Platform API standard).

**Fix**: `07-async-concurrency.md` ID-24, ID-26.

---

## ID-24: Functions That Both Return AND Throw for Expected Cases

**Strength**: MUST-AVOID

**Summary**: A function should use one error channel. Don't return `null` on some failures and throw on others.

```js
// Anti-pattern — mixed error channels
function parseConfig(path) {
  if (!path) return null;          // absence → return
  const raw = Deno.readTextFileSync(path);
  if (!raw) throw new Error("Empty file");  // absence → throw
  return JSON.parse(raw);
}
// Caller needs both try/catch AND null check — confusing

// Fix — consistent: throw for all failures
function parseConfig(path) {
  if (!path) throw new TypeError("path is required");
  const raw = Deno.readTextFileSync(path);
  if (!raw) throw new Error(`Config file is empty: ${path}`);
  return JSON.parse(raw);
}

// Fix — consistent: return for expected absence, throw only for unexpected
function findUser(id) {
  return users.get(id);  // undefined if not found (expected)
}
```

**Why it's wrong**: Mixed error channels force callers to handle two different patterns (null-check AND try/catch) for the same function. The rule: throw for unexpected failures; return `undefined`/`null` for expected absence. Pick one channel per function (Exploring JS Ch. 26; JS Definitive Guide, §5.5.6).

**Fix**: `03-error-handling.md` ID-02, ID-25. `02-api-design.md` ID-04.

---

## ID-25: Boolean Parameters — Unreadable Call Sites

**Strength**: SHOULD-AVOID

**Summary**: `render(true, false)` at the call site is unreadable. Use options objects for boolean configuration.

```js
// Anti-pattern — what do true and false mean?
createUser("Alice", true, false, true);

// Fix — options object with named properties
createUser("Alice", { admin: true, verified: false, notify: true });
```

**Why it's wrong**: Boolean parameters are positional and self-documenting only at the definition site, not at the call site. Multiple booleans in a row are a maintenance hazard — inserting a new parameter shifts all positions. Named options are self-documenting and order-independent (Exploring JS Ch. 15; Deep JS Ch. 3).

**Fix**: `02-api-design.md` ID-01.

---

## ID-26: Returning Objects from Constructors

**Strength**: SHOULD-AVOID

**Summary**: Returning a non-primitive from a constructor replaces the new instance. This breaks `instanceof` and surprises callers.

```js
// Anti-pattern — constructor returns a different object
class Config {
  constructor(data) {
    return Object.freeze(data);  // replaces the new instance
  }
}
const c = new Config({ port: 8080 });
c instanceof Config;  // false — the returned object is not a Config

// Fix — use a static factory if you need a different return type
class Config {
  static create(data) {
    return Object.freeze(data);
  }
}
```

**Why it's wrong**: When a constructor returns an object (not a primitive), `new` discards the automatically created instance and returns the explicit object instead. This breaks `instanceof`, prototype chain expectations, and the mental model of `new`. Use static factory methods when the creation result is not an instance of the class (JS Definitive Guide, §9.2; Exploring JS Ch. 31).

**Fix**: `02-api-design.md` ID-13, ID-14.

---

## ID-27: Overloaded Functions That Change Behavior Based on Argument Count or Type

**Strength**: SHOULD-AVOID

**Summary**: Functions that do different things depending on how many arguments are passed or what types they receive are hard to reason about.

```js
// Anti-pattern — overloaded behavior
function createPoint(...args) {
  if (args.length === 1 && args[0] instanceof Point) {
    return new Point(args[0].x, args[0].y);  // copy
  } else if (args.length === 2) {
    return new Point(args[0], args[1]);  // from coordinates
  } else if (args.length === 1 && typeof args[0] === "string") {
    const [x, y] = args[0].split(",").map(Number);
    return new Point(x, y);  // from string
  }
}

// Fix — separate, named functions
Point.from = (other) => new Point(other.x, other.y);
Point.fromString = (s) => {
  const [x, y] = s.split(",").map(Number);
  return new Point(x, y);
};
```

**Why it's wrong**: Overloaded functions require callers to understand implicit dispatch rules. They resist static analysis, produce confusing error messages, and make JSDoc annotations nearly impossible. Named static factory methods make intent explicit at every call site (Deep JS Ch. 14; JS Definitive Guide, §9.2).

**Fix**: `02-api-design.md` ID-13.

---

## ID-28: `var` in Any New Code

**Strength**: MUST-AVOID

**Summary**: `var` is function-scoped, hoists to `undefined`, allows redeclaration, and creates global properties. Never use it.

```js
// Anti-pattern
var x = 10;
if (true) {
  var x = 20;  // redeclaration — no error, same variable
}
console.log(x);  // 20 — leaked out of the block

// Fix
const x = 10;
if (true) {
  const x = 20;  // different variable, block-scoped
}
console.log(x);  // 10 — contained
```

**Why it's wrong**: `var` ignores block boundaries, silently allows redeclaration (masking typos), creates properties on `globalThis` at the top level, and hoists to `undefined` instead of throwing on early access. Every behavior of `var` has a better alternative in `const`/`let` (Exploring JS Ch. 11; JS Definitive Guide, §3.10.2; Eloquent JS Ch. 2).

**Fix**: `01-core-idioms.md` ID-01. Biome's `noVar` rule catches this.

---

## ID-29: `for...in` for Array Iteration

**Strength**: MUST-AVOID

**Summary**: `for...in` iterates enumerable property keys (strings), including inherited ones. On arrays, this is always wrong.

```js
// Anti-pattern — for...in on arrays
const arr = ["a", "b", "c"];
arr.custom = "oops";

for (const key in arr) {
  console.log(key);  // "0", "1", "2", "custom" — string keys, plus custom property
}

// Fix — for...of for values
for (const value of arr) {
  console.log(value);  // "a", "b", "c"
}

// Fix — for...of with entries for index + value
for (const [i, value] of arr.entries()) {
  console.log(i, value);
}
```

**Why it's wrong**: `for...in` yields string keys (not numbers), includes non-index properties, includes inherited enumerable properties (if any library has polluted `Array.prototype`), and does not guarantee numeric order. Both Rauschmayer and Flanagan call this a "common source of bugs" (Exploring JS Ch. 34; JS Definitive Guide, §7.6).

**Fix**: `01-core-idioms.md` ID-25, `06-functions-closures.md` ID-24.

---

## ID-30: Using the `arguments` Object

**Strength**: SHOULD-AVOID

**Summary**: `arguments` is array-like but not an Array, is unavailable in arrow functions, and hides the function's arity.

```js
// Anti-pattern
function sum() {
  let total = 0;
  for (let i = 0; i < arguments.length; i++) {
    total += arguments[i];
  }
  return total;
}

// Fix — rest parameters
function sum(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}
```

**Why it's wrong**: `arguments` is not a real Array (no `.map()`, `.filter()`, `.reduce()`), does not work in arrow functions, makes the function's arity invisible in the signature, and in non-strict mode has a live link to named parameters that creates obscure bugs. Flanagan: "inefficient and hard to optimize" (JS Definitive Guide, §8.3.3; Exploring JS Ch. 15).

**Fix**: `01-core-idioms.md` ID-17.

---

## ID-31: `eval()` and `new Function()`

**Strength**: MUST-AVOID

**Summary**: `eval()` executes arbitrary code in the current scope. It is a security vulnerability and prevents engine optimization.

```js
// Anti-pattern — security hole and optimization blocker
const result = eval(userInput);

// Anti-pattern — slightly safer but still dangerous
const fn = new Function("x", "return x * 2");

// Fix — use specific language features instead
// Dynamic property access:
obj[propertyName];
// Computed property names:
{ [key]: value };
// JSON parsing:
JSON.parse(jsonString);
```

**Why it's wrong**: Direct `eval()` can read and write variables in the caller's scope, defeating all static analysis and preventing JIT optimization. It is a code injection vulnerability when processing external input. May be blocked by Content Security Policy. In strict mode, `eval()` gets its own scope but remains a security and performance hazard. `new Function()` is less dangerous (global scope only) but still prevents static analysis (Exploring JS Ch. 26; JS Definitive Guide, §4.12).

**Fix**: Use specific alternatives: `obj[key]` for dynamic access, `JSON.parse()` for data, template literals for string building.

---

## ID-32: IIFEs in ESM Code

**Strength**: CONSIDER-AVOIDING

**Summary**: IIFEs were needed pre-ES6 for scope isolation. In ESM, they add complexity with zero benefit.

```js
// Anti-pattern — pointless IIFE in a module
const api = (function () {
  const secret = "hidden";
  return { getSecret: () => secret };
})();

// Fix — module scope is already isolated
const secret = "hidden";  // private to this module
export function getSecret() { return secret; }
```

**Why it's wrong**: ESM modules are their own scope — top-level declarations are private by default. `const`/`let` are block-scoped. Neither justification for IIFEs (scope isolation, private state) applies in modern code. An IIFE adds indentation, a wrapping function, and cognitive overhead for no benefit (Exploring JS Ch. 29; JS Definitive Guide, §10.1).

**Fix**: `06-functions-closures.md` ID-15.

---

## ID-33: CommonJS `require()` in ESM Context

**Strength**: MUST-AVOID

**Summary**: CommonJS is synchronous, dynamic, and prevents tree shaking. Use ESM exclusively in Deno.

```js
// Anti-pattern
const { readFile } = require("fs");
module.exports = { process };

// Fix — Deno-native ESM
const data = await Deno.readTextFile("./input.txt");
export function process(data) { /* ... */ }
```

**Why it's wrong**: `require()` loads synchronously (blocking), is evaluated at runtime (not statically analyzable), prevents tree shaking, and does not enforce strict mode. Haverbeke: "there is no real reason to write new programs in [CommonJS] style anymore." Deno uses ESM natively (Exploring JS Ch. 29; JS Definitive Guide, §10.2-10.3; Eloquent JS Ch. 10).

**Fix**: `01-core-idioms.md` ID-08.

---

## ID-34: `delete` on Array Elements

**Strength**: SHOULD-AVOID

**Summary**: `delete arr[i]` creates a hole. The array length does not change, and iteration behavior becomes inconsistent.

```js
// Anti-pattern — creates a hole
const arr = [1, 2, 3];
delete arr[1];
arr;          // [1, empty, 3]
arr.length;   // 3 — unchanged!
1 in arr;     // false — the element is gone
arr.map(String);  // ["1", empty, "3"] — hole preserved

// Fix — splice to remove and close the gap
const arr = [1, 2, 3];
arr.splice(1, 1);
arr;          // [1, 3]
arr.length;   // 2

// Fix — toSpliced for non-destructive removal (ES2023)
const result = arr.toSpliced(1, 1);
```

**Why it's wrong**: `delete arr[i]` removes the property but does not shift subsequent elements or update `.length`. The result is a sparse array with holes, which are handled inconsistently by array methods: `.forEach()` skips holes, `.map()` preserves them, `for-of` yields `undefined` for them. This is never what the programmer intends (Exploring JS Ch. 34; JS Definitive Guide, §7.5).

**Fix**: `08-performance.md` ID-09.

---

## ID-35: `JSON.parse(JSON.stringify(obj))` for Deep Copy

**Strength**: SHOULD-AVOID

**Summary**: The JSON round-trip silently drops `undefined`, functions, and symbols, corrupts `Date` objects, and throws on circular references.

```js
// Anti-pattern — silent data loss
const original = {
  date: new Date(),
  fn: () => {},
  undef: undefined,
  sym: Symbol("x"),
};
const copy = JSON.parse(JSON.stringify(original));
// copy.date  → string, not Date
// copy.fn    → missing
// copy.undef → missing
// copy.sym   → missing

// Throws on circular references:
const circular = { self: null };
circular.self = circular;
JSON.parse(JSON.stringify(circular));  // TypeError

// Fix
const copy = structuredClone(original);
// Handles: circular refs, Date, Map, Set, ArrayBuffer
// Cannot clone: functions, Symbols
```

**Why it's wrong**: `JSON.stringify()` silently omits `undefined` values, functions, and symbol keys. `Date` objects become strings (data loss). `BigInt` throws `TypeError`. Circular references throw `TypeError`. `structuredClone()` handles all of these except functions and symbols (Deep JS Ch. 7; JS Definitive Guide, §6.8).

**Fix**: `04-values-references.md` ID-09, ID-10.

---

## ID-36: Catching Errors and Only Logging — Swallowed Errors

**Strength**: SHOULD-AVOID

**Summary**: Catching an error and only logging it converts a failure into silent success. Handle, rethrow, or both.

```js
// Anti-pattern — error is swallowed
try {
  await processData(input);
} catch (err) {
  console.log(err);  // logged but execution continues as if nothing happened
}
continueWithAssumptionThatDataIsProcessed();

// Fix — rethrow after logging
try {
  await processData(input);
} catch (err) {
  console.error("processData failed:", err);
  throw err;  // propagate to caller
}

// Fix — handle the specific error, rethrow unknown
try {
  await processData(input);
} catch (err) {
  if (err instanceof ValidationError) {
    return showError(err.message);
  }
  throw err;  // unknown error — propagate
}
```

**Why it's wrong**: A caught-and-logged error stops propagating. The code after the catch block runs as if the operation succeeded, potentially corrupting state or producing wrong results. Haverbeke: "blanket-catching hides bugs and makes debugging nearly impossible." At minimum: log AND rethrow, or handle the specific error and rethrow everything else (Eloquent JS Ch. 8; Exploring JS Ch. 26).

**Fix**: `03-error-handling.md` ID-08, ID-09, ID-10.

---

## Best Practices Summary

### Quick Reference Table

| ID | Anti-Pattern | Strength | Root Cause |
|----|-------------|----------|------------|
| 01 | `==` instead of `===` | MUST-AVOID | Multi-step coercion cascade |
| 02 | Trusting `typeof` universally | SHOULD-AVOID | `null`, arrays, NaN all mislead |
| 03 | `\|\|` for defaults | MUST-AVOID | Swallows `0`, `""`, `false` |
| 04 | Global `isNaN()` | SHOULD-AVOID | Coerces argument first |
| 05 | `parseInt` without radix | SHOULD-AVOID | Infers base from prefix |
| 06 | `new String/Number/Boolean` | SHOULD-AVOID | Creates truthy wrapper objects |
| 07 | Method extraction loses `this` | MUST-AVOID | Dynamic `this` set by call site |
| 08 | Regular function as callback | SHOULD-AVOID | Loses `this` in strict mode |
| 09 | Arrow function as method | SHOULD-AVOID | Inherits wrong `this` |
| 10 | `var` in loops with closures | MUST-AVOID | One binding shared across iterations |
| 11 | Accidental globals | MUST-AVOID | Missing declaration in non-strict mode |
| 12 | Accidental shadowing | SHOULD-AVOID | Inner binding hides outer silently |
| 13 | Relying on `var` hoisting | SHOULD-AVOID | Silent `undefined` instead of error |
| 14 | Mutating function arguments | MUST-AVOID | Caller's data destroyed |
| 15 | `const` = immutable | SHOULD-AVOID | Binding frozen, value mutable |
| 16 | Shallow copy surprise | SHOULD-AVOID | Nested refs shared |
| 17 | `.sort()` mutates + string default | SHOULD-AVOID | Returns same ref; default is lexicographic |
| 18 | Sequential `await` (independent) | MUST-AVOID | Serializes parallel work |
| 19 | `.map(async fn)` without `all()` | MUST-AVOID | Returns `Promise[]` not values |
| 20 | Fire-and-forget promises | MUST-AVOID | Unhandled rejections crash Deno |
| 21 | Sync throws in Promise functions | SHOULD-AVOID | Sync throws escape `.catch()` chain |
| 22 | `.then()` nesting | SHOULD-AVOID | Recreates callback hell |
| 23 | `fetch()` without `signal` | SHOULD-AVOID | Uncancellable requests |
| 24 | Mixed return/throw error channels | MUST-AVOID | Callers need two patterns |
| 25 | Boolean parameters | SHOULD-AVOID | Unreadable call sites |
| 26 | Return object from constructor | SHOULD-AVOID | Breaks `instanceof` |
| 27 | Overloaded functions | SHOULD-AVOID | Implicit dispatch, hard to analyze |
| 28 | `var` in new code | MUST-AVOID | Function-scoped, hoists, redeclares |
| 29 | `for...in` on arrays | MUST-AVOID | String keys, inherited props, wrong order |
| 30 | `arguments` object | SHOULD-AVOID | Not an array, invisible arity |
| 31 | `eval()` | MUST-AVOID | Security hole, blocks optimization |
| 32 | IIFEs in ESM | CONSIDER-AVOIDING | Module scope already isolated |
| 33 | CommonJS `require()` | MUST-AVOID | Sync, dynamic, prevents tree shaking |
| 34 | `delete` on arrays | SHOULD-AVOID | Creates holes, length unchanged |
| 35 | JSON deep copy | SHOULD-AVOID | Drops undefined, functions, symbols; corrupts Date |
| 36 | Catch-and-log only | SHOULD-AVOID | Converts failure to silent success |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for the positive patterns behind ID-01, 03, 11, 28, 29, 33
- **API Design**: See `02-api-design.md` for ID-24, 25, 26, 27
- **Error Handling**: See `03-error-handling.md` for ID-18, 19, 20, 21, 22, 24, 36
- **Values & References**: See `04-values-references.md` for ID-14, 15, 16, 35
- **Type Discipline**: See `05-type-discipline.md` for ID-01, 02, 04, 05, 06
- **Functions & Closures**: See `06-functions-closures.md` for ID-07, 08, 09, 10, 12, 13
- **Async & Concurrency**: See `07-async-concurrency.md` for ID-18, 19, 22, 23
- **Performance**: See `08-performance.md` for ID-17, 34

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [Biome — Lint Rules](https://biomejs.dev/linter/rules/)
- [MDN — Equality Comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)
- [MDN — typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
