# Type Discipline (without TypeScript)

Discipline for writing type-safe JavaScript without TypeScript. Covers runtime type checking, explicit conversion, coercion traps, number edge cases, JSDoc annotations, null/undefined discipline, discriminated unions, and typed collections. Plain JS with discipline, JSDoc, and runtime validation is a legitimate engineering choice — grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript**, JSDoc for tooling support.

---

## ID-01: Use `typeof` Correctly — Know Its Quirks

**Strength**: MUST

**Summary**: `typeof` works for primitives and functions but fails for `null`, arrays, and object subtypes.

```js
typeof "hello"     // "string"
typeof 42          // "number"
typeof 42n         // "bigint"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof Symbol()    // "symbol"
typeof (() => {})  // "function"

// The quirks:
typeof null        // "object"  — historical bug, null is a primitive
typeof []          // "object"  — arrays are objects
typeof {}          // "object"  — can't distinguish from null or arrays
typeof /regex/     // "object"  — regexps are objects

// Correct checks for the quirky cases:
value === null                          // null check
Array.isArray(value)                    // array check
value !== null && typeof value === "object"  // true object check
```

**Rule of thumb**: `typeof` for primitives; `instanceof` or specific checks for objects (Exploring JS Ch. 13; JS Definitive Guide, §4.13.3).

---

## ID-02: Use `Array.isArray()`, Not `typeof` or `instanceof`

**Strength**: MUST

**Summary**: `Array.isArray()` is the only reliable array check. It works across realms.

```js
// Good — cross-realm safe, specification-endorsed
Array.isArray([1, 2, 3]);   // true
Array.isArray("string");     // false
Array.isArray({ length: 3 }); // false — array-like is not an array

// Bad — typeof cannot distinguish arrays from objects
typeof [];  // "object"

// Bad — fails across iframes, workers, vm contexts
[] instanceof Array;  // true in same realm, false across realms
```

**Rationale**: `typeof` returns `"object"` for arrays. `instanceof` uses the current realm's `Array.prototype`, which differs across iframes and workers. `Array.isArray()` is the spec's answer to both problems (Exploring JS Ch. 34; JS Definitive Guide, §7.8.8).

---

## ID-03: Use `instanceof` for Class Hierarchies, Not for Primitives

**Strength**: SHOULD

**Summary**: `instanceof` walks the prototype chain. It returns `false` for primitives and fails across realms.

```js
// Good — class hierarchy check
class HttpError extends Error { /* ... */ }
const err = new HttpError("Not found");
err instanceof HttpError;  // true
err instanceof Error;      // true — prototype chain

// Bad — primitives always return false
"hello" instanceof String;  // false
42 instanceof Number;        // false

// Bad — cross-realm failure
// iframeArray instanceof Array → false (different Array.prototype)
```

**Rationale**: `instanceof` checks whether `Constructor.prototype` appears in the object's prototype chain. It is the right tool for class-based type identity but must never be used for primitives or cross-realm checks (Exploring JS Ch. 13; JS Definitive Guide, §4.9.4).

---

## ID-04: Use `Number.isFinite()`, `Number.isNaN()`, `Number.isInteger()` — Never the Global Versions

**Strength**: MUST

**Summary**: The `Number.*` methods do not coerce their arguments. The global versions coerce first, producing wrong results.

```js
// Good — no coercion
Number.isNaN(NaN);        // true
Number.isNaN("abc");      // false — string is not NaN
Number.isFinite(42);      // true
Number.isFinite("42");    // false — string is not a number
Number.isInteger(5.0);    // true
Number.isInteger(5.1);    // false

// Bad — global versions coerce first
isNaN("abc");             // true — "abc" becomes NaN, then isNaN checks
isFinite("42");           // true — "42" becomes 42, then isFinite checks
```

**Rationale**: The global `isNaN()` and `isFinite()` convert their argument to a number first, making them unreliable type guards. `Number.isNaN()` returns `true` only for the actual `NaN` value. `Number.isFinite()` returns `true` only for finite numbers (Exploring JS Ch. 18; JS Definitive Guide, §3.2.3).

---

## ID-05: Use `Object.hasOwn()` Instead of `hasOwnProperty()`

**Strength**: SHOULD

**Summary**: `Object.hasOwn()` (ES2022) is a static method that works on all objects, including those with `null` prototypes.

```js
// Good — works on all objects
const config = Object.create(null);
config.timeout = 5000;
Object.hasOwn(config, "timeout");  // true

// Bad — fails on null-prototype objects
config.hasOwnProperty("timeout");  // TypeError: not a function

// Bad — can be spoofed
const sketchy = { hasOwnProperty: () => true };
sketchy.hasOwnProperty("anything");  // true — spoofed
Object.hasOwn(sketchy, "anything");  // false — reliable
```

