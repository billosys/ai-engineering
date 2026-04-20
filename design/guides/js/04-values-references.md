# Values & References

Discipline around JavaScript's value model: primitives vs objects, copying, mutation, shared state, property mechanics, and equality. This is the JS equivalent of Rust's ownership and borrowing — not enforced by the compiler, but equally important to get right. Grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), and *Eloquent JavaScript* (Haverbeke).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: Primitives Are Immutable Values; Objects Are Mutable References

**Strength**: MUST

**Summary**: The seven primitive types are immutable and compared by value. Everything else is a mutable object compared by identity.

```js
// Primitives — immutable, compared by value
const a = "hello";
const b = "hello";
a === b;  // true — same value

// Objects — mutable, compared by identity
const x = { name: "Alice" };
const y = { name: "Alice" };
x === y;  // false — different objects, same content

const z = x;
z === x;  // true — same identity
z.name = "Bob";
x.name;   // "Bob" — mutation visible through shared identity
```

**The seven primitive types**: `undefined`, `null`, `boolean`, `number`, `bigint`, `string`, `symbol`. Everything else — plain objects, arrays, functions, dates, maps, sets, regexps, errors — is an object.

**Rationale**: This is the foundational split in JavaScript's value model. Primitives cannot be mutated (attempting to set a property throws in strict mode). Objects can be freely modified, and multiple variables can share the same object. Understanding this split is prerequisite to every other idiom in this guide (Exploring JS Ch. 13-14; JS Definitive Guide, §3.8).

---

## ID-02: Objects Are Passed by Identity, Not by Reference

**Strength**: SHOULD

**Summary**: JavaScript passes object identities by value. Mutation is visible to the caller; reassignment is not.

```js
function modify(obj) {
  obj.x = 1;   // mutation: caller sees this — shared identity
  obj = {};    // reassignment: caller does NOT see this — local binding only
}

const data = { x: 0 };
modify(data);
data.x;  // 1 — mutation was visible
data;    // { x: 1 } — not {}, reassignment was local

// True pass-by-reference (C++) would make swap() possible.
// JavaScript cannot implement swap() — proof it's NOT pass-by-reference.
```

**Rationale**: Rauschmayer uses the term "pass by identity" (coined by Allen Wirfs-Brock, 2019), also called "pass by sharing." Calling it "pass by reference" is technically wrong — in true pass-by-reference, reassigning a parameter changes the caller's variable. In JavaScript, only mutation is shared; reassignment is local (Exploring JS Ch. 14; Deep JS Ch. 3).

---

## ID-03: `typeof` and Its Quirks

**Strength**: MUST

**Summary**: Know the two `typeof` gotchas: `null` returns `"object"`, and functions return `"function"`.

```js
typeof undefined   // "undefined"
typeof true        // "boolean"
typeof 42          // "number"
typeof 42n         // "bigint"
typeof "hello"     // "string"
typeof Symbol()    // "symbol"
typeof null        // "object"  — historical bug, null is a primitive
typeof {}          // "object"
typeof []          // "object"  — arrays are objects
typeof (() => {})  // "function" — functions are objects, but typeof says "function"

// Correct null check — never use typeof for null
if (value === null) { /* ... */ }

// Correct array check — never use typeof for arrays
if (Array.isArray(value)) { /* ... */ }
```

**Rationale**: `typeof null === "object"` is a well-known historical bug that cannot be fixed without breaking the web. `typeof` returns `"function"` for functions even though functions are objects. Neither behavior is intuitive; explicit checks with `===` and `Array.isArray()` are required (Exploring JS Ch. 13; JS Definitive Guide, §3.1).

---

## ID-04: `const` Freezes the Binding, Not the Value

**Strength**: MUST

**Summary**: `const` prevents reassignment of the variable. It does not prevent mutation of the value.

```js
const config = { debug: false };
config.debug = true;     // legal — mutating the value
config.newKey = "added"; // legal — adding a property
// config = {};          // TypeError — reassigning the binding

const items = [1, 2, 3];
items.push(4);           // [1, 2, 3, 4] — legal
// items = [];           // TypeError
```

**Mental model**: `const` freezes the *arrow* from the name to the value. It does not freeze what the arrow points at. To freeze the value itself, use `Object.freeze()` (Exploring JS Ch. 11; Deep JS Ch. 8).

