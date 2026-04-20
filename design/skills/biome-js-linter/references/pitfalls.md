# Pitfalls & Suspicious Patterns

Patterns that are likely wrong or unintended — potential typos, dubious comparisons, misused operators, debug leftovers.

**49 recommended** | **14 optional**

## Recommended Rules

### noApproximativeNumericConstant

Use standard constants instead of approximated literals.

**Don't:**
```js
let x = 3.141;
```

**Do:**
```js
let x = Math.PI;
let y = 3.14;
```

---

### noArrayIndexKey

Discourage the usage of Array index in keys.

**Don't:**
```js
something.forEach((Element, index) => {
    <Component key={index} >foo</Component>
});
```

**Do:**
```js
something.forEach((item) => {
    <Component key={item.id} >foo</Component>
});
```

---

### noAssignInExpressions

Disallow assignments in expressions.

**Don't:**
```js
let a, b;
a = (b = 1) + 1;
```

**Do:**
```js
let a;
a = 1;
```

---

### noAsyncPromiseExecutor

Disallows using an async function as a Promise executor.

**Don't:**
```js
new Promise(async function foo(resolve, reject) {})
```

**Do:**
```js
new Promise((resolve, reject) => {})
  new Promise((resolve, reject) => {}, async function unrelated() {})
  new Foo(async (resolve, reject) => {})
  new Foo((( (resolve, reject) => {} )))
```

---

### noCatchAssign

Disallow reassigning exceptions in catch clauses.

**Don't:**
```js
try {

} catch (e) {
  e;
  e = 10;
}
```

**Do:**
```js
try {

} catch (e) {
  let e = 10;
  e = 100;
}
```

---

### noClassAssign

Disallow reassigning class members.

**Don't:**
```js
class A {}
A = 0;
```

**Do:**
```js
let A = class A {}
A = 0; // A is a variable.
```

---

### noCompareNegZero

Disallow comparing against -0

**Don't:**
```js
(1 >= -0)
```

**Do:**
```js
(1 >= 0)
```

---

### noConfusingLabels

Disallow labeled statements that are not loops.

**Don't:**
```js
label: f();
```

**Do:**
```js
outer: while (a) {
    while(b) {
        break outer;
    }
}
```

---

### noConstEnum

Disallow TypeScript const enum

**Don't:**
```js
const enum Status {
  Open,
  Close,
}
```

**Do:**
```js
enum Status {
  Open,
  Close,
}
```

---

### noControlCharactersInRegex

Prevents from having control characters and some escape sequences that match control characters in regular expression literals.

**Don't:**
```js
var pattern1 = /\x00/;
```

**Do:**
```js
var pattern1 = /\x20/;
var pattern2 = /\u0020/;
var pattern3 = /\u{20}/u;
var pattern4 = /\t/;
var pattern5 = /\n/;
```

---

### noDebugger

Disallow the use of debugger

**Don't:**
```js
debugger;
```

**Do:**
```js
const test = { debugger: 1 };
test.debugger;
```

---

### noDoubleEquals

Require the use of === and !==.

**Don't:**
```js
foo == bar
```

**Do:**
```js
foo == null
```

---

### noDuplicateCase

Disallow duplicate case labels.

**Don't:**
```js
switch (a) {
    case 1:
        break;
    case 1:
        break;
    default:
        break;
}
```

**Do:**
```js
switch (a) {
    case 1:
        break;
    case 2:
        break;
    default:
        break;
}
```

---

### noDuplicateClassMembers

Disallow duplicate class members.

**Don't:**
```js
class Foo {
  bar() { }
  bar() { }
}
```

**Do:**
```js
class Foo {
  bar() { }
  qux() { }
}
```

---

### noDuplicateCustomProperties

Disallow duplicate custom properties within declaration blocks.

**Don't:**
```js
a { --custom-property: pink; --custom-property: orange;  }
```

**Do:**
```js
a { --custom-property: pink; }
```

---

### noDuplicateElseIf

Disallow duplicate conditions in if-else-if chains

**Don't:**
```js
if (a) {
    foo();
} else if (b) {
    bar();
} else if (b) {
    baz();
}
```