**Rationale**: `Object.hasOwn()` cannot be overridden or absent. It replaces `obj.hasOwnProperty()`, which is an instance method that fails on `Object.create(null)` objects and can be shadowed (Exploring JS Ch. 30; Deep JS Ch. 12).

**See also**: `04-values-references.md` ID-27

---

## ID-06: Duck Typing — Check Properties, Not Constructor Identity

**Strength**: SHOULD

**Summary**: Test for the capabilities an object needs to have, not the class that produced it.

```js
// Good — duck typing: check for the method you need
function processIterable(value) {
  if (typeof value?.[Symbol.iterator] === "function") {
    for (const item of value) { /* ... */ }
  }
}

// Good — check for specific properties
function formatAddress(obj) {
  if (!("street" in obj) || !("city" in obj)) {
    throw new TypeError("Expected an address with street and city");
  }
  return `${obj.street}, ${obj.city}`;
}

// Bad — too rigid; breaks with cross-realm objects or different implementations
function processIterable(value) {
  if (value instanceof Array) { /* misses Sets, Maps, generators, custom iterables */ }
}
```

**Rationale**: JavaScript is structurally typed at runtime. Checking for properties or methods (`"method" in obj`, `typeof obj.method === "function"`) is more flexible and resilient than checking constructor identity, which breaks across realms and tightly couples to implementation (Exploring JS Ch. 30; Deep JS Ch. 12).

---

## ID-07: Use `Number()`, `String()`, `Boolean()` for Explicit Conversion

**Strength**: SHOULD

**Summary**: Call these as functions (without `new`) for explicit type conversion. Never use `new` — it creates wrapper objects.

```js
// Good — explicit conversion, returns primitives
Number("42");     // 42
String(42);       // "42"
Boolean(0);       // false

// Bad — new creates wrapper objects, not primitives
new Number(42);            // object, not number
typeof new Number(42);     // "object"
new Number(42) === 42;     // false
new Boolean(false);        // truthy! (it's an object)
if (new Boolean(false)) {  // executes — objects are always truthy
  console.log("this runs");
}
```

**Rationale**: `Number()`, `String()`, `Boolean()` without `new` are the spec's explicit conversion functions. With `new`, they create wrapper objects whose `typeof` is `"object"`, whose identity comparison fails, and — critically — `new Boolean(false)` is truthy because all objects are truthy (Exploring JS Ch. 13, 18; JS Definitive Guide, §3.9.2).

---

## ID-08: Use `parseInt(s, 10)` / `parseFloat(s)` for Parsing Semantics

**Strength**: SHOULD

**Summary**: `parseInt` parses from the start of a string, stopping at the first invalid character. Always pass radix `10`. Use `Number()` when the entire string must be numeric.

```js
// Good — explicit radix
parseInt("42px", 10);   // 42 — stops at "p", useful for CSS values
parseInt("FF", 16);     // 255 — hex parsing
parseFloat("3.14em");   // 3.14 — stops at "e" (not exponent here)

// Bad — no radix, behavior varies
parseInt("010");        // may be 8 (octal) in some engines

// When the FULL string must be numeric, use Number():
Number("42px");         // NaN — rejects partial match (correct for validation)
Number("42");           // 42
```

**Rationale**: `parseInt` without a radix can produce octal results for strings with leading zeros. Always pass `10` for decimal parsing. For strict validation where trailing characters should be rejected, `Number()` is the correct choice (Exploring JS Ch. 18; JS Definitive Guide, §3.9.2).

---

## ID-09: Avoid Implicit Coercion — No `+x` for Numbers, No `"" + x` for Strings

**Strength**: SHOULD

**Summary**: Use explicit conversion functions. Implicit coercion obscures intent and has edge cases.

```js
// Good — explicit, readable
const n = Number(userInput);
const s = String(count);
const b = Boolean(value);

// Bad — implicit, obscure
const n = +userInput;           // unary + triggers ToNumber
const s = "" + count;           // addition triggers ToString (throws for Symbol)
const s2 = `${symbolValue}`;   // also throws for Symbol
const i = value | 0;           // bitwise coerces to 32-bit int; truncates large numbers
```

| Implicit (avoid) | Explicit (prefer) | Trap |
|-------------------|-------------------|------|
| `+x` | `Number(x)` | Cryptic; `+undefined` → `NaN` silently |
| `"" + x` | `String(x)` | Throws `TypeError` for Symbol |
| `` `${x}` `` | `String(x)` | Also throws for Symbol |
| `!!x` | `Boolean(x)` | Works fine but less self-documenting |
| `x \| 0` | `Math.trunc(x)` | Truncates to 32-bit int; destroys large numbers |

