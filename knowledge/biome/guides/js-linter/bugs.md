# Bugs & Correctness

Rules that catch real bugs — wrong assignments, unreachable code, broken control flow, incorrect operations.

**32 recommended** | **5 optional**

## Recommended Rules

### noConstAssign

Prevents from having const variables being re-assigned.

**Don't:**
```js
const a = 1;
a = 4;
```

**Do:**
```js
const a = 10;
let b = 10;
b = 20;
```

---

### noConstantCondition

Disallow constant expressions in conditions

**Don't:**
```js
if (false) {
    doSomethingUnfinished();
}
```

**Do:**
```js
if (x === 0) {
    doSomething();
}

for (;;) {
    doSomethingForever();
}

while (typeof x === "undefined") {
    doSomething();
}

do {
    doSomething();
} while (x);

var result = x !== 0 ? a : b;

// Exception
while (true) {
    if (x) { break; }
    x = f();
}
```

---

### noConstantMathMinMaxClamp

Disallow the use of Math.min and Math.max to clamp a value where the result itself is constant.

**Don't:**
```js
Math.min(0, Math.max(100, x));
```

**Do:**
```js
Math.min(100, Math.max(0, x));
```

---

### noConstructorReturn

Disallow returning a value from a constructor.

**Don't:**
```js
class A {
    constructor() {
        return 0;
    }
}
```

**Do:**
```js
class A {
    constructor() {}
}
```

---

### noEmptyCharacterClassInRegex

Disallow empty character classes in regular expression literals.

**Don't:**
```js
/^a[]/.test("a"); // false
```

**Do:**
```js
/^a[xy]/.test("ay"); // true
```

---

### noEmptyPattern

Disallows empty destructuring patterns.

**Don't:**
```js
var {} = foo;
```

**Do:**
```js
var {a = {}} = foo;
var {a, b = {}} = foo;
var {a = []} = foo;
function foo({a = {}}) {}
function foo({a = []}) {}
var [a] = foo;
```

---

### noGlobalObjectCalls

Disallow calling global object properties as functions

**Don't:**
```js
var math = Math();
```

**Do:**
```js
function area(r) {
    return Math.PI * r * r;
}

var object = JSON.parse("{}");

var value = Reflect.get({ x: 1, y: 2 }, "x");

var first = Atomics.load(foo, 0);

var segmenterFr = new Intl.Segmenter("fr", { granularity: "word" });
```

---

### noInnerDeclarations

Disallow function and var declarations that are accessible outside their block.

**Don't:**
```js
if (test) {
    var x = 1;
}
```

**Do:**
```js
// inside a module, function declarations are block-scoped and thus allowed.
if (test) {
    function f() {}
}
export {}
```

---

### noInvalidBuiltinInstantiation

Ensure that builtins are correctly instantiated.

**Don't:**
```js
const text = new BigInt(1);
```

**Do:**
```js
const text = BigInt(1);
```

---

### noInvalidConstructorSuper

Prevents the incorrect use of super() inside classes. It also checks whether a call super() is missing from classes that extends other constructors.

**Don't:**
```js
class A {
    constructor() {
        super();
    }
}
```

**Do:**
```js
export default class A extends B {
    constructor() {
        super();
    }
}
```

---

### noInvalidDirectionInLinearGradient

Disallow non-standard direction values for linear gradient functions.

**Don't:**
```js
.foo { background: linear-gradient(top, #fff, #000); }
```

**Do:**
```js
.foo { background: linear-gradient(to top, #fff, #000); }
```

---

### noInvalidUseBeforeDeclaration

Disallow the use of variables, function parameters, classes, and enums before their declaration

**Don't:**
```js
function f() {
    console.log(x);
    let x;
}
```

**Do:**
```js
f();
function f() {}
```

---

### noNonoctalDecimalEscape

Disallow \8 and \9 escape sequences in string literals.

**Don't:**
```js
const x = "\8";
```

**Do:**
```js
const x = "8";
```

---

### noPrecisionLoss

Disallow literal numbers that lose precision

**Don't:**
```js
const x = 9007199254740993
```

**Do:**
```js
const x = 12345
const x = 123.456
const x = 123e34
const x = 12300000000000000000000000
const x = 0x1FFFFFFFFFFFFF
const x = 9007199254740991
const x = 9007_1992547409_91
```

---

### noSelfAssign

Disallow assignments where both sides are exactly the same.

**Don't:**
```js
a = a;
```

**Do:**
```js
a &= a;
var a = a;
let a = a;
const a = a;
[a, b] = [b, a];
```

---

### noSetterReturn

Disallow returning a value from a setter

**Don't:**
```js
class A {
    set foo(x) {
        return x;
    }
}
```

**Do:**
```js
// early-return
class A {
    set foo(x) {
        if (x) {
            return;
        }
    }
}
```

---

### noStringCaseMismatch

Disallow comparison of expressions modifying the string case with non-compliant value.

**Don't:**
```js
if (s.toUpperCase() === "Abc") {}
```

**Do:**
```js
if (s.toUpperCase() === "ABC") {}
while (s.toLowerCase() === "abc") {}
for (;s.toLocaleLowerCase() === "ABC";) {}
while (s.toLocaleUpperCase() === "abc") {}
for (let s = "abc"; s === "abc"; s = s.toUpperCase()) {}
```

---

### noSwitchDeclarations

Disallow lexical declarations in switch clauses.

