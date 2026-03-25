# Bugs & Correctness

Rules that catch real bugs — wrong assignments, unreachable code, broken control flow, incorrect operations.

**41 recommended** | **0 optional**

## Recommended Rules

### constructor-super

Verifies the correct usage of constructors and calls to super().

**Don't:**
```js
class A {}
class Z {
  constructor() {}
}

class B extends Z {
  constructor() {} // missing super() call
}
class C {
  constructor() {
    super(); // Syntax error
  }
}
class D extends null {
  constructor() {} // illegal constructor
}
class E extends null {
  constructor() { // illegal constructor
    super();
  }
}
```

**Do:**
```js
class A {}
class B extends A {}
class C extends A {
  constructor() {
    super();
  }
}
class D extends null {}
```

---

### for-direction

Requires for loop control variables to increment in the correct direction.

**Don't:**
```js
// Infinite loop
for (let i = 0; i < 2; i--) {}
```

**Do:**
```js
for (let i = 0; i < 2; i++) {}
```

---

### getter-return

Requires all property getter functions to return a value.

**Don't:**
```js
let foo = {
  get bar() {},
};

class Person {
  get name() {}
}
```

**Do:**
```js
let foo = {
  get bar() {
    return true;
  },
};

class Person {
  get name() {
    return "alice";
  }
}
```

---

### no-array-constructor

Enforce conventional usage of array construction.

**Don't:**
```js
// This is 4 elements, not a size 100 array of 3 elements
const a = new Array(100, 1, 2, 3);

const b = new Array(); // use [] instead
```

**Do:**
```js
const a = new Array(100);
const b = [];
const c = [1, 2, 3];
```

---

### no-async-promise-executor

Requires that async promise executor functions are not used.

**Don't:**
```js
new Promise(async function (resolve, reject) {});
new Promise(async (resolve, reject) => {});
```

**Do:**
```js
new Promise(function (resolve, reject) {});
new Promise((resolve, reject) => {});
```

---

### no-case-declarations

Requires lexical declarations (let, const, function and class) in switch case or default clauses to be scoped with brackets.

**Don't:**
```js
switch (choice) {
  // `let`, `const`, `function` and `class` are scoped the entire switch statement here
  case 1:
    let a = "choice 1";
    break;
  case 2:
    const b = "choice 2";
    break;
  case 3:
    function f() {
      return "choice 3";
    }
    break;
  default:
    class C {}
}
```

**Do:**
```js
switch (choice) {
  // The following `case` and `default` clauses are wrapped into blocks using brackets
  case 1: {
    let a = "choice 1";
    break;
  }
  case 2: {
    const b = "choice 2";
    break;
  }
  case 3: {
    function f() {
      return "choice 3";
    }
    break;
  }
  default: {
    class C {}
  }
}
```

---

### no-class-assign

Disallows modifying variables of class declarations.

**Don't:**
```js
class A {}
A = 0; // reassigning the class variable itself
```

**Do:**
```js
class A {}
let c = new A();
c = 0; // reassigning the variable `c`
```

---

### no-compare-neg-zero

Disallows comparing against negative zero (-0).

**Don't:**
```js
if (x === -0) {}
```

**Do:**
```js
if (x === 0) {}

if (Object.is(x, -0)) {}
```

---

### no-cond-assign

Disallows the use of the assignment operator, =, in conditional statements.

**Don't:**
```js
let x;
if (x = 0) {
  let b = 1;
}
```

**Do:**
```js
let x;
if (x === 0) {
  let b = 1;
}
```

---

### no-const-assign

Disallows modifying a variable declared as const.

**Don't:**
```js
const a = 0;
a = 1;
a += 1;
a++;
++a;
```

**Do:**
```js
const a = 0;
const b = a + 1;

// `c` is out of scope on each loop iteration, allowing a new assignment
for (const c in [1, 2, 3]) {}
```

---

### no-constant-condition

Disallows the use of a constant expression in conditional test.

**Don't:**
```js
if (true) {}
if (2) {}
do {} while (x = 2); // infinite loop
```

**Do:**
```js
if (x) {}
if (x === 0) {}
do {} while (x === 2);
```

---

### no-control-regex

Disallows the use ASCII control characters in regular expressions.