**Do:**
```js
if (a) {
    foo();
} else if (b) {
    bar();
} else if (c) {
    baz();
}
```

---

### noDuplicateParameters

Disallow duplicate function parameter name.

**Don't:**
```js
var f = function(a, b, b) {}
```

**Do:**
```js
function i(i, b, c) {}
var j = function (j, b, c) {};
function k({ k, b }, { c, d }) {}
function l([, l]) {}
function foo([[a, b], [c, d]]) {}
```

---

### noDuplicateSelectorsKeyframeBlock

Disallow duplicate selectors within keyframe blocks.

**Don't:**
```js
@keyframes foo { from {} from {} }
```

**Do:**
```js
@keyframes foo { 0% {} 100% {} }
```

---

### noExportsInTest

Disallow using export or module.exports in files containing tests

**Don't:**
```js
export function myHelper() {}
describe('a test', () => {
    expect(1).toBe(1);
});
```

**Do:**
```js
function myHelper() {}
describe('a test', () => {
    expect(1).toBe(1);
});
```

---

### noFallthroughSwitchClause

Disallow fallthrough of switch clauses.

**Don't:**
```js
switch (bar) {
	case 0:
		a();
	case 1:
		b();
}
```

**Do:**
```js
switch (foo) {
	case 1:
    case 2:
		doSomething();
		break;
    case 3: {
        if (cond) {
            break;
        } else {
            break;
        }
    }
	case 4:
		doSomething();
}
```

---

### noFocusedTests

Disallow focused tests.

**Don't:**
```js
describe.only("foo", () => {});
```

**Do:**
```js
test("foo", () => {});
```

---

### noFunctionAssign

Disallow reassigning function declarations.

**Don't:**
```js
function foo() { };
foo = bar;
```

**Do:**
```js
function foo() {
    var foo = bar;
 }
```

---

### noGlobalAssign

Disallow assignments to native objects and read-only global variables.

**Don't:**
```js
Object = null;
```

**Do:**
```js
a = 0;
```

---

### noGlobalIsFinite

Use Number.isFinite instead of global isFinite.

**Don't:**
```js
isFinite(false); // true
```

**Do:**
```js
Number.isFinite(false); // false
```

---

### noGlobalIsNan

Use Number.isNaN instead of global isNaN.

**Don't:**
```js
isNaN({}); // true
```

**Do:**
```js
Number.isNaN({}); // false
```

---

### noImplicitAnyLet

Disallow use of implicit any type on variable declarations.

**Don't:**
```js
var a;
a = 2;
```

**Do:**
```js
var a = 1;
let a:number;
var b: number
var b =10;
```

---

### noImportantInKeyframe

Disallow invalid !important within keyframe declarations

**Don't:**
```js
@keyframes foo {
    from {
      opacity: 0;
    }
    to {
      opacity: 1 !important;
    }
}
```

**Do:**
```js
@keyframes foo {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
}
```

---

### noIrregularWhitespace

Disallows the use of irregular whitespace characters.

**Don't:**
```js
letcount;
```

**Do:**
```js
const count = 1;
```

---

### noLabelVar

Disallow labels that share a name with a variable

**Don't:**
```js
const x1 = "test";
x1: expr;
```

**Do:**
```js
const x = "test";
z: expr;
```

---

### noMisleadingCharacterClass

Disallow characters made with multiple code points in character class syntax.

**Don't:**
```js
/^[Á]$/u;
```

**Do:**
```js
/^[abc]$/;
/^[👍]$/u;
/^[\q{👶🏻}]$/v;
```

---

### noMisrefactoredShorthandAssign

Disallow shorthand assign when variable appears on both sides.

**Don't:**
```js
a += a + b
```

**Do:**
```js
a += b
```

---

### noNonNullAssertedOptionalChain

Disallow non-null assertions after optional chaining expressions.

**Don't:**
```js
obj?.prop!;
```

**Do:**
```js
obj?.prop;
```

---

### noOctalEscape

Disallow octal escape sequences in string literals

**Don't:**
```js
const foo = "Copyright \251";
```

