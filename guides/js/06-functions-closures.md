# Functions & Closures

The heart of JavaScript composition. Covers function forms, closure mechanics, scope, `this` binding, higher-order functions, partial application, generators, and pure function discipline. Where Rust uses traits, JS uses functions — this guide ensures they are used correctly. Grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: `function` Declarations for Named Module-Level Functions

**Strength**: SHOULD

**Summary**: Use `function` declarations for named, standalone, module-level functions. They are hoisted, named in stack traces, and communicate "this is a key API entry point."

```js
// Good — hoisted, named, clear intent
export function parseConfig(raw) {
  const lines = raw.split("\n");
  return Object.fromEntries(lines.map(parseLine));
}

// Can be called before the declaration (hoisting)
const config = parseConfig(text);

function parseLine(line) {
  const [key, ...rest] = line.split("=");
  return [key.trim(), rest.join("=").trim()];
}
```

**Rationale**: Function declarations are fully hoisted — the entire definition is available from the moment the scope is entered. This enables top-down code organization where the public API appears first and helpers below. The name is required and appears directly in stack traces (Exploring JS Ch. 27; JS Definitive Guide, §8.1.1).

---

## ID-02: Arrow Functions for Callbacks and Inline Closures

**Strength**: SHOULD

**Summary**: Use arrow functions for callbacks, array method arguments, and any inline function that needs the enclosing `this`.

```js
// Good — concise, inherits this
const doubled = items.map((x) => x * 2);
const adults = users.filter((u) => u.age >= 18);

// Good — arrow captures method's this
class Formatter {
  prefix = ">> ";
  formatAll(items) {
    return items.map((item) => `${this.prefix}${item}`);
  }
}

// Bad — ordinary function loses this
class Formatter {
  prefix = ">> ";
  formatAll(items) {
    return items.map(function (item) {
      return `${this.prefix}${item}`; // TypeError: this is undefined
    });
  }
}
```

**Arrow constraints**: No own `this`, `arguments`, `super`, or `prototype`. Cannot be used with `new`. Object literal return requires parentheses: `() => ({ key: value })`.

**Rationale**: Arrow functions eliminate the `const self = this` pattern and are syntactically concise for callbacks. They are specialized for the "real function" role — standalone computation and closures, not methods or constructors (Exploring JS Ch. 27; JS Definitive Guide, §8.1.3).

**See also**: `01-core-idioms.md` ID-09

---

## ID-03: Never Use `function` as a Callback — Arrow Inherits `this`

**Strength**: MUST

**Summary**: Ordinary functions as callbacks lose `this` in strict mode. Always use arrow functions for callbacks inside methods.

```js
// Bad — this is undefined inside the callback
const obj = {
  prefix: "=>",
  format(items) {
    return items.map(function (x) {
      return `${this.prefix} ${x}`; // TypeError
    });
  },
};

// Good — arrow inherits this from the method
const obj = {
  prefix: "=>",
  format(items) {
    return items.map((x) => `${this.prefix} ${x}`);
  },
};
```

**Rationale**: In strict mode (which ESM enables automatically), a plain `function` callback receives `this === undefined`. This is the single most common `this`-related bug. Arrow functions inherit `this` from the enclosing scope, which is the method's `this` — exactly what you want (Exploring JS Ch. 27, 30; JS Definitive Guide, §8.2.1).

---

## ID-04: Method Shorthand in Objects and Classes

**Strength**: SHOULD

**Summary**: Use method shorthand (`{ method() {} }`) in object literals and classes. Never use `prop: function()` syntax.

```js
// Good — method shorthand
const calculator = {
  total: 0,
  add(n) { this.total += n; },
  reset() { this.total = 0; },
};

class Stack {
  #items = [];
  push(item) { this.#items.push(item); }
  pop() { return this.#items.pop(); }
  get size() { return this.#items.length; }
}

// Bad — verbose, no benefit
const calculator = {
  total: 0,
  add: function (n) { this.total += n; },
};
```

**Rationale**: Method shorthand is concise, communicates intent (this property is a method, not data), and cannot be constructor-called. It is the standard syntax in ES6+ (Exploring JS Ch. 27; JS Definitive Guide, §6.10.5).

---

## ID-05: Generator Functions for Lazy Sequences and Iterator Implementation

**Strength**: SHOULD

**Summary**: Use `function*` for lazy evaluation, infinite sequences, and implementing `Symbol.iterator`.

