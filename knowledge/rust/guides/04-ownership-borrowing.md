# Ownership, Borrowing, and Lifetimes

Patterns for working with Rust's ownership system: moves and copies, the borrow rules, references and slices, lifetime annotations and elision, `'static` and `Cow`, smart pointers (`Box`, `Rc`, `Arc`, `Weak`), interior mutability, and the deeper machinery (OBRM, drop check, subtyping and variance, splitting borrows) that governs how the compiler reasons about references and destructors.


## OB-01: The Three Ownership Rules

**Strength**: MUST

**Summary**: Every value has exactly one owner; when the owner goes out of scope, the value is dropped. Assignment of a non-`Copy` value moves it — the source becomes invalid.

```rust
// Each value has one owner; assignment moves
let s1 = String::from("hello");
let s2 = s1;                    // s1 is MOVED into s2
// println!("{s1}");            // ❌ compile error: value borrowed after move
println!("{s2}");               // ✅ s2 is the owner now

// Copy types are duplicated instead of moved
let x: i32 = 5;
let y = x;                      // i32 implements Copy
println!("{x} {y}");            // ✅ both valid

// Drop runs automatically when the owner leaves scope
{
    let s = String::from("scoped");
    // ... use s ...
}                               // s is dropped here
```

**Rationale**: Move semantics eliminate double-free bugs at compile time: there is always exactly one owner, so exactly one `drop` runs. The distinction between `Copy` (cheap, stack-only, duplicated) and non-`Copy` (moved) is load-bearing — a type with a heap allocation or a custom `Drop` impl cannot be `Copy`. When you see `let y = x`, read it as "ownership transferred" unless `x`'s type is `Copy`.

**See also**: OB-02 (borrowing avoids the move), OB-15 (OBRM)

---

## OB-02: The Borrow Rules

**Strength**: MUST

**Summary**: At any point, a piece of data has either any number of shared references (`&T`) or exactly one mutable reference (`&mut T`) — never both. References must never outlive their referent.

```rust
// ✅ Many shared borrows — fine
let s = String::from("hello");
let a = &s;
let b = &s;
println!("{a} {b}");

// ✅ One exclusive mutable borrow — fine
let mut v = vec![1, 2, 3];
let m = &mut v;
m.push(4);

// ❌ Shared and mutable at the same time — rejected
let mut v = vec![1, 2, 3];
let r = &v;
let w = &mut v;                     // error: cannot borrow `v` as mutable
println!("{r:?} {w:?}");            // because `r` is still alive here

// ✅ NLL: shared borrow ends at last use, then mutable is fine
let mut v = vec![1, 2, 3];
let r = &v;
println!("{r:?}");                  // last use of r
let w = &mut v;                     // ✅ r is dead, w is fine
w.push(4);
```

**Rationale**: The exclusivity of `&mut` is not just about concurrency — it is what lets the compiler cache reads, reorder writes, eliminate dead stores, and vectorize loops. Non-lexical lifetimes (NLL) make the rule usage-based rather than scope-based: a borrow lives from creation to last use, so refactoring code to end a borrow earlier often fixes conflicts without restructuring.

**See also**: OB-03, OB-12 (splitting borrows when you need disjoint mutable access)

---

## OB-03: References Encode Read vs Exclusive Access

**Strength**: MUST

**Summary**: `&T` is a shared read-only borrow; `&mut T` is an exclusive borrow (not merely a mutable one). Choose the reference kind from how the function uses the data, not from whether it happens to mutate today.

```rust
// ✅ Read-only — takes &T
fn len(v: &Vec<i32>) -> usize { v.len() }

// ✅ Mutates in place — takes &mut T
fn push_one(v: &mut Vec<i32>) { v.push(1); }

// ✅ Needs ownership (consumes or stores) — takes T
fn into_first(v: Vec<i32>) -> Option<i32> { v.into_iter().next() }

// Reborrowing: &mut T reborrowed as &T or &mut T shrinks lifetime to local
fn twice(x: &mut i32) {
    let r: &mut i32 = &mut *x;      // reborrow — r is a fresh &mut with shorter lifetime
    *r += 1;
    *x += 1;                        // original access resumes after r is done
}
```

**Rationale**: `&mut` means "exclusive access," and the compiler relies on that exclusivity for optimization. A function that takes `&mut T` is telling callers "while you've lent this to me, nobody else can see it." Reborrowing is how methods on `&mut self` hand out shorter-lived `&mut` or `&` borrows without consuming the original.

**See also**: OB-09 (prefer borrowing), OB-10 (return owned vs borrowed)

---

## OB-04: Use Slices for Contiguous Views

**Strength**: SHOULD

**Summary**: Accept `&str` instead of `&String`, `&[T]` instead of `&Vec<T>`, `&Path` instead of `&PathBuf`. Slices are fat pointers (pointer + length) that borrow a contiguous range.

```rust
// ❌ BAD: narrow parameter type — forces caller to own a String
fn first_word(s: &String) -> &str {
    s.split_whitespace().next().unwrap_or("")
}
// first_word("hello");                // error: `&str` won't coerce to `&String`

// ✅ GOOD: slice parameter accepts &str, &String (via Deref), and string literals
fn first_word(s: &str) -> &str {
    s.split_whitespace().next().unwrap_or("")
}

first_word("hello");                   // ✅ string literal
first_word(&String::from("hello"));    // ✅ &String coerces to &str
for word in "a b c".split(' ') {
    first_word(word);                  // ✅ already &str
}

