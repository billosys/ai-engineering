# Performance

Rules that catch performance anti-patterns — O(n^2) patterns, blocking operations, unnecessary allocations.

**2 recommended** | **6 optional**

## Recommended Rules

### noAccumulatingSpread

Disallow the use of spread (...) syntax on accumulators.

**Don't:**
```js
var a = ['a', 'b', 'c'];
a.reduce((acc, val) => [...acc, val], []);
```

**Do:**
```js
var a = ['a', 'b', 'c'];
a.reduce((acc, val) => {acc.push(val); return acc}, []);
```

---

### noDynamicNamespaceImportAccess

Disallow accessing namespace imports dynamically.

**Don't:**
```js
import * as foo from "foo"
foo["bar"]
```

**Do:**
```js
import * as foo from "foo"
foo.bar
```

---

## Optional Rules

### noAwaitInLoops

Disallow await inside loops.

**Don't:**
```js
async function invalid() {
    for (const thing of things) {
        const result = await asyncWork();
    }
}
```

**Do:**
```js
async function valid() {
    await Promise.all(things.map((thing) => asyncWork(thing)))
}
```

---

### noBarrelFile

Disallow the use of barrel file.

**Don't:**
```js
export * from "foo";
export * from "bar";
```

**Do:**
```js
export type * from "foo";
export type { foo } from "foo";
```

---

### noDelete

Disallow the use of the delete operator.

**Don't:**
```js
const arr = [1, 2, 3];
delete arr[0];
```

**Do:**
```js
const foo = new Set([1,2,3]);
foo.delete(1);
```

---

### noNamespaceImport

Disallow the use of namespace imports.

**Don't:**
```js
import * as foo from "foo";
```

**Do:**
```js
import { foo } from "foo"
import type { bar } from "bar"
import type * as baz from "baz"
```

---

### noReExportAll

Avoid re-export all.

**Don't:**
```js
export * from "foo";
```

**Do:**
```js
export { foo } from "foo";
```

---

### useTopLevelRegex

Require regex literals to be declared at the top level.

**Don't:**
```js
function foo(someString) {
    return /[a-Z]*/.test(someString)
}
```

**Do:**
```js
const REGEX = /[a-Z]*/;

function foo(someString) {
    return REGEX.test(someString)
}
```

---
