# Documentation

The writing discipline of documentation: when and what to comment, how to write effective JSDoc descriptions, module-level documentation, code as documentation, tests as documentation, and what NOT to document. This guide covers the *prose* side of documentation — Guide 05 covers JSDoc *type annotations*. The core tension: comments explain *why*, not *what*. Code should be clear enough that *what* it does is self-evident. Grounded in *Exploring JavaScript* (Rauschmayer), *Deep JavaScript* (Rauschmayer), *JavaScript: The Definitive Guide* (Flanagan), *Eloquent JavaScript* (Haverbeke), and Deno documentation.

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (JSDoc where needed).

---

## ID-01: Comments Explain *Why*, Not *What*

**Strength**: MUST

**Summary**: If the code needs a comment to explain what it does, refactor the code. Comments exist for intent, context, and non-obvious decisions.

```js
// Bad — restates the code (zero information added)
const arr = []; // Create a new array
count++;        // Increment count
const user = await getUser(id); // Get the user by ID

// Bad — describes the "what" instead of the "why"
// Loop through all users and check if they are active
for (const user of users) {
  if (user.active) {
    activeUsers.push(user);
  }
}

// Good — explains WHY, not what
// Retry with exponential backoff because the upstream API rate-limits
// at 100 req/min and returns 429 without a Retry-After header.
await retry(fetchData, { maxAttempts: 5, backoff: "exponential" });

// Good — explains a non-obvious decision
// Using Set here instead of Array.includes() because the banned list
// is checked once per request and has ~10,000 entries. See perf notes.
const bannedSet = new Set(bannedList);
```

**Rationale**: Haverbeke's comment examples in Eloquent JS illustrate the spectrum: a block comment explaining the provenance of a mysterious constant is valuable; a comment that restates `x = x + 1` is noise. The code's *what* should be self-evident from naming and structure. Comments capture the *why* that code cannot express (Eloquent JS Ch. 2; Exploring JS Ch. 9).

---

## ID-02: Don't Comment Obvious Code — The AI Anti-Pattern

**Strength**: MUST

**Summary**: Verbose, line-by-line comments that restate visible code add noise and obscure the code they describe. This is the most common documentation anti-pattern in AI-generated code.

```js
// Bad — AI-generated comment pattern (every line narrated)
// Import the path module
import { join } from "@std/path";

// Define the maximum number of retries
const MAX_RETRIES = 3;

// Create an async function to fetch user data
async function fetchUser(id) {
  // Make a fetch request to the API
  const response = await fetch(`/api/users/${id}`);
  // Parse the response as JSON
  const data = await response.json();
  // Return the data
  return data;
}

// Good — same code, no comments needed (it's self-documenting)
import { join } from "@std/path";

const MAX_RETRIES = 3;

async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}
```

**The test**: For each comment, ask "does this tell me something the code doesn't?" If the answer is no, delete it. Code that needs narration to be understood needs *refactoring*, not comments.

**Rationale**: Every comment is a maintenance liability — it must be updated when the code changes. Obvious comments double the maintenance surface for zero information gain. They also obscure the genuinely useful comments that explain non-obvious decisions.

---

## ID-03: Comment Non-Obvious Intent — Workarounds, Edge Cases, Business Rules

**Strength**: SHOULD

**Summary**: Comment when the code does something surprising, works around a bug, implements a business rule that isn't self-evident, or deliberately avoids an obvious approach.

```js
// Good — workaround with context
// AbortController.abort() doesn't accept a reason in Safari < 16.4.
// Pass the reason via a custom property until we drop Safari 16.3 support.
controller.signal.reason = new Error("User cancelled");
controller.abort();

// Good — business rule
// Users created before 2020-01-01 are on the legacy pricing tier
// regardless of their current plan. Legal requirement per contract §4.2.
const isLegacy = user.createdAt < LEGACY_CUTOFF;

// Good — "why not the obvious approach"
// Using a manual loop instead of .map() here because we need to break
// on the first validation failure and report which field failed.
for (const field of fields) {
  const error = validate(field);
  if (error) return { field: field.name, error };
}

// Good — edge case documentation
// Empty string is a valid title (user explicitly cleared it).
// Using ?? instead of || to preserve it. See 01-core-idioms ID-03.
const title = input.title ?? "Untitled";
```