**Don't:**
```js
// Examples using ASCII (31) Carriage Return (hex x0d)
const pattern1 = /\x0d/;
const pattern2 = /\u000d/;
const pattern3 = new RegExp("\\x0d");
const pattern4 = new RegExp("\\u000d");
```

**Do:**
```js
// Examples using ASCII (32) Space (hex x20)
const pattern1 = /\x20/;
const pattern2 = /\u0020/;
const pattern3 = new RegExp("\\x20");
const pattern4 = new RegExp("\\u0020");
```

---

### no-delete-var

Disallows the deletion of variables.

**Don't:**
```js
const a = 1;
let b = 2;
let c = 3;
delete a; // would return false
delete b; // would return false
delete c; // would return false
```

**Do:**
```js
let obj = {
  a: 1,
};
delete obj.a; // return true
```

---

### no-dupe-args

Disallows using an argument name more than once in a function signature.

**Don't:**
```js
function withDupes(a, b, a) {
  console.log("I'm the value of the second a:", a);
}
```

**Do:**
```js
function withoutDupes(a, b, c) {
  console.log("I'm the value of the first (and only) a:", a);
}
```

---

### no-dupe-class-members

Disallows using a class member function name more than once.

**Don't:**
```js
class Foo {
  bar() {}
  bar() {}
}
```

**Do:**
```js
class Foo {
  bar() {}
  fizz() {}
}
```

---

### no-dupe-else-if

Disallows using the same condition twice in an if/else if statement.

**Don't:**
```js
if (a) {}
else if (b) {}
else if (a) {} // duplicate of condition above

if (a === 5) {}
else if (a === 6) {}
else if (a === 5) {} // duplicate of condition above
```

**Do:**
```js
if (a) {}
else if (b) {}
else if (c) {}

if (a === 5) {}
else if (a === 6) {}
else if (a === 7) {}
```

---

### no-dupe-keys

Disallows duplicate keys in object literals.

**Don't:**
```js
const foo = {
  bar: "baz",
  bar: "qux",
};
```

**Do:**
```js
const foo = {
  bar: "baz",
  quxx: "qux",
};
```

---

### no-duplicate-case

Disallows using the same case clause in a switch statement more than once.

**Don't:**
```js
const someText = "a";
switch (someText) {
  case "a": // (1)
    break;
  case "b":
    break;
  case "a": // duplicate of (1)
    break;
  default:
    break;
}
```

**Do:**
```js
const someText = "a";
switch (someText) {
  case "a":
    break;
  case "b":
    break;
  case "c":
    break;
  default:
    break;
}
```

---

### no-empty-character-class

Disallows using the empty character class in a regular expression.

**Don't:**
```js
/^abc[]/.test("abcdefg"); // false, as `d` does not match an empty character class
"abcdefg".match(/^abc[]/); // null
```

**Do:**
```js
// Without a character class
/^abc/.test("abcdefg"); // true
"abcdefg".match(/^abc/); // ["abc"]

// With a valid character class
/^abc[a-z]/.test("abcdefg"); // true
"abcdefg".match(/^abc[a-z]/); // ["abcd"]
```

---

### no-empty-pattern

Disallows the use of empty patterns in destructuring.

**Don't:**
```js
// In these examples below, {} and [] are not object literals or empty arrays,
// but placeholders for destructured variable names
const {} = someObj;
const [] = someArray;
const {a: {}} = someObj;
const [a: []] = someArray;
function myFunc({}) {}
function myFunc([]) {}
```

**Do:**
```js
const { a } = someObj;
const [a] = someArray;

// Correct way to default destructured variable to object literal
const { a = {} } = someObj;

// Correct way to default destructured variable to empty array
const [a = []] = someArray;

function myFunc({ a }) {}
function myFunc({ a = {} }) {}
function myFunc([a]) {}
function myFunc([a = []]) {}
```

---

### no-ex-assign

Disallows the reassignment of exception parameters.

**Don't:**
```js
try {
  someFunc();
} catch (e) {
  e = true;
  // can no longer access the thrown error
}
```

**Do:**
```js
try {
  someFunc();
} catch (e) {
  const anotherVar = true;
}
```

---

### no-fallthrough

Disallows the implicit fallthrough of case statements.

**Don't:**
```js
switch (myVar) {
  case 1:
    console.log("1");

  case 2:
    console.log("2");
}
// If myVar = 1, outputs both `1` and `2`.  Was this intentional?
```

