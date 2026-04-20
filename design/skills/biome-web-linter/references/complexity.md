# Complexity

Rules that flag unnecessarily complex code and suggest simpler alternatives.

**33 recommended** (enabled by default) | **10 optional** (enable individually)

## Recommended Rules

### noAdjacentSpacesInRegex

Disallow unclear usage of consecutive space characters in regular expression literals

**Don't:**
```js
/   /
```

**Do:**
```js
/foo {2}bar/
```

---

### noArguments

Disallow the use of arguments.

**Don't:**
```js
function f() {
   console.log(arguments);
}
```

---

### noBannedTypes

Disallow primitive type aliases and misleading types.

**Don't:**
```js
let foo: String = "bar";
```

**Do:**
```ts
const foo: string = "bar";
```

---

### noCommaOperator

Disallow comma operator.

**Don't:**
```js
const foo = (doSomething(), 0);
```

**Do:**
```js
for(a = 0, b = 0; (a + b) < 10; a++, b += 2) {}
```

---

### noEmptyTypeParameters

Disallow empty type parameters in type aliases and interfaces.

**Don't:**
```ts
interface Foo<> {}
```

**Do:**
```ts
interface Foo {}
```

---

### noExtraBooleanCast

Disallow unnecessary boolean casts

**Don't:**
```js
if (!Boolean(foo)) {
}
```

**Do:**
```js
Boolean(!x);
!x;
!!x;
```

---

### noFlatMapIdentity

Disallow to use unnecessary callback on flatMap.

**Don't:**
```js
array.flatMap((arr) => arr);
```

**Do:**
```js
array.flatMap((arr) => arr * 2);
```

---

### noStaticOnlyClass

This rule reports when a class has no non-static members, such as for a class used exclusively as a static namespace.

**Don't:**
```js
class X {
  static foo = false;
  static bar() {};
}
```

**Do:**
```js
const X = {
  foo: false,
  bar() {}
};
```

---

### noThisInStatic

Disallow this and super in static contexts.

**Don't:**
```js
class A {
    static CONSTANT = 0;

    static foo() {
        this.CONSTANT;
    }
 }
```

**Do:**
```js
class B extends A {
    static ANOTHER_CONSTANT = A.CONSTANT + 1;

    static foo() {
        A.CONSTANT;
        B.ANOTHER_CONSTANT;
    }

    bar() {
        this.property;
    }
}
```

---

### noUselessCatch

Disallow unnecessary catch clauses.

**Don't:**
```js
try {
    doSomething();
} catch(e) {
    throw e;
}
```

**Do:**
```js
try {
    doSomething();
} catch(e) {
    doSomethingWhenCatch();
    throw e;
}
```

---

### noUselessConstructor

Disallow unnecessary constructors.

**Don't:**
```js
class A {
    constructor (a) {}
}
```

**Do:**
```js
class A {
    constructor (prop) {
        this.prop = prop;
    }
}
```

---

### noUselessContinue

Avoid using unnecessary continue.

**Don't:**
```js
loop: for (let i = 0; i < 5; i++) {
  continue loop;
}
```

**Do:**
```js
while (i) {
  if (i > 5) {
    continue;
  }
  console.log(i);
  i--;
}

loop: while (1) {
  forLoop: for (let i = 0; i < 5; i++) {
    if (someCondition) {
      continue loop;
    }
  }
}
```

---

### noUselessEmptyExport

Disallow empty exports that don't change anything in a module file.

**Don't:**
```js
import { A } from "module";
export {};
```

**Do:**
```js
export {};
```

---

### noUselessEscapeInRegex

Disallow unnecessary escape sequence in regular expression literals.

**Don't:**
```js
/\a/;
```

**Do:**
```js
/\^\d\b/
```

---

### noUselessFragments

Disallow unnecessary fragments

**Don't:**
```jsx
<>
    <>foo</>
    <SomeComponent />
</>
```

