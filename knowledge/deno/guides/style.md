# Style & Idioms

Code style consistency — const vs let vs var, naming conventions, cleaner declarations, modern idioms.

**6 recommended** | **5 optional**

## Recommended Rules

### no-extra-boolean-cast

Disallows unnecessary boolean casts.

**Don't:**
```js
if (!!foo) {}
if (Boolean(foo)) {}
while (!!foo) {}
for (; Boolean(foo);) {}
```

**Do:**
```js
if (foo) {}
while (foo) {}
for (; foo;) {}
```

---

### no-this-alias

Disallows assigning variables to this.

**Don't:**
```js
const self = this;

function foo() {
  const self = this;
}

const bar = () => {
  const self = this;
};
```

**Do:**
```js
const self = "this";

const [foo] = this;
```

---

### no-unused-labels

Disallows unused labels.

**Don't:**
```js
LABEL1:
while (true) {
  console.log(42);
}

LABEL2:
for (let i = 0; i < 5; i++) {
  console.log(42);
}

LABEL3:
for (const x of xs) {
  console.log(x);
}
```

**Do:**
```js
LABEL1:
while (true) {
  console.log(42);
  break LABEL1;
}

LABEL2:
for (let i = 0; i < 5; i++) {
  console.log(42);
  continue LABEL2;
}

for (const x of xs) {
  console.log(x);
}
```

---

### no-unused-vars

Enforces all variables are used at least once.

**Don't:**
```js
const a = 0;

const b = 0; // this `b` is never used
function foo() {
  const b = 1; // this `b` is used
  console.log(b);
}
foo();

let c = 2;
c = 3;

// recursive function calls are not considered to be used, because only when `d`
// is called from outside the function body can we say that `d` is actually
// called after all.
function d() {
  d();
}

// `x` is never used
export function e(x: number): number {
  return 42;
}

const f = "unused variable";
```

**Do:**
```js
const a = 0;
console.log(a);

const b = 0;
function foo() {
  const b = 1;
  console.log(b);
}
foo();
console.log(b);

let c = 2;
c = 3;
console.log(c);

function d() {
  d();
}
d();

export function e(x: number): number {
  return x + 42;
}

export const f = "exported variable";
```

---

### no-var

Enforces the use of block scoped variables over more error prone function scoped variables. Block scoped variables are defined using const and let keywords.

**Don't:**
```js
var foo = "bar";
```

**Do:**
```js
const foo = 1;
let bar = 2;
```

---

### prefer-const

Recommends declaring variables with [const] over [let].

**Don't:**
```js
let a = 0;

let b = 0;
someOperation(b);

// `const` could be used instead
for (let c in someObject) {}

// `const` could be used instead
for (let d of someArray) {}

// variable that is uninitialized at first and then assigned in the same scope is NOT allowed
// because we could simply write it like `const e = 2;` instead
let e;
e = 2;
```

**Do:**
```js
// uninitialized variable is allowed
let a;

let b = 0;
b += 1;

let c = 0;
c = 1;

// variable that is uninitialized at first and then assigned in the same scope _two or more times_ is allowed
// because we cannot represent it with `const`
let d;
d = 2;
d = 3;

const e = 0;

// `f` is mutated through `f++`
for (let f = 0; f < someArray.length; f++) {}

// variable that is initialized (or assigned) in another scope is allowed
let g;
function func1() {
  g = 42;
}

// conditionally initialized variable is allowed
let h;
if (trueOrFalse) {
  h = 0;
}
```

---

## Optional Rules

### camelcase

Enforces the use of camelCase in variable names.

**Don't:**
```js
let first_name = "Ichigo";
const obj1 = { last_name: "Hoshimiya" };
const obj2 = { first_name };
const { last_name } = obj1;

function do_something() {}
function foo({ snake_case = "default value" }) {}

class snake_case_class {}
class Also_Not_Valid_Class {}

import { not_camelCased } from "external-module.js";
export * as not_camelCased from "mod.ts";

enum snake_case_enum {
  snake_case_variant,
}

type snake_case_type = { some_property: number };

interface snake_case_interface {
  some_property: number;
}
```

**Do:**
```js
let firstName = "Ichigo";
const FIRST_NAME = "Ichigo";
const __myPrivateVariable = "Hoshimiya";
const myPrivateVariable_ = "Hoshimiya";
const obj1 = { "last_name": "Hoshimiya" }; // if an object key is wrapped in quotation mark, then it's valid
const obj2 = { "first_name": first_name };
const { last_name: lastName } = obj;

function doSomething() {} // function declarations must be camelCase but...
do_something(); // ...snake_case function calls are allowed
function foo({ snake_case: camelCase = "default value" }) {}

class PascalCaseClass {}

import { not_camelCased as camelCased } from "external-module.js";
export * as camelCased from "mod.ts";

enum PascalCaseEnum {
  PascalCaseVariant,
}

type PascalCaseType = { someProperty: number };

interface PascalCaseInterface {
  someProperty: number;
}
```

---

### default-param-last

Enforces default parameter(s) to be last in the function signature.

**Don't:**
```js
function f(a = 2, b) {}
function f(a = 5, b, c = 5) {}
```

**Do:**
```js
function f() {}
function f(a) {}
function f(a = 5) {}
function f(a, b = 5) {}
function f(a, b = 5, c = 5) {}
function f(a, b = 5, ...c) {}
function f(a = 2, b = 3) {}
```

---

### no-useless-rename

Disallow useless rename operations where both the original and new name are exactly the same. This is often a leftover from a refactoring procedure and can be safely removed.

**Don't:**
```js
import { foo as foo } from "foo";
const { foo: foo } = obj;
export { foo as foo };
```

**Do:**
```js
import { foo as bar } from "foo";
const { foo: bar } = obj;
export { foo as bar };
```

---

### prefer-ascii

Ensures that the code is fully written in ASCII characters.

**Don't:**
```js
const π = Math.PI;

// string literals are also checked
const ninja = "🥷";

function こんにちは(名前: string) {
  console.log(`こんにちは、${名前}さん`);
}

// “comments” are also checked
// ^        ^
// |        U+201D
// U+201C
```

**Do:**
```js
const pi = Math.PI;

const ninja = "ninja";

function hello(name: string) {
  console.log(`Hello, ${name}`);
}

// "comments" are also checked
```

---

### single-var-declarator

Disallows multiple variable definitions in the same declaration statement.

**Don't:**
```js
const foo = 1, bar = "2";
```

**Do:**
```js
const foo = 1;
const bar = "2";
```

---