**Do:**
```js
const foo = "Copyright \u00A9"; // unicode escape
const bar = "Copyright \xA9"; // hexadecimal escape
```

---

### noPrototypeBuiltins

Disallow direct use of Object.prototype builtins.

**Don't:**
```js
var invalid = foo.hasOwnProperty("bar");
```

**Do:**
```js
var valid = Object.hasOwn(foo, "bar");
var valid = Object.prototype.isPrototypeOf.call(foo, bar);
var valid = {}.propertyIsEnumerable.call(foo, "bar");
```

---

### noRedeclare

Disallow variable, function, class, and type redeclarations in the same scope.

**Don't:**
```js
var a = 3;
var a = 10;
```

**Do:**
```js
var a = 3;
a = 10;
```

---

### noSparseArray

Prevents the use of sparse arrays (arrays with holes).

**Don't:**
```js
[1,,2]
```

**Do:**
```js
[1, undefined, 2]
```

---

### noTemplateCurlyInString

Disallow template literal placeholder syntax in regular strings.

**Don't:**
```js
const a = "Hello ${name}!";
```

**Do:**
```js
const a = `Hello ${name}!`;
const a = `Time: ${12 * 60 * 60 * 1000}`;

const a = templateFunction`Hello ${name}`;
```

---

### noThenProperty

Disallow then property.

**Don't:**
```js
export {then};
```

**Do:**
```js
export {then as success};
```

---

### noTsIgnore

Prevents the use of the TypeScript directive @ts-ignore.

**Don't:**
```js
// @ts-ignore
let foo;
```

**Do:**
```js
// @ts-expect-error
let foo;
```

---

### noUnsafeDeclarationMerging

Disallow unsafe declaration merging between interfaces and classes.

**Don't:**
```js
interface Foo {
    f(): void
}

class Foo {}

const foo = new Foo();
foo.f(); // Runtime Error: Cannot read properties of undefined.
```

**Do:**
```js
interface Foo {}
class Bar implements Foo {}
```

---

### noUnsafeNegation

Disallow using unsafe negation.

**Don't:**
```js
!1 in [1,2];
```

**Do:**
```js
-1 in [1,2];
~1 in [1,2];
typeof 1 in [1,2];
void 1 in [1,2];
delete 1 in [1,2];
+1 instanceof [1,2];
```

---

### noUselessEscapeInString

Disallow unnecessary escapes in string literals.

**Don't:**
```js
a::after {
  content: "\z"
}
```

**Do:**
```js
a::after {
  content: "\""
}
```

---

### noUselessRegexBackrefs

Disallow useless backreferences in regular expression literals that always match an empty string.

**Don't:**
```js
/(a)|b\1/;
```

**Do:**
```js
/(a)\1/;
```

---

### useAdjacentOverloadSignatures

Disallow the use of overload signatures that are not next to each other.

**Don't:**
```js
type Foo = {
  foo_type(s: string): void;
  foo_type(n: number): void;
  bar_type(): void;
  foo_type(sn: string | number): void;
};
```

**Do:**
```js
declare namespace Foo {
  export function foo_declare(s: string): void;
  export function foo_declare(n: number): void;
  export function foo_declare(sn: string | number): void;
  export function bar_declare(): void;
}
```

---

### useDefaultSwitchClauseLast

Enforce default clauses in switch statements to be last

**Don't:**
```js
switch (foo) {
    default:
        break;
    case 0:
        break;
}
```

**Do:**
```js
switch (foo) {
    case 0:
        break;
    case 1:
    default:
        break;
}
```

---

### useGetterReturn

Enforce get methods to always return a value.

**Don't:**
```js
class Person {
    get firstName() {}
}
```

**Do:**
```js
class Person {
    get firstName() {
        return this.fullname.split(" ")[0];
    }
}
```

---

### useIsArray

Use Array.isArray() instead of instanceof Array.

**Don't:**
```js
const xs = [];
if (xs instanceof Array) {}
```

**Do:**
```js
const xs = [];
if (Array.isArray(xs)) {}
```

---

### useIterableCallbackReturn

Enforce consistent return values in iterable callbacks.

**Don't:**
```js
[].map(() => {
    // Missing return value
});
```