**Rationale**: These are comments that prevent the next developer (or Claude Code) from "fixing" correct code. Without the workaround comment, someone will remove the Safari workaround. Without the business rule comment, someone will simplify the condition. The comment protects intentional decisions from well-meaning but uninformed changes.

---

## ID-04: TODO/FIXME/HACK Comments — Include Context

**Strength**: SHOULD

**Summary**: Use standardized markers for incomplete work. Always include who, why, and a reference to a ticket or issue.

```js
// Good — actionable, traceable
// TODO(alice, #347): Replace with AbortSignal.any() when Deno 2.1 ships
const signal = manualCombineSignals(controller.signal, timeoutSignal);

// FIXME(bob, #512): This breaks for BigInt IDs > 2^53. Need to switch
// to string IDs or use the database's native BigInt support.
const userId = Number(rawId);

// HACK: The upstream API returns Content-Type: text/plain for JSON
// responses. Remove this when they fix their server.
const data = JSON.parse(await response.text());

// Bad — no context, no owner, not traceable
// TODO: fix this later
// FIXME: doesn't work
// HACK
```

**Rationale**: A bare `TODO` with no context becomes invisible technical debt — nobody knows who wrote it, why, or when it should be addressed. Including an owner and ticket number makes it searchable, assignable, and deletable when resolved.

---

## ID-05: Every Exported Function Gets a JSDoc Description

**Strength**: SHOULD

**Summary**: Exported functions are the public API. Every one should have a JSDoc block that describes what it does in prose — not just type annotations.

```js
// Good — description explains the behavior, not just the types
/**
 * Fetch a user by ID. Returns null if the user does not exist.
 * Throws HttpError for non-404 server errors.
 *
 * @param {string} id - The user's unique identifier.
 * @returns {Promise<User | null>}
 * @throws {HttpError} For server errors other than 404.
 */
export async function fetchUser(id) { /* ... */ }

// Bad — types only, no description
/**
 * @param {string} id
 * @returns {Promise<User | null>}
 */
export async function fetchUser(id) { /* ... */ }
```

**The distinction from Guide 05**: Guide 05 (Type Discipline) covers the `@param {string} id` syntax. This guide covers the prose: *"Fetch a user by ID. Returns null if the user does not exist."* Both are needed. Types tell the machine; prose tells the human.

**See also**: `05-type-discipline.md` ID-16

---

## ID-06: First Sentence Is the Summary — Keep It Under 15 Words

**Strength**: SHOULD

**Summary**: The first sentence of a JSDoc block appears in hover tooltips, `deno doc` output, and autocomplete. Make it count.

```js
// Good — first sentence is a concise summary
/**
 * Hash a password using bcrypt with a random salt.
 *
 * The salt is generated automatically. The cost factor defaults to 12
 * but can be overridden via the options parameter.
 *
 * @param {string} password
 * @param {{ cost?: number }} [options]
 * @returns {Promise<string>} The hashed password.
 */
export async function hashPassword(password, options = {}) { /* ... */ }

// Bad — first sentence is a wall of text
/**
 * This function takes a password string as its first argument and an
 * optional options object as its second argument, and then it hashes
 * the password using the bcrypt algorithm with a randomly generated
 * salt value, returning a Promise that resolves to the hashed string.
 */
export async function hashPassword(password, options = {}) { /* ... */ }
```

**Rationale**: IDE hover tooltips and `deno doc` summaries typically show only the first sentence or paragraph. A concise summary ensures developers get useful information without clicking through to the full doc block.

---

## ID-07: Document Parameters with Prose — Valid Values, Edge Cases

**Strength**: SHOULD

**Summary**: Type annotations say what a parameter *is*. Prose says what values are valid, what edge cases exist, and what happens at boundaries.

```js
// Good — prose explains constraints and behavior
/**
 * Create a paginated query.
 *
 * @param {string} query - SQL query string. Must not contain LIMIT/OFFSET
 *   — those are added automatically.
 * @param {number} pageSize - Items per page. Clamped to [1, 100].
 * @param {number} [page=1] - 1-indexed page number. Values < 1 are
 *   treated as 1.
 * @returns {Promise<{ items: unknown[], total: number, page: number }>}
 */
export async function paginate(query, pageSize, page = 1) { /* ... */ }

// Bad — types only, no constraints
/**
 * @param {string} query
 * @param {number} pageSize
 * @param {number} [page]
 */
export async function paginate(query, pageSize, page = 1) { /* ... */ }
```

