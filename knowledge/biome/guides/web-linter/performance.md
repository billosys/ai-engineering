# Performance

Rules that catch performance pitfalls — O(n^2) patterns, unnecessary re-renders, blocking operations.

**5 recommended** (enabled by default) | **7 optional** (enable individually)

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

### noImgElement

Prevent usage of <img> element in a Next.js project.

**Don't:**
```jsx
<img alt="Foo" />
```

**Do:**
```jsx
<img />
```

---

### noUnwantedPolyfillio

Prevent duplicate polyfills from Polyfill.io.

**Don't:**
```jsx
<script src='https://polyfill.io/v3/polyfill.min.js?features=AbortController,Object.fromEntries'></script>
```

**Do:**
```jsx
<>
  <script src='https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=AbortController'></script>
  <script src='https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=IntersectionObserver'></script>
  <Script src='https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=IntersectionObserver' />
  <Script src='https://polyfill-fastly.io/v3/polyfill.min.js?features=IntersectionObserver' />
</>
```

---

### useGoogleFontPreconnect

Ensure the preconnect attribute is used when using Google Fonts.

**Don't:**
```jsx
<link href="https://fonts.gstatic.com"/>
```

**Do:**
```jsx
<link rel="preconnect" href="https://fonts.gstatic.com"/>
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
```ts
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
```ts
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

### useSolidForComponent

Enforce using Solid's <For /> component for mapping an array to JSX elements.

**Don't:**
```js
let Component = (props) => <ol>{props.data.map(d => <li>{d.text}</li>)}</ol>;
```

**Do:**
```js
let Component = (props) => <ol><For each={props.data}>{d => <li>{d.text}</li>}</For></ol>;
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