**Rationale**: Explicit conversion makes intent visible in code review. Implicit coercion relies on operator behavior that differs by type and is a frequent source of subtle bugs. `String()` is the only safe way to convert Symbols to strings (Exploring JS Ch. 16; Deep JS Ch. 14).

---

## ID-10: Understand the `+` Operator's Dual Nature

**Strength**: MUST

**Summary**: `+` adds numbers OR concatenates strings, depending on operand types after coercion. String wins.

```js
// If either operand is (or coerces to) a string → concatenation
"1" + 2;            // "12"
1 + "2";            // "12"
1 + 2 + "3";        // "33" — left-to-right: 1+2=3, then 3+"3"="33"
"1" + 2 + 3;        // "123" — "1"+2="12", "12"+3="123"

// Otherwise → numeric addition
true + true;         // 2 — both coerce to 1
2 + null;            // 2 — null coerces to 0
2 + undefined;       // NaN — undefined coerces to NaN
[] + [];             // "" — both arrays coerce to "" via toString()
1 + {};              // "1[object Object]"

// Good — explicit about intent
const sum = Number(a) + Number(b);     // arithmetic
const label = `Count: ${count}`;       // string building
```

**Rationale**: The `+` operator applies `ToPrimitive()` to both operands, then checks if either result is a string. If so, both are converted to strings and concatenated; otherwise, both are converted to numbers and added. This dual nature is the single largest source of type coercion bugs in JavaScript (Exploring JS Ch. 16; Deep JS Ch. 14; JS Definitive Guide, §4.8.1).

---

## ID-11: `NaN` Is Not Equal to Itself — Always Use `Number.isNaN()`

**Strength**: MUST

**Summary**: `NaN === NaN` is `false`. Use `Number.isNaN()` to detect it.

```js
// Bad — always false
NaN === NaN;         // false
x === NaN;           // always false, regardless of x

// Bad — global isNaN coerces first
isNaN("abc");        // true — "abc" becomes NaN, then checked

// Good — precise NaN detection
Number.isNaN(NaN);   // true
Number.isNaN("abc"); // false — no coercion

// Array pitfall:
[1, NaN, 3].indexOf(NaN);    // -1 — indexOf uses ===
[1, NaN, 3].includes(NaN);   // true — includes uses SameValueZero
[1, NaN, 3].findIndex((x) => Number.isNaN(x)); // 1
```

**Rationale**: `NaN` is the only JavaScript value not equal to itself. This is an IEEE 754 property, not a bug, but it means `===` can never detect `NaN`. `Number.isNaN()` is the only reliable check (Exploring JS Ch. 18; JS Definitive Guide, §3.2.3).

---

## ID-12: `-0` Exists and `=== 0` — Use `Object.is()` When It Matters

**Strength**: CONSIDER

**Summary**: JavaScript has both `+0` and `-0`. Strict equality cannot distinguish them.

```js
0 === -0;            // true — === treats them as equal
Object.is(0, -0);   // false — the only reliable check

-0 .toString();      // "0" — sign lost in string conversion
JSON.stringify(-0);  // "0"

// When it matters: direction, signed infinity
1 / 0;               // Infinity
1 / -0;              // -Infinity

// Good — use Object.is() when the sign of zero carries meaning
if (Object.is(velocity, -0)) {
  direction = "backward";
}
```

**Rationale**: `-0` exists because IEEE 754 requires a sign bit on all floats, including zero. In most code, the distinction is irrelevant. In physics simulations, direction tracking, or any domain where the sign of zero carries meaning, `Object.is()` is required (Exploring JS Ch. 18; JS Definitive Guide, §3.2.3).

---

## ID-13: Floating-Point Precision — `0.1 + 0.2 !== 0.3`

**Strength**: MUST

**Summary**: JavaScript numbers are IEEE 754 doubles. Most decimal fractions cannot be represented exactly.

```js
// The classic
0.1 + 0.2 === 0.3;   // false — result is 0.30000000000000004
1.3 * 3 === 3.9;      // false — result is 3.9000000000000004

// Good — epsilon tolerance for near-equality
function nearlyEqual(a, b) {
  return Math.abs(a - b) < Number.EPSILON;
}
nearlyEqual(0.1 + 0.2, 0.3); // true

// Good — integer arithmetic for money (store cents, not dollars)
const priceInCents = 199;     // $1.99
const taxInCents = 15;        // $0.15
const totalInCents = priceInCents + taxInCents; // 214 — exact

// Bad — floating-point for money
const price = 1.99;
const tax = 0.15;
const total = price + tax; // 2.1400000000000001
```