**Rationale**: The type `number` for `pageSize` doesn't tell you it's clamped to [1, 100]. The type `string` for `query` doesn't tell you it must not contain LIMIT. These constraints are part of the contract and must be documented in prose.

---

## ID-08: Document Thrown Errors with `@throws`

**Strength**: SHOULD

**Summary**: If a function throws, document which error types and under what conditions.

```js
// Good — @throws documents the error contract
/**
 * Parse a configuration file.
 *
 * @param {string} path - Path to the JSON config file.
 * @returns {Config}
 * @throws {TypeError} If path is not a string.
 * @throws {Deno.errors.NotFound} If the file does not exist.
 * @throws {SyntaxError} If the file contains invalid JSON.
 */
export function parseConfig(path) { /* ... */ }

// Bad — no @throws, caller must read the implementation
/**
 * @param {string} path
 * @returns {Config}
 */
export function parseConfig(path) { /* ... */ }
```

**Rationale**: Callers need to know which errors to catch and under what conditions. Without `@throws`, the only way to discover the error contract is to read the source — which defeats the purpose of documentation (Exploring JS Ch. 26; JS Definitive Guide, §11.5).

**See also**: `03-error-handling.md` ID-05, ID-09

---

## ID-09: Document Return Values — Especially When `null`/`undefined` Have Meaning

**Strength**: SHOULD

**Summary**: Document what the return value means, not just its type. Clarify the semantics of `null`, `undefined`, and empty collections.

```js
// Good — return semantics are explicit
/**
 * Look up a user by email.
 *
 * @param {string} email
 * @returns {User | null} The matching user, or null if no user has
 *   this email address. Returns null (not undefined) because the
 *   search was performed and explicitly found nothing.
 */
export function findUserByEmail(email) { /* ... */ }

// Good — empty array vs null distinction
/**
 * Get the user's active sessions.
 *
 * @param {string} userId
 * @returns {Session[]} Active sessions. Returns an empty array (not null)
 *   if the user exists but has no active sessions.
 * @throws {HttpError} If the user does not exist (404).
 */
export async function getActiveSessions(userId) { /* ... */ }
```

**Rationale**: Is `null` "not found" or "error"? Is an empty array "no results" or "not loaded yet"? The type alone doesn't disambiguate. Prose makes the contract unambiguous (Exploring JS Ch. 16; JS Definitive Guide, §3.5).

**See also**: `02-api-design.md` ID-23, ID-24

---

## ID-10: Include `@example` for Non-Obvious APIs

**Strength**: CONSIDER

**Summary**: A code example is worth a paragraph of description. Use `@example` for APIs with complex inputs, multiple use patterns, or surprising behavior.

```js
/**
 * Create a debounced version of a function.
 *
 * @param {Function} fn - The function to debounce.
 * @param {number} wait - Milliseconds to wait after the last call.
 * @returns {Function} The debounced function.
 *
 * @example
 * const search = debounce(async (query) => {
 *   const results = await fetch(`/api/search?q=${query}`);
 *   displayResults(await results.json());
 * }, 300);
 *
 * input.addEventListener("input", (e) => search(e.target.value));
 */
export function debounce(fn, wait) { /* ... */ }
```

**Bonus**: `deno test --doc` extracts `@example` blocks and runs them as tests. Documentation examples that are also tests cannot silently become stale.

**Rationale**: Examples show the API in context — how it's called, what the typical arguments look like, and how the result is used. This is especially valuable for functions with options objects, callbacks, or multi-step usage patterns.

---

## ID-11: Every Module Gets a Top-of-File JSDoc Block

**Strength**: SHOULD

**Summary**: One sentence at the top of each file explaining what the module does and when you'd use it.

```js
// Good — module purpose is immediately clear
/**
 * Password hashing and verification using bcrypt.
 *
 * All functions in this module are async because bcrypt is CPU-intensive
 * and delegated to a worker thread.
 *
 * @module
 */

export async function hashPassword(password, options = {}) { /* ... */ }
export async function verifyPassword(password, hash) { /* ... */ }
```