// Same pattern for Vec and PathBuf
fn sum(xs: &[i32]) -> i32 { xs.iter().sum() }
fn open(p: &std::path::Path) -> std::io::Result<std::fs::File> {
    std::fs::File::open(p)
}
```

**Rationale**: Slices are the universal borrowed form — `String`, `Vec`, `PathBuf`, and `Box<[T]>` all deref to them. Writing `&str` accepts every caller shape for free; writing `&String` rejects string literals and iterator slices for no gain. Clippy flags this as `ptr_arg`.

**See also**: OB-09, TD-02 (strong types)

---

## OB-05: Prefer Borrowing in Parameters

**Strength**: SHOULD

**Summary**: Take `&T` or `&mut T` by default; take `T` only when the function must store, consume, or transform ownership of the value.

```rust
// ❌ BAD: takes ownership for a read-only operation
fn sum_owned(v: Vec<i32>) -> i32 {
    v.iter().sum()
}
// Caller must clone if they want to keep using the vec:
let v = vec![1, 2, 3];
let _ = sum_owned(v.clone());           // unnecessary allocation

// ✅ GOOD: borrow for read, caller retains the vec
fn sum(v: &[i32]) -> i32 {
    v.iter().sum()
}
let v = vec![1, 2, 3];
let _ = sum(&v);
println!("{v:?}");                      // still valid

// ✅ OWNERSHIP IS APPROPRIATE when the function stores or transforms
struct Record { tags: Vec<String> }

impl Record {
    pub fn new(tags: Vec<String>) -> Self {    // storing — takes ownership
        Self { tags }
    }
    pub fn consume_into_count(self) -> usize {  // transforms — consumes self
        self.tags.len()
    }
}
```

**Rationale**: Taking ownership at API boundaries forces callers to give up (or clone) even when the function only reads. Borrowing keeps callers flexible; `self` consumption should be reserved for constructors, builders' terminal `build`, and explicit transformations.

**See also**: OB-04 (slices), OB-06 (clone strategically)

---

## OB-06: Clone Intentionally, Not to Silence the Borrow Checker

**Strength**: SHOULD

**Summary**: `clone()` is a signal that you need an independent copy. Cloning to work around a borrow error is usually the wrong fix — restructure, reborrow, or use `mem::take`.

```rust
// ❌ BAD: clone-to-satisfy-borrow-checker
fn process(data: &Data) {
    let owned = data.clone();           // why?
    use_data(&owned);                   // &Data would have worked
}

// ✅ GOOD: clone because an independent owner is required
fn spawn_worker(data: &Data) -> std::thread::JoinHandle<()> {
    let owned = data.clone();           // the thread needs 'static ownership
    std::thread::spawn(move || work(&owned))
}

// ✅ GOOD: Rc/Arc clone is cheap — reference count bump
use std::rc::Rc;
let shared = Rc::new(expensive());
let a = Rc::clone(&shared);             // just increments the count
let b = Rc::clone(&shared);

// ✅ GOOD: mem::take instead of clone, when you have &mut
fn drain_name(e: &mut Entry) -> String {
    std::mem::take(&mut e.name)         // steals the String, leaves ""
}
```

**Rationale**: Every `clone()` is a line item in the program's allocation budget. The `Rc::clone(&x)` form (instead of `x.clone()`) is a deliberate convention to make reference-count bumps visually distinct from deep clones. When a borrow checker error says "cannot borrow as X because also borrowed as Y," prefer `mem::take` (OB-19), reborrowing, or splitting the struct (OB-12) before cloning.

**See also**: OB-19 (`mem::take`/`replace`), OB-22 (`Rc`/`Arc`)

---

## OB-07: Return Owned Values; Return References Only When Borrowing from Inputs

**Strength**: SHOULD

**Summary**: A function returning a reference must borrow that reference from one of its inputs (or `&self`). Returning a reference to a local is impossible; returning an owned value is always safe.

```rust
// ✅ Return owned — no lifetime gymnastics
fn greet(name: &str) -> String {
    format!("Hello, {name}!")
}

// ❌ Can't compile: reference to a local dies with the function
fn bad_greet(name: &str) -> &str {
    let s = format!("Hello, {name}!");
    &s                                  // error: `s` does not live long enough
}

// ✅ OK: reference borrowed from input
fn first_word(s: &str) -> &str {
    s.split_whitespace().next().unwrap_or("")
}

// ✅ OK: reference borrowed from &self
impl User {
    pub fn name(&self) -> &str { &self.name }
}

// ✅ Cow: owned OR borrowed depending on input
use std::borrow::Cow;
fn sanitize(s: &str) -> Cow<'_, str> {
    if s.contains('\t') { Cow::Owned(s.replace('\t', " ")) }
    else                { Cow::Borrowed(s) }
}
```

**Rationale**: Lifetimes propagate from inputs to outputs, not out of nowhere. If the data lives inside the function, only an owned return type can carry it out. `Cow<'_, str>` is the right middle ground when the function sometimes allocates and sometimes doesn't — callers pay only when mutation is needed.

**See also**: OB-17 (`Cow`), OB-24 (avoid unbounded lifetimes)

---

## OB-08: Move Closures for Transferring Ownership

**Strength**: SHOULD

**Summary**: Use `move` on a closure to capture its environment by ownership rather than by reference. Required whenever the closure outlives the current scope (threads, async tasks, stored callbacks).

```rust
// ❌ Won't compile: closure borrows, but thread may outlive scope
fn spawn_bad(msg: String) {
    std::thread::spawn(|| {
        println!("{msg}");              // error: may outlive `msg`
    });
}

// ✅ move transfers ownership into the closure
fn spawn_ok(msg: String) {
    std::thread::spawn(move || {
        println!("{msg}");              // msg is owned by the closure
    });
}

// Selective capture: rebind before moving
fn example() {
    let big = vec![0_u8; 1_000_000];
    let summary = big.len();            // Copy the small part out
    std::thread::spawn(move || {
        println!("size = {summary}");   // only `summary` moved
    });
    // big.len() still usable — wait, no; `big` was moved too if referenced
}
```

