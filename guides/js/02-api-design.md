# API Design

Essential patterns for designing clean, consistent, and composable JavaScript APIs. These idioms cover function signatures, module interfaces, class design, iteration protocols, return conventions, and naming — grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: Options Objects for Functions with More Than 2-3 Parameters

**Strength**: SHOULD

**Summary**: Use a destructured options object for functions with multiple optional or configuration-style parameters.

```js
// Good — named parameters via destructuring
function createServer({ port = 8080, host = "localhost", tls = false } = {}) {
  return { port, host, tls };
}
createServer({ port: 3000, tls: true });
createServer(); // all defaults apply

// Bad — positional args are unreadable at the call site
function createServer(port, host, tls) { /* ... */ }
createServer(3000, "localhost", true); // what is true?
```

**Rationale**: Call sites become self-documenting, argument order is irrelevant, new parameters can be added without breaking callers, and partial overrides work naturally. Rauschmayer demonstrates this as the canonical "named parameters" simulation in JavaScript (Deep JS Ch. 3; Exploring JS Ch. 15).

**See also**: ID-02, `01-core-idioms.md` ID-06

---

## ID-02: Per-Property Defaults with `= {}` Outer Default

**Strength**: SHOULD

**Summary**: When using an options object, provide defaults at two levels: per-property and an outer `= {}` for the no-argument case.

```js
// Good — both layers present
function move({ x = 0, y = 0 } = {}) {
  return [x, y];
}
move({ x: 3 });  // [3, 0] — per-property default fills y
move();           // [0, 0] — outer default prevents TypeError

// Bad — whole-object default only
function move({ x, y } = { x: 0, y: 0 }) {
  return [x, y];
}
move({ z: 3 });   // [undefined, undefined] — partial arg bypasses whole-object default
```

**Rationale**: The outer `= {}` handles the missing-argument case; per-property defaults handle partial objects. These two layers serve distinct purposes and both are required for a robust API. The "whole-object default" pattern silently breaks when callers pass partial arguments (Deep JS Ch. 3; Exploring JS Ch. 15).

---

## ID-03: Positional Args for Required, Options for Optional

**Strength**: SHOULD

**Summary**: Place required parameters as positional arguments first, then optional/configuration parameters in an options object.

```js
// Good — hybrid signature
function fetchResource(url, { method = "GET", headers = {}, timeout = 5000 } = {}) {
  /* ... */
}
fetchResource("/api/users");
fetchResource("/api/users", { method: "POST", timeout: 10000 });

// Bad — optional before required (forces placeholder)
function fetchResource(method, url, headers) { /* ... */ }
fetchResource(undefined, "/api/users", undefined); // painful
```

**Rationale**: Required positional args are unambiguous at the call site. Optional parameters in an options object can be omitted, reordered, or extended without affecting existing callers. Never place optional parameters before required ones — callers would be forced to pass `undefined` as a placeholder (Exploring JS Ch. 15; JS Definitive Guide, §8.3.1).

---

## ID-04: Return Consistent Types

**Strength**: MUST

**Summary**: Every code path in a function must return the same type. Never return different types depending on success or failure.

```js
// Good — always returns same shape: User | undefined
function findUser(id) {
  const user = users.get(id);
  return user ?? undefined;
}

// Good — always returns an array (possibly empty)
function search(query) {
  if (!query) return [];
  return db.query(query);
}

// Bad — returns object on success, false on failure
function findUser(id) {
  if (!users.has(id)) return false; // type mismatch
  return users.get(id);
}

// Bad — returns string or array depending on input
function parse(input) {
  if (typeof input === "string") return input.split(",");
  return input; // sometimes string[], sometimes who-knows-what
}
```

**Rationale**: Mixed return types force callers to check the type before using the value. The `IteratorResult` protocol is a canonical example of consistent shape: always `{ value, done }`, never switching to a bare value (Exploring JS Ch. 37; Eloquent JS Ch. 3).

---

## ID-05: Accept Iterables, Return Arrays

**Strength**: CONSIDER

**Summary**: When a function accepts a collection, accept any iterable. When it returns a collection, return a concrete array.

