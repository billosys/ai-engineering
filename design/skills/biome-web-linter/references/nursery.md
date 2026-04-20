# Nursery (Experimental)

Experimental rules under evaluation. Not recommended by default — enable individually.

**0 recommended** (enabled by default) | **76 optional** (enable individually)

## Optional Rules

### noAmbiguousAnchorText

Disallow ambiguous anchor descriptions.

**Don't:**
```jsx
<a>learn more</a>
```

**Do:**
```jsx
<a>documentation</a>
```

---

### noBeforeInteractiveScriptOutsideDocument

Prevent usage of next/script's beforeInteractive strategy outside of pages/_document.js in a Next.js project.

**Don't:**
```js
// pages/index.jsx
import Script from 'next/script'

export default function Index() {
  return (
    <div>
      <Script
        src="https://example.com/script.js"
        strategy="beforeInteractive"
      ></Script>
    </div>
  )
}
```

**Do:**
```js
// pages/_document.jsx
import { Html, Head, Main, NextScript } from 'next/document'
import Script from 'next/script'

export default function Document() {
    return (
        <Html>
            <Head />
            <body>
                <Main />
                <NextScript />
                <Script
                  src="https://example.com/script.js"
                  strategy="beforeInteractive"
                ></Script>
            </body>
        </Html>
    )
}
```

---

### noConditionalExpect

Disallow conditional expect() calls inside tests.

**Don't:**
```js
test("conditional expect", async ({ page }) => {
    if (someCondition) {
        await expect(page).toHaveTitle("Title");
    }
});
```

**Do:**
```js
test("unconditional expect", async ({ page }) => {
    await expect(page).toHaveTitle("Title");
});
```

---

### noContinue

Disallow continue statements.

**Don't:**
```js
let sum = 0,
    i;

for(i = 0; i < 10; i++) {
    if(i >= 5) {
        continue;
    }

    sum += i;
}
```

**Do:**
```js
let sum = 0,
    i;

for(i = 0; i < 10; i++) {
    if(i < 5) {
        sum += i;
    }
}
```

---

### noDeprecatedMediaType

Disallow deprecated media types.

**Don't:**
```css
@media tv {}
```

**Do:**
```css
@media screen {}
```

---

### noDivRegex

Disallow equal signs explicitly at the beginning of regular expressions.

**Don't:**
```js
function bar() {
  return /=foo/;
}
```

**Do:**
```js
function bar() {
  return /[=]foo/;
}
```

---

### noDrizzleDeleteWithoutWhere

Require .where() to be called when using .delete() with Drizzle ORM.

**Don't:**
```js
await db.delete(users);
```

**Do:**
```js
await db.delete(users).where(eq(users.id, 1));
```

---

### noDrizzleUpdateWithoutWhere

Require .where() to be called when using .update() with Drizzle ORM.

**Don't:**
```js
await db.update(users).set({ name: "John" });
```

**Do:**
```js
await db.update(users).set({ name: "John" }).where(eq(users.id, 1));
```

---

### noDuplicateArgumentNames

Require all argument names for fields & directives to be unique.

**Don't:**
```js
query {
  field(arg1: "value", arg1: "value")
}
```

**Do:**
```js
query {
  field(arg1: "value", arg2: "value")
}
```

---

### noDuplicateAttributes

Disallow duplication of attributes.

**Don't:**
```jsx
<div foo="a" foo="b"></div>
```

**Do:**
```jsx
<div foo="a" bar="b"></div>
```

---

### noDuplicateEnumValueNames

Require all enum value names to be unique.

**Don't:**
```js
enum A {
  TEST
  OTHER
  TEST
}
```

**Do:**
```js
enum A {
  TEST
  OTHER
}
```

---

### noDuplicateEnumValues

Disallow duplicate enum member values.

**Don't:**
```js
enum E {
  A = 0,
  B = 0,
}
```

**Do:**
```js
enum E {
  A = 0,
  B = 1,
}
```

---

### noDuplicateFieldDefinitionNames

Require all fields of a type to be unique.

**Don't:**
```ts
type SomeObject {
  foo: String
  foo: String
}
```

