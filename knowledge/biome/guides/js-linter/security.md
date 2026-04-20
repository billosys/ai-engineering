# Security

Rules that prevent security vulnerabilities — eval(), hardcoded secrets.

**0 recommended** | **1 optional**

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