**See also**: `01-core-idioms.md` ID-14

---

## ID-05: Reassignment vs Mutation — Know Which You're Doing

**Strength**: MUST

**Summary**: Reassignment (`=` to a variable) changes which value a name points to. Mutation (`.prop =`, `.push()`) changes the value itself.

```js
// Reassignment — changes the binding
let x = [1, 2, 3];
x = [4, 5, 6];  // x now points to a different array

// Mutation — changes the value
const y = [1, 2, 3];
y.push(4);       // same array, modified in place
y[0] = 99;       // same array, element changed

// The distinction matters for shared state:
const shared = [1, 2];
const alias = shared;
shared.push(3);        // mutation: alias is now [1, 2, 3] too
// shared = [1, 2, 3]; // reassignment: would NOT affect alias (if shared were let)
```

**Rationale**: Confusing reassignment with mutation is a common source of bugs. Reassignment is safe — it only affects the local binding. Mutation is dangerous — it affects every alias to the same object. `const` prevents reassignment but not mutation, making this distinction critical (Deep JS Ch. 3, 6).

---

## ID-06: Spread for Shallow Copies of Objects and Arrays

**Strength**: SHOULD

**Summary**: Use spread (`{...obj}` / `[...arr]`) for shallow copies. Understand what "shallow" means.

```js
// Good — shallow copy of an object
const original = { name: "Alice", scores: [90, 85] };
const copy = { ...original };
copy.name = "Bob";         // independent — top-level primitive
original.name;             // "Alice"

// Danger — nested reference is shared
copy.scores.push(95);
original.scores;           // [90, 85, 95] — same array!

// Good — shallow copy of an array
const arrCopy = [...original.scores];
arrCopy.push(100);
original.scores.length;    // 3 — arrCopy is independent
```

**What spread copies**: All own enumerable properties (string and symbol keys). It does NOT copy: the prototype, non-enumerable properties, or accessor definitions (getters are invoked, their return values stored as data properties).

**Rationale**: Spread is concise and idiomatic for flat data. For nested data that must be independently mutable, use `structuredClone()` or manually spread at each level (Deep JS Ch. 7; Exploring JS Ch. 30).

---

## ID-07: `Object.assign()` vs Spread — Know the Difference

**Strength**: CONSIDER

**Summary**: Both do shallow copies of own enumerable properties, but they differ in how target properties are created.

```js
// Spread uses property definition — ignores inherited setters
const copy1 = { ...source };

// Object.assign() uses property assignment — invokes inherited setters
Object.assign(target, source);
```

| Concern | `{...obj}` | `Object.assign({}, obj)` |
|---------|-----------|-------------------------|
| Creates properties via | Definition | Assignment |
| Invokes inherited setters on target | No | Yes |
| `__proto__` key | Stored as own property | Triggers the setter, changes prototype |

**Practical rule**: Prefer spread in modern code. Use `Object.assign()` only when you need assignment semantics (trigger setters) or need to mutate an existing target: `Object.assign(existingObj, patch)`.

**To copy accessor properties faithfully**:
```js
Object.defineProperties(target, Object.getOwnPropertyDescriptors(source));
```

**Rationale**: The `__proto__` edge case is the clearest demonstration of the difference. In `Object.assign()`, a source property named `__proto__` triggers the `__proto__` setter and changes the target's prototype. With spread, it becomes a regular own property (Deep JS Ch. 7, 12).

---

## ID-08: Shallow Copies Share Nested References

**Strength**: MUST

**Summary**: A shallow copy is independent at the top level but shares all nested objects with the original.

```js
const original = { user: { name: "Alice" }, tags: ["admin"] };
const copy = { ...original };

// Top-level: independent
copy.tags = ["viewer"];
original.tags; // ["admin"] — unaffected

// BUT if you mutate the nested object instead of replacing it:
copy.user.name = "Bob";
original.user.name; // "Bob" — shared reference!
```

**Rule of thumb**: Shallow copies are safe for flat data structures. If any property holds an object that might be mutated, you need a deep copy or must spread at each nested level.

**Rationale**: This is the single most common source of "my copy changed the original" bugs. It applies equally to `{...obj}`, `[...arr]`, `Object.assign()`, `Array.from()`, and `.slice()` (Deep JS Ch. 7; Exploring JS Ch. 30).

