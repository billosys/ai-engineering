# Core JavaScript Idioms

Essential JavaScript idioms for writing clean, modern, Deno-first code. These patterns represent fundamental best practices grounded in authoritative sources: *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: `const` by Default, `let` When Needed, Never `var`

**Strength**: MUST

**Summary**: Use `const` for all bindings unless reassignment is required; use `let` for reassignment; never use `var`.

```js
// Good
const maxRetries = 3;
const users = [];
users.push("Alice"); // mutation of value is fine
let count = 0;
count += 1;

// Bad
var maxRetries = 3;  // function-scoped, hoisted to undefined, creates global property
let users = [];      // misleading — suggests the binding will change
```

**Rationale**: `var` is function-scoped, silently hoists declarations as `undefined`, allows redeclaration, and creates properties on `globalThis` at the top level — all sources of bugs. `const` communicates intent: this binding will not change. `let` communicates: this value will change. Rauschmayer recommends `const` as the default; Flanagan calls `var` hoisting "one of the important misfeatures that `let` corrects" (Exploring JS Ch. 11; JS Definitive Guide, §3.10.2).

**See also**: ID-14

---

## ID-02: Always Use `===` and `!==`

**Strength**: MUST

**Summary**: Use strict equality for all comparisons. Never use `==` or `!=` except the one documented exception.

```js
// Good
if (x === 0) { /* ... */ }
if (name !== "") { /* ... */ }

// Bad
if (x == 0) { /* ... */ }    // "" == 0 is true, [] == 0 is true
if (name != "") { /* ... */ } // undefined != "" is true (accidentally correct, but fragile)
```

**The `==` coercion traps** (Deep JS, §14.2; JS Definitive Guide, §4.9.1):

```js
"" == 0           // true — string converts to number
2 == true         // false — true becomes 1, not "truthy match"
[] == false       // true — [] → "" → 0, false → 0
"0" == false      // true — both become 0
null == undefined // true — special case, the ONLY accepted use of ==
null == 0         // false — null is not coerced to a number
```

**The one exception**: `x == null` is an accepted idiom for testing both `null` and `undefined` in a single check. All four sources acknowledge this pattern. Comment it when used.

```js
// Acceptable — tests null OR undefined, nothing else
if (value == null) {
  throw new Error("value is required");
}
```

**Rationale**: `===` compares type and value with zero coercion. `==` applies an asymmetric, multi-step coercion cascade that produces surprising results even for experienced developers (Exploring JS Ch. 13; Eloquent JS Ch. 1).

---

## ID-03: Use `??` for Nullish Defaults, Not `||`

**Strength**: SHOULD

**Summary**: Use nullish coalescing (`??`) when providing default values. Reserve `||` for boolean logic.

```js
// Good — ?? only triggers on null/undefined
const timeout = options.timeout ?? 5000;    // 0 is preserved
const title = options.title ?? "Untitled";  // "" is preserved
const verbose = options.verbose ?? true;    // false is preserved

// Bad — || treats 0, "", false as missing
const timeout = options.timeout || 5000;    // 0 becomes 5000!
const title = options.title || "Untitled";  // "" becomes "Untitled"!
const verbose = options.verbose || true;    // false becomes true!
```

**Mixing `??` with `&&`/`||` requires explicit parentheses** — omitting them is a SyntaxError:

```js
// Good
const x = (a ?? b) || c;

// Bad — SyntaxError
const x = a ?? b || c;
```

**Rationale**: `||` returns the right-hand side for any falsy value (including `0`, `""`, `false`, `NaN`). `??` returns the right-hand side only for `null` or `undefined`. When `0`, `""`, or `false` are legitimate values, `||` silently discards them (Exploring JS Ch. 14; JS Definitive Guide, §4.13.2).

---

## ID-04: Use Optional Chaining `?.` for Safe Property Access

**Strength**: SHOULD

**Summary**: Use `?.` to safely access properties on potentially nullish values. Combine with `??` for defaults.

```js
// Good
const street = person?.address?.street ?? "(unknown)";
const len = arr?.length;
const result = callback?.();

// Bad — verbose guard chains
const street = person && person.address && person.address.street;
if (typeof callback === "function") { callback(); }
```

**Three forms** (JS Definitive Guide, §4.4.1; Exploring JS Ch. 14):
- `obj?.prop` — property access
- `obj?.[expr]` — computed access
- `func?.(args)` — conditional invocation

