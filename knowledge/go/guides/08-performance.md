# Performance

Performance patterns for Go programs — where Uber or Google explicitly documents a Good/Bad that materially affects runtime or memory cost. Grounded in the *Uber Go Style Guide* (notably its `Performance` chapter) and the *Google Go Style Guide* (Decisions §§ Size hints, String concatenation, Receiver type, Pass values, Copying; Best Practices §§ Logging, Must functions).

The underlying discipline is not "do these things always." It is: **write clear code first (chapters 01–07), profile, then apply these patterns where profiling says they help.** Uber's Performance chapter opens with the rule verbatim — "Performance-specific guidelines apply only to the hot path." Google Decisions §Size hints: "Most code does not need a size hint or preallocation." Google Decisions §Receiver type: "When the performance does matter, it is important to profile both approaches with a realistic benchmark before deciding that one approach outperforms the other."

Target environment: **Go 1.22+**, standard library first, `go test -bench` / `pprof` / `benchstat` for measurement.

---

## PF-01: Profile Before Optimizing — Benchmarks Drive Changes

**Strength**: MUST

**Summary**: Before rewriting code for performance, measure it. Go ships `testing.B` benchmarks, `pprof`, and `benchstat`; use them to confirm that (a) the target is actually the bottleneck and (b) the change improves it.

```go
// Good — benchmark both approaches, compare with benchstat
func BenchmarkParseOld(b *testing.B) {
    for i := 0; i < b.N; i++ {
        _ = parseOld(input)
    }
}

func BenchmarkParseNew(b *testing.B) {
    for i := 0; i < b.N; i++ {
        _ = parseNew(input)
    }
}
// go test -bench=Parse -benchmem -count=10 > old.txt
// ... change the code ...
// go test -bench=Parse -benchmem -count=10 > new.txt
// benchstat old.txt new.txt

// Bad — optimize by intuition, ship, hope
func Parse(s string) (Result, error) {
    // "I made this faster by replacing the map with a slice"
    // ... but did the benchmark change? nobody knows
}
```

**Rationale**: Performance intuition is unreliable; the Go runtime, compiler, and CPU all conspire to make "obviously slower" code sometimes faster. Uber's performance chapter is introduced with empirical benchmark numbers for every Good/Bad it lists. Google Decisions §Size hints: "Size hints and preallocation are important steps **when combined with empirical analysis of the code and its integrations**." Google Decisions §Receiver type adds: "There is a lot of misinformation about whether passing a value or a pointer to a function can affect performance... When the performance does matter, it is important to profile both approaches with a realistic benchmark before deciding" (Uber Style Guide §Performance; Google Decisions §Size hints; Google Decisions §Receiver type).

**See also**: PF-02, PF-34

---

## PF-02: Apply Performance Guidelines Only to the Hot Path

**Strength**: SHOULD

**Summary**: The patterns in this chapter trade small amounts of clarity for measurable performance. Apply them where profiling shows the code matters — not to every function in the codebase.

```go
// Good — the hot loop justifies the hoisted buffer and preallocation
func serveBatch(w http.ResponseWriter, rs []Record) error {
    buf := bufPool.Get().(*bytes.Buffer)
    defer bufPool.Put(buf)
    buf.Reset()

    buf.Grow(len(rs) * 64) // profiling showed median record ~60 bytes
    for _, r := range rs {
        fmt.Fprintf(buf, "%d,%s\n", r.ID, r.Name)
    }
    _, err := w.Write(buf.Bytes())
    return err
}

// Bad — micro-optimizing code that is called twice at startup
func loadConfig() (*Config, error) {
    // 15 lines of hand-tuned byte-slice manipulation
    // instead of json.Unmarshal, for a path that runs once
    // ...
}
```

**Rationale**: Every performance tweak imposes a readability cost. Concentrated on the hot path, that cost is a fair trade; spread across the whole codebase, it is waste. Uber §Performance: "Performance-specific guidelines apply only to the hot path." Google §Size hints: "It is acceptable to preallocate when the final size is known... but this is not a readability requirement, and may not be worth the clutter in small cases" (Uber Style Guide §Performance; Google Decisions §Size hints).

**See also**: PF-01

---

## PF-03: Prefer `strconv` over `fmt.Sprintf` for Primitive Conversions

**Strength**: SHOULD

**Summary**: Converting numbers and booleans to strings is substantially faster with `strconv` than with `fmt`, because `fmt` pays for format-string parsing and reflection on its arguments.

```go
// Good
for i := 0; i < b.N; i++ {
    s := strconv.Itoa(rand.Int())
}
// BenchmarkStrconv-4     64.2 ns/op    1 allocs/op

// Bad
for i := 0; i < b.N; i++ {
    s := fmt.Sprint(rand.Int())
}
// BenchmarkFmtSprint-4  143 ns/op     2 allocs/op

// Good — common variants
s := strconv.Itoa(n)             // int -> string
s := strconv.FormatInt(v, 10)    // int64 -> string
s := strconv.FormatFloat(f, 'f', -1, 64)
s := strconv.FormatBool(b)
s := strconv.Quote(raw)          // equivalent to %q
```

**Rationale**: `fmt` uses reflection to inspect its arguments and parse a format specifier; `strconv` is a typed, specialized routine. Uber §Prefer strconv over fmt: "When converting primitives to/from strings, `strconv` is faster than `fmt`." The difference is about 2× on both time and allocations. Use `fmt` only when you actually need formatting (padding, width, `%q`, multiple arguments) (Uber Style Guide §Prefer strconv over fmt).

**See also**: PF-04

---

## PF-04: Choose the Right String Concatenation Tool for the Job

**Strength**: SHOULD

**Summary**: `+` for a handful of strings, `fmt.Sprintf` when you are really formatting, `strings.Builder` when assembling a string in a loop. The three have very different cost curves.

```go
// Good — few strings: use +
key := "projectid: " + p

// Good — actual formatting: use fmt.Sprintf
str := fmt.Sprintf("%s [%s:%d]-> %s", src, qos, mtu, dst)

// Bad — simulating fmt.Sprintf with +
bad := src.String() + " [" + qos.String() + ":" + strconv.Itoa(mtu) + "]-> " + dst.String()

// Good — piecemeal construction in a loop: use strings.Builder
var b strings.Builder
b.Grow(len(digitsOfPi) * 32) // optional capacity hint
for i, d := range digitsOfPi {
    fmt.Fprintf(&b, "the %d digit of pi is: %d\n", i, d)
}
str := b.String()

// Bad — concatenating in a loop with += (quadratic)
var s string
for i, d := range digitsOfPi {
    s += fmt.Sprintf("the %d digit of pi is: %d\n", i, d)
}
```