**Rationale**: A plain closure captures by the least restrictive form: `&T` if it only reads, `&mut T` if it mutates, owned if it moves. `move` forces capture by ownership regardless — this is what `thread::spawn`, async tasks, and `'static` callback slots need. Rebind data into smaller locals before the closure to move only what you want.

**See also**: CA-guide (async tasks), OB-16 (`'static`)

---

## OB-09: Prefer Lifetime Elision

**Strength**: SHOULD

**Summary**: Annotate lifetimes explicitly only when elision can't cover the case. The compiler applies three rules that handle almost every signature.

```rust
// Rule 1: each elided input lifetime becomes a distinct parameter
// Rule 2: if one input lifetime, it's assigned to all elided outputs
// Rule 3: if &self or &mut self is present, its lifetime is assigned to outputs

// ✅ Elided — one input lifetime flows to the output (rule 2)
fn first(s: &str) -> &str { &s[..1] }

// ✅ Elided — self's lifetime flows to the output (rule 3)
impl Parser {
    fn remaining(&self) -> &str { &self.input[self.pos..] }
}

// ❌ Ambiguous — two input lifetimes, no &self, rule 2 doesn't apply
// fn longest(a: &str, b: &str) -> &str { ... }   // compile error

// ✅ Must annotate
fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() > b.len() { a } else { b }
}

// ✅ Annotate when the relationship is non-default
struct Parser<'input> { input: &'input str, pos: usize }
impl<'input> Parser<'input> {
    fn new(input: &'input str) -> Self { Self { input, pos: 0 } }
    fn remaining(&self) -> &'input str {     // return lives as long as input, not self
        &self.input[self.pos..]
    }
}
```

**Rationale**: Lifetime elision is syntactic sugar over a small set of rules — it never changes meaning, only readability. Explicit lifetimes are required when multiple inputs could be the source of the output, or when you want the return reference to outlive `self` (tied to the struct's `'input` instead).

**See also**: OB-10 (struct lifetimes), OB-24 (unbounded lifetimes)

---

## OB-10: Declare Lifetime Parameters on Borrowing Structs

**Strength**: MUST

**Summary**: A struct that stores a reference must name the lifetime as a generic parameter; instances cannot outlive what they borrow.

```rust
// ✅ Single borrowed field — one lifetime parameter
pub struct Parser<'input> {
    input: &'input str,
    pos: usize,
}