**Short-circuiting applies to the entire chain** — side effects in skipped portions do not execute:

```js
let i = 0;
const val = nullObj?.[i++]; // val is undefined, i is still 0
```

**Do not overuse** — Rauschmayer warns that scattering `?.` throughout code can silently hide bugs. Prefer normalizing data shapes at ingestion boundaries.

---

## ID-05: Prefer Template Literals over String Concatenation

**Strength**: SHOULD

**Summary**: Use backtick template literals for any string that embeds expressions or spans multiple lines.

```js
// Good
const msg = `Hello, ${name}! You have ${count} items.`;
const sql = `
  SELECT *
  FROM users
  WHERE id = ${userId}
`;

// Bad
const msg = "Hello, " + name + "! You have " + count + " items.";
const sql = "SELECT *\n" +
  "FROM users\n" +
  "WHERE id = " + userId;
```

**Rationale**: Template literals are more readable, support multiline without escapes, and use `${}` interpolation that accepts any expression. Concatenation with `+` is error-prone (the `+` operator doubles as numeric addition) and harder to scan visually (Exploring JS Ch. 19; JS Definitive Guide, §3.3.4).

**Caveat**: Literal newlines and indentation inside backticks become part of the string. Use `.trim()` or a `dedent` tagged template for indentation-sensitive output.

---

## ID-06: Destructure at the Point of Use

**Strength**: SHOULD

**Summary**: Extract needed properties at the point of use — in parameters, assignments, or loop heads.

```js
// Good — destructure in parameter
function formatUser({ name, email, role = "member" }) {
  return `${name} <${email}> [${role}]`;
}

// Good — destructure in loop
for (const [index, value] of arr.entries()) {
  console.log(`${index}: ${value}`);
}

// Good — destructure in assignment
const { host, port = 8080 } = config;

// Bad — manual extraction
function formatUser(user) {
  const name = user.name;
  const email = user.email;
  const role = user.role || "member";
}
```

**Named parameters via destructuring** — the robust pattern (Deep JS, §16.2):

```js
// Good — per-property defaults + outer = {} for no-argument case
function move({ x = 0, y = 0 } = {}) {
  return [x, y];
}
move({ x: 3 });  // [3, 0]
move();           // [0, 0]

// Bad — whole-object default breaks with partial arguments
function move({ x, y } = { x: 0, y: 0 }) {
  return [x, y];
}
move({ z: 3 });   // [undefined, undefined] — surprise!
```

**Rationale**: Destructuring is concise, self-documenting (parameter names are visible in the signature), and enables default values. Defaults trigger only on `undefined`, not `null` (Exploring JS Ch. 15).

---

## ID-07: Use Named Exports, Avoid Default Exports

**Strength**: SHOULD

**Summary**: Prefer named exports. Reserve default exports only for modules with a single, obvious purpose.

```js
// Good — named exports
export function formatDate(d) { /* ... */ }
export function parseDate(s) { /* ... */ }
export const DATE_FORMAT = "YYYY-MM-DD";

// Bad — default export
export default function formatDate(d) { /* ... */ }
// Importers can name it anything — formatDate, fmt, dateFormatter, x...
```

**Rationale**: Named exports enforce a consistent name across the codebase, enable tree-shaking (bundlers eliminate individual unused exports), and support IDE autocomplete. Default exports let importers choose arbitrary names, making search and refactoring harder. Rauschmayer recommends against mixing default and named exports in the same module (Exploring JS Ch. 29; JS Definitive Guide, §10.3).

---

## ID-08: ESM Only — No CommonJS, No `require()`

**Strength**: MUST

**Summary**: Use ECMAScript modules exclusively. Never use `require()`, `module.exports`, or `exports`.

```js
// Good — ESM with Deno APIs and standard library
import { formatDate } from "./utils.js";
import { join } from "@std/path";

const data = await Deno.readTextFile(join("config", "app.json"));
export function processData(input) { /* ... */ }

// Bad — CommonJS / Node.js
const { readFile } = require("fs/promises");
const { join } = require("path");
module.exports = { processData };
```