**Rationale**: Base-2 cannot exactly represent fractions whose denominator has a prime factor of 5 (like 1/10). This is inherent to IEEE 754, not a JavaScript bug — Java, Python, and C++ have the same issue. For currency, use integer arithmetic (cents) or a decimal library (Exploring JS Ch. 18; JS Definitive Guide, §3.2.4).

---

## ID-14: `BigInt` Cannot Be Mixed with `Number` in Operations

**Strength**: MUST

**Summary**: Arithmetic operators throw `TypeError` when mixing `BigInt` and `Number`. Convert explicitly.

```js
// Bad — throws TypeError
2n + 1;              // TypeError: Cannot mix BigInt and other types
2n * 3;              // TypeError
+2n;                 // TypeError: unary + not supported for BigInt

// Good — explicit conversion
2n + BigInt(1);      // 3n
Number(2n) + 1;      // 3 (beware: precision loss if value > 2^53)

// Comparison operators DO work across types
2n > 1;              // true
2n === 2;            // false (different types)
2n == 2;             // true (loose equality coerces)
```

**When to use BigInt**: Integers beyond the 53-bit safe range — 64-bit database IDs, cryptographic values, financial amounts in smallest units. Do not use BigInt "for safety" when 53 bits suffice — regular numbers are more efficient and broadly supported (Exploring JS Ch. 20; JS Definitive Guide, §3.2.5).

---

## ID-15: Safe Integers — Know the Limits

**Strength**: MUST

**Summary**: JavaScript numbers can only represent integers exactly up to `2^53 - 1`. Beyond that, distinct values collide.

```js
Number.MAX_SAFE_INTEGER;          // 9007199254740991 (2^53 - 1)
Number.isSafeInteger(2 ** 53);    // false
2 ** 53 + 1 === 2 ** 53;          // true — precision lost!

// Good — validate before arithmetic
function safeAdd(a, b) {
  if (!Number.isSafeInteger(a) || !Number.isSafeInteger(b)) {
    throw new RangeError("Operands must be safe integers");
  }
  const result = a + b;
  if (!Number.isSafeInteger(result)) {
    throw new RangeError("Result exceeds safe integer range");
  }
  return result;
}

// Good — use BigInt for large values
const largeId = 9007199254740993n; // exact as BigInt
```

**Rationale**: `Number.isSafeInteger()` checks both integer-ness and range. A computation `a op b` is correct only when all three — `a`, `b`, and the result — are safe integers. Contexts: large database IDs, timestamps in microseconds, Twitter/X post IDs (Exploring JS Ch. 18).

---

## ID-16: Annotate Function Parameters and Return Types with JSDoc

**Strength**: SHOULD

**Summary**: JSDoc annotations give Deno's LSP, VS Code, and other editors type information without TypeScript.

```js
/**
 * Parse a port number from a string.
 * @param {string} input - The string to parse
 * @returns {number} The parsed port number
 * @throws {RangeError} If the port is invalid
 */
export function parsePort(input) {
  const port = Number(input);
  if (!Number.isFinite(port) || port < 0 || port > 65535) {
    throw new RangeError(`Invalid port: ${input}`);
  }
  return port;
}

/**
 * Fetch a resource with options.
 * @param {string} url
 * @param {{ method?: string, headers?: Record<string, string>, timeout?: number }} [options]
 * @returns {Promise<Response>}
 */
export async function fetchResource(url, options = {}) {
  /* ... */
}
```

**Rationale**: JSDoc `@param` and `@returns` annotations are read by Deno's built-in language server (based on `tsc`), providing autocomplete, hover documentation, and inline type errors in VS Code. Enable `// @ts-check` at the top of a file or `"checkJs": true` in `deno.json` for full type checking (Exploring JS Ch. 9; Deno docs).

---

## ID-17: Use `@typedef` for Complex Object Shapes

**Strength**: SHOULD

**Summary**: Define reusable types for object shapes with `@typedef`. Reference them across the codebase.

```js
/**
 * @typedef {object} ServerConfig
 * @property {string} host
 * @property {number} port
 * @property {boolean} [tls] - Optional, defaults to false
 * @property {string[]} [allowedOrigins] - Optional
 */

/**
 * @param {ServerConfig} config
 * @returns {void}
 */
export function startServer(config) {
  const { host, port, tls = false } = config;
  /* ... */
}

/**
 * @typedef {{ status: "ok", data: unknown } | { status: "error", message: string }} ApiResult
 */

/** @type {ApiResult} */
const result = { status: "ok", data: [1, 2, 3] };
```

**Rationale**: `@typedef` defines a named type that Deno's LSP resolves for autocomplete, hover info, and type checking. It is the JSDoc equivalent of a TypeScript `type` or `interface`, keeping type definitions co-located with the code that uses them.

---

## ID-18: Use `@enum` for String/Number Constant Sets

**Strength**: CONSIDER