```js
// Good — accepts any iterable
function sum(items) {
  let total = 0;
  for (const n of items) total += n;
  return total;
}
sum([1, 2, 3]);           // array
sum(new Set([1, 2, 3]));  // Set
sum(range(1, 4));          // generator

// Good — returns a concrete array
function filter(items, pred) {
  const result = [];
  for (const item of items) {
    if (pred(item)) result.push(item);
  }
  return result;
}
```

**Rationale**: Accepting iterables makes APIs composable with arrays, Sets, Maps, generators, and custom iterables. Returning arrays gives callers a concrete, indexable, multi-pass collection with the full Array method suite (Exploring JS Ch. 37; JS Definitive Guide, §12.2).

---

## ID-06: One Module, One Responsibility

**Strength**: SHOULD

**Summary**: Each module should do one thing well. Prefer focused modules over kitchen-sink collections.

```js
// Good — focused modules
// date-format.js
export function formatDate(d) { /* ... */ }
export function parseDate(s) { /* ... */ }

// Good — separate module for a separate concern
// date-math.js
export function addDays(d, n) { /* ... */ }
export function diffDays(a, b) { /* ... */ }

// Bad — one module doing everything
// utils.js
export function formatDate(d) { /* ... */ }
export function slugify(s) { /* ... */ }
export function debounce(fn, ms) { /* ... */ }
export function deepClone(obj) { /* ... */ }
```

**Rationale**: Focused modules compose cleanly, are independently testable, and enable fine-grained tree-shaking. Haverbeke: modules that "compute values are applicable in a wider range of programs than bigger modules that perform complicated actions with side effects" (Eloquent JS Ch. 10; Exploring JS Ch. 29).

---

## ID-07: Export Functions, Not Objects with Methods

**Strength**: SHOULD

**Summary**: Prefer named function exports over a single default-exported object bundling methods.

```js
// Good — named exports, individually tree-shakeable
export function mean(data) { /* ... */ }
export function stddev(data) { /* ... */ }
export function median(data) { /* ... */ }

// Bad — single default object, all-or-nothing import
export default {
  mean(data) { /* ... */ },
  stddev(data) { /* ... */ },
  median(data) { /* ... */ },
};
```

**Rationale**: Named function exports are individually removable by tree-shaking. A default-exported object is a single export unit — the bundler must include the entire object even if only one method is used. Named exports also enable IDE autocomplete and consistent naming across the codebase (Exploring JS Ch. 29, Ch. 49).

**See also**: `01-core-idioms.md` ID-07

---

## ID-08: Re-Export for Public API Surfaces

**Strength**: CONSIDER

**Summary**: Use barrel files with selective re-exports to define a module's public API.

```js
// Good — selective re-exports (tree-shaking friendly)
// mod.js
export { mean } from "./stats/mean.js";
export { stddev } from "./stats/stddev.js";
export { median } from "./stats/median.js";

// Good — namespace re-export (ES2020)
export * as stats from "./stats/core.js";

// Risky — wildcard re-export (bundler may include more than needed)
export * from "./stats/core.js"; // does NOT include default exports
```

**Rules**:
- `export *` does NOT re-export the default export — use explicit renaming: `export { default as mean } from "./stats/mean.js"`
- Re-exported names are NOT available in the re-exporting module's own scope
- Prefer selective re-exports over wildcards for tree-shaking precision

**Rationale**: Barrel files provide a stable public API while allowing internal reorganization. Selective re-exports preserve tree-shaking granularity (Exploring JS Ch. 29; JS Definitive Guide, §10.3.4).

---

## ID-09: No Module-Level Side Effects

**Strength**: MUST

**Summary**: Module top-level code must not produce side effects. Keep all side effects inside exported functions.

```js
// Good — no side effects at module level
const DEFAULT_TIMEOUT = 5000;

export function createClient(options) {
  return new Client({ timeout: DEFAULT_TIMEOUT, ...options });
}

// Bad — side effect at import time
console.log("stats module loaded"); // runs on every import
const db = await connect("localhost:5432"); // blocks all importers
export function query(sql) { return db.execute(sql); }
```

**Rationale**: Module code runs once, on first import. Top-level side effects make modules unpredictable when import order matters, defeat tree-shaking (a module with side effects can never be safely eliminated), and make testing difficult. Keep computation pure at the module level; let callers trigger side effects explicitly (Exploring JS Ch. 29; Eloquent JS Ch. 10).

