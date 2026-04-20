# Style

Code style consistency — naming, syntax preferences, idiomatic patterns.

**13 recommended** (enabled by default) | **56 optional** (enable individually)

## Recommended Rules

### noDescendingSpecificity

Disallow a lower specificity selector from coming after a higher specificity selector.

**Don't:**
```css
b a { color: red; }
a { color: red; }
```

**Do:**
```css
a { color: red; }
b a { color: red; }
```

---

### noHeadElement

Prevent usage of <head> element in a Next.js project.

**Don't:**
```js
function Index() {
  return (
    <head>
      <title>Invalid</title>
    </head>
  )
}
```

**Do:**
```js
import Head from 'next/head'

function Index() {
  return (
    <Head>
      <title>All good!</title>
    </Head>
  )
}
```

---

### noNonNullAssertion

Disallow non-null assertions using the ! postfix operator.

**Don't:**
```ts
interface Example {
  property?: string;
}
declare const foo: Example;
const includesBaz = foo.property!.includes('baz');
```

**Do:**
```ts
interface Example {
  property?: string;
}

declare const foo: Example;
const includesBaz = foo.property?.includes('baz') ?? false;
```

---

### useArrayLiterals

Disallow Array constructors.

**Don't:**
```js
const xs = Array();
```

**Do:**
```js
const xs = Array(65000);
```

---

### useConst

Require const declarations for variables that are only assigned once.

**Don't:**
```js
let a = 3;
console.log(a);
```

**Do:**
```js
let a = 2;
a = 3;
console.log(a);
```

---

### useDeprecatedReason

Require specifying the reason argument when using @deprecated directive

**Don't:**
```js
query {
  member @deprecated
}
```

**Do:**
```js
query {
  member @deprecated(reason: "Why?")
}
```

---

### useExponentiationOperator

Disallow the use of Math.pow in favor of the ** operator.

**Don't:**
```js
const foo = Math.pow(2, 8);
```

**Do:**
```js
const foo = 2 ** 8;

const bar = a ** b;

let baz = (a + b) ** (c + d);

let quux = (-1) ** n;
```

---

### useExportType

Promotes the use of export type for types.

**Don't:**
```ts
interface I {}
export { I };
```

**Do:**
```js
class C {}
function f() {}
export { C, f };
```

---

### useImportType

Promotes the use of import type for types.

**Don't:**
```ts
import { A } from "./mod.js";
type TypeOfA = typeof A;
let a: A;
```

**Do:**
```ts
import type { A } from "./mod.js";
let a: A;
```

---

### useLiteralEnumMembers

Require all enum members to be literal values.

**Don't:**
```js
const x = 2;
enum Computed {
    A,
    B = x,
}
```

**Do:**
```js
enum Direction {
    Left,
    Right,
}
```

---

### useNodejsImportProtocol

Enforces using the node: protocol for Node.js builtin modules.

**Don't:**
```js
import fs from 'fs';
```

**Do:**
```js
import fs from 'node:fs';

import os from 'node:os';

import path from 'node:path';
```

---

### useShorthandFunctionType

Enforce using function types instead of object type with call signatures.

**Don't:**
```ts
interface Example {
  (): string;
}
```

**Do:**
```ts
type Example = () => string;
```

---

### useTemplate

Prefer template literals over string concatenation.

**Don't:**
```js
const s = foo + "baz";
```

**Do:**
```js
let s = "foo" + "bar" + `baz`;
```

---

## Optional Rules

### noCommonJs

Disallow use of CommonJs module system in favor of ESM style imports.

**Don't:**
```js
require('node:fs');
```

**Do:**
```js
import fs from 'node:fs';
```

---

### noDefaultExport

Disallow default exports.

**Don't:**
```js
export default function f() {};
```

**Do:**
```js
export function f () {};
export class C {};
export { default as X } from "mod";
```

---

### noDoneCallback

Disallow using a callback in asynchronous tests and hooks.

**Don't:**
```js
beforeEach((done) => {
    // ...
});
```

**Do:**
```js
beforeEach(async () => {
    // ...
});
```

---

### noEnum

Disallow TypeScript enum.

**Don't:**
```js
enum Foo {
    BAR = 'bar',
    BAZ = 'baz',
}
```

**Do:**
```js
const Foo = {
    BAR: 'bar',
    BAZ: 'baz',
} as const
```

---

### noExportedImports

Disallow exporting an imported variable.

**Don't:**
```js
import { A } from "mod";
export { A };
```