**Do:**
```ts
type SomeObject {
  foo: String
  bar: String
}
```

---

### noDuplicateGraphqlOperationName

Enforce unique operation names across a GraphQL document.

**Don't:**
```js
query user {
  user {
    id
  }
}

query user {
  me {
    id
  }
}
```

**Do:**
```js
query user {
  user {
    id
  }
}

query me {
  me {
    id
  }
}
```

---

### noDuplicateInputFieldNames

Require fields within an input object to be unique.

**Don't:**
```js
query {
  field(arg: { f1: "value", f1: "value" })
}
```

**Do:**
```js
query {
  field(arg: { f1: "value", f2: "value" })
}
```

---

### noDuplicateVariableNames

Require all variable definitions to be unique.

**Don't:**
```js
query ($x: Int, $x: Int) {
  field
}
```

**Do:**
```js
query ($x: Int, $y: Int) {
  field
}
```

---

### noDuplicatedSpreadProps

Disallow JSX prop spreading the same identifier multiple times.

**Don't:**
```jsx
<div {...props} something="else" {...props} />
```

**Do:**
```jsx
<div something="else" {...props} />
```

---

### noEqualsToNull

Require the use of === or !== for comparison with null.

**Don't:**
```js
foo == null;
```

**Do:**
```js
foo === null;
```

---

### noExcessiveClassesPerFile

Enforce a maximum number of classes per file.

**Don't:**
```js
class Foo {}
class Bar {}
```

**Do:**
```js
class Foo {}
```

---

### noExcessiveLinesPerFile

Restrict the number of lines in a file.

**Don't:**
```css
.a { color: red; }
.b { color: blue; }
.c { color: green; }
```

**Do:**
```css
.a { color: red; }
.b { color: blue; }
```

---

### noFloatingClasses

Disallow new operators outside of assignments or comparisons.

**Don't:**
```js
new Thing();
```

**Do:**
```js
const thing = new Thing();
```

---

### noForIn

Disallow iterating using a for-in loop.

**Don't:**
```js
for (const i in array) {
  console.log(i, array[i]);
}
```

**Do:**
```js
for (const value of array) {
  console.log(value);
}
```

---

### noHexColors

Disallow hex colors.

**Don't:**
```css
a { color: #000; }
```

**Do:**
```css
a { color: black; }
```

---

### noIncrementDecrement

Disallows the usage of the unary operators ++ and --.

**Don't:**
```js
let foo = 0;
foo++;
```

**Do:**
```js
let foo = 0;
foo += 1;
```

---

### noInlineStyles

Disallow the use of inline styles.

**Don't:**
```css
<div style={{ color: "red" }}>Error</div>
```

**Do:**
```jsx
<div className="text-red">Error</div>
```

---

### noJsxPropsBind

Disallow .bind(), arrow functions, or function expressions in JSX props

**Don't:**
```jsx
<Foo onClick={this._handleClick.bind(this)}></Foo>
```

**Do:**
```jsx
<Foo onClick={this._handleClick}></Foo>
```

---

### noLeakedRender

Prevent problematic leaked values from being rendered.

**Don't:**
```js
const Component = () => {
  const count = 0;
  return <div>{count && <span>Count: {count}</span>}</div>;
}
```

**Do:**
```js
const Component = () => {
  const count = 0;
  return <div>{count > 0 && <span>Count: {count}</span>}</div>;
}
```

---

### noMultiAssign

Disallow use of chained assignment expressions

**Don't:**
```js
const foo = bar = "baz";
```

**Do:**
```js
const foo = "baz";
const bar = "baz";
```

---

### noMultiStr

Disallow creating multiline strings by escaping newlines.

**Don't:**
```js
const foo =
    "Line 1\n\
Line 2";
```

**Do:**
```js
const foo = "Line 1\nLine 2";
```

---

### noNestedPromises

Disallow nested .then() or .catch() promise calls.

**Don't:**
```js
doThing().then(function() { return a.then() })
```

**Do:**
```js
// Simple returns
doThing().then(function() { return 4 })
doThing().then(() => 4)
```

---

### noParametersOnlyUsedInRecursion

Disallow function parameters that are only used in recursive calls.