---

## ID-09: `structuredClone()` for Deep Copies

**Strength**: SHOULD

**Summary**: Use `structuredClone()` when you need a fully independent copy of nested data.

```js
// Good — deep copy, all nesting independent
const original = { user: { name: "Alice" }, tags: ["admin"] };
const deep = structuredClone(original);
deep.user.name = "Bob";
original.user.name; // "Alice" — independent

// Handles circular references
const circular = { self: null };
circular.self = circular;
const copy = structuredClone(circular); // works
```

**Limitations**:
- Cannot clone functions (throws `DOMException`)
- Cannot clone Symbol-keyed properties
- Class instances become plain objects (lose prototype)
- Property descriptors are reset to defaults

**Rationale**: `structuredClone()` handles circular references, `Date`, `RegExp`, `Map`, `Set`, and `ArrayBuffer`. It is the correct choice for deep copying in all but edge cases involving functions or class identity (Exploring JS Ch. 17; Deep JS Ch. 7).

**See also**: `01-core-idioms.md` ID-23

---

## ID-10: JSON Round-Trip Is NOT a Reliable Deep Copy

**Strength**: MUST

**Summary**: `JSON.parse(JSON.stringify(obj))` silently drops or corrupts non-JSON-safe values. Use `structuredClone()` instead.

```js
const original = {
  date: new Date(),
  pattern: /abc/gi,
  fn: () => {},
  undef: undefined,
  sym: Symbol("x"),
};

const bad = JSON.parse(JSON.stringify(original));
// bad.date   → string, not Date
// bad.pattern → {} (empty object)
// bad.fn     → missing (silently dropped)
// bad.undef  → missing (silently dropped)
// bad.sym    → missing (silently dropped)

// Also throws on:
JSON.stringify({ n: 42n });      // TypeError (BigInt)
JSON.stringify(circular);         // TypeError (circular reference)
```

**Rationale**: The JSON hack is commonly recommended but silently loses data for `undefined`, functions, symbols, `Date`, `RegExp`, `Map`, `Set`, and `BigInt`. It also throws on circular references. `structuredClone()` handles all of these except functions and symbols (Deep JS Ch. 7).

---

## ID-11: Prefer Non-Destructive Updates over Deep Copying

**Strength**: SHOULD

**Summary**: When you need to change one field in a nested structure, spread at each modified level instead of deep-copying the entire object.

```js
// Good — non-destructive update, structural sharing
const original = {
  user: { name: "Alice", prefs: { theme: "dark" } },
  tags: ["admin"],
};

const updated = {
  ...original,
  user: {
    ...original.user,
    prefs: { ...original.user.prefs, theme: "light" },
  },
};
// original is completely unchanged
// updated.tags === original.tags — shared (unmodified branches)
// updated.user !== original.user — new object (modified branch)

// Good — non-destructive array update
const replaced = [...arr.slice(0, 2), "new", ...arr.slice(3)];

// Good — ES2023 non-destructive method
const replaced = arr.with(2, "new");
```

**Rationale**: Deep copying clones everything, including branches you didn't change. Non-destructive updates via spread only create new objects along the modified path, sharing unmodified branches with the original. This is more efficient and is the foundation of state management patterns (Deep JS Ch. 8; Exploring JS Ch. 34).

---

## ID-12: Don't Mutate Function Arguments

**Strength**: MUST

**Summary**: Never mutate objects or arrays received as parameters. Copy first if you need to modify them.

```js
// Bad — destroys the caller's array
function logAll(arr) {
  while (arr.length > 0) {
    console.log(arr.shift()); // mutates arr
  }
}

// Good — defensive copy at the boundary
function logAll(arr) {
  for (const item of [...arr]) {
    console.log(item);
  }
}

// Bad — sorts the caller's array in place
function getSorted(arr) {
  return arr.sort(); // mutates and returns the same array
}

// Good — non-destructive sort
function getSorted(arr) {
  return arr.toSorted(); // ES2023, returns new array
}
```

**Rationale**: The caller does not expect passing an argument to destroy it. Mutating arguments creates action-at-a-distance bugs that are difficult to diagnose — the symptom appears far from the cause. Copy at the function boundary or use non-destructive methods (Deep JS Ch. 6).

---