**Do:**
```js
export { A } from "mod";
export * as ns from "mod";
export { default as D } from "mod";
```

---

### noImplicitBoolean

Disallow implicit true values on JSX boolean attributes

**Don't:**
```jsx
<input disabled />
```

**Do:**
```jsx
<input disabled={false} />
```

---

### noInferrableTypes

Disallow type annotations for variables, parameters, and class properties initialized with a literal expression.

**Don't:**
```js
const variable: 1 = 1;
```

**Do:**
```ts
const variable: number = 1;
```

---

### noJsxLiterals

Disallow string literals inside JSX elements.

**Don't:**
```jsx
<div>Hello World</div>
```

**Do:**
```jsx
<div>{'Hello World'}</div>
```

---

### noMagicNumbers

Reports usage of "magic numbers" — numbers used directly instead of being assigned to named constants.

**Don't:**
```js
let total = price * 1.23; // Magic number for tax rate
```

**Do:**
```js
const TAX_RATE = 1.23;
let total = price * TAX_RATE;
```

---

### noNamespace

Disallow the use of TypeScript's namespaces.

**Don't:**
```js
module foo {}
```

**Do:**
```js
import foo from 'foo';
export { bar };
```

---

### noNegationElse

Disallow negation in the condition of an if statement if it has an else clause.

**Don't:**
```js
if (!cond) { f();} else { g();}
```

**Do:**
```js
if (!cond) { f(); }
```

---

### noNestedTernary

Disallow nested ternary expressions.

**Don't:**
```js
const thing = foo ? bar : baz === qux ? quxx : foobar;
```

**Do:**
```js
const thing = foo ? bar : foobar;
```

---

### noParameterAssign

Disallow reassigning function parameters.

**Don't:**
```js
function f(param) {
    param = 13;
}
```

**Do:**
```js
function f(param) {
    let local = param;
}
```

---

### noParameterProperties

Disallow the use of parameter properties in class constructors.

**Don't:**
```ts
class A {
    constructor(readonly name: string) {}
}
```

**Do:**
```ts
class A {
    constructor(name: string) {}
}
```

---

### noProcessEnv

Disallow the use of process.env.

**Don't:**
```js
if (process.env.NODE_ENV === 'development') {
  // ...
}
```

**Do:**
```js
const config = require('./config');
if (config.NODE_ENV === 'development') {
  // ...
}
```

---

### noRestrictedGlobals

This rule allows you to specify global variable names that you don’t want to use in your application.

**Don't:**
```js
console.log(event)
```

**Do:**
```js
function f(event) {
    console.log(event)
}
```

---

### noRestrictedImports

Disallow specified modules when loaded by import or require.

**Don't:**
```js
import "lodash";
```

**Do:**
```js
import "allowed-import";
const myImport = await import("allowed-import");
const myImport = require("allowed-import");
```

---

### noShoutyConstants

Disallow the use of constants which its value is the upper-case version of its name.

**Don't:**
```js
const FOO = "FOO";
console.log(FOO);
```

**Do:**
```js
let FOO = "FOO";
console.log(FOO);
```

---

### noSubstr

Enforce the use of String.slice() over String.substr() and String.substring().

**Don't:**
```js
foo.substr();
```

**Do:**
```js
foo.slice(beginIndex, endIndex);
```

---

### noUnusedTemplateLiteral

Disallow template literals if interpolation and special-character handling are not needed

**Don't:**
```js
const foo = `bar`
```

**Do:**
```js
const foo = `bar
has newline`;
```

---

### noUselessElse

Disallow else block when the if block breaks early.

**Don't:**
```js
while (x > 0) {
    if (f(x)) {
        break;
    } else {
        x++
    }
}
```

**Do:**
```js
function f(x) {
    if (x < 0) {
        return 0;
    }
    return x;
}
```

---

### noYodaExpression

Disallow the use of yoda expressions.

**Don't:**
```js
if ("red" == value) {}
```

**Do:**
```js
if (value === "red") {}
```

---

### useAsConstAssertion

Enforce the use of as const over literal type and type annotation.

**Don't:**
```js
let bar: 2 = 2;
```

**Do:**
```js
let foo = 'bar';
let foo = 'bar' as const;
let foo: 'bar' = 'bar' as const;
let bar = 'bar' as string;
let foo = { bar: 'baz' };
```

---

### useAtIndex

Use at() instead of integer index access.

**Don't:**
```js
const foo = array[array.length - 1];
```