**Do:**
```jsx
<>
foo
</>
```

---

### noUselessLabel

Disallow unnecessary labels.

**Don't:**
```js
loop: while(a) {
    break loop;
}
```

**Do:**
```js
outer: while(a) {
    while(b) {
        break outer;
    }
}
```

---

### noUselessLoneBlockStatements

Disallow unnecessary nested block statements.

**Don't:**
```js
{}
```

**Do:**
```js
while (foo) {
  bar();
}
```

---

### noUselessRename

Disallow renaming import, export, and destructured assignments to the same name.

**Don't:**
```js
import { foo as foo } from "bar";
```

**Do:**
```js
import { foo as bar } from "baz";
```

---

### noUselessStringRaw

Disallow unnecessary String.raw function in template string literals without any escape sequence.

**Don't:**
```js
String.raw`a`;
```

**Do:**
```js
String.raw`\n ${a}`;
```

---

### noUselessSwitchCase

Disallow useless case in switch statements.

**Don't:**
```js
switch (foo) {
    case 0:
    default:
        break;
    case 1:
        break;
}
```

**Do:**
```js
switch (foo) {
    case 0:
        break;
    default:
        break;
}
```

---

### noUselessTernary

Disallow ternary operators when simpler alternatives exist.

**Don't:**
```js
var a = x ? true : true;
```

**Do:**
```js
var a = x === 2 ? 'Yes' : 'No';
```

---

### noUselessThisAlias

Disallow useless this aliasing.

**Don't:**
```js
class A {
    method() {
        const self = this;
        return () => {
            return self;
        }
    }
}
```

**Do:**
```js
class A {
    method() {
        const self = this;
        return function() {
            this.g();
            return self;
        }
    }
}
```

---

### noUselessTypeConstraint

Disallow using any or unknown as type constraint.

**Don't:**
```ts
interface FooAny<T extends any> {}
```

**Do:**
```ts
interface Foo<T> {}

type Bar<T> = {};
```

---

### noUselessUndefinedInitialization

Disallow initializing variables to undefined.

**Don't:**
```js
var a = undefined;
```

**Do:**
```js
var a = 1;
```

---

### useArrowFunction

Use arrow functions over function expressions.

**Don't:**
```js
const z = function() {
    return 0;
}
```

**Do:**
```js
const f = function() {
    return this.prop;
}
```

---

### useDateNow

Use Date.now() to get the number of milliseconds since the Unix Epoch.

**Don't:**
```js
const foo = new Date().getTime();
```

**Do:**
```js
const foo = Date.now();
```

---

### useFlatMap

Promotes the use of .flatMap() when map().flat() are used together.

**Don't:**
```js
const array = ["split", "the text", "into words"];
array.map(sentence => sentence.split(' ')).flat();
```

**Do:**
```js
const array = ["split", "the text", "into words"];
array.map(sentence => sentence.split(' ')).flat(2);
```

---

### useIndexOf

Prefer Array#{indexOf,lastIndexOf}() over Array#{findIndex,findLastIndex}() when looking for the index of an item.

**Don't:**
```js
const index = foo.findIndex(x => x === 'foo');
```

**Do:**
```js
const index = foo.indexOf('foo');
```

---

### useLiteralKeys

Enforce the usage of a literal access to properties over computed property access.

**Don't:**
```js
a.b["c"];
```

**Do:**
```js
a["c" + "d"];
a[d.c];
```

---

### useNumericLiterals

Disallow parseInt() and Number.parseInt() in favor of binary, octal, and hexadecimal literals

**Don't:**
```js
parseInt("111110111", 2);
```

**Do:**
```js
parseInt(1);
parseInt(1, 3);
Number.parseInt(1);
Number.parseInt(1, 3);

0b111110111 === 503;
0o767 === 503;
0x1F7 === 503;

a[parseInt](1,2);

parseInt(foo);
parseInt(foo, 2);
Number.parseInt(foo);
Number.parseInt(foo, 2);
```