**Rationale**: ESM is the JavaScript standard. CommonJS is synchronous, prevents static analysis and tree-shaking, and is not supported as the primary module system in Deno. Haverbeke: "there is no real reason to write new programs in [CommonJS] style anymore" (Eloquent JS Ch. 10; Exploring JS Ch. 29; JS Definitive Guide, §10.2-10.3).

**Module characteristics**:
- Automatic strict mode (no `"use strict"` needed)
- Own scope (top-level declarations are not global)
- Singleton execution (code runs once, on first import)
- Static structure enables tree-shaking
- Live bindings (imports reflect current export values)

---

## ID-09: Arrow Functions for Callbacks, `function` for Declarations

**Strength**: SHOULD

**Summary**: Use arrow functions for inline callbacks and closures. Use `function` declarations for named, module-level functions.

```js
// Good — arrow for callback (inherits this, concise)
const doubled = items.map((x) => x * 2);
button.addEventListener("click", (e) => {
  this.handleClick(e); // arrow inherits this from enclosing scope
});

// Good — function declaration for named export (hoisted, named in stack traces)
export function parseConfig(raw) {
  /* ... */
}

// Bad — ordinary function as callback (loses this in strict mode)
items.map(function (x) {
  return this.transform(x); // TypeError: this is undefined
});

// Bad — arrow for method (no own this)
const obj = {
  name: "bad",
  greet: () => `Hello, ${this.name}`, // this is undefined, not obj
};
```

**Arrow function constraints** (Exploring JS Ch. 27; JS Definitive Guide, §8.1.3):
- No own `this` — inherits from enclosing scope
- Cannot be constructors (`new` throws TypeError)
- No `arguments` object (use rest parameters)
- Object literal return requires parentheses: `() => ({ key: value })`

**Rationale**: Arrow functions eliminate the `const self = this` pattern and are syntactically concise for callbacks. `function` declarations are hoisted, produce clear stack traces, and are the conventional form for named standalone functions.

---

## ID-10: Avoid `this` Unless in Classes or Methods

**Strength**: SHOULD

**Summary**: Restrict `this` usage to class methods and object method shorthand. Avoid it in standalone functions and callbacks.

```js
// Good — this in a class method
class Counter {
  #count = 0;
  increment() { this.#count++; }
  get value() { return this.#count; }
}

// Good — this in method shorthand
const calculator = {
  total: 0,
  add(n) { this.total += n; },
};

// Bad — this in a standalone function (undefined in strict mode / ESM)
function getUser() {
  return this.currentUser; // TypeError: Cannot read properties of undefined
}

// Bad — this in a callback (use arrow instead)
class Logger {
  prefix = "[LOG]";
  logAll(items) {
    items.forEach(function (item) {
      console.log(`${this.prefix} ${item}`); // this is undefined
    });
  }
}
```

**`this` context table** (Exploring JS Ch. 30):

| Context | Value of `this` |
|---------|----------------|
| Ordinary function call (strict/ESM) | `undefined` |
| Method call `obj.method()` | `obj` |
| `new Constructor()` | new instance |
| Arrow function | inherited from enclosing scope |
| Module top level | `undefined` |

**Rationale**: In strict mode (which ESM enables automatically), `this` in a standalone function is `undefined` — not the global object. Misuse of `this` is one of the most common JavaScript bugs. Confine it to classes and method shorthand where its value is predictable (Exploring JS Ch. 30; JS Definitive Guide, §8.2).

---

## ID-11: Document All Magic Values

**Strength**: MUST

**Summary**: Every literal number, string, or value that isn't self-evident must be named or commented.

```js
// Good — named constant with explanation
/** Maximum retry attempts before circuit-breaker opens. */
const MAX_RETRIES = 3;

/** HTTP 429 Too Many Requests — back off and retry. */
const TOO_MANY_REQUESTS = 429;

if (response.status === TOO_MANY_REQUESTS) {
  await backoff(attempt, MAX_RETRIES);
}

// Bad — unexplained magic numbers
if (response.status === 429) {
  await backoff(attempt, 3);
}
```

**Rationale**: Magic values obscure intent, make code harder to search, and resist refactoring. Named constants are self-documenting, searchable, and changeable in one place.

---

## ID-12: Naming — `camelCase` for Values, `PascalCase` for Classes, `UPPER_CASE` for Constants

**Strength**: MUST

**Summary**: Follow JavaScript naming conventions consistently.