---

## ID-10: Export at Declaration

**Strength**: SHOULD

**Summary**: Use `export` at the declaration site rather than a bottom-of-file export list.

```js
// Good — inline export, intent is visible at definition
export function formatDate(d) { /* ... */ }
export const DATE_FORMAT = "YYYY-MM-DD";

// Acceptable — clause style for renaming
function sq(x) { return x * x; }
export { sq as square };

// Less preferred — export list at bottom (disconnected from definitions)
function formatDate(d) { /* ... */ }
const DATE_FORMAT = "YYYY-MM-DD";
export { formatDate, DATE_FORMAT };
```

**Rationale**: Inline exports make the file self-documenting — the public API is visible at each declaration, not hidden at the bottom. The clause style is appropriate when the internal name differs from the public name (Exploring JS Ch. 29; JS Definitive Guide, §10.3.1).

---

## ID-11: Prefer Factory Functions over Classes for Simple Data

**Strength**: SHOULD

**Summary**: For objects that are just data with no shared behavior or identity, use factory functions instead of classes.

```js
// Good — factory function for simple data
function createPoint(x, y) {
  return { x, y };
}

// Good — factory with computed properties
function createRange(start, end) {
  return {
    start,
    end,
    get size() { return end - start; },
  };
}

// Overkill — class for data-only object
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}
```

**When to use classes instead**: When you need `instanceof` checks, shared prototype methods across many instances, subclassing, or static members (JS Definitive Guide, §9.1-9.2; Deep JS Ch. 14).

**Rationale**: Factory functions are simpler, avoid `new`, and return plain objects that are easy to serialize, spread, and test. Classes add prototype machinery that is unnecessary for simple data shapes.

---

## ID-12: Use `#private` Fields, Not `_convention`

**Strength**: MUST

**Summary**: Use ES2022 `#` private fields for encapsulation. The `_` prefix convention has zero enforcement.

```js
// Good — language-enforced privacy
class Buffer {
  #data = [];
  #size = 0;

  push(item) {
    this.#data.push(item);
    this.#size++;
  }

  get size() { return this.#size; }
}

const buf = new Buffer();
buf.push("a");
buf.size;    // 1
// buf.#data; // SyntaxError — truly private

// Bad — convention-only, accessible from anywhere
class Buffer {
  constructor() {
    this._data = [];
    this._size = 0;
  }
}
const buf = new Buffer();
buf._size = 999; // no error — convention violated silently
```

**Rationale**: `#` private fields are invisible to `Reflect.ownKeys()`, cannot be accessed outside the class (SyntaxError), and never clash between classes. The `_` prefix is a social contract with zero enforcement — any code can read or write `_` properties (Exploring JS Ch. 31; JS Definitive Guide, §9.3.3; Deep JS Ch. 14).

---

## ID-13: Static Factory Methods for Alternative Construction

**Strength**: SHOULD

**Summary**: Use static methods for construction paths beyond the primary constructor.

```js
// Good — named factory methods
class Point {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
  }

  static fromPolar(radius, angle) {
    return new Point(radius * Math.cos(angle), radius * Math.sin(angle));
  }

  static from(other) {
    return new Point(other.x, other.y);
  }
}

const p1 = new Point(3, 4);
const p2 = Point.fromPolar(5, Math.PI / 4);
const p3 = Point.from(p1);

// Bad — overloaded constructor with type checking
class Point {
  constructor(...args) {
    if (args[0] instanceof Point) {
      this.x = args[0].x;
      this.y = args[0].y;
    } else {
      [this.x, this.y] = args;
    }
  }
}
```

**Naming conventions** (Deep JS Ch. 14):
- `.create()` — from scratch
- `.from(other)` — copy/convert from another object
- `.of(...args)` — assemble from values

**Rationale**: Static factory methods have descriptive names, can return cached instances, and avoid overloaded constructors with runtime type checking. Standard library precedents: `Array.from()`, `Object.create()`, `Promise.resolve()` (Exploring JS Ch. 31; Deep JS Ch. 14).

---

## ID-14: Async Initialization — Factory Function, Not Async Constructor

**Strength**: MUST