**Do:**
```js
const foo = array.at(-1);
```

---

### useCollapsedElseIf

Enforce using else if instead of nested if in else clauses.

**Don't:**
```js
if (condition) {
    // ...
} else {
    if (anotherCondition) {
        // ...
    }
}
```

**Do:**
```js
if (condition) {
    // ...
} else if (anotherCondition) {
    // ...
}
```

---

### useCollapsedIf

Enforce using single if instead of nested if clauses.

**Don't:**
```js
if (condition) {
    if (anotherCondition) {
        // ...
    }
}
```

**Do:**
```js
if (condition && anotherCondition) {
    // ...
}
```

---

### useComponentExportOnlyModules

Enforce declaring components only within modules that export React Components exclusively.

**Don't:**
```js
export const foo = () => {};
export const Bar = () => <></>;
```

**Do:**
```js
export default function Foo() {
    return <></>;
}
```

---

### useConsistentArrayType

Require consistently using either T[] or Array<T>

**Don't:**
```js
let invalid: Array<foo>;
```

**Do:**
```ts
const valid: Array<string | number> = ['a', 'b'];
const valid: Array<{ prop: string }> = [{ prop: 'a' }];
const valid: Array<() => void> = [() => {}];
const valid: MyType[] = ['a', 'b'];
const valid: string[] = ['a', 'b'];
const valid: readonly string[] = ['a', 'b'];
```

---

### useConsistentArrowReturn

Enforce consistent arrow function bodies.

**Don't:**
```js
const bar = () => {
     return {
         bar: {
             foo: 1,
             bar: 2,
         }
     };
 };
```

**Do:**
```js
const foo = () => 0;
const bar = () => { "use strict"; return 1 }
const baz = () => { /* intentional */ return x }
const qux = () => ({ a: 1 })   // already concise with parens
```

---

### useConsistentBuiltinInstantiation

Enforce the use of new for all builtins, except String, Number and Boolean.

**Don't:**
```js
const text = new String(10);
```

**Do:**
```js
const text = String(10);
```

---

### useConsistentCurlyBraces

This rule enforces consistent use of curly braces inside JSX attributes and JSX children.

**Don't:**
```jsx
<Foo>{'Hello world'}</Foo>
```

**Do:**
```jsx
<>
    <Foo>Hello world</Foo>
    <Foo foo="bar" />
    <Foo foo={5} />
    <Foo foo={<Bar />} />
</>
```

---

### useConsistentMemberAccessibility

Require consistent accessibility modifiers on class properties and methods.

**Don't:**
```js
class Animal {
  public constructor(breed, name) {
    // ...
  }
}
```

**Do:**
```ts
class Animal {
  constructor(
    private breed,
    name,
  ) {
    this.animalName = name;
  }
  private animalName: string; // Property
  get name(): string {
    // get accessor
    return this.animalName;
  }
  set name(value: string) {
    // set accessor
    this.animalName = value;
  }
  protected walk() {
    // method
  }
}
```

---

### useConsistentObjectDefinitions

Require the consistent declaration of object literals. Defaults to explicit definitions.

**Don't:**
```js
let foo = 1;
let invalid = {
    foo: foo
};
```

**Do:**
```js
let foo = 1;
let valid = {
    foo,
    bar() { return "bar"; },
};
```

---

### useConsistentTypeDefinitions

Enforce type definitions to consistently use either interface or type.

**Don't:**
```ts
type Point = { x: number; y: number; };
```

**Do:**
```ts
interface Point {
  x: number;
  y: number;
}
```

---

### useDefaultParameterLast

Enforce default function parameters and optional function parameters to be last.

**Don't:**
```js
function f(a = 0, b) {}
```

**Do:**
```js
function f(a, b = 0) {}
```

---

### useDefaultSwitchClause

Require the default clause in switch statements.

**Don't:**
```js
switch (a) {
    case 1:
        /* code */
        break;
}
```

**Do:**
```js
switch (a) {
    case 1:
        /* code */
        break;
    default:
        /* code */
        break;
}
```

---

### useEnumInitializers

Require that each enum member value be explicitly initialized.

**Don't:**
```js
enum Version {
    V1,
}
```

**Do:**
```js
enum Status {
    Open = 1,
    Close = 2,
}
```

---

### useExplicitLengthCheck

Enforce explicitly comparing the length, size, byteLength or byteOffset property of a value.

**Don't:**
```js
const isEmpty = !foo.length;
```