**Rationale**: `strings.Builder` accumulates into an internal `[]byte` and produces one final string; its total cost is amortized O(n). `+=` in a loop repeatedly allocates and copies — O(n²). Google Decisions §String concatenation: "Prefer using `strings.Builder` when building a string bit-by-bit. `strings.Builder` takes amortized linear time, whereas `+` and `fmt.Sprintf` take quadratic time when called sequentially to form a larger string" (Google Decisions §String concatenation).

**Note**: When the destination is an `io.Writer`, skip the builder entirely and use `fmt.Fprintf(w, ...)` rather than building a string and writing it.

**See also**: PF-03, PF-05, PF-06

---

## PF-05: Write Directly to `io.Writer` with `Fprintf`, Skip the Temporary

**Strength**: SHOULD

**Summary**: When the final destination of a string is an `io.Writer` (an HTTP response, a log, a file), use `fmt.Fprintf(w, ...)` instead of `w.Write([]byte(fmt.Sprintf(...)))`.

```go
// Good
fmt.Fprintf(w, "user %d: %s\n", id, name)

// Bad — builds an intermediate string and byte slice
w.Write([]byte(fmt.Sprintf("user %d: %s\n", id, name)))
```

**Rationale**: `Sprintf` allocates a string; `[]byte(s)` copies it into a new byte slice. `Fprintf` writes directly through the `Writer` using an internal buffer pool. Google Decisions §String concatenation: "When the output of the string-building operation is an `io.Writer`, don't construct a temporary string with `fmt.Sprintf` just to send it to the Writer. Instead, use `fmt.Fprintf` to emit to the Writer directly" (Google Decisions §String concatenation).

**See also**: PF-04

---

## PF-06: `strings.Builder` over `bytes.Buffer` When the Result Is a String

**Strength**: SHOULD

**Summary**: `strings.Builder` produces a `string` without an extra copy. `bytes.Buffer` produces `[]byte`; calling `.String()` on it incurs a copy (by design, so the buffer can continue to be used safely).

```go
// Good — result is a string
var b strings.Builder
b.WriteString("hello, ")
b.WriteString(name)
return b.String()

// Good — result is bytes, or the buffer is also used as an io.Reader
var buf bytes.Buffer
json.NewEncoder(&buf).Encode(v)
return buf.Bytes()

// Bad — using bytes.Buffer when you only need a string
var buf bytes.Buffer
buf.WriteString("hello, ")
buf.WriteString(name)
return buf.String() // copies the bytes to a new string
```

**Rationale**: `strings.Builder` was added (Go 1.10) specifically to avoid the `.String()` copy that `bytes.Buffer` performs. It is also a value type and its zero value is ready to use. Google Decisions §Copying warns that `bytes.Buffer` additionally contains an inline small-array optimization, so copying a `Buffer` value can produce aliasing bugs — another reason to reach for `strings.Builder` when bytes are not the goal (Google Decisions §Copying; Google Decisions §String concatenation).

**See also**: PF-04

---

## PF-07: Avoid Repeated `[]byte`/`string` Conversion of Constants

**Strength**: SHOULD

**Summary**: Every `[]byte("literal")` inside a loop copies the bytes. Hoist the conversion once; pay it once.

```go
// Good
data := []byte("Hello world")
for i := 0; i < b.N; i++ {
    w.Write(data)
}
// BenchmarkGood-4  500000000   3.25 ns/op

// Bad
for i := 0; i < b.N; i++ {
    w.Write([]byte("Hello world"))
}
// BenchmarkBad-4    50000000  22.2 ns/op
```

**Rationale**: Although the compiler can sometimes optimize the string-to-byte conversion of a constant, the general case is a byte-by-byte copy on every iteration. Hoisting the conversion makes the allocation explicit and executed once. Uber §Avoid repeated string-to-byte conversions: "Do not create byte slices from a fixed string repeatedly. Instead, perform the conversion once and capture the result" (Uber Style Guide §Avoid repeated string-to-byte conversions).

---

## PF-08: Understand `[]byte` ↔ `string` Conversion Costs

**Strength**: CONSIDER

**Summary**: Converting between `string` and `[]byte` copies the bytes in both directions — `string` is immutable and `[]byte` is mutable, so the runtime must not share the backing memory. Design APIs so you stay in whichever type matches the work.

```go
// Good — the API accepts and returns []byte; no conversion needed at boundaries
func transform(data []byte) []byte {
    return bytes.ToUpper(data)
}

// Good — accept string when the caller has a string; convert once at the edge
func countVowels(s string) int {
    var n int
    for i := 0; i < len(s); i++ {
        switch s[i] {
        case 'a', 'e', 'i', 'o', 'u':
            n++
        }
    }
    return n
}

// Bad — roundtripping for no reason
func countVowels(s string) int {
    data := []byte(s)            // copy 1
    // ... byte-oriented work ...
    return n
}
```

**Warning — `unsafe` tricks**: Internet posts sometimes recommend using `unsafe.Pointer` or `reflect.SliceHeader` to avoid the copy. **Do not do this in normal code.** Go's string/byte model guarantees that strings are immutable. Aliasing a `string` and `[]byte` through `unsafe` breaks that guarantee, and the compiler is free to assume it does not happen. The GC and string-interning may also misbehave. If you truly need zero-copy at an FFI boundary, isolate it, document it, and cover it with race and fuzz tests — but profile first to confirm the copy is actually the bottleneck.

**Rationale**: `string` is a `(pointer, length)` to immutable bytes; `[]byte` is a `(pointer, length, capacity)` to mutable bytes. The compiler cannot share memory between them without breaking immutability, so any conversion copies. The fix is not to cheat the type system; it is to pick one type per layer.

---

## PF-09: Specify Slice Capacity When the Final Size Is Known

**Strength**: SHOULD

**Summary**: `make([]T, 0, n)` allocates the backing array in one go; subsequent `append`s to length ≤ `n` do not reallocate. When you know the eventual size, specify it.

```go
// Good
func activeUserIDs(users []User) []int {
    ids := make([]int, 0, len(users))
    for _, u := range users {
        if u.Active {
            ids = append(ids, u.ID)
        }
    }
    return ids
}

// Bad — grows in powers of two, copying on each growth
func activeUserIDs(users []User) []int {
    var ids []int
    for _, u := range users {
        if u.Active {
            ids = append(ids, u.ID)
        }
    }
    return ids
}
```

**Uber benchmark** (Uber §Specifying Slice Capacity):
```
BenchmarkBad-4    100000000    2.48s
BenchmarkGood-4   100000000    0.21s
```