**Summary**: Constructors cannot be `async`. Use a static async factory method for objects that require asynchronous setup.

```js
// Good — static async factory
class DataStore {
  #connection;

  static async create(url) {
    const conn = await connect(url);
    return new DataStore(conn);
  }

  constructor(connection) {
    this.#connection = connection;
  }

  async query(sql) {
    return this.#connection.execute(sql);
  }
}

const store = await DataStore.create("postgres://localhost/mydb");

// Bad — async constructor is not valid syntax
class DataStore {
  async constructor(url) { // SyntaxError
    this.#connection = await connect(url);
  }
}
```

**To prevent direct constructor use**, combine with the secret-token pattern:

```js
const SECRET = Symbol("DataStore.create");

class DataStore {
  #connection;

  static async create(url) {
    const conn = await connect(url);
    return new DataStore(SECRET, conn);
  }

  constructor(token, connection) {
    if (token !== SECRET) throw new Error("Use DataStore.create()");
    this.#connection = connection;
  }
}
```

**Rationale**: The factory keeps the constructor synchronous and guarantees callers always receive a fully initialized instance. The secret-token pattern prevents misuse without exposing implementation details (Deep JS Ch. 14; Exploring JS Ch. 31).

---

## ID-15: Throw in Constructors for Invalid Arguments

**Strength**: MUST

**Summary**: Validate constructor arguments eagerly and throw on invalid input. Never produce a half-initialized object.

```js
// Good — fail fast
class Range {
  constructor(start, end) {
    if (typeof start !== "number" || typeof end !== "number") {
      throw new TypeError("Range requires numeric start and end");
    }
    if (start > end) {
      throw new RangeError(`start (${start}) must be <= end (${end})`);
    }
    this.start = start;
    this.end = end;
  }
}

// Bad — silently produces invalid object
class Range {
  constructor(start, end) {
    this.start = start; // might be undefined or "hello"
    this.end = end;
  }
}
```

**Rationale**: Constructors that accept invalid input create objects whose methods fail later with confusing errors. Throwing immediately localizes the bug to the construction site (JS Definitive Guide, §9.2; Deep JS Ch. 14).

**See also**: `03-error-handling.md`

---

## ID-16: Method Names Are Verbs, Property Names Are Nouns

**Strength**: SHOULD

**Summary**: Methods do things (verbs). Properties describe state (nouns/adjectives).

```js
// Good
class Collection {
  #items = [];

  get size() { return this.#items.length; }     // noun — state
  get isEmpty() { return this.#items.length === 0; } // adjective — state

  add(item) { this.#items.push(item); }         // verb — action
  remove(item) { /* ... */ }                     // verb — action
  contains(item) { return this.#items.includes(item); } // verb — query
  serialize() { return JSON.stringify(this.#items); }   // verb — action
}

// Bad — verb-named property, noun-named method
class Collection {
  get calculate() { return this.#items.length; } // "calculate" is a verb, not a state
  size() { return this.#items.length; }          // "size" reads as a noun, not an action
}
```

**Rationale**: The verb/noun distinction signals to callers whether something is computed on access (property) or triggers work (method). This matches standard library patterns: `array.length` (noun), `array.push()` (verb) (Exploring JS Ch. 9; Deep JS Ch. 21).

---

## ID-17: Boolean-Returning Methods Use `is`, `has`, `can`, `should`

**Strength**: SHOULD

**Summary**: Prefix boolean-returning methods with a predicate verb that reads as a question.

```js
// Good — reads as a question
if (user.isActive()) { /* ... */ }
if (collection.has(key)) { /* ... */ }
if (editor.canUndo()) { /* ... */ }
if (task.shouldRetry()) { /* ... */ }
if (list.isEmpty) { /* ... */ }     // getter also works

// Bad — ambiguous: is this a command or a query?
if (user.active()) { /* ... */ }    // activates the user? checks if active?
if (collection.check(key)) { /* ... */ } // checks what?
```

**Convention**:
- `isX()` — state predicate: `isValid()`, `isConnected()`
- `hasX()` — possession predicate: `has(key)`, `hasChildren()`
- `canX()` — capability predicate: `canEdit()`, `canSubmit()`
- `shouldX()` — advisory predicate: `shouldRetry()`, `shouldCache()`