**Don't:**
```js
function factorial(n, acc) {
    if (n === 0) return 1;
    return factorial(n - 1, acc);
}
```

**Do:**
```js
function factorial(n, acc) {
    if (n === 0) return acc;
    return factorial(n - 1, acc * n);
}
```

---

### noPlaywrightElementHandle

Disallow usage of element handles (page.$() and page.$$()).

**Don't:**
```js
const button = await page.$('button');
```

**Do:**
```js
const button = page.locator('button');
await button.click();
```

---

### noPlaywrightEval

Disallow usage of page.$eval() and page.$$eval().

**Don't:**
```js
await page.$eval('.foo', el => el.textContent);
```

**Do:**
```js
const text = await page.locator('.foo').evaluate(el => el.textContent);
```

---

### noPlaywrightForceOption

Disallow usage of the { force: true } option.

**Don't:**
```js
await page.locator('button').click({ force: true });
```

**Do:**
```js
await page.locator('button').click();
```

---

### noPlaywrightMissingAwait

Enforce Playwright async APIs to be awaited or returned.

**Don't:**
```js
test('example', async ({ page }) => {
    expect(page.getByRole('button')).toBeVisible();
});
```

**Do:**
```js
test('example', async ({ page }) => {
    await expect(page.getByRole('button')).toBeVisible();
});
```

---

### noPlaywrightNetworkidle

Disallow usage of the networkidle option.

**Don't:**
```js
await page.waitForLoadState('networkidle');
```

**Do:**
```js
await page.waitForLoadState('load');
```

---

### noPlaywrightPagePause

Disallow using page.pause().

**Don't:**
```js
await page.pause();
```

**Do:**
```js
test('example', async ({ page }) => {
    await page.click('button');
    await expect(page.locator('.result')).toBeVisible();
});
```

---

### noPlaywrightUselessAwait

Disallow unnecessary await for Playwright methods that don't return promises.

**Don't:**
```js
await page.locator('.my-element');
```

**Do:**
```js
page.locator('.my-element');
await page.locator('.my-element').click();
```

---

### noPlaywrightWaitForNavigation

Disallow using page.waitForNavigation().

**Don't:**
```js
await page.waitForNavigation();
```

**Do:**
```js
await page.waitForURL('/home');
```

---

### noPlaywrightWaitForSelector

Disallow using page.waitForSelector().

**Don't:**
```js
await page.waitForSelector('.submit-button');
```

**Do:**
```js
await page.locator('.submit-button').click();
```

---

### noPlaywrightWaitForTimeout

Disallow using page.waitForTimeout().

**Don't:**
```js
await page.waitForTimeout(5000);
```

**Do:**
```js
await page.waitForLoadState();
```

---

### noProto

Disallow the use of the deprecated __proto__ object property.

**Don't:**
```js
obj.__proto__ = a;
```

**Do:**
```js
const a = Object.getPrototypeOf(obj);
```

---

### noRedundantDefaultExport

Checks if a default export exports the same symbol as a named export.

**Don't:**
```js
export const foo = 42;
export default foo;
```

**Do:**
```js
export const foo = 42;
export default 42;
```

---

### noReturnAssign

Disallow assignments in return statements.

**Don't:**
```js
function f(a) {
    return a = 1;
}
```

**Do:**
```js
function f(a) {
    a = 1;
    return a;
}
```

---

### noRootType

Disallow the usage of specified root types

**Don't:**
```ts
type Mutation {
  createUser(input: CreateUserInput!): User!
}
```

**Do:**
```ts
type Query {
  users: [User!]!
}
```

---

### noScriptUrl

Disallow javascript: URLs in HTML.

**Don't:**
```jsx
<a href="javascript:void(0)">Click me</a>
```

**Do:**
```jsx
<a href="https://example.com">Click me</a>
<a href="/path/to/page">Click me</a>
<a href="#section">Click me</a>
<span href="javascript:void(0)">Not a real href</span>
```

---

### noShadow

Disallow variable declarations from shadowing variables declared in the outer scope.

**Don't:**
```js
const foo = "bar";
if (true) {
   const foo = "baz";
}
```

**Do:**
```js
const foo = "bar";
if (true) {
   const qux = "baz";
}
```