**Rationale**: Unlike map hints, slice capacity is a guarantee: the compiler allocates exactly that much backing storage. When the size is unknown, don't lie — just omit the hint and accept the growth cost. When the size is known (converting between collections, fixed-size iterations), supply it. Uber §Specifying Slice Capacity: "Slice capacity is not a hint: the compiler will allocate enough memory for the capacity of the slice as provided to `make()`." Google §Size hints: "It is acceptable to preallocate when the final size is known" (Uber Style Guide §Specifying Slice Capacity; Google Decisions §Size hints).

**Warning**: Over-preallocating wastes memory. Google §Size hints: "Preallocating more memory than you need can waste memory in the fleet or even harm performance."

**See also**: PF-10, PF-01

---

## PF-10: Provide Map Capacity Hints When the Eventual Size Is Known

**Strength**: SHOULD

**Summary**: `make(map[K]V, n)` asks the runtime to pre-size the map's bucket array. It does not guarantee zero reallocation, but it reduces growth steps substantially when you know the approximate final size.

```go
// Good
files, _ := os.ReadDir("./files")

m := make(map[string]os.DirEntry, len(files))
for _, f := range files {
    m[f.Name()] = f
}

// Bad
m := make(map[string]os.DirEntry)
for _, f := range files {
    m[f.Name()] = f
}
```

**Rationale**: Maps use open-addressing buckets internally; growing the map means allocating a new bucket array and rehashing every entry. Sizing up front avoids most of that. Uber §Specifying Map Capacity Hints: "Providing a capacity hint to `make()` tries to right-size the map at initialization time, which reduces the need for growing the map and allocations as elements are added." Unlike slices, the hint is approximate — allocations may still happen (Uber Style Guide §Specifying Map Capacity Hints; Google Decisions §Size hints).

**See also**: PF-09

---

## PF-11: Copying Slices and Maps at Boundaries Has a Memory Cost

**Strength**: SHOULD

**Summary**: Copying at input or output boundaries of a struct (to prevent aliasing — see chapter 06 for the lifetime angle) adds an allocation and a copy. Make the trade explicit: copy for safety; skip it only when you can document that the caller must not retain the slice.

```go
// Good — defensive copy, explicit about the memory cost
func (d *Driver) SetTrips(trips []Trip) {
    d.trips = make([]Trip, len(trips))
    copy(d.trips, trips)
}

// Good — explicit ownership transfer; no copy needed
// SetTripsBorrowed stores trips; the caller MUST NOT modify the slice
// after this call.
func (d *Driver) SetTripsBorrowed(trips []Trip) {
    d.trips = trips
}

// Bad — hidden aliasing, expensive to debug
func (d *Driver) SetTrips(trips []Trip) {
    d.trips = trips // caller's trips[0] = ... now mutates d
}
```

**Rationale**: Slices and maps are headers that point to shared storage. When the cost of a copy matters — thousands of records per request, or a map with millions of entries — measure it and consider an ownership-transfer API. In most code the defensive copy is the right default. Uber §Copy Slices and Maps at Boundaries discusses both directions (receiving and returning); that section covers the correctness angle. This entry is about the fact that those copies are not free (Uber Style Guide §Copy Slices and Maps at Boundaries).

**Note**: Correctness (preventing aliasing bugs) is covered in chapter 06. This entry is the performance framing.

**See also**: PF-09

---

## PF-12: Reset and Reuse Buffers Instead of Allocating per Call

**Strength**: SHOULD

**Summary**: A `bytes.Buffer` or `strings.Builder` can be `.Reset()` and reused. In a hot loop, reuse avoids one allocation per iteration.

```go
// Good — one buffer, reset per iteration
var buf bytes.Buffer
for _, r := range records {
    buf.Reset()
    if err := encode(&buf, r); err != nil {
        return err
    }
    if _, err := out.Write(buf.Bytes()); err != nil {
        return err
    }
}

// Bad — new buffer per iteration
for _, r := range records {
    var buf bytes.Buffer
    if err := encode(&buf, r); err != nil {
        return err
    }
    out.Write(buf.Bytes())
}
```

**Rationale**: After `.Reset()`, the buffer retains its backing array; subsequent writes refill it without reallocating (until they exceed the previous peak capacity). This is a purely mechanical improvement with no cost to readability. Note that `bytes.Buffer` has an inline small-byte array as an optimization for tiny contents, which is also why copying a `Buffer` value is unsafe — see PF-14 and Google Decisions §Copying (Google Decisions §Copying).

**See also**: PF-13, PF-14

---

## PF-13: Use `sync.Pool` for Expensive-to-Create, Reusable Objects

**Strength**: CONSIDER

**Summary**: `sync.Pool` caches objects for reuse across goroutines. It is the right tool when (a) the object is expensive to allocate, (b) allocations are frequent, and (c) the object has no persistent state between uses.

```go
// Good — typical HTTP handler pattern
var bufPool = sync.Pool{
    New: func() any { return new(bytes.Buffer) },
}

func handle(w http.ResponseWriter, r *http.Request) {
    buf := bufPool.Get().(*bytes.Buffer)
    defer bufPool.Put(buf)
    buf.Reset() // IMPORTANT: pool entries are not zeroed for you

    if err := render(buf, r); err != nil {
        http.Error(w, err.Error(), 500)
        return
    }
    w.Write(buf.Bytes())
}

// Bad — using sync.Pool for cheap objects, or objects with state
var intPool = sync.Pool{New: func() any { return new(int) }}
// An int is so cheap that the pool overhead exceeds the saving.

var connPool = sync.Pool{New: func() any { return newConn() }}
// A connection has state (open, closed, idle) and must not be handed out randomly.
// Use a proper pool implementation.
```

**Warnings**:
- Always `Reset()` before using a pooled item, or initialize it fully. `sync.Pool.Get` may return a previously used item or a freshly created one; you cannot tell.
- The pool is allowed to drop items at any time (typically between GC cycles). It is a cache, not a guarantee.
- Do not use it for objects whose lifetime or identity matters (connections, file handles, things with `Close`).

**Rationale**: `sync.Pool` is explicitly about reducing GC pressure in hot paths. It is not mentioned in the Uber or Google style guides as a first-reach tool; treat it the way they treat all performance work — apply it only after a benchmark points at allocation as the bottleneck (Uber Style Guide §Performance general discipline; Google Decisions §Size hints discipline).

**See also**: PF-12, PF-01

---

## PF-14: Don't Copy Types Whose Methods Use a Pointer Receiver

**Strength**: SHOULD