**Do:**
```js
switch (myVar) {
  case 1:
    console.log("1");
    break;

  case 2:
    console.log("2");
    break;
}
// If myVar = 1, outputs only `1`

switch (myVar) {
  case 1:
    console.log("1");
    /* falls through */
  case 2:
    console.log("2");
}
// If myVar = 1, intentionally outputs both `1` and `2`
```

---

### no-func-assign

Disallows the overwriting/reassignment of an existing function.

**Don't:**
```js
function foo() {}
foo = bar;

const a = function baz() {
  baz = "now I'm a string";
};

myFunc = existingFunc;
function myFunc() {}
```

**Do:**
```js
function foo() {}
const someVar = foo;

const a = function baz() {
  const someStr = "now I'm a string";
};

const anotherFuncRef = existingFunc;

let myFuncVar = function () {};
myFuncVar = bar; // variable reassignment, not function re-declaration
```

---

### no-global-assign

Disallows assignment to native Javascript objects.

**Don't:**
```js
Object = null;
undefined = true;
window = {};
```

---

### no-import-assign

Disallows reassignment of imported module bindings.

**Don't:**
```js
import defaultMod, { namedMod } from "./mod.js";
import * as modNameSpace from "./mod2.js";

defaultMod = 0;
namedMod = true;
modNameSpace.someExportedMember = "hello";
modNameSpace = {};
```

**Do:**
```js
import defaultMod, { namedMod } from "./mod.js";
import * as modNameSpace from "./mod2.js";

// properties of bound imports may be set
defaultMod.prop = 1;
namedMod.prop = true;
modNameSpace.someExportedMember.prop = "hello";
```

---

### no-inner-declarations

Disallows variable or function definitions in nested blocks.

**Don't:**
```js
if (someBool) {
  function doSomething() {}
}

function someFunc(someVal: number): void {
  if (someVal > 4) {
    var a = 10;
  }
}
```

**Do:**
```js
function doSomething() {}
if (someBool) {}

var a = 10;
function someFunc(someVal: number): void {
  var foo = true;
  if (someVal > 4) {
    let b = 10;
    const fn = function doSomethingElse() {};
  }
}
```

---

### no-invalid-regexp

Disallows specifying invalid regular expressions in RegExp constructors.

**Don't:**
```js
const invalidRegExp = new RegExp(")");
```

**Do:**
```js
const goodRegExp = new RegExp(".");
```

---

### no-new-symbol

Disallows the use of new operators with built-in Symbols.

**Don't:**
```js
const foo = new Symbol("foo");
```

**Do:**
```js
const foo = Symbol("foo");

function func(Symbol: typeof SomeClass) {
  // This `Symbol` is not built-in one
  const bar = new Symbol();
}
```

---

### no-obj-calls

Disallows calling built-in global objects like functions.

**Don't:**
```js
const math = Math();
const newMath = new Math();

const json = JSON();
const newJSON = new JSON();

const reflect = Reflect();
const newReflect = new Reflect();

const atomics = Atomics();
const newAtomics = new Atomics();
```

**Do:**
```js
const area = (radius: number): number => Math.PI * radius * radius;

const parsed = JSON.parse("{ foo: 42 }");

const x = Reflect.get({ x: 1, y: 2 }, "x");

const first = Atomics.load(foo, 0);
```

---

### no-octal

Disallows expressing octal numbers via numeric literals beginning with 0.

**Don't:**
```js
const a = 042;
const b = 7 + 042;
```

**Do:**
```js
const a = 0o42;
const b = 7 + 0o42;
const c = "042";
```

---

### no-prototype-builtins

Disallows the use of Object.prototype builtins directly.

**Don't:**
```js
const a = foo.hasOwnProperty("bar");
const b = foo.isPrototypeOf("bar");
const c = foo.propertyIsEnumerable("bar");
```

**Do:**
```js
const a = Object.prototype.hasOwnProperty.call(foo, "bar");
const b = Object.prototype.isPrototypeOf.call(foo, "bar");
const c = Object.prototype.propertyIsEnumerable.call(foo, "bar");
```

---

### no-redeclare

Disallows redeclaration of variables, functions, parameters with the same name.