```js
// Bad — file starts with imports, no context
import { encode } from "@std/encoding/base64";
import { timingSafeEqual } from "@std/crypto";

export async function hashPassword(password, options = {}) { /* ... */ }
```

**Rationale**: `deno doc` and JSR auto-generate documentation from JSDoc. A module-level block provides the entry point for generated docs. Without it, the auto-generated page is a bare list of exports with no context about what the module is for.

---

## ID-12: Write for Tooling, Not Just Humans

**Strength**: SHOULD

**Summary**: `deno doc` and IDE hover tooltips read JSDoc. Structure your documentation for both human and tool consumption.

```js
// Good — structured for tooling
/**
 * Parse a CSV string into an array of row objects.
 *
 * @param {string} csv - Raw CSV text with headers in the first row.
 * @param {{ delimiter?: string, trim?: boolean }} [options]
 * @returns {Record<string, string>[]} Array of objects keyed by header names.
 *
 * @example
 * const rows = parseCSV("name,age\nAlice,30\nBob,25");
 * // [{ name: "Alice", age: "30" }, { name: "Bob", age: "25" }]
 */
export function parseCSV(csv, options = {}) { /* ... */ }
```

**What tools extract**:
- `deno doc` → module docs, export summaries, parameter types and descriptions
- IDE hover → first sentence of JSDoc block
- `deno test --doc` → `@example` blocks as executable tests
- JSR → auto-generated documentation pages from JSDoc

**Rationale**: JSR auto-generates documentation from published code. Well-documented modules on JSR are the ecosystem standard. `deno test --doc` collapses the distinction between examples and tests — documentation examples that compile and run correctly are verified at CI time.

---

## ID-13: Document Re-Export Modules (Barrels)

**Strength**: CONSIDER

**Summary**: A barrel file (`mod.js`) that re-exports from sub-modules should document what public surface it exposes and how the module is intended to be used.

```js
// Good — barrel with module-level doc
/**
 * Authentication module — login, session management, and password hashing.
 *
 * @example
 * import { login, createSession } from "./auth/mod.js";
 * const session = await login(credentials);
 *
 * @module
 */
export { login, logout } from "./login.js";
export { createSession, destroySession } from "./session.js";
export { hashPassword, verifyPassword } from "./password.js";
```

**Rationale**: Barrel files are the public API surface. Without a module-level doc block, `deno doc` shows a bare list of re-exports with no explanation of what the module is for or how to use it.

**See also**: `02-api-design.md` ID-08, `10-project-structure.md` ID-09

---

## ID-14: Self-Documenting Code — Descriptive Names Eliminate Most Comment Needs

**Strength**: MUST

**Summary**: The most effective documentation is code that doesn't need documentation. Descriptive names for functions, variables, and parameters convey intent without prose.

```js
// Bad — comment needed because names are vague
// Check if the user can access the resource
function check(u, r) {
  return u.role === "admin" || r.ownerId === u.id;
}

// Good — names are the documentation
function canUserAccessResource(user, resource) {
  return user.role === "admin" || resource.ownerId === user.id;
}

// Bad — comment explains what the code does
// Filter out inactive users and get their emails
const emails = users.filter(u => u.active).map(u => u.email);

// Good — intermediate variable names explain each step
const activeUsers = users.filter((user) => user.active);
const activeEmails = activeUsers.map((user) => user.email);
```

**Rationale**: Rauschmayer presents naming conventions as a community-wide readability contract. `camelCase` signals a variable or function; `PascalCase` signals a class; `ALL_CAPS` signals a constant. Each convention carries semantic information without a comment. The goal is code where the "what" is self-evident, so comments can focus exclusively on the "why" (Exploring JS Ch. 9).

---

## ID-15: Named Constants over Magic Values

**Strength**: SHOULD

**Summary**: A named constant documents its purpose. A magic number documents nothing.

```js
// Bad — what is 429? what is 5? what is 1000?
if (response.status === 429) {
  await delay(1000);
  if (attempt < 5) return retry();
}

// Good — names explain everything
const TOO_MANY_REQUESTS = 429;
const RETRY_DELAY_MS = 1000;
const MAX_RETRY_ATTEMPTS = 5;

if (response.status === TOO_MANY_REQUESTS) {
  await delay(RETRY_DELAY_MS);
  if (attempt < MAX_RETRY_ATTEMPTS) return retry();
}
```