**Summary**: Types like `bytes.Buffer`, `strings.Builder`, `sync.Mutex`, and `sync.WaitGroup` must not be copied once in use. Copying them produces silent aliasing bugs or lost state.

```go
// Bad — copies both the mutex and the buffer's inline array
type Record struct {
    buf bytes.Buffer
    // ...
}

func (r Record) Process() { /* copies r, including r.buf */ }

// Good — pointer receiver; one Record instance in play
func (r *Record) Process() { /* ... */ }

// Bad
b1 := bytes.Buffer{}
b2 := b1 // b2's small-array pointer may alias b1

// Good — use pointers or take care to initialize separately
b2 := &bytes.Buffer{}
```

**Rationale**: `bytes.Buffer` uses a small inline byte array as an optimization. When copied, the copy's `[]byte` slice header may point into the *original's* inline array. Mutations through one propagate weirdly to the other until the buffer grows past the inline size. `sync.Mutex` copies lose their locking state. Google Decisions §Copying: "In general, do not copy a value of type `T` if its methods are associated with the pointer type, `*T`." `go vet` flags this for `sync.Mutex` and several standard types; running `go vet` is part of the contract (Google Decisions §Copying).

**See also**: PF-12, PF-15

---

## PF-15: Pass Small Values by Value; Pass Large Structs by Pointer

**Strength**: SHOULD

**Summary**: Passing a small value (an int, a `time.Time`, a short struct) by value is as cheap as passing a pointer — and avoids heap allocation. Passing a large struct (or any protobuf message) by value copies every field; prefer a pointer.

```go
// Good — small value, no pointer needed
func isActive(now, start, stop time.Time) bool { /* ... */ }

// Good — large struct or proto: pass by pointer
func Process(req *pb.LargeRequest) error { /* ... */ }

// Bad — pointer to a primitive: extra indirection for no benefit
func isActive(now, start, stop *time.Time) bool { /* ... */ }

// Bad — passing a big struct by value; every call copies every field
func Process(req pb.LargeRequest) error { /* ... */ }
```

**Rationale**: Google Decisions §Pass values: "Do not pass pointers as function arguments just to save a few bytes. If a function reads its argument `x` only as `*x` throughout, then the argument shouldn't be a pointer." But the same section notes: "This advice does not apply to large structs, or even small structs that may increase in size. In particular, protocol buffer messages should generally be handled by pointer rather than by value." The crossover point is roughly when the struct exceeds a few machine words — measure when it matters (Google Decisions §Pass values; Google Decisions §Receiver type).

**Note**: Interfaces and maps and channels are already reference-like — pass them by value.

**See also**: PF-16

---

## PF-16: Choose Receiver Type Deliberately — Pointer for Large Types, Value for Small Immutable Ones

**Strength**: SHOULD

**Summary**: Method receivers follow the same cost logic as function parameters, plus some correctness rules. Use pointer receivers for large structs, types with `sync.Mutex`, and types whose methods mutate state. Use value receivers for small immutable types (`time.Time`, typed ints, short POD structs).

```go
// Good — pointer: mutates state, or contains a mutex
type Counter struct {
    mu    sync.Mutex
    total int
}

func (c *Counter) Inc() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.total++
}

// Good — value: small, immutable, plain-old-data
type Duration int64

func (d Duration) Millis() int64 { return int64(d) / 1e6 }

// Good — slice receiver can be value if methods don't reslice
type Buffer []byte
func (b Buffer) Len() int { return len(b) }

// Bad — inconsistent: some methods take *T, some take T
func (c Counter) Read() int   { return c.total } // value
func (c *Counter) Inc()       { c.total++ }       // pointer
// Choose one style per type.
```

**Rationale**: Google Decisions §Receiver type: "**Correctness wins over speed or simplicity.**" Pointer receivers are required for types with uncopyable fields (mutexes, `bytes.Buffer`), for mutation, and for large types where copying becomes expensive. Value receivers are fine for small POD. Keep methods consistent across a single type. Google's note on performance is worth repeating: "There is a lot of misinformation about whether passing a value or a pointer to a function can affect performance... When the performance does matter, it is important to profile both approaches with a realistic benchmark" (Google Decisions §Receiver type).

**See also**: PF-14, PF-15, PF-01

---

## PF-17: Iterate Large Structs by Index, Not by `for range`'s Value Copy

**Strength**: CONSIDER

**Summary**: `for _, v := range bigStructs` copies each element into `v`. For slices of large structs, iterating by index avoids the per-iteration copy.

```go
// Good — index iteration: no per-element copy
for i := range records {
    r := &records[i]
    if !r.Active {
        continue
    }
    process(r)
}

// Fine for small elements — the copy is a few words
for _, id := range ids { // ids is []int
    process(id)
}

// Potentially costly — each iteration copies a LargeRecord (e.g., 500 bytes)
for _, r := range records {
    if !r.Active {
        continue
    }
    process(&r) // also: &r points into the loop variable, not records[i]
}
```

**Rationale**: The `for _, v := range s` form copies `s[i]` into `v` on each iteration. For element sizes beyond a few machine words, the copies accumulate. Profile first — Go 1.22 changed the loop-variable semantics and the compiler may eliminate the copy in simple cases. When profiling confirms the cost, switch to the index form. This is an applied consequence of Google's Pass values / Receiver type guidance (Google Decisions §Pass values; Google Decisions §Receiver type).

**Pitfall**: `&r` in the value-copy form takes the address of the loop variable, not the element. For pointer-to-element semantics, always use `&s[i]`.

**See also**: PF-15, PF-16

---

## PF-18: Compile Regular Expressions Once; Reuse at Call Sites

**Strength**: SHOULD

**Summary**: `regexp.Compile` parses the pattern into a DFA/NFA. For a regex used more than once, compile it at package scope with `regexp.MustCompile` and reuse the compiled value.

```go
// Good — compiled once at package load
var emailRE = regexp.MustCompile(`^[^@]+@[^@]+\.[^@]+$`)

func isEmail(s string) bool {
    return emailRE.MatchString(s)
}

// Bad — recompiled on every call
func isEmail(s string) bool {
    re := regexp.MustCompile(`^[^@]+@[^@]+\.[^@]+$`)
    return re.MatchString(s)
}
```

**Rationale**: Pattern compilation is dramatically more expensive than matching — often by two orders of magnitude. Compiling once amortizes that cost across every call. The `MustCompile` variant panics on a bad pattern, which is acceptable at package init because a literal pattern either compiles or is a bug (see chapter 01 CI-33). Google Decisions §Must functions: `regexp.MustCompile` is the canonical example of safe `Must` use. Uber §Don't Panic lists `template.Must` / `regexp.MustCompile` as the accepted program-initialization exception (Uber Style Guide §Don't Panic; Google Decisions §Must functions).