```js
// Good — lazy infinite sequence
function* naturals(start = 0) {
  for (let n = start; ; n++) yield n;
}

// Good — generator as Symbol.iterator implementation
class NumberRange {
  constructor(from, to) { this.from = from; this.to = to; }
  *[Symbol.iterator]() {
    for (let i = this.from; i <= this.to; i++) yield i;
  }
}
[...new NumberRange(1, 5)]; // [1, 2, 3, 4, 5]

// Good — yield* for recursive traversal
class Tree {
  constructor(value, children = []) { this.value = value; this.children = children; }
  *[Symbol.iterator]() {
    yield this.value;
    for (const child of this.children) yield* child;
  }
}

// Good — lazy transformation (no intermediate array)
function* map(iterable, fn) {
  for (const x of iterable) yield fn(x);
}
```

**Key rules**: `function*` syntax only (no arrow generators). `yield` cannot appear inside nested callbacks — use `for-of` inside the generator. Each `*[Symbol.iterator]()` call creates a fresh iterator (many-times iterable).

**Rationale**: Generators eliminate manual iterator state management. `yield*` enables delegation to sub-iterables for recursive structures. Lazy evaluation avoids allocating intermediate arrays for large datasets (Exploring JS Ch. 38; JS Definitive Guide, §12.3).

**See also**: `02-api-design.md` ID-20, ID-21

---

## ID-06: Closures Capture Variables, Not Values

**Strength**: MUST

**Summary**: A closure holds a live reference to the variable's binding in its environment. It sees the current value, not a snapshot at creation time.

```js
function makeCounter() {
  let count = 0;
  return {
    increment: () => ++count, // reads and writes the live binding
    get: () => count,
  };
}

const c = makeCounter();
c.increment(); // 1
c.increment(); // 2
c.get();       // 2 — reads the same binding, not a frozen snapshot
```

**The spec mechanism** (Deep JS Ch. 4): Each scope has a heap-allocated **environment** mapping variable names to current values. Every function object carries an internal `[[Scope]]` property set at creation time to the current environment. When called, a new environment is created with its `outer` reference pointing to `[[Scope]]`, forming the **scope chain**. Because environments live on the heap, they survive the function call that created them — this is what makes closures work.

**Consequence**: If a variable changes after a closure is created, the closure sees the new value. This is the root of both the power of closures (shared mutable private state) and their primary gotcha (stale closures, loop variables).

**Rationale**: "A closure is a function plus a connection to the variables that exist at its 'birth place'" (Exploring JS Ch. 13). Understanding that closures hold bindings, not values, prevents an entire category of bugs (Deep JS Ch. 4; JS Definitive Guide, §8.6).

---

## ID-07: The `let`-in-Loop Fix — `let` Creates a Fresh Binding Per Iteration

**Strength**: MUST

**Summary**: `var` shares one binding across all loop iterations. `let` creates a new binding per iteration. This matters when closures are created inside loops.

```js
// Bad — var: all callbacks share the same i, which ends at 3
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// logs: 3, 3, 3

// Good — let: each iteration gets its own i
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// logs: 0, 1, 2
```

**Mechanism**: Each iteration of a `for` loop with `let` creates a new block-scoped environment. Closures created during that iteration close over that iteration's environment, which has its own `i` binding (Exploring JS Ch. 13; Deep JS Ch. 4; JS Definitive Guide, §3.10.1).

**Rationale**: This is the classic closure-in-loop bug. The `var` version is still one of the most common errors in AI-generated code that uses loops with callbacks. Always use `let` (or `const` in `for-of`) in loops where closures will be created.

---

## ID-08: Closures for Encapsulation — Private State Without Classes

**Strength**: SHOULD

**Summary**: Variables inside a function are invisible from outside. Returning closures gives controlled, exclusive access — private state without `#`.

```js
// Good — private state via closure
function createCounter(initial = 0) {
  let count = initial;
  return {
    increment() { return ++count; },
    decrement() { return --count; },
    reset() { count = initial; },
    get value() { return count; },
  };
}

const c = createCounter(10);
c.increment(); // 11
c.increment(); // 12
c.reset();
c.value;       // 10
// count is not accessible from outside — truly private
```

**Key insight**: Multiple closures returned from the **same invocation** share the same private state. Different invocations produce independent states. This predates class `#privateField` syntax; both achieve data hiding via different mechanisms (JS Definitive Guide, §8.6; Exploring JS Ch. 13).

---

## ID-09: Factory Functions That Return Closures

**Strength**: SHOULD

**Summary**: Use factory functions to create specialized closures with captured configuration.

```js
// Good — factory captures configuration
function createLogger(prefix) {
  return (message) => {
    console.log(`[${prefix}] ${message}`);
  };
}
const dbLog = createLogger("DB");
const apiLog = createLogger("API");
dbLog("Connected");  // [DB] Connected
apiLog("Request");   // [API] Request

// Good — factory for partial application
function createMultiplier(factor) {
  return (x) => x * factor;
}
const double = createMultiplier(2);
const triple = createMultiplier(3);
[1, 2, 3].map(double); // [2, 4, 6]
```