## ID-13: Defensive Copying at Module Boundaries

**Strength**: SHOULD

**Summary**: Copy data at the boundary between modules or components — both incoming (parameters) and outgoing (return values).

```js
// Good — input defense: copy so internal operations are safe
export function processItems(items) {
  const local = [...items]; // defensive copy
  local.sort((a, b) => a.priority - b.priority);
  return local.map(transform);
}

// Good — output defense: don't expose internal state
class Store {
  #items = [];

  add(item) { this.#items.push(item); }

  getItems() {
    return [...this.#items]; // caller gets a copy, not a reference to internals
  }
}
```

**Rationale**: Input defense protects your function from external mutations. Output defense protects your internal state from external corruption. Both are needed for a robust boundary. Defensive copies only need to be as deep as the mutation risk — shallow is sufficient for flat data (Deep JS Ch. 6).

---

## ID-14: Non-Destructive Updates with Spread

**Strength**: SHOULD

**Summary**: Create modified copies instead of mutating originals. The original is preserved for other consumers.

```js
// Object — spread with override
const updated = { ...config, timeout: 5000 };

// Object — generic set function
function set(obj, key, value) {
  return { ...obj, [key]: value };
}

// Array — replace at index
const replaced = [...arr.slice(0, i), newValue, ...arr.slice(i + 1)];

// Array — remove at index
const removed = [...arr.slice(0, i), ...arr.slice(i + 1)];

// Array — prepend and append
const prepended = [newItem, ...arr];
const appended = [...arr, newItem];
```

**Override order matters**: `{ ...obj, key: value }` ensures the override wins. `{ key: value, ...obj }` lets the spread overwrite your value if `obj` has the same key.

**Rationale**: Non-destructive updates are the default in functional and state-management patterns (React, Redux). They eliminate shared-state bugs because the original is never modified (Deep JS Ch. 8; Exploring JS Ch. 34).

---

## ID-15: Prefer Non-Destructive Array Methods

**Strength**: SHOULD

**Summary**: Use ES2023 non-destructive array methods instead of their mutating counterparts.

```js
// Destructive (mutates) → Non-destructive (returns new array)
arr.reverse()       → arr.toReversed()
arr.sort(fn)        → arr.toSorted(fn)
arr.splice(i, n, x) → arr.toSpliced(i, n, x)
arr[i] = v          → arr.with(i, v)

// Example
const original = [3, 1, 2];
const sorted = original.toSorted();
original; // [3, 1, 2] — unchanged
sorted;   // [1, 2, 3]

// Pre-ES2023 workaround: copy first, then mutate
const sorted = [...original].sort();
```

**Common trap**: `.reverse()` and `.sort()` return the **same array reference** they mutated, not a new array. Code like `const sorted = arr.sort()` both mutates `arr` and aliases `sorted` to it.

**Rationale**: The destructive methods are legacy designs from ES1. The non-destructive alternatives (ES2023) eliminate accidental mutation and are safer in functional pipelines (Exploring JS Ch. 34; Deep JS Ch. 8).

---

## ID-16: `Object.freeze()` for Shallow Protection

**Strength**: SHOULD

**Summary**: `Object.freeze()` makes all own properties non-writable and the object non-extensible. It is shallow — nested objects are not frozen.

```js
// Good — frozen configuration
const CONFIG = Object.freeze({
  maxRetries: 3,
  timeout: 5000,
});
CONFIG.maxRetries = 99;  // TypeError in strict mode
CONFIG.newProp = "x";    // TypeError in strict mode

// Shallow trap — nested object is NOT frozen
const NESTED = Object.freeze({
  db: { host: "localhost", port: 5432 },
});
NESTED.db.port = 9999;  // succeeds! db is not frozen
```

**Rationale**: `Object.freeze()` is the strongest built-in protection level. It prevents property addition, deletion, and modification. But it is shallow — every nested object must be frozen separately for full immutability (Deep JS Ch. 8; JS Definitive Guide, §14.2).

**See also**: `01-core-idioms.md` ID-15

---

## ID-17: `seal` vs `freeze` vs `preventExtensions`

**Strength**: CONSIDER

**Summary**: Three progressive protection levels, each a superset of the previous.