**Note**: If the pattern is supplied at runtime (user input, config), use `regexp.Compile` and handle the error — never `MustCompile` user input.

**See also**: PF-04

---

## PF-19: Buffered I/O with `bufio` — Don't Hit the Kernel on Every Byte

**Strength**: SHOULD

**Summary**: Unbuffered reads/writes to files, pipes, or network sockets cross the user/kernel boundary on every call. Wrap them with `bufio.Reader` / `bufio.Writer` to amortize syscall cost.

```go
// Good — one syscall per ~4KB, not per line
f, err := os.Open(path)
if err != nil {
    return err
}
defer f.Close()

s := bufio.NewScanner(f)
for s.Scan() {
    processLine(s.Text())
}
if err := s.Err(); err != nil {
    return err
}

// Good — buffered output; remember to Flush
out, err := os.Create(path)
if err != nil {
    return err
}
defer out.Close()

bw := bufio.NewWriter(out)
defer bw.Flush() // or check Flush error explicitly
for _, r := range records {
    fmt.Fprintln(bw, r)
}

// Bad — per-byte read is N syscalls for N bytes
var b [1]byte
for {
    n, err := f.Read(b[:])
    // ...
}
```

**Rationale**: Each `Read` or `Write` on an unbuffered `*os.File` is typically a `read`/`write` syscall. `bufio` performs reads/writes in chunks (4KB default), so the syscall count drops by orders of magnitude on line- or record-oriented workloads. Google Decisions §Size hints example uses `make([]byte, 131072)` as a "preferred buffer size" — same family of concerns (Google Decisions §Size hints).

**Pitfall**: `bufio.Writer` buffers internally; you must `Flush` before it closes, or bytes are lost. A deferred `Flush` with a checked error is the standard pattern.

---

## PF-20: Use `strings.Builder.Grow` / `bytes.Buffer.Grow` When You Know the Output Size

**Strength**: CONSIDER

**Summary**: `Grow(n)` asks the builder to pre-allocate room for `n` more bytes. In a loop with a known lower bound on the output size, this replaces several allocations with one.

```go
// Good
var b strings.Builder
b.Grow(len(parts) * avgLen) // one allocation
for _, p := range parts {
    b.WriteString(p)
}

// Acceptable — builder grows exponentially, so this is only a few allocations
var b strings.Builder
for _, p := range parts {
    b.WriteString(p)
}
```

**Rationale**: The builder doubles its backing array when full; a known `Grow` avoids the doublings. The savings are usually small (log₂ N allocations avoided) and only matter in hot paths. Apply per the general hot-path discipline.

**See also**: PF-04, PF-09

---

## PF-21: Avoid Reflection in Hot Paths

**Strength**: SHOULD

**Summary**: The `reflect` package inspects types at runtime. It is flexible and slow. Replace it with typed code, code generation, or a type switch when it appears in a hot path.

```go
// Good — type switch: fast, type-safe
func Marshal(v any) ([]byte, error) {
    switch x := v.(type) {
    case int:
        return strconv.AppendInt(nil, int64(x), 10), nil
    case string:
        return []byte(x), nil
    // ...
    default:
        return nil, fmt.Errorf("unsupported type %T", v)
    }
}

// Bad — reflection on every call
func Marshal(v any) ([]byte, error) {
    rv := reflect.ValueOf(v)
    switch rv.Kind() {
    case reflect.Int:
        return strconv.AppendInt(nil, rv.Int(), 10), nil
    // ...
    }
}
```

**Rationale**: Google Decisions §Equality comparisons: "`reflect.DeepEqual` should not be used for checking equality [in tests], as it is sensitive to changes in unexported fields and other implementation details." More broadly, `reflect` is a performance trap — it disables inlining, allocates `reflect.Value` wrappers, and cannot be statically optimized. Standard library routines like `encoding/json` tolerate this because they serve many types; your production code usually does not need that flexibility (Google Decisions §Equality comparisons).

**See also**: PF-01

---

## PF-22: Avoid Unnecessary Allocations in Hot Loops

**Strength**: SHOULD

**Summary**: Every literal, closure, deferred call, and interface conversion inside a hot loop can allocate. Hoist invariants; keep the loop body allocation-free.

```go
// Good — everything allocation-free inside the loop
errRE := regexp.MustCompile(`^ERROR`) // compiled once at package scope
prefix := []byte("log: ")
for _, line := range lines {
    if errRE.MatchString(line) {
        errs++
    }
    out.Write(prefix)
    out.WriteString(line)
}

// Bad — three hidden allocations per iteration
for _, line := range lines {
    if regexp.MustCompile(`^ERROR`).MatchString(line) { // recompiled + allocated
        errs++
    }
    out.Write([]byte("log: ")) // new byte slice each iteration
    out.WriteString(line)
}
```

**Rationale**: Per-iteration allocations compound into GC pressure. `go test -bench -benchmem` reports `allocs/op`; a target of zero allocations in a hot inner loop is reasonable when the work is straightforward. Uber's benchmark comparisons throughout its §Performance chapter emphasize `allocs/op` alongside `ns/op` (Uber Style Guide §Performance).

**See also**: PF-07, PF-18, PF-12

---

## PF-23: Prefer Non-Capturing Closures or Hoist the Capture

**Strength**: CONSIDER

**Summary**: A closure that captures variables allocates a heap-allocated environment record. Inside a hot loop, this can be expensive. Prefer plain functions or move the closure out of the loop.

```go
// Good — closure defined once
normalize := func(s string) string { return strings.ToLower(strings.TrimSpace(s)) }
for _, s := range inputs {
    out = append(out, normalize(s))
}

// Bad — new closure (and environment) per iteration
for _, s := range inputs {
    normalize := func(s string) string { return strings.ToLower(strings.TrimSpace(s)) }
    out = append(out, normalize(s))
}
```

**Rationale**: The closure literal is semantically re-created on each iteration. The Go compiler is often smart enough to stack-allocate the environment or reuse it, but the conservative rule is: hoist closures to where they're created once. Apply only when profiling shows the allocation matters.

**See also**: PF-22

---

## PF-24: Goroutines Are Cheap but Not Free — Don't Fire-and-Forget at Scale

**Strength**: SHOULD

**Summary**: A goroutine costs roughly 2-4 KB of stack and a scheduler entry — far less than an OS thread (≈1 MB default) but not zero. Spawning an unbounded number of goroutines, or leaking them, causes real resource problems.