**Do:**
```js
const isEmpty = foo.length === 0;
```

---

### useExportsLast

Require that all exports are declared after all non-export statements.

**Don't:**
```js
export const a = 1;
const b = 2;
```

**Do:**
```js
const a = 1;
export const b = 2;
```

---

### useForOf

Prefer using for...of loops over standard for loops where possible.

**Don't:**
```js
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}
```

**Do:**
```js
for (let item of array) {
   console.log(item);
 }
```

---

### useGraphqlNamingConvention

Validates that all enum values are capitalized.

**Don't:**
```js
enum MyEnum {
 value
}
```

**Do:**
```js
enum MyEnum {
 VALUE
}
```

---

### useGroupedAccessorPairs

Enforce that getters and setters for the same property are adjacent in class and object definitions.

**Don't:**
```js
class User {
  get name() { return this._name; }
  constructor() {}
  set name(value) { this._name = value; }
}
```

**Do:**
```js
class User {
  get name() { return this._name; }
  set name(value) { this._name = value; }
  get age() { return this._age; }
  set age(age) { this._age = age; }
}
```

---

### useNodeAssertStrict

Promotes the usage of node:assert/strict over node:assert.

**Don't:**
```js
import * as assert from "node:assert"
```

**Do:**
```js
import * as assert from "node:assert/strict"
```

---

### useNumberNamespace

Use the Number properties instead of global ones.

**Don't:**
```js
parseInt("1"); // true
```

**Do:**
```js
Number.parseInt("1"); // false
```

---

### useNumericSeparators

Enforce the use of numeric separators in numeric literals.

**Don't:**
```js
var a = 1234567890;
```

**Do:**
```js
var a = 1_234_567_890;
```

---

### useObjectSpread

Prefer object spread over Object.assign() when constructing new objects.

**Don't:**
```js
Object.assign({}, foo);
```

**Do:**
```js
({ ...foo });
```

---

### useReactFunctionComponents

Enforce that components are defined as functions and never as classes.

**Don't:**
```js
class Foo extends React.Component {
  render() {
    return (
      <div>This is a class component.</div>
    );
  }
}
```

**Do:**
```js
function Foo() {
  return <div>This is a function component.</div>;
}
```

---

### useReadonlyClassProperties

Enforce marking members as readonly if they are never modified outside the constructor.

**Don't:**
```ts
class Container {
    private onlyModifiedInConstructor = 1;
    constructor(
        member1: number,
    ) {
        this.onlyModifiedInConstructor = onlyModifiedInConstructor;
    }
}
```

**Do:**
```ts
class Container {
    private readonly neverModifiedMember = true;
    private readonly onlyModifiedInConstructor: number;
    readonly #neverModifiedPrivateField = 3;

    public constructor(
        onlyModifiedInConstructor: number,
        private readonly neverModifiedParameter: string,
    ) {
        this.onlyModifiedInConstructor = onlyModifiedInConstructor;
    }
}
```

---

### useSelfClosingElements

Prevent extra closing tags for components without children.

**Don't:**
```jsx
<div></div>
```

**Do:**
```jsx
<div />
```

---

### useShorthandAssign

Require assignment operator shorthand where possible.

**Don't:**
```js
a = a + 1;
```

**Do:**
```js
a += 1;
```

---

### useSingleVarDeclarator

Disallow multiple variable declarations in the same variable statement

**Don't:**
```js
let foo = 0, bar, baz;
```

**Do:**
```js
const foo = 0;
let bar;
let baz;
```

---

### useSymbolDescription

Require a description parameter for the Symbol().

**Don't:**
```js
Symbol();
```

**Do:**
```js
Symbol('description');
```

---

### useThrowNewError

Require new when throwing an error.

**Don't:**
```js
throw Error();
```

**Do:**
```js
throw new Error();
```

---

### useThrowOnlyError

Disallow throwing non-Error values.

**Don't:**
```js
throw undefined;
```

**Do:**
```js
throw new Error();
```

---

### useTrimStartEnd

Enforce the use of String.trimStart() and String.trimEnd() over String.trimLeft() and String.trimRight().

**Don't:**
```js
const foo = bar.trimLeft();
```

**Do:**
```js
const foo = bar.trimStart();
```

---

### useUnifiedTypeSignatures

Disallow overload signatures that can be unified into a single signature.

**Don't:**
```ts
function f(a: number): void;
function f(a: string): void;
```

**Do:**
```ts
function f(a: number | string): void {}
```

---