**Rationale**: Boolean names that read as questions make conditionals self-documenting. Avoid names that could be read as commands (`enable()` vs `isEnabled()`) (Deep JS Ch. 21; JS Definitive Guide §6.10.6).

---

## ID-18: Conversion Methods — `toX()` Creates New, `fromX()` Constructs

**Strength**: SHOULD

**Summary**: Use `toX()` for instance methods that convert to another type. Use `ClassName.from()` for static construction from another type.

```js
// Good — toX() on instances for conversion
class Color {
  constructor(r, g, b) { this.r = r; this.g = g; this.b = b; }

  toString() { return `rgb(${this.r}, ${this.g}, ${this.b})`; }
  toJSON() { return { r: this.r, g: this.g, b: this.b }; }
  toHex() {
    const hex = (n) => n.toString(16).padStart(2, "0");
    return `#${hex(this.r)}${hex(this.g)}${hex(this.b)}`;
  }

  // Good — static from() for construction from another type
  static from(hex) {
    const m = hex.match(/^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
    if (!m) throw new Error(`Invalid hex color: ${hex}`);
    return new Color(parseInt(m[1], 16), parseInt(m[2], 16), parseInt(m[3], 16));
  }
}
```

**Standard library precedents**: `toString()`, `toJSON()`, `Array.from()`, `Object.fromEntries()`.

**Rationale**: `toX()` on the source signals "convert this instance." `ClassName.from()` on the target signals "construct from external data." This mirrors built-in JavaScript conventions (Exploring JS Ch. 9; Deep JS Ch. 21).

---

## ID-19: Private Methods and Fields Use `#`

**Strength**: MUST

**Summary**: Use `#` for all internal methods and fields. Do not expose implementation details.

```js
// Good — # private methods and fields
class Parser {
  #input;
  #pos = 0;

  constructor(input) { this.#input = input; }

  parse() {
    const tokens = this.#tokenize();
    return this.#buildAST(tokens);
  }

  #tokenize() { /* ... */ }
  #buildAST(tokens) { /* ... */ }
}

// Bad — _ convention leaks implementation
class Parser {
  constructor(input) {
    this._input = input;
    this._pos = 0;
  }
  _tokenize() { /* ... */ } // callable from outside
}
```

**Rationale**: `#` private methods cannot be called from outside the class — they are a true encapsulation boundary, not a naming convention. This makes refactoring safe: internal methods can be renamed, removed, or restructured without breaking external code (Exploring JS Ch. 31; JS Definitive Guide, §9.3.3).

**See also**: ID-12

---

## ID-20: Implement `Symbol.iterator` for Custom Collections

**Strength**: SHOULD

**Summary**: Any object that represents a sequence or collection should implement `Symbol.iterator` to work with `for-of`, spread, destructuring, and `Array.from()`.

```js
// Good — generator method creates fresh iterator each time
class NumberRange {
  constructor(from, to) {
    this.from = from;
    this.to = to;
  }

  *[Symbol.iterator]() {
    for (let i = Math.ceil(this.from); i <= this.to; i++) {
      yield i;
    }
  }
}

// Works with all iteration consumers
for (const n of new NumberRange(1, 5)) console.log(n);
const arr = [...new NumberRange(1, 5)];          // [1, 2, 3, 4, 5]
const [first, second] = new NumberRange(10, 20); // 10, 11

// Bad — not iterable, forces callers into manual access
class NumberRange {
  constructor(from, to) { this.from = from; this.to = to; }
  toArray() { /* ... */ } // callers must know to call this
}
```

**Rationale**: `Symbol.iterator` is the bridge between data sources and all language constructs that consume iteration. Implementing it makes your collection a first-class citizen of the language (Exploring JS Ch. 37; JS Definitive Guide, §12.1-12.2).

---

## ID-21: Use Generators to Simplify Iterator Implementation

**Strength**: SHOULD

**Summary**: Use `function*` or `*method()` to implement iterators. Generators eliminate manual state management.