```go
// Good — bounded parallelism with a semaphore
sem := make(chan struct{}, 32) // at most 32 in flight
var wg sync.WaitGroup
for _, job := range jobs {
    sem <- struct{}{}
    wg.Add(1)
    go func(j Job) {
        defer wg.Done()
        defer func() { <-sem }()
        process(j)
    }(job)
}
wg.Wait()

// Good — controlled worker pool
jobs := make(chan Job)
var wg sync.WaitGroup
for i := 0; i < workerCount; i++ {
    wg.Add(1)
    go func() {
        defer wg.Done()
        for j := range jobs {
            process(j)
        }
    }()
}
for _, j := range work {
    jobs <- j
}
close(jobs)
wg.Wait()

// Bad — one goroutine per request, unbounded
for _, req := range incoming {
    go handle(req) // 100,000 requests => 100,000 goroutines
}
```

**Rationale**: Uber §Don't fire-and-forget goroutines: "Goroutines are lightweight, but they're not free: at minimum, they cost memory for their stack and CPU to be scheduled. While these costs are small for typical uses of goroutines, they can cause significant performance issues when spawned in large numbers without controlled lifetimes." Google Decisions §Goroutine lifetimes agrees: "Leaving goroutines in-flight for arbitrarily long can lead to unpredictable memory usage" (Uber Style Guide §Don't fire-and-forget goroutines; Google Decisions §Goroutine lifetimes).

**Note**: The lifetime-management side of goroutines (stop channels, `sync.WaitGroup`, `context` cancellation) is covered in chapter 06. This entry is the cost framing.

---

## PF-25: `defer` Is Nearly Free — Don't Unroll Cleanup for Performance

**Strength**: SHOULD

**Summary**: `defer`'s overhead is in the nanoseconds. Unless you are in a function whose total runtime is in the same range, `defer` is the right choice for cleanup.

```go
// Good
func process(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()
    // ... do work that returns errors ...
    return nil
}

// Bad — manual cleanup on every return path; easy to miss one
func process(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    data, err := io.ReadAll(f)
    if err != nil {
        f.Close() // remembered
        return err
    }
    if err := validate(data); err != nil {
        f.Close() // remembered
        return err
    }
    f.Close() // remembered
    return nil
}
```

**Rationale**: Uber §Defer to Clean Up: "Defer has an extremely small overhead and should be avoided only if you can prove that your function execution time is in the order of nanoseconds. The readability win of using defers is worth the miniscule cost of using them." The cost framing here is a performance entry; the correctness framing (pair acquire+release) is in chapter 01 CI-34 (Uber Style Guide §Defer to Clean Up).

---

## PF-26: Struct Field Alignment Matters Only for Cache-Critical Types

**Strength**: CONSIDER

**Summary**: Go inserts padding between fields so each is aligned to its natural boundary. Ordering fields from largest to smallest minimizes padding. This matters for types allocated in large quantities; it is noise everywhere else.

```go
// Inefficient — 24 bytes on 64-bit: 1 + 7 pad + 8 + 1 + 7 pad
type Bad struct {
    a bool    // 1 byte + 7 padding
    b int64   // 8 bytes
    c bool    // 1 byte + 7 padding (tail)
}

// Efficient — 16 bytes: 8 + 1 + 1 + 6 pad (tail)
type Good struct {
    b int64
    a bool
    c bool
}

// Check actual size
fmt.Println(unsafe.Sizeof(Good{})) // 16
```

**When it matters**:
- Types allocated by the millions (particles, graph nodes, cache entries).
- Types passed across cache lines or embedded in large arrays.
- `atomic.Int64` and other 64-bit atomic values on 32-bit platforms — must be 8-byte aligned; put them first.

**Rationale**: A struct whose fields span an extra cache line costs an extra cache miss per access. For typical application code — request structs, config, DTOs — the savings are micro-optimizations that don't survive a readability cost. Apply when profiling or memory analysis identifies the type as hot (profile-driven, per PF-01). The Go style guides do not dedicate a section to alignment; treat this entry as applied common sense that must clear the profiling bar.

**See also**: PF-01

---

## PF-27: `//go:inline` and `//go:noinline` — Use Only with Profiling Evidence

**Strength**: CONSIDER

**Summary**: The Go compiler decides inlining automatically. Directives like `//go:noinline` exist to suppress that for specific, measured reasons (keeping a function visible in profiles, ensuring it appears in stack traces). Reaching for `//go:inline` is rare and should be justified by `-gcflags="-m"` output.

```go
// Good — measured reason: keep this function in the profile
//go:noinline
func hotBenchmarkedFunc(x int) int {
    return x*x + x
}

// Check what's being inlined:
// go build -gcflags="-m" ./...

// Bad — sprinkling directives without measurement
//go:inline  // does this even work? did you benchmark?
func trivial(x int) int { return x + 1 }
```

**Rationale**: The compiler's inliner uses a cost budget based on function body complexity. Manual overrides are blunt. The standard technique is: build with `-gcflags="-m"` to see what the compiler already decided, profile to see what actually matters, and only then consider directives — usually `//go:noinline` to keep a function separately attributable in profiles. Google Decisions §Size hints' broader discipline applies: measure, then adjust.

**See also**: PF-01, PF-31

---

## PF-28: Guard Expensive Log Arguments on Disabled Verbosity Levels

**Strength**: SHOULD

**Summary**: An expression passed as a log argument is evaluated even when the log level would discard the result. In hot code paths, wrap expensive argument computation in a conditional.

```go
// Good — cheap argument: direct formatting is fine
log.V(1).Infof("handling %v", sql) // sql is a small value

// Good — expensive argument: guard the call
if log.V(2) {
    log.Infof("handling %v", sql.Explain()) // Explain() does real work
}

// Bad — Explain() runs even when V(2) is disabled
log.V(2).Infof("handling %v", sql.Explain())
```

**Rationale**: Go evaluates function arguments eagerly. `log.V(2).Infof(...)` still calls `Explain()` regardless of whether V(2) is enabled. Google Best Practices §Custom verbosity levels: "To minimize the cost of verbose logging, you should ensure not to accidentally call expensive functions even when `log.V` is turned off... When in doubt, use the slightly more verbose style" with the `if log.V(2) { ... }` guard. Same source: "`log.Error` ... causes a flush and is more expensive than lower logging levels" (Google Best Practices §Custom verbosity levels; Google Best Practices §Logging errors).

---

## PF-29: Preallocate I/O Buffers Sized to the Target

**Strength**: CONSIDER