| | `preventExtensions()` | `seal()` | `freeze()` |
|-|:--------------------:|:-------:|:--------:|
| Add new properties | No | No | No |
| Delete properties | Yes | No | No |
| Modify values | Yes | Yes | No |
| Change attributes | Yes | No | No |
| Reversible | No | No | No |
| Check with | `!isExtensible()` | `isSealed()` | `isFrozen()` |
| Depth | Shallow | Shallow | Shallow |

```js
const obj = { x: 1 };

Object.preventExtensions(obj);
obj.y = 2;     // TypeError — can't add
obj.x = 99;    // ok — can still modify
delete obj.x;  // ok — can still delete

const obj2 = { x: 1 };
Object.seal(obj2);
obj2.x = 99;   // ok — can still modify
delete obj2.x;  // TypeError — can't delete

const obj3 = { x: 1 };
Object.freeze(obj3);
obj3.x = 99;   // TypeError — can't modify
```

**Rationale**: `seal()` is often misunderstood — it does NOT make properties read-only, only `freeze()` does. All three are shallow and irreversible (Deep JS Ch. 8).

---

## ID-18: Deep Freeze for Full Immutability

**Strength**: CONSIDER

**Summary**: Recursively apply `Object.freeze()` to achieve deep immutability.

```js
function deepFreeze(value) {
  if (typeof value === "object" && value !== null && !Object.isFrozen(value)) {
    Object.freeze(value);
    for (const v of Object.values(value)) {
      deepFreeze(v);
    }
    if (Array.isArray(value)) {
      for (const element of value) {
        deepFreeze(element);
      }
    }
  }
  return value;
}

const config = deepFreeze({
  db: { host: "localhost", port: 5432 },
  limits: [10, 20, 50],
});
config.db.port = 9999;    // TypeError
config.limits.push(100);  // TypeError
```

**Caveat**: The simple implementation above can infinite-loop on circular references. Production code needs a `visited` Set. Libraries exist for this purpose, but for configuration objects with known shapes, manual freezing at each level is simpler.

**Rationale**: Rauschmayer: "If data is immutable, it can be shared without any risks." Deep freeze is the strongest guarantee — no party can accidentally mutate shared data (Deep JS Ch. 8).

---

## ID-19: Frozen Objects as Lookup Tables and Configuration

**Strength**: SHOULD

**Summary**: Use `Object.freeze()` for constant lookup tables and configuration objects that must never change at runtime.

```js
// Good — frozen enum-like lookup
const HttpStatus = Object.freeze({
  OK: 200,
  NOT_FOUND: 404,
  INTERNAL_ERROR: 500,
});

// Good — frozen configuration
const DEFAULTS = Object.freeze({
  timeout: 5000,
  retries: 3,
  baseUrl: "https://api.example.com",
});

// Usage — spread to override (non-destructive)
const config = { ...DEFAULTS, timeout: 10000 };
```

**Rationale**: Frozen objects serve as immutable constants — they cannot be accidentally modified by any consumer. Combining frozen defaults with spread overrides gives a clean, safe configuration pattern (Deep JS Ch. 8; JS Definitive Guide, §14.2).

---

## ID-20: Definition vs Assignment — They Are Not the Same

**Strength**: SHOULD

**Summary**: Assignment (`obj.prop = v`) invokes setters and checks `writable`. Definition (`Object.defineProperty`) ignores inherited setters and controls all attributes.

```js
// Assignment invokes inherited setters
const proto = {
  set data(v) { console.log("setter called:", v); },
};
const obj = Object.create(proto);
obj.data = 42;  // logs "setter called: 42" — does NOT create own property

// Definition ignores inherited setters
Object.defineProperty(obj, "data", { value: 42, writable: true, enumerable: true, configurable: true });
// obj now has its own "data" property, setter was NOT called

// Assignment is blocked by inherited read-only
const proto2 = Object.defineProperty({}, "x", { value: 1, writable: false });
const child = Object.create(proto2);
// child.x = 2;  // TypeError in strict mode — inherited non-writable blocks assignment
Object.defineProperty(child, "x", { value: 2 }); // works — definition bypasses the check
```

**Rationale**: This distinction is fundamental to understanding property behavior in JavaScript. Object literals and class field declarations use definition semantics. The `=` operator uses assignment semantics. Confusing them leads to subtle bugs with setters and inherited properties (Deep JS Ch. 12).