```js
// Good — generator method, simple and correct
class BinaryTree {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }

  *[Symbol.iterator]() {
    yield this.value;
    if (this.left) yield* this.left;   // yield* delegates to sub-iterable
    if (this.right) yield* this.right;
  }
}

// Good — standalone generator for lazy transformation
function* map(iterable, fn) {
  for (const x of iterable) yield fn(x);
}

// Bad — manual iterator implementation (verbose, error-prone)
class ManualRange {
  constructor(from, to) { this.from = from; this.to = to; }
  [Symbol.iterator]() {
    let current = this.from;
    const end = this.to;
    return {
      next() {
        if (current <= end) return { value: current++, done: false };
        return { value: undefined, done: true };
      },
    };
  }
}
```

**Rationale**: Generator functions pause at each `yield` and resume on `.next()`, eliminating the need for explicit `{ value, done }` objects and state tracking. `yield*` enables recursive traversal with zero boilerplate (Exploring JS Ch. 38; JS Definitive Guide, §12.3).

---

## ID-22: Prefer Many-Times Iterables over One-Time

**Strength**: SHOULD

**Summary**: Design iterable classes so that each call to `[Symbol.iterator]()` returns a fresh, independent iterator.

```js
// Good — many-times iterable (generator method on class)
class Evens {
  constructor(limit) { this.limit = limit; }
  *[Symbol.iterator]() {
    for (let i = 0; i < this.limit; i += 2) yield i;
  }
}
const evens = new Evens(10);
[...evens]; // [0, 2, 4, 6, 8]
[...evens]; // [0, 2, 4, 6, 8] — still works

// Bad — one-time iterable (returns this)
function* evens(limit) {
  for (let i = 0; i < limit; i += 2) yield i;
}
const iter = evens(10);
[...iter]; // [0, 2, 4, 6, 8]
[...iter]; // [] — exhausted
```

**Rationale**: One-time iterables silently produce incomplete results when iterated twice. Many-times iterables (like Array, Set, Map) are safe to pass to multiple consumers. If you must pass a one-time iterator, materialize it first: `Array.from(iter)` (Exploring JS Ch. 37).

---

## ID-23: Return `undefined` for "No Meaningful Value"

**Strength**: SHOULD

**Summary**: Use `undefined` (implicit or explicit) when a function has no meaningful return value or when a lookup finds nothing.

```js
// Good — undefined for "not found" (matches Array.prototype.find)
function findUser(id) {
  return users.get(id); // undefined if not present
}

// Good — void functions implicitly return undefined
function logMessage(msg) {
  console.log(msg);
  // implicit return undefined
}
```

**Rationale**: `undefined` is JavaScript's own default non-value — it appears when variables are uninitialized, properties are missing, and functions lack a `return`. Using it for "no result" is consistent with language semantics and built-in methods like `Array.prototype.find()` and `Map.prototype.get()` (Exploring JS Ch. 16; JS Definitive Guide, §3.5).

**See also**: ID-24

---

## ID-24: Return `null` Only When the API Explicitly Models Absence

**Strength**: CONSIDER

**Summary**: Use `null` as a deliberate signal meaning "intentionally empty" or "explicitly no value," distinct from `undefined`'s "nothing here."

```js
// Good — null as explicit "switched off"
function getOverride(key) {
  if (!(key in overrides)) return undefined; // key not recognized
  return overrides[key] ?? null;             // key recognized, explicitly unset
}

// Good — null in JSON-serializable data (undefined is omitted by JSON)
const config = {
  theme: "dark",
  customHeader: null, // explicitly no custom header
};
JSON.stringify(config); // {"theme":"dark","customHeader":null}
```

**Rationale**: `null` serializes to JSON while `undefined` is silently dropped. Use `null` when absence is a meaningful domain value (e.g., "no selection," "cleared"), not when something was simply never set (Exploring JS Ch. 16; JS Definitive Guide, §3.5).

---

## ID-25: Never Return Different Types from the Same Function

**Strength**: MUST

**Summary**: A function must return the same type across all code paths. Use `undefined`/`null` for absence, not a different type.

```js
// Good — always string | undefined
function getLabel(id) {
  return labels.get(id); // Map.get returns V | undefined
}

// Good — always Array (possibly empty)
function getResults(query) {
  if (!query) return [];
  return db.search(query);
}

// Bad — string on success, boolean on failure
function getLabel(id) {
  if (!labels.has(id)) return false;
  return labels.get(id);
}

// Bad — sometimes number, sometimes null, sometimes string
function parse(input) {
  if (!input) return null;
  const n = Number(input);
  if (Number.isNaN(n)) return input; // string fallback
  return n;
}
```