---

### noSyncScripts

Prevent the usage of synchronous scripts.

**Don't:**
```jsx
<script src=""></script>
```

**Do:**
```jsx
<script src="" async></script>
<script src="" defer></script>
<script src="" type="module"></script>
```

---

### noTernary

Disallow ternary operators.

**Don't:**
```js
const foo = isBar ? baz : qux;
```

**Do:**
```js
let foo;

if (isBar) {
	foo = baz;
} else {
	foo = qux;
}
```

---

### noUndeclaredEnvVars

Disallow the use of undeclared environment variables.

**Don't:**
```js
const value = process.env.MY_VAR;
```

**Do:**
```js
// NODE_ENV is always allowed
const value = process.env.NODE_ENV;
```

---

### noUnknownAttribute

Disallow unknown DOM properties.

**Don't:**
```jsx
<div allowTransparency="true" />
```

**Do:**
```jsx
<div className="foo" />
```

---

### noUnnecessaryConditions

Disallow unnecessary type-based conditions that can be statically determined as redundant.

**Don't:**
```ts
function head<T>(items: T[]) {
  if (items) {  // This check is unnecessary
    return items[0].toUpperCase();
  }
}
```

**Do:**
```ts
function head<T>(items: T[] | null) {
  if (items) {  // This check is necessary
    return items[0].toUpperCase();
  }
}
```

---

### noUselessReturn

Disallow redundant return statements.

**Don't:**
```js
function foo() {
    return;
}
```

**Do:**
```js
function foo() {
    return 5;
}
```

---

### noVueOptionsApi

Disallow the use of Vue Options API.

**Don't:**
```js
import { defineComponent } from 'vue'

defineComponent({
  name: 'MyComponent',
  data() {
    return { count: 0 }
  }
})
```

---

### noVueRefAsOperand

Disallow the use of value wrapped by ref()(Composition API) as operand

**Don't:**
```js
import { ref } from "vue"

const count = ref(0)
count++
```

**Do:**
```js
import { ref } from "vue"

const count = ref(0)
count.value++
```

---

### useArraySome

Prefer Array.prototype.some() over verbose existence checks.

**Don't:**
```js
array.filter(predicate).length > 0;
```

**Do:**
```js
array.some(predicate);
```

---

### useBaseline

Disallow CSS properties, values, at-rules, functions, and selectors that are not part of the configured Baseline.

**Don't:**
```js
a {
  backdrop-filter: blur(4px);
}
```

**Do:**
```css
a { color: red; }
```

---

### useConsistentEnumValueType

Disallow enums from having both number and string members.

**Don't:**
```js
enum Status {
  Unknown,
  Closed = 1,
  Open = 'open',
}
```

**Do:**
```js
enum Status {
  Unknown = 0,
  Closed = 1,
  Open = 2,
}
```

---

### useConsistentGraphqlDescriptions

Require all descriptions to follow the same style (either block or inline) to maintain consistency and improve readability across the schema.

**Don't:**
```js
enum EnumValue {
  "this is a description"
  DEFAULT
}
```

**Do:**
```js
enum EnumValue {
  """
  this is a description
  """
  DEFAULT
}
```

---

### useConsistentMethodSignatures

Enforce consistent use of either method signatures or function properties within interfaces and type aliases.

**Don't:**
```ts
interface Example {
  methodFunc(arg: string): number;
}
```

**Do:**
```ts
interface Prop {
  propFunc: (arg: string) => number;
}
```

---

### useDestructuring

Require destructuring from arrays and/or objects

**Don't:**
```js
var foo = array[0];
```

**Do:**
```js
var [foo] = array;
```

---

### useErrorCause

Enforce that new Error() is thrown with the original error as cause.

**Don't:**
```js
try {
  // ...
} catch (err) {
  throw new Error(err.message);
}
```

**Do:**
```js
try {
  // ...
} catch (err) {
  throw new Error("Something went wrong", { cause: err });
}

try {
    throw "Not a rethrow, so it's ignored when nested";
} catch (err) {
    const fn = () => {
        throw new Error("New unrelated error");
    }
    fn();
}
```

---

### useExpect

