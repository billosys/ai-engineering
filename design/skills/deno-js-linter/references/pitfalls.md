# Pitfalls & Suspicious Patterns

Patterns that are likely wrong or unintended — dubious comparisons, misused async, debug leftovers, eval, empty blocks.

**8 recommended** | **10 optional**

## Recommended Rules

### no-await-in-sync-fn

Disallow await keyword inside a non-async function.

**Don't:**
```js
function foo() {
  await bar();
}

const fooFn = function foo() {
  await bar();
};

const fooFn = () => {
  await bar();
};
```

**Do:**
```js
async function foo() {
  await bar();
}

const fooFn = async function foo() {
  await bar();
};

const fooFn = async () => {
  await bar();
};
```

---

### no-debugger

Disallows the use of the debugger statement.

**Don't:**
```js
function isLongString(x: string) {
  debugger;
  return x.length > 100;
}
```

**Do:**
```js
function isLongString(x: string) {
  return x.length > 100; // set breakpoint here instead
}
```

---

### no-empty

Disallows the use of empty block statements.

**Don't:**
```js
if (foo) {}

while (foo) {}

switch (foo) {}

try {
  doSomething();
} catch (e) {
} finally {
}
```

**Do:**
```js
if (foo) {
  // empty
}

while (foo) {
  /* empty */
}

try {
  doSomething();
} catch (e) {
  // continue regardless of error
}

try {
  doSomething();
} finally {
  /* continue regardless of error */
}
```

---

### no-irregular-whitespace

Disallows the use of non-space or non-tab whitespace characters.

---

### no-regex-spaces

Disallows multiple spaces in regular expression literals.

**Don't:**
```js
const re1 = /  /;
const re2 = /foo  bar/;
const re3 = / a b  c d /;
const re4 = /foo  {3}bar/;

const re5 = new RegExp("  ");
const re6 = new RegExp("foo  bar");
const re7 = new RegExp(" a b  c d ");
const re8 = new RegExp("foo  {3}bar");
```

**Do:**
```js
const re1 = /foo/;
const re2 = / /;
const re3 = / {3}/;
const re4 = / +/;
const re5 = / ?/;
const re6 = / */;

const re7 = new RegExp("foo");
const re8 = new RegExp(" ");
const re9 = new RegExp(" {3}");
const re10 = new RegExp(" +");
const re11 = new RegExp(" ?");
const re12 = new RegExp(" *");
```

---

### no-with

Disallows the usage of with statements.

**Don't:**
```js
with (someVar) {
  console.log("foo");
}
```

---

### require-await

Disallows async functions that have no await expression or await using declaration.

**Don't:**
```js
async function f1() {
  doSomething();
}

const f2 = async () => {
  doSomething();
};

const f3 = async () => doSomething();

const obj = {
  async method() {
    doSomething();
  },
};

class MyClass {
  async method() {
    doSomething();
  }
}
```

**Do:**
```js
await asyncFunction();

function normalFunction() {
  doSomething();
}

async function f1() {
  await asyncFunction();
}

const f2 = async () => {
  await asyncFunction();
};

const f3 = async () => await asyncFunction();

async function f4() {
  for await (const num of asyncIterable) {
    console.log(num);
  }
}

async function f5() {
  using = createResource();
}

// empty functions are valid
async function emptyFunction() {}
const emptyArrowFunction = async () => {};

// generators are also valid
async function* gen() {
  console.log(42);
}
```

---

### require-yield

Disallows generator functions that have no yield.

**Don't:**
```js
function* f1() {
  return "f1";
}
```

**Do:**
```js
function* f1() {
  yield "f1";
}

// generator function with empty body is allowed
function* f2() {}

function f3() {
  return "f3";
}
```

---

## Optional Rules

### eqeqeq

Enforces the use of type-safe equality operators === and !== instead of the more error prone == and != operators.

**Don't:**
```js
if (a == 5) {}
if ("hello world" != input) {}
```

**Do:**
```js
if (a === 5) {}
if ("hello world" !== input) {}
```

---

### guard-for-in

Require for-in loops to include an if statement.

**Don't:**
```js
for (const key in obj) {
  foo(obj, key);
}
```

**Do:**
```js
for (const key in obj) {
  if (Object.hasOwn(obj, key)) {
    foo(obj, key);
  }
}
```

---

### no-await-in-loop

Requires await is not used in a for loop body.

**Don't:**
```js
async function doSomething(items) {
  const results = [];
  for (const item of items) {
    // Each item in the array blocks on the previous one finishing
    results.push(await someAsyncProcessing(item));
  }
  return processResults(results);
}
```

**Do:**
```js
async function doSomething(items) {
  const results = [];
  for (const item of items) {
    // Kick off all item processing asynchronously...
    results.push(someAsyncProcessing(item));
  }
  // ...and then await their completion after the loop
  return processResults(await Promise.all(results));
}
```

---

### no-boolean-literal-for-arguments

Requires all functions called with any amount of boolean literals as parameters to use a self-documenting constant instead.

**Don't:**
```js
function redraw(allViews: boolean, inline: boolean) {
  // redraw logic.
}
redraw(true, true);

function executeCommand(recursive: boolean, executionMode: EXECUTION_MODES) {
  // executeCommand logic.
}
executeCommand(true, EXECUTION_MODES.ONE);

function enableLogs(enable: boolean) {
  // enabledLogs logic.
}
enableLogs(true);
```

**Do:**
```js
function redraw(allViews: boolean, inline: boolean) {
  // redraw logic.
}
const ALL_VIEWS = true, INLINE = true;
redraw(ALL_VIEWS, INLINE);

function executeCommand(recursive: boolean, executionMode: EXECUTION_MODES) {
  // executeCommand logic.
}
const RECURSIVE = true;
executeCommand(RECURSIVE, EXECUTION_MODES.ONE);

function enableLogs(enable: boolean) {
  // enabledLogs logic.
}
const ENABLE = true;
enableLogs(ENABLE);
```

---

### no-console

Disallows the use of the console global.

**Don't:**
```js
console.log("Debug message");
console.error("Debug message");
console.debug(obj);

if (debug) console.log("Debugging");

function log() {
  console.log("Log");
}
```

**Do:**
```js
function logWarning(message: string) {
  // deno-lint-ignore no-console
  console.warn(message);
}
```

---

### no-eval

Disallows the use of eval.

**Don't:**
```js
const obj = { x: "foo" };
const key = "x",
const value = eval("obj." + key);
```

**Do:**
```js
const obj = { x: "foo" };
const value = obj[x];
```

---

### no-self-compare

Disallows comparisons where both sides are exactly the same.

**Don't:**
```js
if (x === x) {
}
if ("x" === "x") {
}
if (a.b === a.b) {
}
if (a["b"] === a["b"]) {
}
```

**Do:**
```js
if (x === y) {
}
if ("x" === "y") {
}
if (a.b === a.c) {
}
if (a["b"] === a["c"]) {
}
```

---

### no-sparse-arrays

Disallows sparse arrays.

**Don't:**
```js
const items = ["foo", , "bar"];
```

**Do:**
```js
const items = ["foo", "bar"];
```

---

### no-throw-literal

Disallow throwing literals as exceptions.

**Don't:**
```js
throw "error";
throw 0;
throw undefined;
throw null;
```

**Do:**
```js
throw new Error("error");
```

---

### no-undef

Disallow the use of undeclared variables.

**Don't:**
```js
const foo = someFunction();
const bar = a + 1;
```

---