```js
// Good
const maxRetries = 3;                     // camelCase: local variable
const MAX_CONNECTIONS = 100;              // UPPER_CASE: module-level constant
function computeTotal(items) { /* ... */ } // camelCase: function
class EventEmitter { /* ... */ }          // PascalCase: class

// Bad
const MaxRetries = 3;      // PascalCase signals a class
const max_retries = 3;     // snake_case is not JS convention
function ComputeTotal() {} // PascalCase implies constructor / class
```

**Naming conventions** (Exploring JS Ch. 9; JS Definitive Guide, §2.4):

| Element | Convention | Example |
|---------|-----------|---------|
| Variables, functions, methods | camelCase | `getUserName`, `itemCount` |
| Classes, constructors | PascalCase | `HttpClient`, `EventEmitter` |
| Module-level constants | UPPER_CASE | `MAX_RETRIES`, `API_BASE_URL` |
| Module filenames | kebab-case | `date-utils.js`, `http-client.js` |
| Unused parameters | `_` prefix | `arr.map((_item, i) => i)` |

**Rationale**: JavaScript is case-sensitive. PascalCase for non-classes is a false signal that `new` is required. UPPER_CASE for local `const` variables is noisy — reserve it for shared module-level constants.

---

## ID-13: Avoid Weasel Words in Names

**Strength**: MUST

**Summary**: Use specific, descriptive names. Avoid generic terms that add syllables without meaning.

```js
// Good — specific names
function validateEmail(input) { /* ... */ }
function buildUserQuery(filters) { /* ... */ }
class ConnectionPool { /* ... */ }
class RequestRouter { /* ... */ }

// Bad — weasel words
function handleData(data) { /* ... */ }    // "handle" and "data" say nothing
function processInfo(info) { /* ... */ }   // "process" and "info" are vague
class UserManager { /* ... */ }            // "Manager" — manages what?
class DataService { /* ... */ }            // "Data" + "Service" = zero information
```

**Words to avoid as primary identifiers**: `Manager`, `Service`, `Handler`, `Helper`, `Utils`, `Data`, `Info`, `Process`, `Handle`, `Do`, `Perform`, `Execute` (when used generically).

**Rationale**: Vague names force readers to inspect the implementation to understand the code. Specific names enable scanning and reasoning without reading function bodies.

---

## ID-14: `const` Does Not Mean Immutable

**Strength**: MUST

**Summary**: Understand that `const` freezes the binding (the variable cannot be reassigned), not the value.

```js
// const prevents reassignment
const config = { debug: false };
// config = {};              // TypeError: Assignment to constant variable

// const does NOT prevent mutation
config.debug = true;         // perfectly legal
config.newProp = "added";    // also legal

const items = [1, 2, 3];
items.push(4);               // [1, 2, 3, 4] — legal
// items = [];               // TypeError
```

**Rationale**: This is one of the most common JavaScript misconceptions. `const` means "constant binding" not "constant value." The distinction between a binding (the name-to-value association) and the value itself is fundamental. All four sources emphasize this (Exploring JS Ch. 11; Deep JS Ch. 8; JS Definitive Guide, §3.10.1).

**See also**: ID-01, ID-15

---

## ID-15: Prefer `Object.freeze()` for True Constant Objects

**Strength**: CONSIDER

**Summary**: When you need an object whose properties cannot be modified, use `Object.freeze()`.

```js
// Good — truly immutable configuration
const CONFIG = Object.freeze({
  maxRetries: 3,
  timeout: 5000,
  baseUrl: "https://api.example.com",
});
CONFIG.maxRetries = 99; // TypeError in strict mode (silently ignored in sloppy)

// Shallow only — nested objects are NOT frozen
const NESTED = Object.freeze({
  db: { host: "localhost", port: 5432 },
});
NESTED.db.port = 9999; // succeeds! nested object is not frozen

// For deep immutability, freeze recursively or use structuredClone + freeze
function deepFreeze(obj) {
  for (const value of Object.values(obj)) {
    if (typeof value === "object" && value !== null) {
      deepFreeze(value);
    }
  }
  return Object.freeze(obj);
}
```

**Three levels of object protection** (JS Definitive Guide, §14.2):

| Method | New props | Modify | Delete | Reversible |
|--------|-----------|--------|--------|------------|
| `preventExtensions()` | Blocked | Yes | Yes | No |
| `seal()` | Blocked | Yes | No | No |
| `freeze()` | Blocked | No | No | No |