**Don't:**
```js
var a = 3;
var a = 10;

let b = 3;
let b = 10;

const c = 3;
const c = 10;

function d() {}
function d() {}

function e(arg: number) {
  var arg: number;
}

function f(arg: number, arg: string) {}
```

**Do:**
```js
var a = 3;
function f() {
  var a = 10;
}

if (foo) {
  let b = 2;
} else {
  let b = 3;
}
```

---

### no-self-assign

Disallows self assignments.

**Don't:**
```js
a = a;
[a] = [a];
[a, b] = [a, b];
[a, b] = [a, c];
[a, ...b] = [a, ...b];
a.b = a.b;
```

**Do:**
```js
let a = a;
a += a;
a = [a];
[a, b] = [b, a];
a.b = a.c;
```

---

### no-setter-return

Disallows returning values from setters.

**Don't:**
```js
const a = {
  set foo(x: number) {
    return "something";
  },
};

class B {
  private set foo(x: number) {
    return "something";
  }
}

const c = {
  set foo(x: boolean) {
    if (x) {
      return 42;
    }
  },
};
```

**Do:**
```js
// return without a value is allowed since it is used to do early-return
const a = {
  set foo(x: number) {
    if (x % 2 == 0) {
      return;
    }
  },
};

// not a setter, but a getter
class B {
  get foo() {
    return 42;
  }
}

// not a setter
const c = {
  set(x: number) {
    return "something";
  },
};
```

---

### no-shadow-restricted-names

Disallows shadowing of restricted names.

**Don't:**
```js
const undefined = 42;

function NaN() {}

function foo(Infinity) {}

const arguments = () => {};

try {
} catch (eval) {}
```

**Do:**
```js
// If not assigned a value, `undefined` may be shadowed
const undefined;

const Object = 42;

function foo(a: number, b: string) {}

try {
} catch (e) {}
```

---

### no-this-before-super

Disallows use of this or super before calling super() in constructors.

**Don't:**
```js
class A extends B {
  constructor() {
    this.foo = 0;
    super();
  }
}

class C extends D {
  constructor() {
    super.foo();
    super();
  }
}
```

**Do:**
```js
class A extends B {
  constructor() {
    super();
    this.foo = 0;
  }
}

class C extends D {
  constructor() {
    super();
    super.foo();
  }
}

class E {
  constructor() {
    this.foo = 0;
  }
}
```

---

### no-unreachable

Disallows the unreachable code after the control flow statements.

**Don't:**
```js
function foo() {
  return true;
  console.log("done");
}
```

**Do:**
```js
function foo() {
  return bar();
  function bar() {
    return 1;
  }
}
```

---

### no-unsafe-finally

Disallows the use of control flow statements within finally blocks.

**Don't:**
```js
let foo = function () {
  try {
    return 1;
  } catch (err) {
    return 2;
  } finally {
    return 3;
  }
};
```

**Do:**
```js
let foo = function () {
  try {
    return 1;
  } catch (err) {
    return 2;
  } finally {
    console.log("hola!");
  }
};
```

---

### no-unsafe-negation

Disallows the usage of negation operator ! as the left operand of relational operators.

**Don't:**
```js
if (!key in object) {}
if (!foo instanceof Foo) {}
```

**Do:**
```js
if (!(key in object)) {}
if (!(foo instanceof Foo)) {}
if ((!key) in object) {}
if ((!foo) instanceof Foo) {}
```

---

### use-isnan

Disallows comparisons to NaN.

**Don't:**
```js
if (foo == NaN) {
  // ...
}

if (foo != NaN) {
  // ...
}

switch (NaN) {
  case foo:
    // ...
}

switch (foo) {
  case NaN:
    // ...
}
```

**Do:**
```js
if (isNaN(foo)) {
  // ...
}

if (!isNaN(foo)) {
  // ...
}
```

---

### valid-typeof

Restricts the use of the typeof operator to a specific set of string literals.

**Don't:**
```js
// typo
typeof foo === "strnig";
typeof foo == "undefimed";
typeof bar != "nunber";
typeof bar !== "fucntion";

// compare with non-string literals
typeof foo === undefined;
typeof bar == Object;
typeof baz === anotherVariable;
typeof foo == 5;
```

**Do:**
```js
typeof foo === "undefined";
typeof bar == "object";
typeof baz === "string";
typeof bar === typeof qux;
```

---