Ensure that test functions contain at least one expect() or similar assertion.

**Don't:**
```js
test("no assertion", async ({ page }) => {
    await page.goto("/");
    await page.click("button");
});
```

**Do:**
```js
test("has assertion", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveTitle("Title");
});
```

---

### useExplicitType

Enforce types in functions, methods, variables, and parameters.

**Don't:**
```js
// Should indicate that no value is returned (void)
function test() {
  return;
}
```

**Do:**
```js
// No return value should be expected (void)
function test(): void {
  return;
}
```

---

### useGlobalThis

Enforce the use of globalThis over window, self, and global.

**Don't:**
```js
window.foo;
```

**Do:**
```js
globalThis.foo;
```

---

### useImportsFirst

Enforce that all imports appear at the top of the module.

**Don't:**
```js
import { foo } from "foo";
const bar = 1;
import { baz } from "baz";
```

**Do:**
```js
import { foo } from "foo";
import { bar } from "bar";
const baz = 1;
```

---

### useInlineScriptId

Enforce id attribute on next/script components with inline content or dangerouslySetInnerHTML.

**Don't:**
```js
import Script from 'next/script'

export default function Page() {
  return (
     <Script>{`console.log('Hello world!');`}</Script>
  )
}
```

**Do:**
```js
import Script from 'next/script'

export default function Page() {
  return (
     <Script id="my-script">{`console.log('Hello world!');`}</Script>
  )
}
```

---

### useInputName

Require mutation argument to be always called "input"

**Don't:**
```ts
type Mutation {
  SetMessage(message: InputMessage): String
}
```

**Do:**
```ts
type Mutation {
  SetMessage(input: SetMessageInput): String
}
```

---

### useLoneAnonymousOperation

Disallow anonymous operations when more than one operation specified in document.

**Don't:**
```js
query {
  fieldA
}

query B {
  fieldB
}
```

**Do:**
```js
query A {
  fieldA
}

query B {
  fieldB
}
```

---

### useLoneExecutableDefinition

Require queries, mutations, subscriptions or fragments each to be located in separate files.

**Don't:**
```js
query Foo {
  id
}

fragment Bar on Baz {
  id
}
```

**Do:**
```js
query Foo {
  id
}
```

---

### useNamedCaptureGroup

Enforce using named capture groups in regular expression.

**Don't:**
```js
/(ba[rz])/;
```

**Do:**
```js
/(?<id>ba[rz])/;
/(?:ba[rz])/;
/ba[rz]/;
/(?<year>[0-9]{4})-(?<month>[0-9]{2})/;
new RegExp("(?<id>foo)");
new RegExp(pattern);
```

---

### useNullishCoalescing

Enforce using the nullish coalescing operator (??) instead of logical or (||).

**Don't:**
```ts
declare const maybeString: string | null;
const value = maybeString || 'default'; // should use ??
```

**Do:**
```ts
// Already using ??
declare const maybeString: string | null;
const value = maybeString ?? 'default';
```

---

### usePlaywrightValidDescribeCallback

Enforce valid describe() callback.

**Don't:**
```js
test.describe('suite', async () => {
    test('one', async ({ page }) => {});
});
```

**Do:**
```js
test.describe('suite', () => {
    test('one', async ({ page }) => {});
    test('two', async ({ page }) => {});
});
```

---

### useSpread

Enforce the use of the spread operator over .apply().

**Don't:**
```js
foo.apply(null, args);
```

**Do:**
```js
foo(...args);

obj.foo(...args);

foo.apply(obj, [1, 2, 3]);
```

---

### useUnicodeRegex

Enforce the use of the u or v flag for regular expressions.

**Don't:**
```js
/foo/;
```

**Do:**
```js
/foo/u;
/foo/v;
/foo/giu;
new RegExp("foo", "u");
new RegExp("foo", "giv");
new RegExp("foo", flags); // dynamic flags are ignored
```

---

### useVueMultiWordComponentNames

Enforce multi-word component names in Vue components.

**Don't:**
```js
import { defineComponent } from "vue";
export default defineComponent({
  name: "Header"
});
```

**Do:**
```js
export default {
  name: "my-component"
};
```

---