**Summary**: `@enum` documents a frozen set of constants and gives the LSP a closed type.

```js
/**
 * @enum {string}
 */
export const LogLevel = Object.freeze({
  DEBUG: "debug",
  INFO: "info",
  WARN: "warn",
  ERROR: "error",
});

/**
 * @param {string} message
 * @param {LogLevel} level
 */
export function log(message, level = LogLevel.INFO) {
  /* ... */
}

log("Server started", LogLevel.DEBUG);
```

**Rationale**: `@enum` combined with `Object.freeze()` gives you a closed set of constants with editor autocomplete and type checking — the JSDoc equivalent of a TypeScript `enum` or string union. The LSP knows the valid values and flags incorrect ones.

**See also**: `04-values-references.md` ID-19

---

## ID-19: Use `@template` for Generic Patterns

**Strength**: CONSIDER

**Summary**: `@template` adds type parameters to functions and classes without TypeScript.

```js
/**
 * @template T
 * @param {T[]} arr
 * @param {(item: T) => boolean} predicate
 * @returns {T | undefined}
 */
export function find(arr, predicate) {
  for (const item of arr) {
    if (predicate(item)) return item;
  }
  return undefined;
}

/**
 * @template K, V
 * @param {Map<K, V>} map
 * @param {V} defaultValue
 * @returns {(key: K) => V}
 */
export function mapGetOrDefault(map, defaultValue) {
  return (key) => map.get(key) ?? defaultValue;
}
```

**Rationale**: `@template` lets you express generic relationships (the return type depends on the input type) without TypeScript. Deno's LSP resolves these at call sites, providing accurate autocomplete for the inferred type.

---

## ID-20: JSDoc Works with Deno's Language Server — Leverage It

**Strength**: SHOULD

**Summary**: Deno's LSP reads JSDoc annotations and provides type checking, autocomplete, and error diagnostics for plain JS files.

```js
// Enable type checking for a single file:
// @ts-check

// Or enable globally in deno.json:
// { "compilerOptions": { "checkJs": true } }

// Wire declaration files for JS imports:
// @ts-types="./my-lib.d.ts"
import { something } from "./my-lib.js";

// Wire external type declarations:
// @ts-types="npm:@types/lodash"
import _ from "npm:lodash";
```

**Key integration points**:
- `deno check *.js` — type-check JS files with JSDoc annotations (use in CI)
- `deno run --check script.js` — type-check before executing
- `// @ts-check` pragma — opt-in per file
- `// @ts-types="..."` — wire `.d.ts` files to JS imports
- `// @ts-self-types="..."` — wire `.d.ts` to the file that declares it

**Rationale**: Deno's language server is `tsc` under the hood. It reads JSDoc annotations the same way it reads TypeScript types. Combined with `@ts-check`, you get most of TypeScript's static analysis for plain JS files (Deno docs).

---

## ID-21: Distinguish "Not Provided" (`undefined`) from "Explicitly Empty" (`null`)

**Strength**: SHOULD

**Summary**: Use `undefined` for system-level absence (missing parameters, uninitialized). Use `null` for programmer-intentional absence.

```js
// undefined — system-level: not provided, not initialized
let x;                      // undefined (language-assigned)
function f(a) { return a; }
f();                        // undefined (missing parameter)
const obj = {};
obj.missing;                // undefined (missing property)

// null — program-level: intentionally empty
const config = {
  theme: "dark",
  customHeader: null,       // explicitly "no custom header"
};

// JSON behavior differs:
JSON.stringify({ a: undefined, b: null });
// '{"b":null}' — undefined dropped, null preserved
```

**Rationale**: This distinction matters for serialization (JSON drops `undefined`), API design (return `undefined` for "not found," `null` for "explicitly cleared"), and default parameters (defaults trigger on `undefined`, not `null`). Both sources agree on this convention (Exploring JS Ch. 16; JS Definitive Guide, §3.5).

**See also**: `02-api-design.md` ID-23, ID-24

---

## ID-22: Use `??` and `?.` — They Understand the Null/Undefined Distinction

**Strength**: MUST

**Summary**: `??` defaults only on `null`/`undefined`. `?.` short-circuits only on `null`/`undefined`. Both preserve `0`, `""`, and `false`.

```js
// Good — ?? preserves valid falsy values
const timeout = options.timeout ?? 5000;   // 0 is preserved
const name = options.name ?? "Anonymous";  // "" is preserved

// Bad — || discards valid falsy values
const timeout = options.timeout || 5000;   // 0 becomes 5000!

// Good — ?. chains safely
const zip = user?.address?.zipCode ?? "N/A";

// Good — conditional method call
callback?.();
```