**Rationale**: `const` alone does not prevent property modification. For configuration objects, lookup tables, and other data that must not change, `Object.freeze()` provides enforcement. Be aware it is shallow (Deep JS Ch. 8; JS Definitive Guide, §14.2).

---

## ID-16: Prefer `Map`/`Set` over Plain Objects for Dynamic Collections

**Strength**: SHOULD

**Summary**: Use `Map` for key-value collections and `Set` for unique-value collections when keys are dynamic or non-string.

```js
// Good — Map for dynamic keys
const cache = new Map();
cache.set(userObj, computeExpensiveResult(userObj)); // object as key
cache.set(42, "forty-two");                          // number as key
cache.size;                                          // accurate count

// Bad — plain object for dynamic keys
const cache = {};
cache[userObj] = result; // key becomes "[object Object]" — collision!
cache[42] = "forty-two"; // key becomes string "42"
Object.keys(cache).length; // verbose size check

// Good — Set for uniqueness
const visited = new Set();
visited.add(url);
if (visited.has(url)) { /* skip */ }

// Bad — object as set
const visited = {};
visited[url] = true;
```

**When to use plain objects**: For fixed-shape records with known string keys (configuration, DTOs, JSON-compatible data).

**Rationale**: `Map` accepts any key type, provides a `.size` property, iterates in insertion order, and has no prototype pollution risk. Plain objects coerce all keys to strings and inherit from `Object.prototype` (Exploring JS Ch. 33; JS Definitive Guide, §11.1).

---

## ID-17: Use Rest Parameters Instead of `arguments`

**Strength**: MUST

**Summary**: Use rest parameters (`...args`) for variadic functions. Never use the legacy `arguments` object.

```js
// Good — rest parameter is a real Array
function max(first = -Infinity, ...rest) {
  for (const n of rest) {
    if (n > first) first = n;
  }
  return first;
}

// Bad — arguments is not a real Array, unavailable in arrow functions
function max() {
  const args = Array.from(arguments); // conversion required
  return args.reduce((a, b) => Math.max(a, b));
}
```

**Rationale**: Rest parameters produce a real `Array` (with `.map()`, `.filter()`, etc.), work in arrow functions, are visible in the function signature, and can have a name that communicates intent. The `arguments` object is array-like but not an `Array`, is unavailable in arrow functions, and hides the function's arity (Exploring JS Ch. 15; JS Definitive Guide, §8.3.2-8.3.3).

---

## ID-18: Use Spread Syntax Instead of `apply()`

**Strength**: SHOULD

**Summary**: Use spread (`...`) to expand iterables into function arguments or array/object literals.

```js
// Good — spread into function call
Math.max(...numbers);

// Bad — apply
Math.max.apply(null, numbers);

// Good — shallow copy / merge
const merged = [...arr1, ...arr2];
const updated = { ...defaults, ...overrides };

// Good — convert iterable to Array
const unique = [...new Set(items)];

// Bad — manual conversion
const unique = Array.from(new Set(items));  // acceptable but verbose
```

**Rationale**: Spread is more readable and does not require a `this` argument. It works with any iterable (arrays, sets, maps, strings, generators), while `apply()` requires an array-like object (Exploring JS Ch. 15; JS Definitive Guide, §8.3.4).

---

## ID-19: Explicit Returns in Arrow Functions

**Strength**: SHOULD

**Summary**: Use concise body (`=>` expression) for single-expression returns. Use block body (`=> { }`) when logic requires multiple statements.

```js
// Good — concise body for single expression
const double = (x) => x * 2;
const isEven = (n) => n % 2 === 0;
const getName = (user) => user.name;

// Good — block body for multiple statements
const processItem = (item) => {
  const normalized = item.trim().toLowerCase();
  const validated = validate(normalized);
  return validated;
};

// Bad — unnecessary block body
const double = (x) => { return x * 2; };

// Gotcha — returning an object literal requires parentheses
const toPoint = (x, y) => ({ x, y });     // Good
const toPoint = (x, y) => { x, y };       // Bad — returns undefined, {} is a block
```

**Rationale**: Concise bodies improve readability for simple transformations. Block bodies make multi-step logic clear. The object literal parentheses requirement is a common source of silent bugs (Exploring JS Ch. 27; JS Definitive Guide, §8.1.3).