**Rationale**: Mixed return types force callers into defensive type checking and produce fragile code. Consistent types enable chaining, composition, and reliable destructuring (Exploring JS Ch. 37; Eloquent JS Ch. 3).

**See also**: ID-04

---

## ID-26: Async Functions Always Return Promises — No Callback Alternatives

**Strength**: MUST

**Summary**: If a function is async, it returns a Promise. Never provide a callback-based alternative alongside an async version.

```js
// Good — async function, callers use await or .then()
export async function fetchUser(id) {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) throw new Error(`User ${id} not found`);
  return res.json();
}

// Bad — dual interface (callback + promise)
export function fetchUser(id, callback) {
  const promise = fetch(`/api/users/${id}`).then((r) => r.json());
  if (callback) {
    promise.then((data) => callback(null, data)).catch((err) => callback(err));
  }
  return promise;
}
```

**Rationale**: Dual interfaces double the API surface, confuse callers, and complicate error handling. Every `async` function wraps its return value in a Promise automatically. Let callers choose their consumption style (`await`, `.then()`, `Promise.all()`) without the API dictating it (Exploring JS Ch. 42; JS Definitive Guide, §13.2-13.3).

---

## ID-27: Use Symbols for Non-Enumerable Metadata Properties

**Strength**: CONSIDER

**Summary**: Use Symbol-keyed properties for internal metadata that should not appear in `Object.keys()`, `for...in`, or `JSON.stringify()`.

```js
// Good — Symbol key for internal metadata
const META = Symbol("meta");

class Collection {
  constructor(items) {
    this.items = items;
    this[META] = { version: 1, created: Date.now() };
  }
}

const c = new Collection([1, 2, 3]);
Object.keys(c);         // ["items"] — META is hidden
JSON.stringify(c);       // {"items":[1,2,3]} — META excluded

// Bad — string key pollutes enumerable namespace
class Collection {
  constructor(items) {
    this.items = items;
    this.__meta__ = { version: 1, created: Date.now() }; // visible everywhere
  }
}
```

**Rationale**: Symbol-keyed properties are non-enumerable by default, cannot collide with string keys, and operate at a separate "meta level." This prevents name collisions between application and library code (Exploring JS Ch. 32; JS Definitive Guide, §14.4).

---

## ID-28: Proxy-Based Validation at API Boundaries

**Strength**: CONSIDER

**Summary**: Use Proxy `set` traps to enforce constraints on objects at API boundaries. Always forward with `Reflect.set()`.

```js
// Good — validated property assignment
function createValidated(schema) {
  return new Proxy({}, {
    set(target, prop, value, receiver) {
      if (!(prop in schema)) {
        throw new Error(`Unknown property: ${prop}`);
      }
      if (typeof value !== schema[prop]) {
        throw new TypeError(`${prop} must be ${schema[prop]}, got ${typeof value}`);
      }
      return Reflect.set(target, prop, value, receiver);
    },
  });
}

const point = createValidated({ x: "number", y: "number" });
point.x = 10;    // ok
point.y = 20;    // ok
point.x = "ten"; // TypeError: x must be number, got string
point.z = 0;     // Error: Unknown property: z

// Bad — set trap without Reflect forwarding
set(target, prop, value) {
  target[prop] = value; // bypasses receiver and inherited setters
  // no return — undefined is falsy, strict mode throws TypeError
}
```

**Rationale**: Proxy `set` traps validate at the point of assignment, catching errors immediately rather than at usage time. Always use `Reflect.set()` to correctly handle receivers, prototype chains, and accessor properties. The `set` trap must return `true` on success (Deep JS Ch. 19-20; JS Definitive Guide, §14.7).

---

## ID-29: Prefer Composition over Inheritance

**Strength**: SHOULD

**Summary**: Use delegation (has-a) instead of inheritance (is-a) unless objects truly share behavior and type identity.