---

## ID-21: Property Descriptor Defaults Differ by Creation Method

**Strength**: CONSIDER

**Summary**: Properties created by literals/assignment default to all-`true` attributes. Properties created by `Object.defineProperty()` default to all-`false`.

| Creation method | `writable` | `enumerable` | `configurable` |
|----------------|:----------:|:------------:|:--------------:|
| Object literal `{ x: 1 }` | `true` | `true` | `true` |
| Assignment `obj.x = 1` | `true` | `true` | `true` |
| `defineProperty()` (omitted) | **`false`** | **`false`** | **`false`** |

```js
// This creates a read-only, non-enumerable, non-configurable property:
Object.defineProperty(obj, "x", { value: 1 });
// Equivalent to:
Object.defineProperty(obj, "x", {
  value: 1, writable: false, enumerable: false, configurable: false,
});

// To get "normal" behavior via defineProperty, be explicit:
Object.defineProperty(obj, "x", {
  value: 1, writable: true, enumerable: true, configurable: true,
});
```

**Rationale**: This asymmetry is one of the most common `defineProperty` surprises. Omitting attributes silently creates a maximally locked-down property (Deep JS Ch. 12; JS Definitive Guide, §14.1).

---

## ID-22: Getters and Setters for Computed Properties

**Strength**: SHOULD

**Summary**: Use getters for derived/computed values and setters for validated assignment. Accessor properties enable upgrading data properties without breaking callers.

```js
// Good — computed property via getter
class Circle {
  #radius;
  constructor(radius) { this.#radius = radius; }
  get area() { return Math.PI * this.#radius ** 2; }
  get radius() { return this.#radius; }
  set radius(value) {
    if (typeof value !== "number" || value < 0) {
      throw new RangeError("radius must be a non-negative number");
    }
    this.#radius = value;
  }
}

const c = new Circle(5);
c.area;       // 78.54... — computed on access
c.radius = 10; // validated assignment
// c.radius = -1; // RangeError
```

**Pitfall**: `Object.assign()` and spread flatten getters — they read the return value and store it as a plain data property. To copy accessors faithfully: `Object.defineProperties(target, Object.getOwnPropertyDescriptors(source))`.

**Rationale**: Getters expose computed values with property syntax. Setters enforce invariants at the assignment site. The key advantage: you can upgrade a data property to a getter/setter later without changing any call sites (Exploring JS Ch. 30; JS Definitive Guide, §6.10.6; Deep JS Ch. 12).

---

## ID-23: Enumerability Controls Visibility in Listing Operations

**Strength**: SHOULD

**Summary**: Enumerability determines which properties appear in `for-in`, `Object.keys()`, spread, and `JSON.stringify()`.

| Operation | Enumerable only | Includes inherited |
|-----------|:--------------:|:-----------------:|
| `for-in` | Yes | Yes |
| `Object.keys()` / `.values()` / `.entries()` | Yes | No |
| `{...spread}` / `Object.assign()` | Yes | No |
| `JSON.stringify()` | Yes | No |
| `Object.getOwnPropertyNames()` | No | No |
| `Reflect.ownKeys()` | No | No |

```js
const obj = Object.defineProperty({ visible: 1 }, "hidden", {
  value: 2,
  enumerable: false,
});

Object.keys(obj);    // ["visible"]
{ ...obj };          // { visible: 1 }
JSON.stringify(obj);  // '{"visible":1}'
Reflect.ownKeys(obj); // ["visible", "hidden"]
```

**Rationale**: Class prototype methods are non-enumerable by design — this keeps them out of `for-in` and spread. Properties you create via literals or assignment are enumerable. Understanding this split explains why some properties "disappear" in certain contexts (Deep JS Ch. 13; Exploring JS Ch. 30).

---

## ID-24: `===` Compares Identity for Objects, Value for Primitives

**Strength**: MUST

**Summary**: Strict equality compares object identity (same reference) and primitive value (same content).

```js
// Primitives — value comparison
1 === 1;             // true
"abc" === "abc";     // true

// Objects — identity comparison
{} === {};           // false — different objects
[] === [];           // false — different arrays
const a = {};
a === a;             // true — same reference

// Consequence for function returns
const result1 = findUser(1);
const result2 = findUser(1);
result1 === result2; // true ONLY if both calls return the same object
```