---

### useOptionalChain

Enforce using concise optional chain instead of chained logical expressions.

**Don't:**
```js
foo && foo.bar && foo.bar.baz && foo.bar.baz.buzz
```

**Do:**
```js
foo && bar;
```

---

### useRegexLiterals

Enforce the use of the regular expression literals instead of the RegExp constructor if possible.

**Don't:**
```js
new RegExp("abc", "u");
```

**Do:**
```js
/abc/u;

new RegExp("abc", flags);
```

---

### useSimpleNumberKeys

Disallow number literal object member names which are not base 10 or use underscore as separator.

**Don't:**
```js
({ 0x1: 1 });
```

**Do:**
```js
({ 0: "zero" });
({ 122: "integer" });
({ 1.22: "floating point" });
({ 3.1e12: "floating point with e" });
```

---

## Optional Rules

### noExcessiveLinesPerFunction

Restrict the number of lines of code in a function.

**Don't:**
```js
function foo () {
  const x = 0;
  const y = 1;
  const z = 2;
  return x + y + z;
};
```

**Do:**
```js
function foo () {
    const x = 0;
    const y = 1;
};
```

---

### noExcessiveNestedTestSuites

This rule enforces a maximum depth to nested describe() in test files.

**Don't:**
```js
describe('foo', () => {
  describe('bar', () => {
    describe('baz', () => {
      describe('qux', () => {
        describe('quxx', () => {
          describe('too many', () => {
            it('should get something', () => {
              expect(getSomething()).toBe('Something');
            });
          });
        });
      });
    });
  });
});
```

**Do:**
```js
describe('foo', () => {
  describe('bar', () => {
    it('should get something', () => {
      expect(getSomething()).toBe('Something');
    });
  });
  describe('qux', () => {
    it('should get something', () => {
      expect(getSomething()).toBe('Something');
    });
  });
});
```

---

### noForEach

Prefer for...of statement instead of Array.forEach.

**Don't:**
```js
els.forEach((el) => {
  f(el);
})
```

**Do:**
```js
els.forEach((el, i) => {
  f(el, i)
})
```

---

### noImplicitCoercions

Disallow shorthand type conversions.

**Don't:**
```js
!!foo;
```

**Do:**
```js
Boolean(foo);
```

---

### noUselessCatchBinding

Disallow unused catch bindings.

**Don't:**
```js
try {
    // Do something
} catch (unused) {}
```

**Do:**
```js
try {
    // Do something
} catch (used) {
    console.error(used);
}
```

---

### noUselessStringConcat

Disallow unnecessary concatenation of string or template literals.

**Don't:**
```js
const a = "a" + "b";
```

**Do:**
```js
const a = 1 + 1;
```

---

### noUselessUndefined

Disallow the use of useless undefined.

**Don't:**
```js
let foo = undefined;
```

**Do:**
```js
let foo;
const {foo} = bar;
function foo() {
  return;
}
function* foo() {
  yield;
}
function foo(bar) {}
function foo({bar}) {}
foo();
```

---

### useMaxParams

Enforce a maximum number of parameters in function definitions.

**Don't:**
```js
function foo(a, b, c, d, e, f, g, h) {
    // too many parameters
}
```

**Do:**
```js
function foo(a, b, c) {
    // within limit
}
```

---

### useSimplifiedLogicExpression

Discard redundant terms from logical expressions.

**Don't:**
```js
const boolExp = true;
const r = true && boolExp;
```

**Do:**
```js
const boolExpr3 = true;
const boolExpr4 = false;
const r5 = !(boolExpr1 && boolExpr2);
const boolExpr5 = true;
const boolExpr6 = false;
```

---

### useWhile

Enforce the use of while loops instead of for loops when the initializer and update expressions are not needed.

**Don't:**
```js
for (; x.running;) {
    x.step();
}
```

**Do:**
```js
for (let x = 0; x < 10; i++) {}
```

---