**Rationale**: `??` and `?.` are the null/undefined-aware operators. They solve the long-standing problem of `||` treating `0`, `""`, and `false` as missing values. Use them consistently for defaults and safe access (Exploring JS Ch. 14; JS Definitive Guide, §4.13.2).

**See also**: `01-core-idioms.md` ID-03, ID-04

---

## ID-23: Don't Check `typeof x === "undefined"` in Modern Code

**Strength**: SHOULD

**Summary**: Use `x === undefined` directly. The `typeof` guard is a legacy pattern from when `undefined` was reassignable.

```js
// Good — direct and modern
if (x === undefined) { /* not provided */ }
if (x === null) { /* explicitly empty */ }
if (x == null) { /* either null or undefined */ }

// Obsolete — unnecessary guard
if (typeof x === "undefined") { /* ... */ }

// Still valid — checking for undeclared globals in feature detection
if (typeof globalThis.Deno !== "undefined") { /* running in Deno */ }
```

**Rationale**: In modern JavaScript, `undefined` is non-writable and non-configurable. The `typeof` guard was needed in ES3 when `undefined` could be reassigned. The only remaining use is checking for variables that may not be declared at all (Exploring JS Ch. 16).

---

## ID-24: Use a `type` or `kind` Property to Discriminate Object Variants

**Strength**: SHOULD

**Summary**: When a function handles multiple object shapes, add a discriminant property and dispatch with `switch`.

```js
/**
 * @typedef {{ kind: "circle", radius: number }} Circle
 * @typedef {{ kind: "rect", width: number, height: number }} Rect
 * @typedef {{ kind: "triangle", base: number, height: number }} Triangle
 * @typedef {Circle | Rect | Triangle} Shape
 */

/**
 * @param {Shape} shape
 * @returns {number}
 */
function area(shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "rect":
      return shape.width * shape.height;
    case "triangle":
      return (shape.base * shape.height) / 2;
    default:
      throw new Error(`Unknown shape: ${shape.kind}`);
  }
}
```

**For collision-proof variants**, use Symbols as discriminants:

```js
const CIRCLE = Symbol("circle");
const RECT = Symbol("rect");

function area(shape) {
  switch (shape.kind) {
    case CIRCLE: return Math.PI * shape.radius ** 2;
    case RECT:   return shape.width * shape.height;
    default:     throw new Error(`Unknown shape: ${String(shape.kind)}`);
  }
}
```

**Rationale**: Discriminated unions are the closest plain JS gets to Rust enums or algebraic data types. A `kind`/`type` property plus `switch` gives exhaustive dispatch, clear control flow, and plays well with JSDoc union types. Biome's `useExhaustiveSwitchCases` rule can enforce completeness (Exploring JS Ch. 30, 32).

---

## ID-25: Use `switch` on the Discriminant for Exhaustive Handling

**Strength**: SHOULD

**Summary**: Always include a `default` case that throws for unexpected variants.

```js
/**
 * @param {{ status: "pending" | "fulfilled" | "rejected", value?: unknown, reason?: Error }} result
 */
function handleResult(result) {
  switch (result.status) {
    case "pending":
      return showSpinner();
    case "fulfilled":
      return showData(result.value);
    case "rejected":
      return showError(result.reason);
    default:
      // Catches typos and future variants added without updating this switch
      throw new Error(`Unhandled status: ${result.status}`);
  }
}
```

**Rationale**: Without a `default` that throws, new variants added to the union silently fall through with no behavior. The throwing `default` acts as an exhaustiveness check — it catches both programmer typos and missing cases at runtime (Exploring JS Ch. 26; Biome `useExhaustiveSwitchCases`).

---

## ID-26: Use `Map<K,V>` and `Set<T>` for Homogeneous Collections

**Strength**: SHOULD

**Summary**: Use `Map` and `Set` for collections with consistent key/value types. Reserve plain objects for fixed-shape records.

```js
// Good — Map for dynamic key-value collections
/** @type {Map<string, number>} */
const wordCounts = new Map();
wordCounts.set("hello", 1);
wordCounts.set("world", 2);

// Good — Set for unique values
/** @type {Set<string>} */
const visited = new Set();
visited.add("/home");
visited.add("/about");

// Bad — plain object as dynamic collection
const wordCounts = {};          // keys coerced to strings
wordCounts[42] = "surprise";    // key becomes "42"
```

**Map advantages**: Any key type (including objects), `.size` property, insertion-order iteration, no prototype pollution, SameValueZero equality (finds `NaN`).

**Rationale**: Plain objects coerce all keys to strings, inherit from `Object.prototype` (risking key collisions like `"constructor"`), and have no `.size`. Map and Set are purpose-built for collection semantics (Exploring JS Ch. 33; JS Definitive Guide, §11.1).