---

## ID-20: No Node.js — Use Deno APIs and Web Platform APIs

**Strength**: MUST

**Summary**: Target Deno as the runtime. Use Web Platform APIs (`fetch`, `URL`, `crypto`, etc.) and Deno namespace APIs. Avoid Node.js-specific patterns.

```js
// Good — Deno/Web Platform APIs
const response = await fetch("https://api.example.com/data");
const text = await Deno.readTextFile("./config.json");
const url = new URL("/path", "https://example.com");

// Bad — Node.js patterns
const fs = require("fs");                    // CommonJS
const data = fs.readFileSync("config.json"); // Sync I/O
const path = require("path");               // Node path module
```

**Deno-specific conventions**:
- File extensions are **required** on local imports: `import { add } from "./calc.js"`
- Permissions are explicit: `deno run --allow-read --allow-net script.js`
- Configuration in `deno.json` replaces `package.json`, `.eslintrc`, `.prettierrc`
- Use `jsr:` specifiers for JSR registry packages, `npm:` for npm packages
- Use `Deno.test()` for testing (built-in test runner)

**Rationale**: Deno is ESM-native, secure-by-default, and ships with a built-in toolchain (linter, formatter, test runner). It uses Web Platform APIs wherever possible, making code portable between Deno and browsers.

---

## ID-21: `const` in Loops — Know What Works

**Strength**: SHOULD

**Summary**: Use `const` in `for-of` and `for-in` loops. Use `let` for `for` loop counters.

```js
// Good — const in for-of (fresh binding each iteration)
for (const item of items) {
  console.log(item);
}

// Good — const in for-in
for (const key in obj) {
  console.log(key, obj[key]);
}

// Good — let for counter (reassigned each iteration)
for (let i = 0; i < items.length; i++) {
  const item = items[i]; // const is fine inside the body
  console.log(item);
}

// Bad — const for counter (TypeError on i++)
// for (const i = 0; i < 10; i++) { }
```

**Rationale**: In `for-of` and `for-in`, each iteration creates a fresh binding initialized to the current value — `const` is correct because no reassignment occurs. A `for` loop counter is reassigned (`i++`), so `let` is required (Exploring JS Ch. 11; JS Definitive Guide, §3.10.1).

---

## ID-22: Prefer Truthiness Checks Carefully

**Strength**: SHOULD

**Summary**: Use truthiness checks (`if (x)`) only when all falsy values should be excluded. Use explicit checks when `0`, `""`, or `false` are valid.

```js
// Good — truthiness is appropriate (we want to exclude null, undefined, "")
if (errorMessage) {
  displayError(errorMessage);
}

// Bad — truthiness discards valid values
function setCount(count) {
  if (!count) {               // fails when count is 0!
    count = 10;
  }
}

// Good — explicit nullish check preserves 0
function setCount(count) {
  count = count ?? 10;
}

// Good — explicit check for property existence
if (!("path" in fileDesc)) {
  throw new Error("Missing property: .path");
}
```

**The 7 falsy values** (Exploring JS Ch. 16; JS Definitive Guide, §3.4):
`false`, `0`, `-0`, `0n`, `NaN`, `""`, `null`, `undefined`

**Everything else is truthy**, including: `[]`, `{}`, `"0"`, `"false"`, `new Boolean(false)`.

**Rationale**: Truthiness checks are concise but imprecise. When `0`, `""`, or `false` are valid domain values, a truthiness check silently discards them. Use `?? ` or explicit `=== undefined` / `=== null` checks instead.

---

## ID-23: Use `structuredClone()` for Deep Copies

**Strength**: SHOULD

**Summary**: Use `structuredClone()` for deep copies. Use spread for shallow copies.

```js
// Good — shallow copy
const copy = { ...original };
const arrCopy = [...original];

// Good — deep copy
const deep = structuredClone(original);

// Bad — JSON round-trip (loses Date, undefined, functions, etc.)
const deep = JSON.parse(JSON.stringify(original)); // fragile
```

**Shallow vs. deep** (Deep JS Ch. 7-8):

```js
// Shallow copy — nested objects are shared
const original = { work: { employer: "Acme" } };
const shallow = { ...original };
shallow.work.employer = "Evil"; // also changes original.work.employer!

// Deep copy — fully independent
const deep = structuredClone(original);
deep.work.employer = "Evil"; // original is unchanged
```