**Don't:**
```js
switch (foo) {
    case 0:
        const x = 1;
        break;
    case 2:
        x; // `x` can be used while it is not initialized
        break;
}
```

**Do:**
```js
switch (foo) {
    case 0: {
        const x = 1;
        break;
    }
    case 1:
        // `x` is not visible here
        break;
}
```

---

### noUnknownTypeSelector

Disallow unknown type selectors.

**Don't:**
```js
unknown {}
```

**Do:**
```js
input {}
```

---

### noUnmatchableAnbSelector

Disallow unmatchable An+B selectors.

**Don't:**
```js
a:nth-child(0) {}
```

**Do:**
```js
a:nth-child(1) {}
```

---

### noUnreachableSuper

Ensures the super() constructor is called exactly once on every code path in a class constructor before this is accessed if the class has a superclass

**Don't:**
```js
class A extends B {
    constructor() {}
}
```

**Do:**
```js
export default class A extends B {
    constructor() {
        super();
    }
}
```

---

### noUnsafeFinally

Disallow control flow statements in finally blocks.

**Don't:**
```js
(() => {
    try {
        return 1; // 1 is returned but suspended until finally block ends
    } catch(err) {
        return 2;
    } finally {
        return 3; // 3 is returned before 1, which we did not expect
    }
})();
```

**Do:**
```js
let foo = function() {
    try {
        return 1;
    } catch(err) {
        return 2;
    } finally {
        console.log("hola!");
    }
};
```

---

### noUnsafeOptionalChaining

Disallow the use of optional chaining in contexts where the undefined value is not allowed.

**Don't:**
```js
1 in obj?.foo;
```

**Do:**
```js
(obj?.foo)?.();
obj?.foo();
(obj?.foo ?? bar)();
obj?.foo.bar;
obj.foo?.bar;
foo?.()?.bar;
```

---

### noUnusedFunctionParameters

Disallow unused function parameters.

**Don't:**
```js
function foo(myVar) {
    console.log('foo');
}
```

**Do:**
```js
function foo(myVar) {
    console.log(myVar);
}
```

---

### noUnusedImports

Disallow unused imports.

**Don't:**
```js
import A from 'mod';
```

**Do:**
```js
import { A, type B } from 'mod';

function f(arg: B): A {
    return new A(arg);
}
```

---

### noUnusedLabels

Disallow unused labels.

**Don't:**
```js
LOOP: for (const x of xs) {
    if (x > 0) {
        break;
    }
    f(x);
}
```

**Do:**
```js
LOOP: for (const x of xs) {
    if (x > 0) {
        break LOOP;
    }
    f(x);
}
```

---

### noUnusedPrivateClassMembers

Disallow unused private class members

**Don't:**
```js
class OnlyWrite {
  #usedOnlyInWrite = 5;

  method() {
       this.#usedOnlyInWrite = 212;
  }
}
```

**Do:**
```js
class UsedMember {
  #usedMember = 42;

  method() {
       return this.#usedMember;
  }
}
```

---

### useIsNan

Require calls to isNaN() when checking for NaN.

**Don't:**
```js
123 == NaN
```

**Do:**
```js
if (Number.isNaN(123) !== true) {}

foo(Number.NaN / 2)

switch(foo) {}
```

---

### useParseIntRadix

Enforce the consistent use of the radix argument when using parseInt().

**Don't:**
```js
parseInt("071");
```

**Do:**
```js
parseInt("071", 10);
parseInt("071", 8);
parseFloat(someValue);
```

---

### useValidForDirection

Enforce "for" loop update clause moving the counter in the right direction.

**Don't:**
```js
for (var i = 0; i < 10; i--) {
}
```

**Do:**
```js
for (var i = 0; i < 10; i++) {
}
```

---

### useValidTypeof

This rule checks that the result of a typeof expression is compared to a valid value.

**Don't:**
```js
typeof foo === "strnig";
```

**Do:**
```js
typeof foo === "string";
```

---

### useYield

Require generator functions to contain yield.

**Don't:**
```js
function* foo() {
  return 10;
}
```

**Do:**
```js
function* foo() {
  yield 5;
  return 10;
}

function foo() {
  return 10;
}

// This rule does not warn on empty generator functions.
function* foo() { }
```

---

## Optional Rules

### noGlobalDirnameFilename

Disallow the use of __dirname and __filename in the global scope.

**Don't:**
```js
const dirname = __dirname;
```

**Do:**
```js
const dirname = import.meta.dirname
const filename = import.meta.filename
const foo = {__filename: import.meta.filename };
if (import.meta.dirname.startsWith("/project/src/")) {}
```

---

### noProcessGlobal

Disallow the use of process global.

**Don't:**
```js
const foo = process.env.FOO;
```

**Do:**
```js
import process from "node:process";

const foo = process.env.FOO;
```

---

### useImportExtensions

Enforce file extensions for relative imports.

**Don't:**
```js
import "./foo";
```

**Do:**
```js
import "biome";
```

---

### useJsonImportAttributes

Enforces the use of with { type: "json" } for JSON module imports.

**Don't:**
```js
import jsonData from './data.json';
```

**Do:**
```js
import jsonData from './data.json' with { type: "json" };

import jsonData from './data.json' with { type: "json", other: "value" };

import code from './script.js'; // Not a JSON import
```

---

### useSingleJsDocAsterisk

Enforce JSDoc comment lines to start with a single asterisk, except for the first one.

**Don't:**
```js
/**
** Description
*/
```

**Do:**
```js
/**
 * Description
 * @public
 */
```

---