**Summary**: When reading from a file or socket, a buffer sized to the expected block size avoids short reads and over-copying. For filesystems, `st_blksize` (typically 4 KB or larger) is a good default.

```go
// Good — buffer matches filesystem block size
buf := make([]byte, 131072) // 128 KB
for {
    n, err := f.Read(buf)
    // ...
}

// Also good — bufio default (4 KB) works for most cases
br := bufio.NewReader(f)
```

**Rationale**: Google Decisions §Size hints presents exactly this example: `buf = make([]byte, 131072)` with the comment "Preferred buffer size for target filesystem: `st_blksize`." The point is the same as PF-19: match the buffer to the work (Google Decisions §Size hints).

**See also**: PF-19

---

## PF-30: `interface{}` / `any` Has a Type-Tag Cost — Keep It Out of Hot Inner Loops

**Strength**: CONSIDER

**Summary**: Values stored in `any` carry a type descriptor and are heap-allocated if larger than a pointer. Boxing primitive values into `any` in a hot loop adds allocations and indirection.

```go
// Good — typed slice, no boxing
func sum(xs []int) int {
    var s int
    for _, x := range xs {
        s += x
    }
    return s
}

// Bad — everything boxed into any
func sum(xs []any) int {
    var s int
    for _, x := range xs {
        s += x.(int) // runtime type assertion per element
    }
    return s
}
```

**Rationale**: `any` is an interface; an interface value is a (type, data) pair. If the underlying value doesn't fit in a word, Go boxes it on the heap. Plus, every method call or type assertion through `any` is an indirect dispatch. Keep typed slices and typed parameters in hot code; reserve `any` for genuinely polymorphic APIs (logging, JSON). This is applied from chapter 01 CI-25 (prefer `any` over `interface{}` in spelling) — the performance framing is: yes, they are identical, and they are both slow compared to concrete types.

**See also**: PF-21

---

## PF-31: Read Compiler Diagnostics with `-gcflags="-m"` for Escape and Inline Info

**Strength**: CONSIDER

**Summary**: The Go compiler can tell you exactly which variables escape to the heap and which function calls were inlined. Use this to confirm that your hot-path changes had the intended effect.

```
# Show escape analysis and inlining decisions
go build -gcflags="-m" ./...

# More verbose
go build -gcflags="-m -m" ./...

# Benchmark memory: compare allocs/op before and after
go test -bench=. -benchmem -count=10 ./pkg > before.txt
# ... change ...
go test -bench=. -benchmem -count=10 ./pkg > after.txt
benchstat before.txt after.txt
```

```go
// Example: a hot-path change aiming to stack-allocate the builder
func format(n int) string {
    var b strings.Builder // does this escape?
    fmt.Fprintf(&b, "n=%d", n)
    return b.String()
}
// gcflags -m output tells you: "b does not escape" or "b escapes to heap"
```

**Rationale**: Escape analysis determines whether a variable lives on the stack (cheap) or the heap (GC-tracked). Inlining eliminates call overhead. Both are opaque from source code; `-gcflags="-m"` makes them visible. `benchstat` turns noisy benchmark numbers into a readable diff with a p-value. These are the standard Go performance tooling surface; use them before and after every performance change (applied discipline from PF-01).

**See also**: PF-01, PF-27

---

## PF-32: Avoid Converting Between Slice Types in Inner Loops

**Strength**: SHOULD

**Summary**: Converting `[]byte` to `string` (or back) inside a loop copies the bytes every time. Convert once — or design the API to take the type you already have.

```go
// Good — accept and return []byte; no conversion
func process(data []byte) []byte { /* ... */ }

// Good — convert once if you must
s := string(data)
for _, line := range strings.Split(s, "\n") { /* ... */ }

// Bad — string(data) in the loop
for i := 0; i < len(items); i++ {
    handle(string(items[i])) // copies each iteration
}

// Specialized map-key optimization (allowed by the compiler):
var m map[string]int
val := m[string(bytes)] // compiler optimizes: no allocation for this specific case
// but don't rely on this outside of map lookup / comparison
```

**Rationale**: The `[]byte`/`string` conversion is a copy (see PF-08). The Go compiler has a small set of optimizations — `m[string(b)]` as a map key, `string(b) == "literal"` as a comparison — that avoid allocation for those exact expressions. Outside those patterns, assume conversion allocates. Uber §Avoid repeated string-to-byte conversions applies the same principle in the reverse direction (Uber Style Guide §Avoid repeated string-to-byte conversions).

**See also**: PF-07, PF-08

---

## PF-33: Zero-Value Types That Are Usable Save One Allocation

**Strength**: SHOULD

**Summary**: `sync.Mutex`, `bytes.Buffer`, `strings.Builder`, nil slices, and nil maps (for reading) all work at their zero value. Starting from zero avoids an explicit `new` / `make` / struct literal in simple cases.

```go
// Good — zero-value buffer is ready
var buf bytes.Buffer
buf.WriteString("hello")

// Good — zero-value mutex
type Stats struct {
    mu    sync.Mutex
    count int
}

// Good — nil slice; append works
var xs []int
xs = append(xs, 1)

// Bad — redundant pointer and allocation
mu := new(sync.Mutex) // makes *sync.Mutex; nil-dereference risks
```

**Rationale**: Uber §Zero-value Mutexes are Valid: "The zero-value of `sync.Mutex` and `sync.RWMutex` is valid, so you almost never need a pointer to a mutex." This is primarily a correctness and style rule (chapter 01 CI-11). Its performance side is that every `new(T)` call is a heap allocation the runtime can skip if you just declare `var x T`. The savings are small but free (Uber Style Guide §Zero-value Mutexes are Valid).

**See also**: PF-12

---

## PF-34: Use `benchstat` to Compare Benchmark Runs Statistically

**Strength**: SHOULD

**Summary**: A single benchmark run is noisy. Run each benchmark at least `-count=10` and compare with `benchstat`, which reports the mean delta plus a significance flag.

```bash
# Before change
go test -bench=Parse -benchmem -count=10 ./pkg > old.txt

# After change
go test -bench=Parse -benchmem -count=10 ./pkg > new.txt

# Compare
benchstat old.txt new.txt
```

Expected output format:
```
name       old time/op    new time/op    delta
Parse-8    1.23µs ± 2%    0.87µs ± 3%   -29.27%  (p=0.000 n=10+10)

name       old alloc/op   new alloc/op   delta
Parse-8      128B ± 0%       64B ± 0%   -50.00%  (p=0.000 n=10+10)

name       old allocs/op  new allocs/op  delta
Parse-8      2.00 ± 0%     1.00 ± 0%    -50.00%  (p=0.000 n=10+10)
```

