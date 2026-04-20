# Correctness

Rules that catch actual bugs — wrong assignments, unreachable code, broken control flow.

**55 recommended** (enabled by default) | **14 optional** (enable individually)

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

### noInvalidGridAreas

Disallows invalid named grid areas in CSS Grid Layouts.

**Don't:**
```js
a { grid-template-areas: "a a"
                         "b b b"; }
```

**Do:**
```js
a { grid-template-areas: "a a a"
                         "b b b"; }
```

---

### noInvalidPositionAtImportRule

Disallow the use of @import at-rules in invalid positions.

**Don't:**
```js
a {}
@import 'foo.css';
```

**Do:**
```js
@import 'foo.css';
a {}
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

### noMissingVarFunction

Disallow missing var function for css variables.

**Don't:**
```css
a {
  --foo: red;
  color: --foo;
}
```

**Do:**
```css
p {
  color: var(--foo);
}
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

### noQwikUseVisibleTask

Disallow useVisibleTask$() functions in Qwik components.

**Don't:**
```js
useVisibleTask$(() => {
  console.log('Component is visible');
});
```

**Do:**
```js
useTask$(() => {
  console.log('Task executed');
});
```

---

### noRenderReturnValue

Prevent the usage of the return value of React.render.

**Don't:**
```js
const foo = ReactDOM.render(<div />, document.body);
```

**Do:**
```js
ReactDOM.render(<div />, document.body);
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

### noUnknownFunction

Disallow unknown CSS value functions.

**Don't:**
```js
a { transform: unknown(1); }
```

**Do:**
```js
a { transform: scale(1); }
```

---

### noUnknownMediaFeatureName

Disallow unknown media feature names.

**Don't:**
```css
@media screen and (unknown > 320px) {}
```

**Do:**
```css
@media screen and (width > 320px) {}
```

---

### noUnknownProperty

Disallow unknown properties.

**Don't:**
```js
a {
  colr: blue;
}
```

**Do:**
```css
a {
  color: green;
}
```

---

### noUnknownPseudoClass

Disallow unknown pseudo-class selectors.

**Don't:**
```js
a:unknown {}
```

**Do:**
```js
a:hover {}
```

---

### noUnknownPseudoElement

Disallow unknown pseudo-element selectors.

**Don't:**
```js
a::pseudo {}
```

**Do:**
```js
a:before {}
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

### noUnknownUnit

Disallow unknown CSS units.

**Don't:**
```js
a {
  width: 10pixels;
}
```

**Do:**
```js
a {
  width: 10px;
}
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
```ts
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

### noUnusedVariables

Disallow unused variables.

**Don't:**
```js
let a = 4;
a++;
```

**Do:**
```js
function foo(b) {
    console.log(b)
};
foo();
```

---

### noVoidTypeReturn

Disallow returning a value from a function with the return type 'void'

**Don't:**
```js
class A {
    f(): void {
        return undefined;
    }
}
```

**Do:**
```js
class A {
    f() {
        return undefined;
    }
}
```

---

### noVueDataObjectDeclaration

Enforce that Vue component data options are declared as functions.

**Don't:**
```js
// component-local data via function
export default {
  /* ✗ BAD */
  data: { foo: null },
};
```

**Do:**
```js
// component-local data via function
export default {
  /* ✓ GOOD */
  data() {
    return { foo: null };
  }
};
```

---

### noVueReservedProps

Disallow reserved names to be used as props.

**Don't:**
```js
import {defineComponent} from 'vue';

export default defineComponent({
    props: [
        'key',
    ]
});
```

**Do:**
```js
import {defineComponent} from 'vue';

export default defineComponent({
    props: ['foo']
});
```

---

### useExhaustiveDependencies

Enforce correct dependency usage within React hooks.

**Don't:**
```js
import { useEffect } from "react";

function component() {
  let a = 1;
  useEffect(() => {
    console.log(a);
  }, []);
}
```

**Do:**
```js
import { useEffect } from "react";

function component() {
  let a = 1;
  useEffect(() => {
    console.log(a);
  }, [a]);
}
```

---

### useGraphqlNamedOperations

Enforce specifying the name of GraphQL operations.

**Don't:**
```js
query {}
```

**Do:**
```js
query Human {
  name
}
```

---