```js
// Good — composition: Histogram wraps Map
class Histogram {
  #map = new Map();

  count(key) { return this.#map.get(key) ?? 0; }
  has(key) { return this.count(key) > 0; }

  add(key) {
    this.#map.set(key, this.count(key) + 1);
  }

  get size() { return this.#map.size; }

  *[Symbol.iterator]() {
    yield* this.#map;
  }
}

// Bad — inheritance exposes the full Map API
class Histogram extends Map {
  // Inherits .delete(), .clear(), .set() — all undesirable for a histogram
}
```

**Rationale**: Inheritance creates tight coupling — changes to the superclass can silently break subclasses. Composition wraps and selectively forwards, exposing only the intended API. All four sources agree: favor composition over inheritance (JS Definitive Guide, §9.5.3; Deep JS Ch. 14; Exploring JS Ch. 31).

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Options objects for 3+ params | SHOULD | Named params via destructuring, order-independent |
| 02 | Per-property defaults + `= {}` | SHOULD | Two layers: per-property AND outer default both needed |
| 03 | Positional required, options optional | SHOULD | Never place optional before required |
| 04 | Consistent return types | MUST | Same type across all code paths |
| 05 | Accept iterables, return arrays | CONSIDER | Composable input, concrete output |
| 06 | One module, one responsibility | SHOULD | Focused modules compose and tree-shake cleanly |
| 07 | Export functions, not method objects | SHOULD | Named exports are individually tree-shakeable |
| 08 | Re-export for public API surfaces | CONSIDER | Selective re-exports preserve tree-shaking |
| 09 | No module-level side effects | MUST | Side effects defeat tree-shaking and testing |
| 10 | Export at declaration | SHOULD | Inline export makes public API visible at definition |
| 11 | Factory functions for simple data | SHOULD | Plain objects over classes when no shared behavior |
| 12 | `#private` fields, not `_convention` | MUST | Language-enforced, invisible, clash-free |
| 13 | Static factory methods | SHOULD | Named construction paths, no constructor overloading |
| 14 | Async factory, not async constructor | MUST | Constructors are synchronous; use static async factory |
| 15 | Throw in constructors for invalid args | MUST | Fail fast, never produce half-initialized objects |
| 16 | Methods = verbs, properties = nouns | SHOULD | Signals action vs state to callers |
| 17 | Boolean methods: `is`/`has`/`can`/`should` | SHOULD | Reads as a question in conditionals |
| 18 | `toX()` converts, `from()` constructs | SHOULD | Matches built-in conventions |
| 19 | `#` for private methods too | MUST | True encapsulation, safe to refactor |
| 20 | `Symbol.iterator` for collections | SHOULD | Integrates with `for-of`, spread, destructuring |
| 21 | Generators simplify iterators | SHOULD | Eliminates manual state and `{ value, done }` |
| 22 | Many-times iterables over one-time | SHOULD | Fresh iterator per `[Symbol.iterator]()` call |
| 23 | `undefined` for "no meaningful value" | SHOULD | Matches language default and built-in methods |
| 24 | `null` for explicit modeled absence | CONSIDER | Serializes to JSON, signals intentional emptiness |
| 25 | Never return mixed types | MUST | Consistent shape enables composition |
| 26 | Async = Promise, no callback alternative | MUST | Single interface, callers choose consumption style |
| 27 | Symbols for metadata properties | CONSIDER | Non-enumerable, clash-free, hidden from JSON |
| 28 | Proxy validation at API boundaries | CONSIDER | `set` trap + `Reflect.set()` for immediate constraint checks |
| 29 | Composition over inheritance | SHOULD | Delegation wraps selectively; inheritance exposes everything |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `const`/`let`, equality, destructuring, ESM basics
- **Error Handling**: See `03-error-handling.md` for error types, try/catch, and Result patterns
- **Values & References**: See `04-values-references.md` for mutation discipline, copying, and immutability
- **Type Discipline**: See `05-type-discipline.md` for JSDoc annotations and runtime type checking
- **Functions & Closures**: See `06-functions-closures.md` for closures, higher-order functions, and composition
- **Async & Concurrency**: See `07-async-concurrency.md` for Promise patterns, async iteration, and concurrency
- **Anti-Patterns**: See `09-anti-patterns.md` for common JavaScript API design mistakes
- **Deno**: See `12-deno/01-runtime-basics.md` for Deno-specific API patterns

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [Biome Documentation](https://biomejs.dev/)
- [MDN Web Docs — JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
