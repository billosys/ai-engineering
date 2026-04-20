# Security

Rules that catch security vulnerabilities — eval(), target=_blank, unsafe innerHTML.

**2 recommended** (enabled by default) | **1 optional** (enable individually)

## Recommended Rules

### noBlankTarget

Disallow target="_blank" attribute without rel="noopener".

**Don't:**
```jsx
<a href='http://external.link' target='_blank'>child</a>
```

**Do:**
```jsx
<a href='http://external.link' rel='noopener' target='_blank'>child</a>
```

---

### noGlobalEval

Disallow the use of global eval().

**Don't:**
```js
eval("var a = 0");
```

**Do:**
```js
let foo = globalThis;
foo.eval("let a = 0;");
```

---

## Optional Rules

### noSecrets

Disallow usage of sensitive data such as API keys and tokens.

**Don't:**
```js
const secret = "AKIA1234567890EXAMPLE";
```

**Do:**
```js
const nonSecret = "hello world";
```

---