impl<'input> Parser<'input> {
    pub fn new(input: &'input str) -> Self { Self { input, pos: 0 } }
}

// ✅ Owned alternative — no lifetime needed
pub struct OwnedParser {
    input: String,
    pos: usize,
}

// ✅ Multiple independent lifetimes when fields come from different sources
pub struct Session<'cfg, 'db> {
    config: &'cfg Config,
    db: &'db mut Database,
}

// ⚠️ A single 'a over unrelated fields is a common mistake — it ties them together
// struct Pair<'a> { x: &'a str, y: &'a str }      // x and y must share a lifetime
// Use two if they come from different sources: struct Pair<'a, 'b> { ... }
```

**Rationale**: Storing a reference in a struct is a promise that the reference outlives the struct. The lifetime parameter is how the borrow checker tracks that. Prefer owned fields when the struct is long-lived or passes between threads; reach for borrowed fields when the struct is short-lived and avoiding an allocation matters.

**See also**: OB-23 (subtyping & variance on struct lifetimes)

---

## OB-11: Understand `'static`

**Strength**: MUST

**Summary**: `'static` means "this value could live forever" — usually because it owns its data or points into static memory. It does not mean "is alive forever."

```rust
// ✅ String literals are &'static str — baked into the binary
let s: &'static str = "hello";

// ✅ Owned types satisfy a 'static bound — they contain no borrowed references
fn spawn<F: FnOnce() + Send + 'static>(f: F) { std::thread::spawn(f); }

let owned = String::from("hi");
spawn(move || println!("{owned}"));     // ✅ String has no borrowed references

// ❌ Borrowed references do NOT satisfy 'static
let local = String::from("hi");
let r: &str = &local;
// spawn(move || println!("{r}"));      // error: `r` has a non-static lifetime

// ✅ Trait objects: `Box<dyn Trait + 'static>` is shorthand for "owns-no-borrows"
fn keep(x: Box<dyn std::fmt::Debug + 'static>) { /* ... */ }
keep(Box::new(String::from("owned")));  // ✅
// keep(Box::new(&local));              // ❌ reference is not 'static
```

**Rationale**: A `'static` bound on a generic parameter means "the value must not borrow from anything short-lived." Owned types (`String`, `Vec`, `Box<T>` where `T: 'static`) trivially satisfy it. The common misreading — "must live for the whole program" — leads to puzzling errors; what the bound really enforces is "no dangling references in your own fields."

**See also**: OB-08 (`move` closures), OB-15 (OBRM)

---

## OB-12: Split Borrows for Disjoint Field Access

**Strength**: SHOULD

**Summary**: The borrow checker tracks struct fields independently. When a method needs mutable access to two fields simultaneously, bind them before the loop or split the struct.

```rust
// ❌ Method-through-&mut-self conflicts with field borrows
struct Game { player: Player, enemies: Vec<Enemy> }

impl Game {
    fn step_bad(&mut self) {
        for enemy in &mut self.enemies {
            // enemy.attack(&mut self.player);   // error: self already mutably borrowed
        }
    }
}

// ✅ Split the borrows into local bindings
impl Game {
    fn step(&mut self) {
        let Game { player, enemies } = self;    // disjoint &mut of each field
        for enemy in enemies.iter_mut() {
            enemy.attack(player);                // ✅ compiles
        }
    }
}

// ⚠️ The borrow checker understands STRUCT FIELDS but not slice elements.
//    For slices, use split_at_mut (the std::slice safe abstraction):
let mut v = [1, 2, 3, 4];
let (left, right) = v.split_at_mut(2);
left[0] += 10;
right[0] += 100;                                // ✅ disjoint halves
```

**Rationale**: "Rust understands struct field disjointness; it does not understand array or slice disjointness" (nomicon). Destructuring `self` into its named fields turns a method-level `&mut self` into per-field borrows that the checker can reason about. For slices, the standard library provides `split_at_mut`, `chunks_mut`, and `iter_mut` as safe abstractions over the unsafe raw-pointer split.

**See also**: OB-20 (safe mutable iterators via `mem::take`), OB-13 (NLL-aware method rewrites)

---

## OB-13: Leverage Non-Lexical Lifetimes

**Strength**: SHOULD

**Summary**: A borrow lives from creation to last use, not to end of scope. If a borrow-checker error blocks a straightforward piece of code, try moving the last use earlier.

```rust
// ✅ NLL: immutable borrow dies at println!; mutable borrow is fine afterward
let mut v = vec![1, 2, 3];
let first = &v[0];
println!("first = {first}");            // last use of `first`
v.push(4);                              // ✅ NLL lets this compile

// ⚠️ CAUTION: destructors count as a "use" — they extend a borrow to end of scope
struct Scoped<'a>(&'a Vec<i32>);
impl Drop for Scoped<'_> { fn drop(&mut self) { /* reads self.0 */ } }

let mut v = vec![1, 2, 3];
let guard = Scoped(&v);
// v.push(4);                           // error: guard's Drop uses `&v` at scope end
drop(guard);                            // explicitly end the borrow early
v.push(4);                              // ✅ now fine
```

**Rationale**: Non-lexical lifetimes make the borrow checker track the last use of each reference rather than its lexical scope, which eliminates a huge class of historically annoying errors. One catch: a type with a `Drop` impl has an implicit "use" at scope end, because its destructor runs there. `drop(x)` forces the end-of-borrow earlier when that matters.

**See also**: OB-02 (borrow rules), OB-16 (Drop recursion)

---

## OB-14: Use `Cow` for Conditional Ownership

**Strength**: CONSIDER

**Summary**: `Cow<'_, T>` (Clone-on-Write) defers allocation: borrow when you can, clone only when you must mutate.

```rust
use std::borrow::Cow;

// ✅ Allocates only when the input actually contains the bad char
pub fn normalize(s: &str) -> Cow<'_, str> {
    if s.contains('\\') {
        Cow::Owned(s.replace('\\', "/"))
    } else {
        Cow::Borrowed(s)                // zero-cost pass-through
    }
}

// ✅ Struct that borrows or owns depending on construction
pub struct Name<'a> {
    value: Cow<'a, str>,
}

impl<'a> Name<'a> {
    pub fn borrowed(s: &'a str) -> Self { Self { value: Cow::Borrowed(s) } }
    pub fn owned(s: String)     -> Self { Self { value: Cow::Owned(s) } }
    pub fn as_str(&self) -> &str { &self.value }
}
```

**Rationale**: `Cow` is the right shape for functions that usually pass through unchanged but occasionally need to allocate. Both variants deref to the borrowed form, so callers read from `&*cow` or `cow.as_ref()` uniformly. Don't reach for `Cow` speculatively — it adds a lifetime parameter and a branch; only use it when measurements or a clearly-conditional allocation justify it.

**See also**: OB-07 (returning references), OB-06 (clone strategically)

---

## OB-15: Ownership-Based Resource Management (OBRM)

**Strength**: MUST

**Summary**: Rust's version of RAII: a type acquires a resource in its constructor and releases it in `Drop`. Every resource — memory, file handles, locks, sockets — is the responsibility of exactly one owner.

```rust
// The standard library's File is an OBRM wrapper around an OS handle
use std::fs::File;
use std::io::Write;

fn write_log(line: &str) -> std::io::Result<()> {
    let mut f = File::create("log.txt")?;   // acquire
    writeln!(f, "{line}")?;
    Ok(())                                  // f drops here — handle closed
}
// No explicit close(). No leak path. No double-close.

// Custom OBRM wrapper
pub struct TempDir { path: std::path::PathBuf }

impl TempDir {
    pub fn new() -> std::io::Result<Self> {
        let path = std::env::temp_dir().join(format!("app-{}", std::process::id()));
        std::fs::create_dir_all(&path)?;    // acquire
        Ok(Self { path })
    }
    pub fn path(&self) -> &std::path::Path { &self.path }
}

impl Drop for TempDir {
    fn drop(&mut self) {
        let _ = std::fs::remove_dir_all(&self.path);   // release; ignore error
    }
}
```

**Rationale**: OBRM is the load-bearing idea behind the entire standard library: `Box`, `Vec`, `File`, `MutexGuard`, `TcpStream` are all convenience wrappers for correct resource management. Because drop runs at scope end on every exit path (normal return, `?`, unwinding), cleanup is not something the programmer must remember. The one caveat (OB-16) is that destructors are not guaranteed to run.

**See also**: OB-16, OB-17 (RAII guards), OB-18 (finalization)

---

## OB-16: Drop Runs Recursively, But Is Not Guaranteed

**Strength**: MUST

**Summary**: After your `Drop::drop` returns, Rust drops every field recursively. Destructors run on normal exit, `?`-return, and unwinding — but `mem::forget`, reference cycles, infinite loops, and aborts can all prevent them. Safety invariants must never depend on drop running.

```rust
// ✅ Drop; fields drop recursively after drop() returns — don't manually drop them
struct Connection {
    socket: std::net::TcpStream,
    buffer: Vec<u8>,
}

impl Drop for Connection {
    fn drop(&mut self) {
        // Flush before closing; fields drop automatically afterward
        let _ = std::io::Write::write_all(&mut self.socket, &self.buffer);
        // Don't: drop(&mut self.socket); — double-free
    }
}

// ❌ DANGEROUS: unsafe code relying on drop to preserve an invariant
// fn leak_guard<'a>(x: &'a Data) -> Guard<'a> { /* unsafe assumes Drop runs */ }
//   This used to be thread::scoped / JoinGuard — REMOVED from std because
//   mem::forget(guard) could skip the join, causing use-after-free.

// ✅ Leak amplification: forgetting a Vec::drain iterator leaks the elements,
//    but does NOT cause use-after-free, because Vec sets len = 0 before iteration.
let mut v = vec![Box::new(1), Box::new(2)];
{
    let d = v.drain(..);
    std::mem::forget(d);                 // skip drop — elements leak
}
assert_eq!(v.len(), 0);                  // v is consistent, not dangling
```

**Rationale**: `mem::forget` is safe. Destructor bypass is always possible through safe code (cycles, forget, panics during unwind). Unsafe code must therefore design invariants so that *skipping* drop just leaks memory rather than causing UB — this is the "leak amplification" pattern used by `Vec::drain` and friends.

**See also**: OB-15, OB-17, OB-21 (drop check)

---

## OB-17: RAII Guards for Scoped Access

**Strength**: SHOULD

**Summary**: Return a guard type from an acquisition method; the guard holds a reference to the resource and releases it in `Drop`. The borrow checker enforces that data accessed through the guard cannot outlive it.

```rust
use std::sync::Mutex;

let m = Mutex::new(Vec::<i32>::new());
{
    let mut guard = m.lock().unwrap();       // acquire — returns MutexGuard<'_, Vec<i32>>
    guard.push(42);                           // Deref gives &mut Vec<i32>
}                                             // guard drops here — lock released

// Custom guard — scope exit restores state
pub struct Indenter<'a> { log: &'a mut Log }

impl<'a> Indenter<'a> {
    pub fn new(log: &'a mut Log) -> Self {
        log.indent += 1;
        Self { log }
    }
}

impl Drop for Indenter<'_> {
    fn drop(&mut self) {
        self.log.indent -= 1;                 // restore on any exit path
    }
}

// Usage: Indenter holds &mut Log, so the log is borrow-locked for the guard's lifetime
fn emit(log: &mut Log) {
    log.write("outer");
    let _nested = Indenter::new(log);
    // log.write(...)  — wait, log is mutably borrowed by `_nested`; use _nested
}                                             // _nested drops — indent back down
```

**Rationale**: The guard pattern replaces "remember to clean up" with "the type system guarantees cleanup." A guard holds `&'a T` (or `&'a mut T`) to its resource, so the borrow checker enforces that any reference obtained through the guard dies before the guard does. `Deref`/`DerefMut` on the guard make it transparent at call sites. Name the guard variable `_name` if you don't reference it — but never just `_`, which drops immediately.

**See also**: OB-15 (OBRM), OB-18 (finalization)

---

## OB-18: Use Destructors as Rust's `finally`

**Strength**: SHOULD

**Summary**: Rust has no `finally`; bind a guard with a `Drop` impl at the start of the scope to ensure cleanup runs regardless of the exit path.

```rust
// ✅ Guard variable runs Drop on every exit: normal, `?`, panic
fn process(paths: &[std::path::Path]) -> std::io::Result<()> {
    struct Exit;
    impl Drop for Exit {
        fn drop(&mut self) {
            eprintln!("process: exiting");
        }
    }
    let _exit = Exit;                        // not `_` — that drops immediately

    for p in paths {
        let _contents = std::fs::read_to_string(p)?;    // early return on error
        // ... work ...
    }
    Ok(())                                   // _exit still runs
}
```

**Rationale**: The `?` operator and panic unwinding make imperative cleanup fragile — a `cleanup()` call before every `return` is easy to forget. A guard bound to a named local (`_exit`, not `_`) runs regardless. Two warnings: (1) a destructor that panics during unwinding aborts the thread, so keep finalization cheap and infallible; (2) guards must be owned locals, not `Rc<Guard>` — shared ownership defeats the scope semantics.

**See also**: OB-17 (guards), OB-15 (OBRM)

---

## OB-19: Move Out of `&mut` with `mem::take` / `mem::replace`

**Strength**: SHOULD

**Summary**: You cannot move a value out of a `&mut` reference, because the referent must remain valid. `mem::take(place)` swaps in `Default::default()`; `mem::replace(place, new)` swaps in a specified value.

```rust
use std::mem;

// ✅ Change an enum variant without cloning
enum Connection {
    Connected { name: String, socket: TcpStream },
    Closed,
}

fn close(c: &mut Connection) {
    if let Connection::Connected { name, .. } = c {
        let owned_name: String = mem::take(name);   // steal, leave empty String
        // ... record the close with owned_name ...
        *c = Connection::Closed;
    }
}

// ✅ mem::replace when there's no sensible Default
fn replace_config(slot: &mut Config, new: Config) -> Config {
    mem::replace(slot, new)                         // returns old value
}

// ✅ Option::take is the specialization for Option<T>
let mut opt = Some(String::from("hi"));
let owned: Option<String> = opt.take();             // opt is now None
```

**Rationale**: The borrow checker requires a `&mut` referent to always hold a valid value. `mem::take` and `mem::replace` satisfy that by swapping something in before handing the old value out. This is the canonical alternative to "clone to satisfy the borrow checker" and is how safe state-machine transitions are written.

**See also**: OB-06 (avoid unnecessary clones), OB-20 (iterators)

---

## OB-20: Safe Mutable Iterators via Borrow Splitting

**Strength**: CONSIDER

**Summary**: Implement mutable iterators without `unsafe` by combining `mem::take` (on the iterator's state) with `split_at_mut` or `Option::take`.

```rust
// ✅ Safe IterMut over a slice — the stdlib pattern
pub struct IterMut<'a, T: 'a>(&'a mut [T]);

impl<'a, T> Iterator for IterMut<'a, T> {
    type Item = &'a mut T;
    fn next(&mut self) -> Option<Self::Item> {
        // Steal the slice, replacing it with an empty one
        let slice = std::mem::take(&mut self.0);
        if slice.is_empty() { return None; }
        let (head, tail) = slice.split_at_mut(1);    // safe abstraction over unsafe split
        self.0 = tail;
        head.get_mut(0)
    }
}

// ✅ Safe IterMut over a singly-linked list — Option::take
pub struct ListIterMut<'a, T> { next: Option<&'a mut Node<T>> }
struct Node<T> { elem: T, next: Option<Box<Node<T>>> }

impl<'a, T> Iterator for ListIterMut<'a, T> {
    type Item = &'a mut T;
    fn next(&mut self) -> Option<Self::Item> {
        self.next.take().map(|node| {                // moves out, leaves None
            self.next = node.next.as_deref_mut();
            &mut node.elem
        })
    }
}
```

**Rationale**: The `Iterator::next(&mut self) -> Option<Self::Item>` signature decouples `Self::Item` from `self`, so callers can hold multiple yielded items simultaneously. Safety comes from yielding each element exactly once, which ownership transfer via `take` enforces structurally. "Perhaps surprisingly, mutable iterators don't require unsafe code to be implemented for many types" (nomicon).

**See also**: OB-12 (splitting borrows), OB-19 (`mem::take`)

---

## OB-21: Drop Check — The Big Rule

**Strength**: CONSIDER

**Summary**: For a generic type with `Drop`, its generic parameters must strictly outlive it, because the destructor might access borrowed data. Adding a `Drop` impl can cause the borrow checker to reject previously-valid programs.

```rust
// ✅ Without Drop: borrowed data need only coexist with, not outlive, the type
struct Inspector<'a>(&'a u8);

fn ok() {
    let mut world = (None, Box::new(1));
    world.0 = Some(Inspector(&world.1));        // ✅ fine without Drop
}

// ❌ With Drop: the destructor might READ self.0 — so 'a must strictly outlive
struct InspectorDrop<'a>(&'a u8);

impl Drop for InspectorDrop<'_> {
    fn drop(&mut self) { println!("saw {}", self.0); }
}

// fn bad() {
//     let mut world = (None, Box::new(1));
//     world.0 = Some(InspectorDrop(&world.1));
//     // ERROR: `world.1` does not live long enough —
//     // Drop order is declaration order, so world.1 drops before world.0's destructor
// }

// Within a struct, fields drop in declaration order. Variables drop in reverse.
// If drop order matters, reorder fields or use ManuallyDrop.
```

**Rationale**: "For a generic type to soundly implement drop, its generics arguments must strictly outlive it" (nomicon, "The Big Rule"). The drop checker enforces this by looking at the parameters of any `Drop` impl on a generic type. Adding `Drop` to an existing generic type is therefore a silently breaking change for users of that type — it constrains lifetimes that were previously unconstrained.

**See also**: OB-23 (variance), TD-17 (`PhantomData`), US-guide (`#[may_dangle]`)

---

## OB-22: Choose the Right Smart Pointer

**Strength**: SHOULD

**Summary**: `Box<T>` for single heap-owned; `Rc<T>` for shared single-threaded; `Arc<T>` for shared cross-thread; `Weak<T>` to break reference cycles.

```rust
// Box: single owner, heap allocation. Required for recursive types, trait objects,
// and moving large values cheaply.
let trait_obj: Box<dyn std::fmt::Debug> = Box::new(42);

// Rc: multiple owners, single-threaded. Rc::clone is a cheap count increment.
use std::rc::Rc;
let shared = Rc::new(vec![1, 2, 3]);
let a = Rc::clone(&shared);
let b = Rc::clone(&shared);            // all three point to the same Vec

// Arc: multiple owners, thread-safe (atomic count). Use instead of Rc in any
// type that may cross threads or appear in a future.
use std::sync::Arc;
let data = Arc::new(vec![1, 2, 3]);
let h = std::thread::spawn({
    let data = Arc::clone(&data);
    move || data.iter().sum::<i32>()
});
let _ = h.join();

// Weak: non-owning back-reference — upgrade() returns Option<Rc<T>>.
use std::rc::Weak;
struct Node { parent: Option<Weak<Node>>, children: Vec<Rc<Node>> }

// Rc<RefCell<T>>: the common "shared mutable" pattern in single-threaded code.
use std::cell::RefCell;
let counter = Rc::new(RefCell::new(0_i32));
*counter.borrow_mut() += 1;
```

| Smart pointer    | Owners   | Check      | Mutability          | Thread-safe |
|------------------|----------|------------|---------------------|-------------|
| `Box<T>`         | Single   | Compile    | Via `&mut Box<T>`   | If T is     |
| `Rc<T>`          | Multiple | Compile    | Immutable only      | No          |
| `Arc<T>`         | Multiple | Compile    | Immutable only      | Yes         |
| `RefCell<T>`     | Single   | **Runtime**| Interior mutability | No          |
| `Rc<RefCell<T>>` | Multiple | Runtime    | Interior mutability | No          |
| `Arc<Mutex<T>>`  | Multiple | Runtime    | Interior mutability | Yes         |
| `Weak<T>`        | Non-owner| —          | —                   | Matches Rc/Arc |

**Rationale**: `Rc`/`Arc` enable multiple ownership; `Weak` breaks cycles (parent↔child links where the child holds `Weak<Parent>`). Reaching for `Rc`/`RefCell` to "silence the borrow checker" is usually a sign that you should restructure the data — shared mutable state is rarely the right first answer.

**See also**: OB-23 (variance of `Rc`/`Arc`), CA-guide (`Arc` across threads)

---

## OB-23: Understand Variance (Briefly)

**Strength**: CONSIDER

**Summary**: Variance determines how lifetime/type subtyping propagates through a generic. `&'a T` is covariant in `'a` and `T`; `&'a mut T` is invariant in `T`; `Cell<T>` and `UnsafeCell<T>` are invariant in `T`. Invariance always wins when combined.

```rust
// ✅ Covariance: &'static str substitutes for &'short str
fn debug<'a>(a: &'a str, b: &'a str) { println!("{a} {b}"); }

let hello: &'static str = "hello";
{
    let world = String::from("world");
    debug(hello, &world);               // hello downgrades 'static → 'world
}

// ❌ Invariance of &mut T: prevents smuggling a short-lived &str
//    into a long-lived &'static str slot, which would be UAF after scope exit.
// fn assign<T>(slot: &mut T, val: T) { *slot = val; }
// let mut hello: &'static str = "hello";
// {
//     let world = String::from("world");
//     assign(&mut hello, &world);      // compile error: world does not live long enough
// }

// Summary:
// - & T, Box<T>, Vec<T>       : covariant in T
// - &mut T, Cell<T>, *mut T   : invariant in T
// - fn(T) -> U                : contravariant in T, covariant in U
// - Struct inherits field variance; INVARIANCE WINS all conflicts
```

**Rationale**: Without covariance, `&'static str` could not pass to a function expecting `&'a str`, which would be unusable. Without invariance on `&mut T`, writes could smuggle short-lived references into long-lived slots. Everyday Rust code rarely confronts variance directly, but it surfaces in library code — particularly around raw pointers, `PhantomData`, and lifetime-parameterized types. When in doubt, invariance is the safe default.

**See also**: TD-17 (`PhantomData` shapes), TD-18 (choosing variance), US-guide (raw pointers)

---

## OB-24: Avoid Unbounded Lifetimes

**Strength**: MUST

**Summary**: A function that returns a reference whose lifetime is not derived from any input has an *unbounded* lifetime — the compiler will shape it to whatever the caller demands. Unbounded lifetimes are more dangerous than `'static` and almost always indicate a bug in `unsafe` code.

```rust
// ❌ Unbounded lifetime from raw pointer deref
// fn leaky<'a>(p: *const u8) -> &'a u8 {
//     unsafe { &*p }              // 'a is unbounded — molds to any caller context
// }

// ✅ Tie output lifetime to an input — prevents unbounded inference
pub fn safe_deref<'a>(p: &'a *const u8) -> &'a u8 {
    unsafe { &**p }                // 'a is now bounded by the input reference
}

// Unbounded > 'static in power:
// &'static &'a T    — fails to typecheck
// &'unbounded &'a T — compiler infers 'unbounded = 'a, compiles fine
```

**Rationale**: Unbounded lifetimes arise most often from dereferencing raw pointers or from `mem::transmute`. "Such a lifetime becomes as big as context demands" (nomicon) — which means the compiler won't catch use-after-free at the call site. The defense is to always constrain output lifetimes to inputs: either via elision (preferred) or explicit `'a` annotation that connects the input and output.

**See also**: OB-09 (elision), US-guide (raw-pointer safety)

---

## OB-25: Interior Mutability — `Cell`, `RefCell`, and Friends

**Strength**: CONSIDER

**Summary**: When a type needs to mutate through a shared reference (`&self`), reach for interior-mutability primitives: `Cell<T>` for `Copy` types, `RefCell<T>` for runtime-checked borrows, `Mutex<T>`/`RwLock<T>` across threads. All are built on `UnsafeCell<T>` (covered in guide 09).

```rust
use std::cell::{Cell, RefCell};

// ✅ Cell<T> for Copy types — zero-overhead set/get, no borrow
struct Counter { n: Cell<u32> }
impl Counter {
    pub fn bump(&self) -> u32 {          // &self, not &mut
        let v = self.n.get() + 1;
        self.n.set(v);
        v
    }
}

// ✅ RefCell<T> for non-Copy — runtime borrow check, panics on violation
struct Document { body: RefCell<String> }
impl Document {
    pub fn append(&self, s: &str) { self.body.borrow_mut().push_str(s); }
    pub fn len(&self) -> usize    { self.body.borrow().len() }
}

// ⚠️ Double borrow_mut() from RefCell panics at runtime:
let d = Document { body: RefCell::new(String::new()) };
let _a = d.body.borrow_mut();
// let _b = d.body.borrow_mut();     // panic: already borrowed: BorrowMutError

// Across threads: swap RefCell for Mutex / RwLock (guide 07).
use std::sync::Mutex;
struct SharedDoc { body: Mutex<String> }
```

**Rationale**: Interior mutability lets a type expose `&self` methods that still mutate internal state — essential for caches, lazy initialization, and observer patterns. The cost: `RefCell` moves a compile-time check to runtime (and *panics* on violation); `Cell` works only for `Copy`. Prefer structural refactoring when a design pulls you toward `Rc<RefCell<T>>` — shared mutable state is expensive to reason about.

**See also**: OB-22 (`Rc<RefCell<T>>`), CA-guide (`Mutex`/`RwLock`), US-guide (`UnsafeCell`)


## Borrow-Checker Debugging Checklist

When a borrow-checker error blocks you, walk this list before reaching for `clone()`:

```rust
// 1. Is this NLL-fixable? Move the last use of the conflicting borrow earlier.
// 2. Can you reborrow? `let r: &mut T = &mut *self.field;`
// 3. Can you split the struct? Destructure `self` into per-field locals.
// 4. Can you use mem::take / mem::replace to move out of &mut?
// 5. Does a Drop impl extend a borrow? `drop(guard)` early to release.
// 6. Is the struct definition over-constraining? Consider separate lifetimes.
// 7. Is a type parameter the problem? Check variance (`PhantomData` tricks).
// 8. Only if none of these apply: clone with a comment explaining why.
```


## Summary Table

| Pattern | Strength | Key Principle |
|---------|----------|---------------|
| OB-01 Three ownership rules | MUST | One owner, moved on assignment, dropped at scope exit |
| OB-02 Borrow rules | MUST | Shared XOR mutable; NLL from creation to last use |
| OB-03 Reference kinds | MUST | `&mut` means exclusive, not just mutable |
| OB-04 Use slices | SHOULD | `&str` over `&String`, `&[T]` over `&Vec<T>` |
| OB-05 Prefer borrowing | SHOULD | Take ownership only to store or consume |
| OB-06 Clone intentionally | SHOULD | Never to "satisfy" the borrow checker |
| OB-07 Return owned, references from inputs | SHOULD | Lifetimes propagate from inputs only |
| OB-08 Move closures | SHOULD | Required when a closure outlives its scope |
| OB-09 Lifetime elision | SHOULD | Annotate only when the three rules don't cover it |
| OB-10 Lifetime params on structs | MUST | Borrowing structs declare `'a` explicitly |
| OB-11 Understand `'static` | MUST | "Could live forever" — owned types qualify |
| OB-12 Split borrows | SHOULD | Destructure `self` for disjoint field access |
| OB-13 Leverage NLL | SHOULD | Borrows end at last use; `drop()` forces earlier |
| OB-14 `Cow` for conditional ownership | CONSIDER | Allocate only when you must mutate |
| OB-15 OBRM | MUST | Acquire in constructor, release in `Drop` |
| OB-16 Drop is recursive but not guaranteed | MUST | Never depend on drop for safety invariants |
| OB-17 RAII guards | SHOULD | Guard holds `&'a T`; borrow checker enforces lifetime |
| OB-18 Destructors as `finally` | SHOULD | Named guard (`_exit`), not bare `_` |
| OB-19 `mem::take` / `mem::replace` | SHOULD | Move out of `&mut` without cloning |
| OB-20 Safe mutable iterators | CONSIDER | `mem::take` + `split_at_mut` / `Option::take` |
| OB-21 Drop check | CONSIDER | Generic `Drop` requires params to strictly outlive |
| OB-22 Smart pointer selection | SHOULD | `Box`/`Rc`/`Arc`/`Weak` for ownership shape |
| OB-23 Understand variance | CONSIDER | Invariance wins; `&mut T` invariant in T |
| OB-24 Avoid unbounded lifetimes | MUST | Output lifetimes must derive from inputs |
| OB-25 Interior mutability | CONSIDER | `Cell` for `Copy`; `RefCell` runtime-checks |


## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for `Clone`/`Copy` derivation and the preference for iteration over index-based loops.
- **Type Design**: See `05-type-design.md` for TD-17/TD-18 (`PhantomData`, variance control) and TD-23–TD-25 (`Pin`, `!Unpin`, self-referential types) that build on the ownership machinery covered here.
- **Concurrency and Async**: See `07-concurrency-async.md` for `Send`/`Sync`, `Arc<Mutex<T>>`, and holding guards across `await`.
- **Unsafe and FFI**: See `09-unsafe-ffi.md` for raw pointers, `UnsafeCell<T>`, `MaybeUninit<T>`, and `#[may_dangle]` — the unsafe foundations under the safe types discussed here.


## External References

- [The Rust Programming Language — Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [The Rust Programming Language — Smart Pointers](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html)
- [The Rustonomicon — Ownership and Lifetimes](https://doc.rust-lang.org/nomicon/ownership.html) (references, aliasing, lifetimes, limits of lifetimes)
- [The Rustonomicon — Subtyping and Variance](https://doc.rust-lang.org/nomicon/subtyping.html)
- [The Rustonomicon — Drop Check](https://doc.rust-lang.org/nomicon/dropck.html) and [PhantomData](https://doc.rust-lang.org/nomicon/phantom-data.html)
- [The Rustonomicon — Splitting Borrows](https://doc.rust-lang.org/nomicon/borrow-splitting.html)
- [The Rustonomicon — OBRM](https://doc.rust-lang.org/nomicon/obrm.html)
- [The Rust Reference — Lifetime Elision](https://doc.rust-lang.org/reference/lifetime-elision.html)
- [`std::mem::take`](https://doc.rust-lang.org/std/mem/fn.take.html), [`std::mem::replace`](https://doc.rust-lang.org/std/mem/fn.replace.html), [`std::borrow::Cow`](https://doc.rust-lang.org/std/borrow/enum.Cow.html)
- Rust Design Patterns: [Borrowed Types for Arguments](https://rust-unofficial.github.io/patterns/idioms/coercion-arguments.html), [RAII Guards](https://rust-unofficial.github.io/patterns/patterns/behavioural/RAII.html), [Finalisation in Destructors](https://rust-unofficial.github.io/patterns/idioms/dtor-finally.html)
- Pragmatic Rust Guidelines: M-AVOID-STATICS, M-TYPES-SEND (see guide 07)