**Rationale**: Constants are searchable (find all uses of `MAX_RETRY_ATTEMPTS`), changeable in one place, and self-documenting. Magic values require the reader to understand the domain context to interpret them.

**See also**: `01-core-idioms.md` ID-11

---

## ID-16: Extract Complex Conditions into Named Booleans or Predicates

**Strength**: SHOULD

**Summary**: A complex boolean expression is a comment waiting to happen. Extract it into a named variable or function instead.

```js
// Bad — what does this condition mean?
if (user.role === "admin" || (user.role === "editor" && resource.status === "draft")) {
  allowEdit(resource);
}

// Good — name IS the documentation
const canEdit = user.role === "admin"
  || (user.role === "editor" && resource.status === "draft");
if (canEdit) {
  allowEdit(resource);
}

// Better — predicate function, reusable and testable
function canEditResource(user, resource) {
  if (user.role === "admin") return true;
  return user.role === "editor" && resource.status === "draft";
}

if (canEditResource(user, resource)) {
  allowEdit(resource);
}
```

**Rationale**: The extracted predicate `canEditResource` is self-documenting, independently testable, and reusable. The original compound condition requires the reader to mentally parse operator precedence and role/status combinations. A named boolean is an assertion about what the condition *means*, not what it *computes*.

---

## ID-17: Function Names Describe the Transformation

**Strength**: SHOULD

**Summary**: A function's name should communicate what goes in and what comes out. Verb-noun combinations are the convention.

```js
// Good — names describe the transformation
function parseConfig(rawText) { /* ... */ }
function validateInput(formData) { /* ... */ }
function formatCurrency(cents) { /* ... */ }
function buildQueryString(params) { /* ... */ }

// Bad — vague names that could mean anything
function process(data) { /* ... */ }
function handle(input) { /* ... */ }
function doStuff(x) { /* ... */ }
function run(config) { /* ... */ }
```

**Rationale**: `parseConfig` documents that the function takes raw text and produces a config object — no JSDoc needed for the basic contract. `process(data)` could mean anything; the reader must inspect the implementation or read the JSDoc to understand what it does (Exploring JS Ch. 9; Deep JS Ch. 21).

**See also**: `02-api-design.md` ID-16, ID-17

---

## ID-18: Tests as Documentation — Well-Named Tests Describe Behavior

**Strength**: SHOULD

**Summary**: Test names are executable specifications. Each test name should describe a behavior the code is expected to exhibit.

```js
// Good — test names read as a specification
Deno.test("parseConfig returns default values for missing fields", () => {
  const config = parseConfig("{}");
  assertEquals(config.timeout, 5000);
  assertEquals(config.retries, 3);
});

Deno.test("parseConfig throws SyntaxError for invalid JSON", () => {
  assertThrows(() => parseConfig("{broken"), SyntaxError);
});

Deno.test("parseConfig preserves explicit zero values", () => {
  const config = parseConfig('{"timeout": 0}');
  assertEquals(config.timeout, 0); // not the default
});

// Bad — test names that don't describe behavior
Deno.test("test1", () => { /* ... */ });
Deno.test("parseConfig works", () => { /* ... */ });
Deno.test("edge case", () => { /* ... */ });
```

**Rationale**: Tests are the only documentation that fails when it becomes wrong. Comments can silently diverge from code; a failing test cannot be ignored. Haverbeke: tests are "small labeled programs that verify aspects of code" — the label is the documentation. `deno test` output reads as a specification when names are descriptive (Eloquent JS Ch. 8; Exploring JS Ch. 8).

---

## ID-19: Don't Document Internal Implementation in Public JSDoc

**Strength**: SHOULD

**Summary**: Public JSDoc describes the *contract* (what, not how). Internal implementation details belong in inline comments, not the API documentation.