**Do:**
```js
[].map(() => {
    return 1; // Correctly returns a value
});
```

---

### useNamespaceKeyword

Require using the namespace keyword over the module keyword to declare TypeScript namespaces.

**Don't:**
```js
module Example {}
```

**Do:**
```js
namespace Example {}
```

---

## Optional Rules

### noBitwiseOperators

Disallow bitwise operators.

**Don't:**
```js
let x = y | z;
```

**Do:**
```js
let x = y || z;
```

---

### noConstantBinaryExpressions

Disallow expressions where the operation doesn't affect the value

**Don't:**
```js
const value1 = +x == null;
```

**Do:**
```js
const value1 = x == null;
```

---

### noEmptyBlockStatements

Disallow empty block statements and static blocks.

**Don't:**
```js
function emptyFunctionBody () {}
```

**Do:**
```js
function foo () {
    doSomething();
}
```

---

### noEmptySource

Disallow empty sources.

**Do:**
```js
query Member {}
```

---

### noEvolvingTypes

Disallow variables from evolving into any type through reassignments.

**Don't:**
```js
let a;
```

**Do:**
```js
let a: number;
let b = 1;
var c : string;
var d = "abn";
const e: never[] = [];
const f = [null];
const g = ['1'];
const h = [1];
let workspace: Workspace | null = null;
```

---

### noMisplacedAssertion

Checks that the assertion function, for example expect, is placed inside an it() function call.

**Don't:**
```js
describe("describe", () => {
    expect()
})
```

**Do:**
```js
import assert from "node:assert";
describe("describe", () => {
    it("it", () => {
        assert.equal()
    })
})
```

---

### noUnusedExpressions

Disallow expression statements that are neither a function call nor an assignment.

**Don't:**
```js
0
```

**Do:**
```js
{} // In this context, this is a block statement, not an object literal

{ myLabel: foo() } // In this context, this is a block statement with a label and expression, not an object literal

function namedFunctionDeclaration () {}

(function aGenuineIIFE () {}());

f()

a = 0

new C

delete a.b

void a
```

---

### noVar

Disallow the use of var

**Don't:**
```js
var foo = 1;
```

**Do:**
```js
const foo = 1;
let bar = 1;
```

---

### useAwait

Ensure async functions utilize await.

**Don't:**
```js
async function fetchData() {
// Missing `await` for the promise returned by `fetch`
  return fetch('/data');
}
```

**Do:**
```js
async function fetchData() {
  const response = await fetch('/data');
  const data = await response.json();
  return data;
}

// This rule does not warn about non-async functions
function processData() {
  return compute(data);
}

// Nor does it warn about empty `async` functions
async function noop() { }

// Async generators that use `yield*` with an async iterable
async function* delegateToAsyncIterable() {
  yield* otherAsyncIterable();
}
```

---

### useDeprecatedDate

Require the @deprecated directive to specify a deletion date.

**Don't:**
```js
query {
  member @deprecated(reason: "Use `members` instead") {
    id
  }
}
```

**Do:**
```js
query {
  member @deprecated(reason: "Use `members` instead", deletionDate: "2099-12-25") {
    id
  }
}
```

---

### useErrorMessage

Enforce passing a message value when creating a built-in error.

**Don't:**
```js
throw Error();
```

**Do:**
```js
throw Error('Unexpected property.');
```

---

### useGuardForIn

Require for-in loops to include an if statement.

**Don't:**
```js
for (key in foo) {
  doSomething(key);
}
```

**Do:**
```js
for (key in foo) {
  if (Object.hasOwn(foo, key)) {
   doSomething(key);
  }
}
```

---

### useNumberToFixedDigitsArgument

Enforce using the digits argument with Number#toFixed().

**Don't:**
```js
const string = number.toFixed();
```

**Do:**
```js
const string = foo.toFixed(0);
```

---

### useStaticResponseMethods

Use static Response methods instead of new Response() constructor when possible.

**Don't:**
```js
new Response(JSON.stringify({ value: 1 }));
```

**Do:**
```js
// JSON.stringify() with a replacer function
new Response(JSON.stringify({ value: 0 }, () => {}))
```

---