**See also**: `01-core-idioms.md` ID-16

---

## ID-27: Use TypedArray When You Need Fixed Element Types

**Strength**: CONSIDER

**Summary**: For binary data and numeric-heavy computation, TypedArrays enforce element type and are significantly faster.

```js
// Good — fixed-type, zero-initialized, memory-efficient
const pixels = new Uint8ClampedArray(width * height * 4); // RGBA
const audioSamples = new Float32Array(sampleRate * duration);

// TypedArray enforces type at assignment:
const u8 = new Uint8Array(3);
u8[0] = 257;    // wraps: becomes 1 (modular arithmetic)
const clamped = new Uint8ClampedArray(3);
clamped[0] = 257; // clamps: becomes 255

// Bad — normal Array for binary work (no type enforcement, more memory)
const pixels = new Array(width * height * 4);
```

**12 element types**: `Int8`, `Uint8`, `Uint8Clamped`, `Int16`, `Uint16`, `Int32`, `Uint32`, `BigInt64`, `BigUint64`, `Float16`, `Float32`, `Float64`.

**Key differences from Array**: Fixed length (no `.push()`), backed by `ArrayBuffer`, zero-initialized (not holes), `Array.isArray()` returns `false`, silent coercion on assignment.

**Rationale**: TypedArrays are essential for WebGL, WebAssembly, audio processing, and network protocols. They are ~4x faster and ~8x more memory-efficient than regular Arrays for numeric data (Exploring JS Ch. 36; JS Definitive Guide, §11.2).

---

## ID-28: Avoid Heterogeneous Arrays — Keep Element Types Consistent

**Strength**: SHOULD

**Summary**: Arrays should contain elements of a single type. Mixed-type arrays force type checking on every access.

```js
// Good — homogeneous arrays
/** @type {string[]} */
const names = ["Alice", "Bob", "Carol"];

/** @type {number[]} */
const scores = [95, 87, 92];

/** @type {Array<{ name: string, score: number }>} */
const results = [
  { name: "Alice", score: 95 },
  { name: "Bob", score: 87 },
];

// Bad — heterogeneous array forces runtime checks
const mixed = ["Alice", 95, true, null]; // what is mixed[1]? number? string?
```

**Rationale**: Homogeneous arrays enable safe `.map()`, `.filter()`, and `.reduce()` without per-element type guards. They also allow V8 to use optimized internal representations (monomorphic arrays) for better performance. JSDoc `@type {string[]}` communicates the contract to editors (Exploring JS Ch. 34).

---

## ID-29: Validate at Public Boundaries with Typed Guards

**Strength**: SHOULD

**Summary**: Check types at the boundary between your module and the outside world. Trust types within.

```js
/**
 * @param {string} host
 * @param {number} port
 * @param {{ tls?: boolean }} [options]
 */
export function connect(host, port, options = {}) {
  if (typeof host !== "string" || host.length === 0) {
    throw new TypeError("host must be a non-empty string");
  }
  if (!Number.isInteger(port) || port < 0 || port > 65535) {
    throw new RangeError(`port must be 0-65535, got ${port}`);
  }
  // Internal code trusts these types — no further checks needed
  return createConnection(host, port, options.tls ?? false);
}
```

**Rationale**: JavaScript's type coercion means wrong-typed arguments produce silent failures (`NaN`, wrong concatenation) rather than errors. Validating at boundaries catches these at the source. Internal functions trust the validated types — redundant checks deep inside are noise (Exploring JS Ch. 16; Deep JS Ch. 14).

**See also**: `03-error-handling.md` ID-23, ID-24

---

## ID-30: Use `Object.freeze()` for Enum-Like Constant Objects

**Strength**: SHOULD

**Summary**: Freeze objects that represent a closed set of constants to prevent accidental modification.

```js
// Good — frozen enum-like constants
const Direction = Object.freeze({
  UP: "up",
  DOWN: "down",
  LEFT: "left",
  RIGHT: "right",
});

// Good — frozen with Symbol values for collision safety
const Token = Object.freeze({
  LPAREN: Symbol("LPAREN"),
  RPAREN: Symbol("RPAREN"),
  NUMBER: Symbol("NUMBER"),
  STRING: Symbol("STRING"),
});

// Usage
function move(direction) {
  switch (direction) {
    case Direction.UP:    return [0, -1];
    case Direction.DOWN:  return [0, 1];
    case Direction.LEFT:  return [-1, 0];
    case Direction.RIGHT: return [1, 0];
    default: throw new Error(`Unknown direction: ${direction}`);
  }
}

// Frozen — accidental mutation is caught
Direction.DIAGONAL = "diagonal"; // TypeError in strict mode
```