**Rationale**: Each factory call creates an independent closure with its own captured state. This is the fundamental pattern for function specialization, configuration injection, and partial application in JavaScript (Exploring JS Ch. 13; Deep JS Ch. 4).

---

## ID-10: Beware Closing Over Mutable State — Stale Closures

**Strength**: SHOULD

**Summary**: Because closures hold live bindings, they always reflect the current value — which may have changed since the closure was created.

```js
// Bad — closure reads the latest value, not the value at registration time
let handler = null;
let count = 0;

handler = () => console.log(`Count: ${count}`);
count = 42;
handler(); // "Count: 42" — not "Count: 0"

// Bad — event handler captures a variable that keeps changing
let url = "/api/v1";
button.addEventListener("click", () => fetch(url)); // fetches whatever url is NOW
url = "/api/v2"; // click now fetches v2, not v1

// Good — capture the value at a specific point by copying to a new binding
const capturedUrl = url;
button.addEventListener("click", () => fetch(capturedUrl));
```

**Rationale**: The `var`-in-loop bug (ID-07) is the classic stale closure. But the pattern generalizes: any closure that reads a variable modified after creation sees the latest value, not the value at closure creation time. When you need to capture a specific point-in-time value, copy it to a new `const` binding (Deep JS Ch. 4; Exploring JS Ch. 13).

---

## ID-11: Block Scope with `const`/`let` — Not Function Scope Like `var`

**Strength**: MUST

**Summary**: `const` and `let` are block-scoped. `var` is function-scoped and leaks out of blocks.

```js
// Good — block-scoped, contained
function process() {
  if (true) {
    const x = 10;
    let y = 20;
  }
  // x and y are not accessible here
}

// Bad — var leaks out of the block
function process() {
  if (true) {
    var x = 10;
  }
  console.log(x); // 10 — leaked!
}
```

| Keyword | Scope | Hoisted | TDZ | Redeclarable |
|---------|-------|---------|-----|-------------|
| `const` | Block | No (TDZ) | Yes | No |
| `let` | Block | No (TDZ) | Yes | No |
| `var` | Function | Yes (`undefined`) | No | Yes |
| `function` | Block (strict) | Yes (fully) | No | Yes |

**Rationale**: Block scoping prevents variable leakage and is the foundation of the `let`-in-loop fix. `var` ignoring block boundaries is a legacy design that causes silent bugs (Exploring JS Ch. 13; JS Definitive Guide, §3.10).

**See also**: `01-core-idioms.md` ID-01

---

## ID-12: Temporal Dead Zone — `let`/`const` Exist but Are Uninitialized

**Strength**: MUST

**Summary**: The TDZ is the region between scope entry and the declaration line. Accessing the variable during TDZ throws `ReferenceError`.

```js
{
  // TDZ for x starts here
  // console.log(x); // ReferenceError
  const x = 42;      // TDZ ends
  console.log(x);    // 42
}

// TDZ is temporal, not spatial:
{
  const fn = () => console.log(y); // defined during TDZ — OK
  let y = 10;                       // TDZ ends
  fn();                             // 10 — called after TDZ, works
}
```

**Rationale**: The TDZ ensures `const` is never observable as `undefined` before its initializer runs. `var` has no TDZ — it hoists to `undefined`, which is a frequent source of subtle bugs (Exploring JS Ch. 13; Deep JS Ch. 4).

---

## ID-13: Function Declarations Hoist Completely; Expressions Do Not

**Strength**: SHOULD

**Summary**: Function declarations are fully available from the start of their scope. Arrow/const expressions have TDZ.

```js
// Good — function declaration, callable before the line
greet("Alice");
function greet(name) { console.log(`Hello, ${name}`); }

// Bad — const arrow, TDZ applies
// greet("Alice"); // ReferenceError
const greet = (name) => console.log(`Hello, ${name}`);

// Bad — var expression, hoisted as undefined
// greet("Alice"); // TypeError: greet is not a function
var greet = function (name) { console.log(`Hello, ${name}`); };
```

**Rationale**: Full hoisting of function declarations enables top-down code organization. `var` expressions are partially hoisted (name → `undefined`, assignment stays in place), producing `TypeError` not `ReferenceError` — a confusing distinction. `const`/`let` expressions have TDZ (Exploring JS Ch. 13; JS Definitive Guide, §8.1).

---

## ID-14: Shadowing — Inner Bindings Mask Outer Ones