```js
// Bad — implementation details in public JSDoc
/**
 * Hash a password.
 *
 * Uses a 128-bit random salt generated via crypto.getRandomValues(),
 * then applies 12 rounds of bcrypt using the Blowfish cipher with
 * a 448-bit key schedule, storing the result as a modular crypt
 * format string with the $2b$ identifier prefix.
 *
 * @param {string} password
 * @returns {Promise<string>}
 */
export async function hashPassword(password) { /* ... */ }

// Good — contract only
/**
 * Hash a password using bcrypt with a random salt.
 *
 * @param {string} password - Plaintext password.
 * @returns {Promise<string>} The hashed password in modular crypt format.
 */
export async function hashPassword(password) {
  // Implementation note: using 12 rounds as recommended by OWASP.
  // Adjust via BCRYPT_ROUNDS env var if benchmarks show this is too slow.
  /* ... */
}
```

**Rationale**: Implementation details change without changing the contract. Documenting them in the public JSDoc creates maintenance liability — the implementation comment must be updated on every refactor. Inline `//` comments inside the function body are the right place for implementation notes.

---

## ID-20: Don't Write Essay-Length JSDoc

**Strength**: SHOULD

**Summary**: A sentence or two is usually sufficient. If a function needs a paragraph of explanation, it may need refactoring.

```js
// Bad — essay-length JSDoc for a simple function
/**
 * This function takes an array of user objects as its first parameter
 * and iterates through each user object in the array to check whether
 * the user's "active" property is set to a truthy value. If the
 * user is active, it is included in the resulting filtered array which
 * is then returned to the caller. The original array is not modified
 * by this operation as Array.prototype.filter() creates a new array.
 *
 * @param {User[]} users - An array of user objects to be filtered.
 * @returns {User[]} A new array containing only the active users.
 */
export function getActiveUsers(users) {
  return users.filter((user) => user.active);
}

// Good — concise, informative
/**
 * Filter to active users only.
 *
 * @param {User[]} users
 * @returns {User[]} Active users (new array, original unchanged).
 */
export function getActiveUsers(users) {
  return users.filter((user) => user.active);
}
```

**Rationale**: Long JSDoc blocks discourage reading. If the function name, parameter types, and a single sentence suffice, that's the right amount. Reserve longer descriptions for complex APIs with multiple use patterns, edge cases, or surprising behavior.

---

## ID-21: Don't JSDoc Internal Functions Unless Non-Obvious

**Strength**: CONSIDER

**Summary**: Private helper functions with descriptive names and clear types often need no documentation. Save JSDoc effort for the public API.

```js
// Internal — descriptive name + types are sufficient
function clampToRange(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

// Internal — non-obvious logic DOES deserve a comment
/**
 * Compute the next retry delay with exponential backoff and jitter.
 * Jitter prevents thundering herd when many clients retry simultaneously.
 */
function nextRetryDelay(attempt, baseMs) {
  const exponential = baseMs * 2 ** attempt;
  const jitter = Math.random() * exponential * 0.1;
  return exponential + jitter;
}
```

**Rationale**: Blanket JSDoc on every function produces noise. Internal functions that are called from one or two places, have descriptive names, and accept obvious parameter types are self-documenting. Reserve JSDoc for functions where the name and types alone don't convey the full contract.

---

## ID-22: Update Comments When Code Changes — Stale Comments Are Worse Than None

**Strength**: MUST

**Summary**: A stale comment that describes old behavior actively misleads readers. It is worse than having no comment at all.

```js
// Bad — stale comment contradicts the code
// Retry up to 3 times with linear backoff
const MAX_RETRIES = 5; // changed from 3, but comment wasn't updated
await retry(fn, { maxAttempts: MAX_RETRIES, backoff: "exponential" }); // changed from linear

// Good — comment and code agree
// Retry up to 5 times with exponential backoff
await retry(fn, { maxAttempts: MAX_RETRIES, backoff: "exponential" });

// Best — code is self-documenting, no comment to maintain
await retry(fn, { maxAttempts: MAX_RETRIES, backoff: "exponential" });
```

**Rationale**: A reader who trusts a stale comment will make wrong decisions based on it. This is strictly worse than a reader who sees no comment and reads the code. Every comment is a maintenance obligation — when you change code, audit its comments. If a comment can't be kept in sync, it should be deleted.

---

## ID-23: Delete Commented-Out Code — That's What Version Control Is For

**Strength**: MUST

**Summary**: Commented-out code is dead weight. It confuses readers, clutters diffs, and will never be re-enabled.