**Rationale**: `structuredClone()` handles circular references, `Date`, `RegExp`, `Map`, `Set`, `ArrayBuffer`, and more. The JSON hack fails silently on non-serializable values. Spread is fast and correct for flat structures (Deep JS Ch. 7; JS Definitive Guide, §6.7).

---

## ID-24: Avoid Shared Mutable State

**Strength**: SHOULD

**Summary**: When data is shared across functions or modules, prevent unintended mutation through defensive copying, non-destructive updates, or `Object.freeze()`.

```js
// Bad — function destroys the caller's array
function logAll(arr) {
  while (arr.length > 0) {
    console.log(arr.shift()); // mutates arr!
  }
}

// Good — defensive copy at the boundary
function logAll(arr) {
  for (const item of [...arr]) {
    console.log(item);
  }
}

// Good — non-destructive update (original unchanged)
const original = { city: "Berlin", country: "Germany" };
const updated = { ...original, city: "Munich" };

// Good — protect output from external mutation
class Store {
  #items = [];
  getItems() {
    return [...this.#items]; // defensive copy
  }
}
```

**Three strategies** (Deep JS Ch. 6-10):
1. **Defensive copying** — copy at boundaries so each party operates independently
2. **Non-destructive updates** — never mutate; create modified copies instead
3. **Immutability** — `Object.freeze()` makes mutation structurally impossible

**Rationale**: Shared mutable state is the root of many bugs, even in single-threaded JavaScript. When one function mutates data that another function relies on, behavior becomes unpredictable. This applies to synchronous code, not just async.

---

## ID-25: Prefer `for-of` over `.forEach()`

**Strength**: SHOULD

**Summary**: Use `for-of` for iteration. Reserve `.forEach()` only when its specific sparse-array behavior is needed.

```js
// Good — for-of: supports break, continue, await, return
for (const item of items) {
  if (item.skip) continue;
  if (item.done) break;
  process(item);
}

// Good — for-of with index via .entries()
for (const [i, item] of items.entries()) {
  console.log(`${i}: ${item}`);
}

// Bad — forEach: no break, no continue, no await, no return-from-function
items.forEach((item) => {
  if (item.done) return; // only exits the callback, not the enclosing function
  process(item);
});

// Bad — forEach with async (fires all callbacks concurrently, does not await)
items.forEach(async (item) => {
  await process(item); // does NOT execute sequentially
});

// Good — for-of with async (sequential execution)
for (const item of items) {
  await process(item);
}
```

**When `.forEach()` is acceptable**: When iterating a sparse array and you want nonexistent elements silently skipped (`.forEach()` skips gaps; `for-of` yields `undefined` for them).

**Rationale**: `for-of` is a statement, not a method call — it supports `break`, `continue`, `return`, `await`, and labeled loops. `.forEach()` cannot be terminated early (`break` is a syntax error, `return` only exits the callback), does not support `await` correctly, and adds a function scope that obscures control flow. Flanagan: "forEach() does not provide a way to terminate iteration before all elements have been passed to the function" (JS Definitive Guide, §7.8.1). Rauschmayer recommends `for-of` as the primary iteration construct (Exploring JS Ch. 34).

---

## ID-26: Prefer Early Returns to Reduce Nesting

**Strength**: SHOULD

**Summary**: Use guard clauses with early `return`, `throw`, or `continue` to handle edge cases at the top, keeping the main logic at a low nesting level.

```js
// Good — guard clauses, flat main logic
function processUser(user) {
  if (!user) throw new Error("user is required");
  if (!user.active) return null;
  if (!user.email) return null;

  const normalized = user.email.toLowerCase();
  return sendWelcome(normalized);
}

// Bad — deeply nested conditionals
function processUser(user) {
  if (user) {
    if (user.active) {
      if (user.email) {
        const normalized = user.email.toLowerCase();
        return sendWelcome(normalized);
      }
    }
  }
  return null;
}

// Good — continue as guard in loops
for (const item of items) {
  if (!item.valid) continue;
  if (item.processed) continue;

  processItem(item);
}

// Bad — nested conditions in loop body
for (const item of items) {
  if (item.valid) {
    if (!item.processed) {
      processItem(item);
    }
  }
}
```