**Rationale**: `benchstat` runs a Welch's t-test on the samples and reports whether the observed difference is statistically significant at p < 0.05. Without it, you cannot distinguish a real 2% speedup from noise. This is the standard Go tooling answer to PF-01's "measure before and after." Google §Size hints references `GoTip #3: Benchmarking Go Code` for the same discipline (Google Decisions §Size hints).

**See also**: PF-01, PF-31

---

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Profile before optimizing | MUST | No change without a benchmark delta |
| 02 | Apply perf rules to hot paths only | SHOULD | Readability elsewhere |
| 03 | `strconv` over `fmt.Sprintf` for primitives | SHOULD | ~2× faster, fewer allocs |
| 04 | Right tool for string concatenation | SHOULD | `+` few, `Sprintf` format, `Builder` loop |
| 05 | `fmt.Fprintf` when writing to `io.Writer` | SHOULD | Skip the temporary string |
| 06 | `strings.Builder` over `bytes.Buffer` for strings | SHOULD | `.String()` on `Buffer` copies |
| 07 | Hoist `[]byte("literal")` out of loops | SHOULD | Each call copies the bytes |
| 08 | `[]byte` ↔ `string` conversion copies | CONSIDER | Design APIs to stay in one type |
| 09 | `make([]T, 0, n)` when size is known | SHOULD | Guaranteed capacity, no growth |
| 10 | `make(map[K]V, n)` with size hint | SHOULD | Reduces rehashes (approximate) |
| 11 | Boundary copies cost memory | SHOULD | Document the trade; correctness defaults to copy |
| 12 | Reset and reuse buffers in loops | SHOULD | `Buffer.Reset()`, `Builder.Reset()` |
| 13 | `sync.Pool` for expensive reusable objects | CONSIDER | `Reset()` on Get; not for stateful things |
| 14 | Don't copy types with pointer-receiver methods | SHOULD | `Buffer`, `Mutex` alias dangerously |
| 15 | Small by value; large by pointer | SHOULD | `time.Time` by value; big structs by pointer |
| 16 | Pick receiver type deliberately | SHOULD | Pointer: mutation, mutex, large; value: small POD |
| 17 | Index iteration for large-struct slices | CONSIDER | `for i := range s { r := &s[i] }` |
| 18 | `regexp.MustCompile` at package scope | SHOULD | Compile once; reuse at calls |
| 19 | `bufio` for file and network I/O | SHOULD | Syscall per chunk, not per byte |
| 20 | `Builder.Grow(n)` / `Buffer.Grow(n)` | CONSIDER | One allocation vs log₂ N |
| 21 | Avoid reflection in hot paths | SHOULD | Type switch or codegen instead |
| 22 | No per-iteration allocations in hot loops | SHOULD | Hoist regex, slices, closures |
| 23 | Hoist closures out of loops | CONSIDER | Closure creates an env record |
| 24 | Bound goroutines; don't fire-and-forget | SHOULD | 2-4 KB each, schedulable cost |
| 25 | `defer` is nearly free | SHOULD | Don't unroll cleanup for perf |
| 26 | Struct field alignment for hot types | CONSIDER | Largest to smallest; measure first |
| 27 | Compiler directives with evidence | CONSIDER | `-gcflags="-m"` first; `//go:noinline` for profiling |
| 28 | Guard expensive log args on V-levels | SHOULD | `if log.V(2) { ... Explain() ... }` |
| 29 | Size I/O buffers to the target | CONSIDER | `st_blksize`, 128 KB for fs |
| 30 | Keep `any` out of hot inner loops | CONSIDER | Boxing + type-assertion cost |
| 31 | `-gcflags="-m"` for escape / inline info | CONSIDER | Confirms the change did what you wanted |
| 32 | Avoid slice-type conversions in inner loops | SHOULD | `[]byte` ↔ `string` copies each time |
| 33 | Use zero-value types when usable | SHOULD | Skip a `new` allocation |
| 34 | `benchstat` with `-count=10` | SHOULD | Single runs are noise; need significance |

---

## Related Guidelines

- **Core Idioms** (`01-core-idioms.md`): CI-11 zero-value types — PF-33 is its performance framing; CI-12 nil slices — PF-11 reuses the boundary-copy context; CI-13 `make` for maps — PF-10's hint variant; CI-25 `any` — PF-30 is the performance framing; CI-33 `Must` functions at init — PF-18 applies it to regex; CI-34 `defer` — PF-25 is the performance framing
- **API Design** (`02-api-design.md`): input/output shapes, accept-interfaces/return-concrete — impacts PF-08, PF-11, PF-15
- **Type Design** (`04-type-design.md`): struct composition — underlying patterns for PF-14, PF-26
- **Interfaces & Methods** (`05-interfaces-methods.md`): receiver type choice in depth — extends PF-15, PF-16
- **Concurrency** (`06-concurrency.md`): goroutine lifetimes, `sync` primitives, `context` propagation — PF-24 is the cost framing; the lifetime rules (stop channels, `WaitGroup`) live in 06. `sync.Pool` (PF-13) is here because it is a performance tool, not a concurrency primitive.
- **Testing** (`07-testing.md`): benchmark conventions, table tests — PF-01, PF-34 extend the "use benchmarks" discipline into optimization work
- **Anti-Patterns** (`09-anti-patterns.md`): premature optimization, micro-optimizations lacking evidence — amplifies PF-01, PF-02

---

## External References

- [*Uber Go Style Guide* — Performance](https://github.com/uber-go/guide/blob/master/style.md#performance) — the empirical backbone of this chapter
- [*Google Go Style Guide — Decisions*](https://google.github.io/styleguide/go/decisions) — Size hints, String concatenation, Receiver type, Pass values, Copying
- [*Google Go Style Guide — Best Practices*](https://google.github.io/styleguide/go/best-practices) — Logging errors, Custom verbosity levels, String concatenation
- [*Effective Go* — Allocation with `new` and `make`](https://go.dev/doc/effective_go#allocation_new)
- [Go Blog — Profiling Go Programs](https://go.dev/blog/pprof)
- [`pkg.go.dev/testing` — `B` benchmarks](https://pkg.go.dev/testing#B)
- [`golang.org/x/perf/cmd/benchstat`](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat)
- [`pkg.go.dev/runtime/pprof`](https://pkg.go.dev/runtime/pprof)
- [`pkg.go.dev/bufio`](https://pkg.go.dev/bufio), [`pkg.go.dev/strings#Builder`](https://pkg.go.dev/strings#Builder), [`pkg.go.dev/sync#Pool`](https://pkg.go.dev/sync#Pool)