```js
// Bad — commented-out code with no context
// const oldConfig = loadLegacyConfig(path);
// if (oldConfig.version < 2) {
//   return migrateConfig(oldConfig);
// }
const config = loadConfig(path);

// Bad — "just in case" preservation
// function deprecatedHelper(x) {
//   return x * 2 + 1;
// }

// Good — clean code, old versions live in git history
const config = loadConfig(path);
```

**Rationale**: Commented-out code raises questions: Is it intentionally disabled? Is it a work-in-progress? Does it need to be re-enabled under some condition? The answer is almost always "no — it was removed but not deleted." Version control (`git log`, `git blame`) preserves every line ever written. Delete the dead code; it's one `git checkout` away if needed. Additionally, block comments (`/* */`) cannot be nested — commenting out code that contains block comments silently truncates at the first `*/`, potentially leaving code executable (Eloquent JS Ch. 2; JS Definitive Guide, §2.2).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Comments explain *why*, not *what* | MUST | Foundation of all documentation discipline |
| 02 | Don't comment obvious code | MUST | AI anti-pattern: line-by-line narration |
| 03 | Comment non-obvious intent | SHOULD | Workarounds, edge cases, business rules |
| 04 | TODO/FIXME with context | SHOULD | Owner, ticket, reason — or don't bother |
| 05 | JSDoc on every exported function | SHOULD | Prose description, not just types |
| 06 | First sentence = summary (< 15 words) | SHOULD | Appears in hover, autocomplete, `deno doc` |
| 07 | Document parameters with prose | SHOULD | Valid values, constraints, edge cases |
| 08 | `@throws` for error contracts | SHOULD | Which errors, under what conditions |
| 09 | Document return value semantics | SHOULD | Especially null vs undefined vs empty |
| 10 | `@example` for non-obvious APIs | CONSIDER | `deno test --doc` runs examples as tests |
| 11 | Module-level JSDoc block | SHOULD | One sentence: what and when to use |
| 12 | Write for tooling | SHOULD | `deno doc`, IDE hover, JSR, `--doc` tests |
| 13 | Document barrel files | CONSIDER | Re-export modules need public surface docs |
| 14 | Self-documenting code | MUST | Descriptive names eliminate most comments |
| 15 | Named constants over magic values | SHOULD | Searchable, changeable, self-documenting |
| 16 | Extract conditions into named predicates | SHOULD | Testable, reusable, reads as intent |
| 17 | Function names describe transformation | SHOULD | Verb-noun: `parseConfig`, `formatDate` |
| 18 | Tests as documentation | SHOULD | Only docs that fail when wrong |
| 19 | Don't expose implementation in JSDoc | SHOULD | Contract, not mechanism |
| 20 | Don't write essay-length JSDoc | SHOULD | A sentence or two; refactor if more is needed |
| 21 | Skip JSDoc for obvious internals | CONSIDER | Save effort for the public API |
| 22 | Update comments with code | MUST | Stale comments are worse than none |
| 23 | Delete commented-out code | MUST | Version control preserves everything |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for naming conventions (ID-12, ID-13) and magic values (ID-11)
- **API Design**: See `02-api-design.md` for method naming (ID-16, ID-17, ID-18), module responsibility (ID-06), and barrel files (ID-08)
- **Error Handling**: See `03-error-handling.md` for custom error types (ID-05, ID-06) and error messages (ID-03)
- **Type Discipline**: See `05-type-discipline.md` for JSDoc type annotations (ID-16–20) — the *syntax* that this guide's *prose* accompanies
- **Functions & Closures**: See `06-functions-closures.md` for `.name` property (ID-30, ID-31) and pure functions (ID-28)
- **Anti-Patterns**: See `09-anti-patterns.md` for naming anti-patterns and verbose-comment patterns
- **Project Structure**: See `10-project-structure.md` for file naming (ID-04, ID-06) and module entry points (ID-08)
- **Deno**: See `12-deno/01-runtime-basics.md` for `deno doc` and `12-deno/02-testing.md` for `deno test --doc`

---

## External References

- [Deno — Documentation Generation](https://docs.deno.com/runtime/reference/cli/doc/)
- [JSR — Auto-Generated Documentation](https://jsr.io/)
- [MDN — JSDoc Reference](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
- *Deep JavaScript* — Axel Rauschmayer
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan
- *Eloquent JavaScript* (4th ed.) — Marijn Haverbeke