**Rationale**: This is why you cannot compare objects with `===` to check if they have the same content. `===` answers "are these the same object?" not "do these objects contain the same data?" (Exploring JS Ch. 13-14; Deep JS Ch. 14).

---

## ID-25: `Object.is()` for `NaN` and `-0` Edge Cases

**Strength**: CONSIDER

**Summary**: `Object.is()` fixes two `===` quirks: `NaN === NaN` is `false`, and `+0 === -0` is `true`.

```js
// === gets these wrong:
NaN === NaN;         // false
+0 === -0;           // true

// Object.is() fixes both:
Object.is(NaN, NaN); // true
Object.is(+0, -0);   // false

// Practical use: finding NaN in an array
const arr = [1, NaN, 3];
arr.indexOf(NaN);                       // -1 — can't find NaN with ===
arr.findIndex((x) => Object.is(x, NaN)); // 1 — correct
arr.includes(NaN);                      // true — uses SameValueZero (also finds NaN)
```

**Rationale**: `Object.is()` implements the SameValue algorithm. For NaN detection, prefer `Number.isNaN()` (clearer intent). The `-0` distinction is rarely needed in practice. `Array.prototype.includes()` uses SameValueZero, which finds `NaN` but treats `+0` and `-0` as equal (Exploring JS Ch. 13; Deep JS Ch. 14).

---

## ID-26: Deep Equality Requires Manual or Library Implementation

**Strength**: SHOULD

**Summary**: JavaScript has no built-in deep structural equality. Use testing libraries for tests; implement manually or with a library for production.

```js
// In tests — use Deno's assert
import { assertEquals } from "@std/assert";
assertEquals({ a: 1, b: [2, 3] }, { a: 1, b: [2, 3] }); // passes

// In production — no built-in option
const a = { x: 1, nested: { y: 2 } };
const b = { x: 1, nested: { y: 2 } };
a === b;                              // false — different identities
JSON.stringify(a) === JSON.stringify(b); // fragile — fails for undefined, functions, key order

// Correct: implement recursive comparison or use a library
```

**Rationale**: `===` and `Object.is()` both compare objects by identity. `JSON.stringify()` comparison fails for `undefined`, functions, symbols, and is sensitive to property order. For tests, `assertEquals` / `assertObjectMatch` handle deep comparison. For production, a dedicated function or library is needed (Exploring JS Ch. 13).

---

## ID-27: Own vs Inherited Properties — Use `Object.hasOwn()`

**Strength**: SHOULD

**Summary**: Use `Object.hasOwn()` (ES2022) to check if a property is directly on the object, not inherited from the prototype.

```js
// Good — works on all objects, including Object.create(null)
const config = Object.create(null);
config.timeout = 5000;
Object.hasOwn(config, "timeout");       // true
Object.hasOwn(config, "toString");      // false — not inherited, proto is null

// Bad — fails on null-prototype objects
const config2 = Object.create(null);
config2.hasOwnProperty("timeout");      // TypeError — no hasOwnProperty method

// Bad — can be overridden
const sketchy = { hasOwnProperty: () => true };
sketchy.hasOwnProperty("anything");     // true — spoofed
Object.hasOwn(sketchy, "anything");     // false — reliable
```

**Rationale**: `Object.hasOwn()` is a static method that cannot be overridden or absent. It replaces `obj.hasOwnProperty()`, which fails on null-prototype objects and can be shadowed by own properties (Exploring JS Ch. 30; Deep JS Ch. 12).

---

## ID-28: Prototype Chain Affects Lookup but NOT Assignment

**Strength**: MUST

**Summary**: Reading traverses the prototype chain. Writing creates an own property that shadows the inherited one — the prototype is never modified.

```js
const proto = { shared: "original" };
const obj = Object.create(proto);

// Reading — traverses chain
obj.shared;               // "original" — found in proto

// Writing — creates own property, does NOT modify proto
obj.shared = "override";
obj.shared;               // "override" — own property shadows
proto.shared;             // "original" — unchanged
Object.hasOwn(obj, "shared"); // true — now has own property

// Other objects sharing the same proto are unaffected
const other = Object.create(proto);
other.shared;             // "original"
```