**Rationale**: Each level of nesting increases cognitive load. Guard clauses invert conditions and exit early, leaving the "happy path" at the top level of indentation. This makes functions easier to scan — the preconditions are listed at the top, and the main logic reads linearly without rightward drift. Haverbeke emphasizes that "control flow functions as 'guard' for the code that comes after them" (Eloquent JS Ch. 1, 8). Flanagan's coverage of `break`, `continue`, and `return` supports using them for early exit (JS Definitive Guide, §5.5).

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `const` default, `let` when needed, never `var` | MUST | `var` is function-scoped, hoists, creates global properties |
| 02 | Always `===` and `!==` | MUST | `==` applies multi-step type coercion cascade |
| 03 | `??` for nullish defaults | SHOULD | `||` discards `0`, `""`, `false` |
| 04 | Optional chaining `?.` | SHOULD | Three forms: `.prop`, `[expr]`, `(args)` |
| 05 | Template literals | SHOULD | Readable interpolation, multiline support |
| 06 | Destructure at point of use | SHOULD | Named params, defaults, self-documenting signatures |
| 07 | Named exports | SHOULD | Tree-shakeable, refactor-safe, IDE-friendly |
| 08 | ESM only | MUST | No `require()`, no CommonJS |
| 09 | Arrow for callbacks, `function` for declarations | SHOULD | Arrow inherits `this`; declarations hoist |
| 10 | Avoid `this` outside classes/methods | SHOULD | `this` is `undefined` in strict/ESM standalone functions |
| 11 | Document magic values | MUST | Named constants are searchable and changeable |
| 12 | camelCase / PascalCase / UPPER_CASE | MUST | PascalCase signals constructors/classes only |
| 13 | Avoid weasel words | MUST | "Manager", "Service", "Handler" say nothing |
| 14 | `const` does not mean immutable | MUST | Binding is frozen, value is not |
| 15 | `Object.freeze()` for constant objects | CONSIDER | Shallow only — freeze recursively for deep |
| 16 | `Map`/`Set` over plain objects | SHOULD | Any key type, no prototype pollution, `.size` |
| 17 | Rest parameters, not `arguments` | MUST | Real Array, visible in signature, works in arrows |
| 18 | Spread instead of `apply()` | SHOULD | Works with any iterable, no `this` argument |
| 19 | Explicit returns in arrows | SHOULD | Object literal return needs `()` — common gotcha |
| 20 | Deno APIs, not Node.js | MUST | Web Platform APIs, explicit permissions, built-in tools |
| 21 | `const` in `for-of`/`for-in` loops | SHOULD | Fresh binding each iteration; `let` for counters |
| 22 | Careful truthiness checks | SHOULD | `0`, `""`, `false` are falsy but often valid |
| 23 | `structuredClone()` for deep copies | SHOULD | Handles circular refs, Date, Map, Set |
| 24 | Avoid shared mutable state | SHOULD | Defensive copy, non-destructive update, or freeze |
| 25 | `for-of` over `.forEach()` | SHOULD | `for-of` supports `break`, `continue`, `await`, `return` |
| 26 | Early returns to reduce nesting | SHOULD | Guard clauses keep the happy path flat and scannable |

---

## Related Guidelines

- **Error Handling**: See `03-error-handling.md` for `try`/`catch`, custom errors, and validation (ID-23, ID-24 reference this guide's boundary patterns)
- **Values & References**: See `04-values-references.md` for mutation discipline, copying, and immutability (ID-04, ID-06, ID-09 extend ID-14, ID-15, ID-23 here)
- **Type Discipline**: See `05-type-discipline.md` for runtime type checks and JSDoc (ID-22 extends ID-03, ID-04 here)
- **Functions & Closures**: See `06-functions-closures.md` for closures, `this` binding, and higher-order functions (ID-02, ID-03 extend ID-09 here)
- **Async & Concurrency**: See `07-async-concurrency.md` for Promises, `async`/`await`, and concurrency
- **Anti-Patterns**: See `09-anti-patterns.md` for ID-01, 03, 11, 28, 29, 33 (amplify patterns from this guide)
- **Deno**: See `12-deno/01-runtime-basics.md` for Deno permissions, APIs, and configuration
- **No-Node Boundary**: See `14-no-node-boundary.md` for what "no Node.js" means in practice

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [Biome Documentation](https://biomejs.dev/)
- [MDN Web Docs — JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