**Strength**: SHOULD

**Summary**: An inner scope can declare a variable with the same name as an outer scope. The inner declaration hides the outer one within its scope.

```js
const x = "outer";
{
  const x = "inner"; // shadows outer x
  console.log(x);    // "inner"
}
console.log(x);      // "outer" — unaffected

// Common legitimate use: nested loop counters
for (let i = 0; i < rows; i++) {
  for (let i = 0; i < cols; i++) { // shadows outer i — intentional
    grid[i] = /* ... */;
  }
}
```

**Caution**: Accidental shadowing can cause bugs when a developer believes they are modifying an outer variable but are creating an independent inner one. Biome/ESLint's `noShadow` rule can warn about this.

**Rationale**: Shadowing is a consequence of block scoping. Redeclaring `let`/`const` in the same scope is a `SyntaxError`, but shadowing across nested scopes is allowed and sometimes intentional (Exploring JS Ch. 13; JS Definitive Guide, §3.10.1).

---

## ID-15: Module Scope — Each ESM File Has Its Own Scope

**Strength**: SHOULD

**Summary**: Module-level declarations are private by default. Nothing is global unless explicitly exported.

```js
// module-a.js
const SECRET = "hidden";        // private to this module
export function getSecret() {   // public
  return SECRET;
}

// module-b.js
import { getSecret } from "./module-a.js";
getSecret();  // "hidden"
// SECRET;    // ReferenceError — not exported
```

**Key facts**:
- Each module has its own scope, nested inside the global scope
- Even `var` inside a module is scoped to the module, NOT `globalThis`
- `this` at module top level is `undefined` (not `globalThis`)
- Module code runs once, on first import (singleton)
- Automatic strict mode

**Rationale**: Module scope replaces the IIFE module pattern (`(function() { ... })()`) that was required pre-ES6. All modern code should be in modules, making global-scope pollution irrelevant (Deep JS Ch. 5; Exploring JS Ch. 29).

**See also**: `01-core-idioms.md` ID-08

---

## ID-16: The Four `this` Rules — Call Site Determines Binding

**Strength**: MUST

**Summary**: `this` is determined at call time by how the function is invoked, not where it is defined.

| Rule | Invocation Pattern | `this` Value | Example |
|------|--------------------|-------------|---------|
| **Default** | Plain function call (strict/ESM) | `undefined` | `fn()` |
| **Implicit** | Method call — object before the dot | The receiver object | `obj.method()` |
| **Explicit** | `.call()` / `.apply()` / `.bind()` | First argument | `fn.call(obj, a)` |
| **`new`** | Constructor invocation | Newly created instance | `new Ctor()` |
| **Arrow** | (not a rule — inherits) | Enclosing scope's `this` | `() => this.x` |

```js
function show() { console.log(this); }

show();              // undefined (default, strict mode)
const obj = { show };
obj.show();          // obj (implicit)
show.call({ x: 1 }); // { x: 1 } (explicit)
new show();          // new instance (new)
```