### useHookAtTopLevel

Enforce that all React hooks are being called from the Top Level component functions.

**Don't:**
```js
function Component1({ a }) {
    if (a == 1) {
        useEffect();
    }
}
```

**Do:**
```js
function Component1() {
    useEffect();
}
```

---

### useImageSize

Enforces that <img> elements have both width and height attributes.

**Don't:**
```jsx
<img src="/image.png"/>
```

**Do:**
```jsx
<img width="200" height="600" src="/static/images/portrait-01.webp" />
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

### useJsxKeyInIterable

Disallow missing key props in iterators/collection literals.

**Don't:**
```js
[<Hello />];
```

**Do:**
```js
[<Hello key="first" />, <Hello key="second" />, <Hello key="third" />];
{items.map(item => <li key={item.id}>{item}</li>)}
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

### useQwikClasslist

Prefer using the class prop as a classlist over the classnames helper.

**Don't:**
```jsx
<div class={classnames({ active: true, disabled: false })} />
```

**Do:**
```jsx
<div class={{ active: true, disabled: false }} />
```

---

### useQwikMethodUsage

Disallow use* hooks outside of component$ or other use* hooks in Qwik applications.

**Don't:**
```js
import { useSignal } from "@builder.io/qwik";

export const Counter = () => {
  const count = useSignal(0);
};
```

**Do:**
```js
import { component$, useSignal } from "@builder.io/qwik";

export const Counter = component$(() => {
  const count = useSignal(0);
});

export const useCounter = () => {
  const count = useSignal(0);
  return count;
};
```

---

### useQwikValidLexicalScope

Disallow unserializable expressions in Qwik dollar ($) scopes.

**Don't:**
```js
// Arrow function assigned without wrapping it in $(...)
const handleClick = () => {
  console.log("clicked");
};
```

**Do:**
```js
const handleClick = $(() => {
  // Valid: only using serializable variables or props
  console.log("clicked");
});
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

### noNestedComponentDefinitions

Disallows defining React components inside other components.

**Don't:**
```js
function ParentComponent() {
  function ChildComponent() {
    return <div>Hello</div>;
  }

  return <ChildComponent />;
}
```

**Do:**
```js
function ChildComponent() {
  return <div>Hello</div>;
}

function ParentComponent() {
  return <ChildComponent />;
}
```

---

### noNextAsyncClientComponent

Prevent client components from being async functions.

**Don't:**
```js
"use client";

export default async function MyComponent() {
  return <div>Hello</div>;
}
```

**Do:**
```js
"use client";

export default function MyComponent() {
  return <div>Hello</div>;
}
```

---

### noNodejsModules

Forbid the use of Node.js builtin modules.

**Don't:**
```js
import fs from "fs";
```

**Do:**
```js
import fs from "fs-custom";
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

### noReactPropAssignments

Disallow assigning to React component props.

**Don't:**
```js
function Foo(props) {
	props.bar = "Hello " + props.bar;

	return <div>{props.bar}</div>
}
```

**Do:**
```js
const Foo = function({bar}) {
   bar = "Hello " + bar;
   return <div>{bar}</div>
 }
```

---

### noRestrictedElements

Disallow the use of configured elements.

**Don't:**
```jsx
<input />
```

**Do:**
```jsx
<TextField />
```

---

### noSolidDestructuredProps

Disallow destructuring props inside JSX components in Solid projects.

**Don't:**
```js
let Component = ({}) => <div />;
```

**Do:**
```js
let Component = (props) => <div />;
```

---

### noUndeclaredVariables

Prevents the usage of variables that haven't been declared inside the document.

**Don't:**
```js
foobar;
```

**Do:**
```ts
type B<T> = PromiseLike<T>
```

---

### noVueSetupPropsReactivityLoss

Disallow destructuring of props passed to setup in Vue projects.

**Don't:**
```js
export default {
  setup({ count }) {
    return () => h('div', count);
  }
}
```

**Do:**
```js
export default {
  setup(props) {
    return () => h('div', props.count);
  }
}
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

### useUniqueElementIds

Prevent the usage of static string literal id attribute on elements.

**Don't:**
```jsx
<div id="foo">bar</div>;
```

**Do:**
```js
const id = useId();
<div id={id}>bar</div>;
```

---