**Exception**: If the inherited property is non-writable (`writable: false`) or is a getter-only accessor, assignment fails (TypeError in strict mode) instead of creating a shadow. Use `Object.defineProperty()` to bypass this.

**Rationale**: This read/write asymmetry is fundamental to prototype-based inheritance. Writing always creates an own property — it never reaches up the chain. This is why `Object.freeze()` on a prototype does not prevent instances from having their own properties (Deep JS Ch. 12; Exploring JS Ch. 30).

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Primitives immutable, objects mutable | MUST | The foundational split in JS's value model |
| 02 | Pass by identity, not reference | SHOULD | Mutation shared, reassignment local |
| 03 | `typeof` quirks | MUST | `null` → `"object"`, functions → `"function"` |
| 04 | `const` freezes binding, not value | MUST | Arrow from name is frozen; target is not |
| 05 | Reassignment vs mutation | MUST | `=` to variable vs `.push()` on value |
| 06 | Spread for shallow copies | SHOULD | Own enumerable props only; no prototype |
| 07 | `Object.assign()` vs spread | CONSIDER | Assignment vs definition semantics |
| 08 | Shallow copies share nested refs | MUST | Top-level independent; nested shared |
| 09 | `structuredClone()` for deep copies | SHOULD | Handles circular refs, Date, Map, Set |
| 10 | JSON round-trip is not reliable | MUST | Drops `undefined`, functions, symbols; corrupts Date |
| 11 | Non-destructive updates over deep copy | SHOULD | Spread at modified levels; share unmodified |
| 12 | Don't mutate function arguments | MUST | Copy first or use non-destructive methods |
| 13 | Defensive copying at boundaries | SHOULD | Copy input AND output at module edges |
| 14 | Non-destructive updates with spread | SHOULD | `{ ...obj, key: value }` — override order matters |
| 15 | Non-destructive array methods | SHOULD | `.toSorted()`, `.toReversed()`, `.with()` (ES2023) |
| 16 | `Object.freeze()` — shallow | SHOULD | Non-writable + non-extensible; nested NOT frozen |
| 17 | seal vs freeze vs preventExtensions | CONSIDER | Progressive protection; only freeze is read-only |
| 18 | Deep freeze for full immutability | CONSIDER | Recursive `Object.freeze()`; watch circular refs |
| 19 | Frozen lookup tables and config | SHOULD | Combine with spread for safe overrides |
| 20 | Definition vs assignment | SHOULD | Assignment invokes setters; definition does not |
| 21 | `defineProperty` defaults are all-false | CONSIDER | Literal/assignment defaults are all-true |
| 22 | Getters/setters for computed properties | SHOULD | Upgrade data props without breaking callers |
| 23 | Enumerability controls listing visibility | SHOULD | `for-in`, `Object.keys()`, spread, JSON filter by it |
| 24 | `===` is identity for objects | MUST | Same content ≠ same object |
| 25 | `Object.is()` for NaN and -0 | CONSIDER | Fixes two `===` edge cases |
| 26 | Deep equality needs manual impl | SHOULD | No built-in; use test libs or explicit code |
| 27 | `Object.hasOwn()` over `hasOwnProperty` | SHOULD | Safe on null-prototype objects; can't be spoofed |
| 28 | Prototype affects lookup, not assignment | MUST | Write creates own property; proto unchanged |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `const`/`let` (ID-01, ID-14), `===` (ID-02), `structuredClone()` (ID-23), `Object.freeze()` (ID-15)
- **API Design**: See `02-api-design.md` for return value conventions (ID-04, ID-23, ID-24) and factory patterns (ID-11, ID-13)
- **Error Handling**: See `03-error-handling.md` for validation at boundaries (ID-23, ID-24)
- **Type Discipline**: See `05-type-discipline.md` for `typeof` guards (ID-01–03), JSDoc annotations (ID-16–20), and `Object.freeze()` for enums (ID-30)
- **Functions & Closures**: See `06-functions-closures.md` for closure capture (ID-06–10) and scope mechanics (ID-11–15)
- **Async & Concurrency**: See `07-async-concurrency.md` for mutation discipline in async contexts (ID-17 references run-to-completion)
- **Anti-Patterns**: See `09-anti-patterns.md` for ID-14, 15, 16, 35 (mutation and copying anti-patterns)

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [MDN — structuredClone()](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone)
- [MDN — Object.freeze()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