**Rationale**: `this` is a keyword, not a variable. Its value is determined entirely by the call site. Understanding these four rules (plus arrow's inheritance) eliminates the guesswork. In ESM (strict mode), the default binding is `undefined`, not `globalThis` (Exploring JS Ch. 30; JS Definitive Guide, §8.2).

---

## ID-17: Arrow Functions Inherit `this` — No Own Binding

**Strength**: MUST

**Summary**: Arrow functions have no own `this`. They inherit it lexically from the enclosing scope, and it cannot be overridden.

```js
class Timer {
  #ticks = 0;

  start(interval) {
    // Arrow inherits this from start(), which is the Timer instance
    setInterval(() => {
      this.#ticks++;
    }, interval);
  }
}

// .call(), .apply(), .bind() cannot override arrow's this:
const arrow = () => this;
arrow.call({ x: 1 }); // still undefined (in ESM module scope), not { x: 1 }
```

**Rationale**: Arrow functions were designed specifically to solve the callback-loses-`this` problem. Their `this` is set permanently at definition time from the enclosing scope and cannot be changed by any invocation pattern (Exploring JS Ch. 27; JS Definitive Guide, §8.1.3).

---

## ID-18: Method Extraction Loses `this` — Use `.bind()` or Arrow Wrappers

**Strength**: MUST

**Summary**: Storing a method in a variable or passing it as a callback disconnects it from its receiver.

```js
class Handler {
  name = "Handler";
  handle(event) {
    console.log(`${this.name}: ${event}`);
  }
}

const h = new Handler();

// Bad — this is lost when method is extracted
const fn = h.handle;
fn("click"); // TypeError: Cannot read properties of undefined

// Bad — this is lost when passed as callback
button.addEventListener("click", h.handle); // this is the button element, not h

// Good — bind fixes this
button.addEventListener("click", h.handle.bind(h));

// Good — arrow wrapper
button.addEventListener("click", (e) => h.handle(e));

// Good — arrow class field (permanently bound)
class Handler {
  name = "Handler";
  handle = (event) => {
    console.log(`${this.name}: ${event}`);
  };
}
```

**Rationale**: Method extraction is one of the most common JavaScript bugs. When `obj.method` is stored in a variable, the object reference is lost — the function is called with the default binding (`undefined` in strict mode). The fix is `.bind()`, an arrow wrapper, or an arrow class field (Exploring JS Ch. 30; JS Definitive Guide, §8.7.5).

---

## ID-19: Don't Use `call`/`apply`/`bind` When an Arrow Function Suffices

**Strength**: SHOULD

**Summary**: Arrow functions handle `this` inheritance automatically. Reserve `.call()`/`.apply()`/`.bind()` for cases where you need to explicitly set `this` to a specific object.

```js
// Bad — unnecessary bind, arrow would work
const handler = function () { this.process(); }.bind(this);

// Good — arrow inherits this naturally
const handler = () => this.process();

// Good — call/apply when you genuinely need a different this
function greet() { return `Hello, ${this.name}`; }
greet.call({ name: "Alice" }); // "Hello, Alice"

// Good — apply for spreading an array as arguments (legacy pattern)
Math.max.apply(null, numbers);
// Better — spread syntax
Math.max(...numbers);
```

**Rationale**: `.call()`, `.apply()`, and `.bind()` predate arrow functions. For callbacks inside methods, arrow functions are cleaner and less error-prone. Reserve the explicit binding methods for cases where you need to invoke a function with a specific receiver that isn't available lexically (JS Definitive Guide, §8.7.4-8.7.5).

---

## ID-20: Prefer `.map()`, `.filter()`, `.reduce()` for Transformations

**Strength**: SHOULD

**Summary**: Use functional array methods when building a new value from an existing array.

```js
// Good — .map() for one-to-one transformation
const names = users.map((u) => u.name);

// Good — .filter() for subset selection
const active = users.filter((u) => u.active);

// Good — .reduce() for aggregation
const total = prices.reduce((sum, p) => sum + p, 0);

// Good — chaining
const activeMails = users
  .filter((u) => u.active)
  .map((u) => u.email);
```

**What each returns**:
- `.map()` — new array of **same length**, each element transformed
- `.filter()` — new array of **equal or shorter length**, elements passing the predicate
- `.reduce()` — **single summary value** of any type

**Always provide `init` for `.reduce()`** — without it, an empty array throws `TypeError`.

**Rationale**: These methods express intent (transform, select, aggregate) more clearly than imperative loops. They return new arrays without mutating the original. Use them when building values; use `for-of` when performing side effects (Exploring JS Ch. 34; JS Definitive Guide, §7.8.1; Eloquent JS Ch. 5).

---

## ID-21: Use `.find()` / `.findIndex()` for Single-Element Search

**Strength**: SHOULD

**Summary**: Use predicate-based search methods instead of filtering and taking the first element.

```js
// Good — .find() returns the first matching element or undefined
const admin = users.find((u) => u.role === "admin");

// Good — .findIndex() returns the index or -1
const idx = items.findIndex((item) => item.id === targetId);

// Good — .findLast() / .findLastIndex() for reverse search (ES2023)
const lastError = logs.findLast((entry) => entry.level === "error");

// Bad — filter then take first (allocates full intermediate array)
const admin = users.filter((u) => u.role === "admin")[0];
```

**Rationale**: `.find()` and `.findIndex()` short-circuit on the first match, avoiding unnecessary iteration. `.filter()[0]` allocates a full array and iterates every element even when you only need one (Exploring JS Ch. 34; JS Definitive Guide, §7.8.6).

---

## ID-22: Use `.some()` / `.every()` for Boolean Aggregate Checks

**Strength**: SHOULD

**Summary**: Use `.some()` for "does any match?" and `.every()` for "do all match?"

```js
// Good — .some() for existence check
const hasErrors = results.some((r) => r.status === "error");

// Good — .every() for validation
const allValid = inputs.every((input) => input.length > 0);

// Edge cases:
[].some(() => true);  // false (no elements to test)
[].every(() => false); // true (vacuous truth)
```

**Both short-circuit**: `.some()` stops on the first `true`; `.every()` stops on the first `false`.

**Rationale**: `.some()` and `.every()` express boolean aggregate intent clearly and efficiently. They short-circuit, unlike `.filter().length > 0` which iterates the entire array (Exploring JS Ch. 34; JS Definitive Guide, §7.8.1).

---

## ID-23: Use `.flatMap()` for Map-Then-Flatten Patterns

**Strength**: SHOULD

**Summary**: `.flatMap()` maps each element to zero or more elements and flattens one level — combining filter, map, and expand in one pass.

```js
// Good — filter + transform in one step
const fulfilledValues = results.flatMap((r) =>
  r.status === "fulfilled" ? [r.value] : [],
);

// Good — split and flatten
const words = lines.flatMap((line) => line.split(/\s+/));

// Good — one-to-many expansion
const allTags = posts.flatMap((post) => post.tags);

// Equivalent but less efficient:
const words = lines.map((line) => line.split(/\s+/)).flat();
```

**Callback return conventions**:
- `[]` → filter out (skip element)
- `[value]` → keep (equivalent to `.map()`)
- `[v1, v2, ...]` → expand (one input → multiple outputs)

**Rationale**: `.flatMap()` (ES2019) is more efficient than `.map().flat()` (single pass) and more expressive than separate `.filter()` + `.map()` chains (Exploring JS Ch. 34; JS Definitive Guide, §7.8.2).

---

## ID-24: When to Use `for-of` Instead of Array Methods

**Strength**: SHOULD

**Summary**: Use `for-of` when you need `break`, `continue`, `await`, or when the primary purpose is side effects.

```js
// Good — for-of with break (impossible with .forEach/.map)
for (const item of items) {
  if (item.done) break;
  process(item);
}

// Good — for-of with await (sequential async)
for (const url of urls) {
  const data = await fetch(url).then((r) => r.json());
  await save(data);
}

// Good — for-of for side effects
for (const user of users) {
  console.log(user.name);
}

// Bad — .map() for side effects (return value discarded)
users.map((u) => console.log(u.name));

// Bad — .forEach() with async (callbacks fire concurrently, not awaited)
urls.forEach(async (url) => {
  await fetch(url); // NOT sequential — all fire at once
});
```

| Use case | Preferred |
|----------|-----------|
| Transform → new array | `.map()` |
| Select subset | `.filter()` |
| Aggregate → single value | `.reduce()` |
| Side effects | `for-of` |
| `break` / `continue` | `for-of` |
| `await` (sequential) | `for-of` |
| Any iterable (Set, Map, generator) | `for-of` |

**Rationale**: `for-of` is a statement that supports `break`, `continue`, `return`, and `await`. `.forEach()` cannot be terminated early, does not support `await`, and silently swallows return values. Use array methods for building values; use `for-of` for imperative control flow (Exploring JS Ch. 34; JS Definitive Guide, §7.8.1).

**See also**: `01-core-idioms.md` ID-25

---

## ID-25: `.bind()` for Partial Application

**Strength**: CONSIDER

**Summary**: `.bind()` can pre-fill arguments from the left, but has trade-offs in readability and debuggability.

```js
// Partial application with .bind()
function add(x, y) { return x + y; }
const add5 = add.bind(null, 5);
add5(3); // 8

// This-fixing + partial application
class Logger {
  log(level, message) { /* ... */ }
}
const logger = new Logger();
const warn = logger.log.bind(logger, "WARN");
warn("Disk space low"); // logger.log("WARN", "Disk space low")
```

**Trade-offs**:
- Arguments fixed left-to-right only — cannot skip positions
- `.name` becomes `"bound add"` — helpful for `this`-fixing, less so for pure partial application
- `null` as first argument is noisy when `this` is irrelevant
- Each call creates a new function object

**Rationale**: `.bind()` works for simple cases but becomes clunky for complex partial application. Prefer manual closures (ID-26) for library-quality code. Reserve `.bind()` for quick `this`-fixing in event handlers (JS Definitive Guide, §8.7.5; Deep JS Ch. 22).

---

## ID-26: Manual Partial Application with Closures

**Strength**: SHOULD

**Summary**: Closures give you named, flexible, debuggable partial application without `.bind()`'s constraints.

```js
// Good — explicit, named, arguments in any position
const double = (x) => multiply(2, x);
const toUpper = (s) => s.toUpperCase();
const getAge = (user) => user.age;

// Good — generic partial helper
function partial(fn, ...presetArgs) {
  return function partiallyApplied(...laterArgs) {
    return fn(...presetArgs, ...laterArgs);
  };
}
const add5 = partial(add, 5);
add5.name; // "partiallyApplied" — appears in stack traces

// Good — currying for pipeline-friendly functions
function createFilter(predicate) {
  return (items) => items.filter(predicate);
}
const getAdults = createFilter((u) => u.age >= 18);
getAdults(users);
```

**Advantages over `.bind()`**: Named wrapper, arguments in any position, no `null` placeholder, fully transparent to debuggers and readers.

**Rationale**: Manual closures are the most common partial application pattern in production JavaScript. They are explicit, composable, and produce clear stack traces. Currying (nesting single-argument functions) is the structural form that makes `add(2)(3)` work (Deep JS Ch. 22; Exploring JS Ch. 13).

---

## ID-27: Function Composition — `pipe()` and `compose()` Patterns

**Strength**: CONSIDER

**Summary**: Combine small, pure, single-argument functions into pipelines.

```js
// pipe — left-to-right (data flow order)
const pipe = (...fns) => (x) => fns.reduce((v, f) => f(v), x);

const processName = pipe(
  (s) => s.trim(),
  (s) => s.toLowerCase(),
  (s) => s.replace(/\s+/g, "-"),
);
processName("  Hello World  "); // "hello-world"

// compose — right-to-left (mathematical order)
const compose = (...fns) => (x) => fns.reduceRight((v, f) => f(v), x);
```

**Practical rules**:
- `pipe()` reads in execution order — preferred in application code
- Functions must be pure (or at least order-insensitive) for composition to be reliable
- Each function must take one argument and return one value (transform pipeline)
- For multi-argument functions, use partial application (ID-26) to reduce to one argument

**Rationale**: Composability is the primary payoff of writing small, pure functions. `pipe()` is a lightweight utility (4 lines) that replaces deeply nested function calls with a readable left-to-right pipeline (JS Definitive Guide, §8.8; Eloquent JS Ch. 5).

---

## ID-28: Prefer Pure Functions — Same Input, Same Output, No Side Effects

**Strength**: SHOULD

**Summary**: A pure function has no side effects and always returns the same output for the same input.

```js
// Good — pure: testable, composable, predictable
function calculateTax(price, rate) {
  return price * rate;
}

function formatCurrency(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}

// Bad — impure: reads external state, produces side effect
let taxRate = 0.08;
function calculateTax(price) {
  console.log(`Calculating tax for ${price}`); // side effect
  return price * taxRate;                       // reads mutable external state
}
```

**Properties of pure functions**:
1. No side effects (no I/O, no mutation of external state)
2. Does not rely on external mutable state
3. Same arguments always produce the same return value
4. Can be replaced by its return value (referential transparency)

**Rationale**: Pure functions are trivially testable (call and assert), safely composable in pipelines, and can be memoized, parallelized, or reordered without changing behavior. Array methods `.map()`, `.filter()`, `.reduce()` assume pure callbacks (Eloquent JS Ch. 3; JS Definitive Guide, §8.8).

---

## ID-29: Isolate Side Effects at the Edges

**Strength**: SHOULD

**Summary**: Push side effects (I/O, logging, mutation) to the boundary of your program. Keep the core logic pure.

```js
// Good — pure core, side effects at the boundary
function processData(raw) {
  // Pure: parse and transform
  const records = parse(raw);
  const filtered = records.filter(isValid);
  return filtered.map(normalize);
}

// Side effects at the edge
async function main() {
  const raw = await Deno.readTextFile("data.csv"); // I/O (side effect)
  const result = processData(raw);                  // pure transformation
  await Deno.writeTextFile("output.json", JSON.stringify(result)); // I/O
  console.log(`Processed ${result.length} records`); // I/O
}
```

**Rationale**: Haverbeke: "There's no need to feel bad when writing functions that are not pure. Side effects are often useful." The goal is not purity for its own sake but **containment** — knowing exactly where the world changes. The pure core is trivially testable; the side-effect edges are where integration tests focus (Eloquent JS Ch. 3).

---

## ID-30: Functions Have a `.name` Property — Understand How It's Set

**Strength**: CONSIDER

**Summary**: Every function has a `.name` string that appears in stack traces. It is set at creation time and follows specific inference rules.

| Construct | `.name` value |
|-----------|---------------|
| `function foo() {}` | `"foo"` |
| `const foo = function() {}` | `"foo"` (inferred from variable) |
| `const foo = () => {}` | `"foo"` (inferred from variable) |
| `const foo = function bar() {}` | `"bar"` (NFE name wins) |
| `{ method() {} }` | `"method"` (property key) |
| `fn.bind(null, 1)` | `"bound fn"` |
| Factory return: `return () => {}` | `""` (no naming context) |
| `export default function() {}` | `"default"` |

**Key rule**: Name is set once at creation time. A factory-returned anonymous function keeps `""` even when stored in a named `const`.

**Rationale**: Meaningful `.name` values improve debugging. Factory-returned functions should use named function expressions to ensure stack traces are informative (Deep JS Ch. 21).

---

## ID-31: Named Function Expressions for Better Stack Traces

**Strength**: SHOULD

**Summary**: When a function will appear in error-prone paths, give it a name via a named function expression (NFE).

```js
// Bad — factory returns anonymous function, stack trace shows ""
function createHandler(config) {
  return function () {
    throw new Error("handler failed");
  };
}

// Good — NFE gives the function a name for stack traces
function createHandler(config) {
  return function configHandler() {
    throw new Error("handler failed");
    // Stack trace: "Error: handler failed\n    at configHandler ..."
  };
}

// The NFE name is accessible inside the function (for self-reference)
// but NOT accessible outside it
const factorial = function fact(n) {
  return n <= 1 ? 1 : n * fact(n - 1);
};
// fact; // ReferenceError — not in scope
```

**Rationale**: Anonymous functions produce empty or inferred names in stack traces. NFEs provide a reliable, explicit name that survives minification if the minifier preserves it. The name is scoped to the function body — useful for recursion without polluting the outer scope (Deep JS Ch. 21; JS Definitive Guide, §8.1).

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `function` declarations for named functions | SHOULD | Hoisted, named in stack traces |
| 02 | Arrow functions for callbacks | SHOULD | Inherits `this`, concise |
| 03 | Never `function` as callback | MUST | Ordinary function loses `this` in strict mode |
| 04 | Method shorthand | SHOULD | `{ m() {} }` — concise, correct intent |
| 05 | Generator functions | SHOULD | Lazy sequences, `yield*` for delegation |
| 06 | Closures capture variables, not values | MUST | Live binding reference, not snapshot |
| 07 | `let`-in-loop fix | MUST | Fresh environment per iteration |
| 08 | Closures for encapsulation | SHOULD | Private state without `#` |
| 09 | Factory functions returning closures | SHOULD | Configuration injection, specialization |
| 10 | Stale closures | SHOULD | Mutable state seen at read time, not creation |
| 11 | Block scope `const`/`let` | MUST | `var` leaks out of blocks |
| 12 | Temporal Dead Zone | MUST | `let`/`const` uninitialized until declaration |
| 13 | Function hoisting vs expression | SHOULD | Declarations fully hoisted; expressions are not |
| 14 | Shadowing | SHOULD | Inner binding masks outer; can cause bugs |
| 15 | Module scope | SHOULD | Private by default; nothing global |
| 16 | Four `this` rules | MUST | Default, implicit, explicit, `new` — call site determines |
| 17 | Arrow inherits `this` | MUST | No own binding; cannot be overridden |
| 18 | Method extraction loses `this` | MUST | `.bind()` or arrow wrapper to fix |
| 19 | Arrow over `call`/`apply`/`bind` | SHOULD | Simpler; reserve explicit binding for specific receivers |
| 20 | `.map()` / `.filter()` / `.reduce()` | SHOULD | Transform, select, aggregate — return new values |
| 21 | `.find()` / `.findIndex()` | SHOULD | Short-circuit on first match |
| 22 | `.some()` / `.every()` | SHOULD | Boolean aggregates with short-circuit |
| 23 | `.flatMap()` | SHOULD | Filter + map + expand in one pass |
| 24 | `for-of` for side effects and control flow | SHOULD | `break`, `continue`, `await` need imperative loops |
| 25 | `.bind()` for partial application | CONSIDER | Left-to-right only; clunky for complex cases |
| 26 | Manual partial application | SHOULD | Named, flexible, debuggable closures |
| 27 | `pipe()` / `compose()` | CONSIDER | Combine pure single-argument functions |
| 28 | Pure functions | SHOULD | Same input → same output, no side effects |
| 29 | Side effects at the edges | SHOULD | Pure core, I/O at boundaries |
| 30 | `.name` property rules | CONSIDER | Set at creation time; factory returns get `""` |
| 31 | Named function expressions | SHOULD | Explicit name in stack traces, self-reference |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `const`/`let`, arrow vs `function`, `for-of` vs `.forEach()`
- **API Design**: See `02-api-design.md` for parameter design, options objects, and iterator protocol
- **Error Handling**: See `03-error-handling.md` for async error patterns and callback errors
- **Values & References**: See `04-values-references.md` for mutation discipline and defensive copying
- **Type Discipline**: See `05-type-discipline.md` for JSDoc annotations and duck typing
- **Async & Concurrency**: See `07-async-concurrency.md` for async functions, `await`, and Promises
- **Anti-Patterns**: See `09-anti-patterns.md` for common closure and `this` bugs

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [MDN — Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [MDN — this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
- [MDN — Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