**Rationale**: `Object.freeze()` prevents property addition, deletion, and modification. Combined with string or Symbol values, frozen objects serve as JavaScript's closest equivalent to enums — a closed, immutable set of named constants (Deep JS Ch. 8; Exploring JS Ch. 32).

**See also**: `04-values-references.md` ID-16, ID-19

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | `typeof` quirks | MUST | `null` → `"object"`, arrays → `"object"` |
| 02 | `Array.isArray()` for arrays | MUST | Only cross-realm safe array check |
| 03 | `instanceof` for classes only | SHOULD | Fails for primitives and across realms |
| 04 | `Number.isNaN/isFinite/isInteger` | MUST | Global versions coerce first — unreliable |
| 05 | `Object.hasOwn()` | SHOULD | Safe on null-prototype objects, can't be spoofed |
| 06 | Duck typing over constructor checks | SHOULD | Check capabilities, not class identity |
| 07 | Explicit conversion functions | SHOULD | `Number()`, `String()`, `Boolean()` — never with `new` |
| 08 | `parseInt` with radix 10 | SHOULD | No radix = unpredictable results |
| 09 | Avoid implicit coercion | SHOULD | `+x`, `""+x` obscure intent and have edge cases |
| 10 | `+` operator dual nature | MUST | String wins; left-to-right evaluation traps |
| 11 | `NaN !== NaN` | MUST | Only `Number.isNaN()` reliably detects it |
| 12 | `-0 === 0` | CONSIDER | `Object.is()` for sign-of-zero edge cases |
| 13 | Floating-point precision | MUST | Integer arithmetic for money; epsilon for comparison |
| 14 | BigInt/Number mixing | MUST | Arithmetic throws `TypeError`; convert explicitly |
| 15 | Safe integer limits | MUST | Beyond 2^53-1, distinct integers collide |
| 16 | JSDoc `@param`/`@returns` | SHOULD | Editor support and type checking without TypeScript |
| 17 | `@typedef` for object shapes | SHOULD | Reusable named types for complex structures |
| 18 | `@enum` for constant sets | CONSIDER | Closed type for LSP autocomplete |
| 19 | `@template` for generics | CONSIDER | Type parameters without TypeScript |
| 20 | Deno LSP + JSDoc integration | SHOULD | `// @ts-check`, `deno check`, `.d.ts` wiring |
| 21 | `undefined` vs `null` semantics | SHOULD | System absence vs intentional emptiness |
| 22 | `??` and `?.` over `\|\|` | MUST | Preserve `0`, `""`, `false` as valid values |
| 23 | No `typeof x === "undefined"` | SHOULD | Use `x === undefined` in modern code |
| 24 | Discriminated unions with `kind` | SHOULD | Closest JS gets to algebraic data types |
| 25 | `switch` + throwing `default` | SHOULD | Exhaustiveness check at runtime |
| 26 | `Map`/`Set` for typed collections | SHOULD | Any key type, `.size`, SameValueZero equality |
| 27 | TypedArray for binary/numeric data | CONSIDER | Fixed type, 4x faster, 8x less memory |
| 28 | Homogeneous arrays | SHOULD | Consistent types enable safe iteration |
| 29 | Validate at boundaries | SHOULD | Type checks at public API; trust within |
| 30 | `Object.freeze()` for enums | SHOULD | Closed, immutable set of named constants |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `===` (ID-02), `??` (ID-03), `?.` (ID-04), `const`/`let` (ID-01), `Map`/`Set` (ID-16)
- **API Design**: See `02-api-design.md` for return value conventions (ID-04, ID-23–25) and discriminated dispatch (ID-24–25 here)
- **Error Handling**: See `03-error-handling.md` for validation at boundaries (ID-23, ID-24) and typed error hierarchies (ID-05, ID-06)
- **Values & References**: See `04-values-references.md` for `Object.freeze()` (ID-16–19), property descriptors (ID-20–23), and equality (ID-24–26)
- **Functions & Closures**: See `06-functions-closures.md` for `this` binding rules (ID-16–18) and generator functions (ID-05)
- **Anti-Patterns**: See `09-anti-patterns.md` for ID-01, 02, 04, 05, 06 (coercion and type-checking anti-patterns)
- **Biome**: See `13-biome/02-lint-rules.md` for types-domain rules and exhaustive switch enforcement
- **Deno**: See `12-deno/01-runtime-basics.md` for `deno check`, LSP configuration, and `.d.ts` wiring

---

## External References

- [Deno Manual — Using JavaScript](https://docs.deno.com/)
- [Deno — Configuring TypeScript/JSDoc](https://docs.deno.com/runtime/fundamentals/typescript/)
- [Biome — Types Domain Rules](https://biomejs.dev/)
- [MDN — typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
- [MDN — JSDoc Reference](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
