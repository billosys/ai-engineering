---
concept: I/O Performance
slug: perf-io
category: performance
subcategory: io-optimization
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "I/O"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "io buffering"
  - "BufReader BufWriter"
  - "stdout locking"
  - "buffered io"
  - "read_until raw bytes"
prerequisites: []
extends: []
related:
  - perf-iterators-and-bounds
  - perf-general-tips
contrasts_with: []
answers_questions:
  - "Why is my Rust I/O slow and how do I speed it up?"
  - "When should I use BufReader or BufWriter?"
  - "How do I avoid locking overhead with println!?"
  - "How do I read input efficiently without UTF-8 validation?"
  - "Should I explicitly flush a BufWriter?"
---

# Quick Definition

Rust file and console I/O is unbuffered by default; wrapping readers/writers in `BufReader`/`BufWriter` dramatically reduces system calls. For repeated `println!` output, manually locking stdout and using `writeln!` avoids per-call lock acquisition. Reading raw bytes with `BufRead::read_until` skips UTF-8 validation overhead.

# Core Definition

The Rust Performance Book identifies three main I/O performance concerns. First, `print!` and `println!` lock stdout on every call, so repeated use in a loop should be replaced with a manual `stdout().lock()` followed by `writeln!` calls. Second, Rust file I/O is unbuffered by default -- many small reads or writes incur a system call each. Wrapping with `BufReader` or `BufWriter` adds an in-memory buffer that batches system calls. Both buffered and unbuffered writers implement the `Write` trait (making the code look similar), while buffered readers implement the distinct `BufRead` trait (making the code structurally different, e.g., providing `read_line` and `lines`). Third, reading input as raw bytes via `BufRead::read_until` avoids the UTF-8 validation overhead inherent in reading into `String`. The `bstr` and `linereader` crates provide further support for byte-oriented processing. (Ch. 12: I/O)

# Prerequisites

This is a foundational performance concept with no prerequisites within this source, though familiarity with Rust's `std::io` traits (`Read`, `Write`, `BufRead`) is assumed.

# Key Properties

1. `print!` and `println!` acquire a lock on stdout for every call; in loops, manually locking stdout once with `stdout().lock()` and using `writeln!` is faster
2. `stdin` and `stderr` can likewise be locked manually for repeated operations
3. Rust file I/O is unbuffered by default -- each `read` or `write` call results in a system call
4. `BufReader` and `BufWriter` maintain an in-memory buffer, minimizing the number of system calls
5. Forgetting to buffer is more common when writing because both buffered and unbuffered writers implement the `Write` trait, making the code look identical
6. Buffered readers implement `BufRead` (not just `Read`), so the code for reading from a buffered reader is structurally different -- it gains `read_line()` and `lines()` methods
7. An explicit `flush()` call on a `BufWriter` is recommended; dropping the writer auto-flushes but silently ignores any flush errors
8. Buffering and manual locking can be combined for maximum throughput when writing many lines to stdout
9. Reading into `String` incurs UTF-8 validation overhead; `BufRead::read_until` reads raw bytes to avoid this
10. The `bstr` and `linereader` crates provide specialized support for byte-oriented line reading

# Construction / Recognition

## To Add Output Buffering:
1. Replace direct file writes: wrap the file handle with `BufWriter::new(file)`
2. Write normally using `writeln!` or `write!` on the `BufWriter`
3. Call `out.flush()?` explicitly before the writer is dropped to surface any flush errors

## To Optimize Repeated stdout Output:
1. Acquire a manual lock: `let mut lock = std::io::stdout().lock()`
2. Use `writeln!(lock, ...)` instead of `println!(...)`
3. The lock is released when `lock` is dropped

## To Read Raw Bytes Efficiently:
1. Wrap the reader with `BufReader::new(reader)`
2. Use `read_until(delimiter, &mut buf)` instead of reading into `String`
3. Consider `bstr` or `linereader` crates for byte-oriented line processing

# Context & Application

Unbuffered I/O is a classic performance pitfall for Rust newcomers, especially those coming from languages where buffering is the default (e.g., Python's file objects or Java's `BufferedWriter`). In Rust, the explicit opt-in to buffering is a design choice that provides transparency but catches developers off guard. The stdout locking optimization matters in CLI tools that produce many lines of output, where per-line lock acquisition becomes measurable. The raw-byte reading optimization is relevant for log processors, data pipelines, and any tool that processes ASCII or binary data where UTF-8 validation is wasted work.

The source notes that buffering also works with stdout, so combining manual locking and buffering (e.g., `BufWriter::new(stdout().lock())`) provides both benefits.

# Examples

**Example 1** (Ch. 12, "Locking"): Replacing a loop of `println!` calls:
```rust
// Before: locks stdout on every iteration
for line in lines {
    println!("{}", line);
}

// After: lock once, write many
use std::io::Write;
let mut lock = std::io::stdout().lock();
for line in lines {
    writeln!(lock, "{}", line)?;
}
```

**Example 2** (Ch. 12, "Buffering"): Wrapping a file in `BufWriter`:
```rust
// Before: unbuffered, one syscall per write
let mut out = std::fs::File::create("test.txt")?;
for line in lines {
    writeln!(out, "{}", line)?;
}

// After: buffered, batched syscalls
use std::io::{BufWriter, Write};
let mut out = BufWriter::new(std::fs::File::create("test.txt")?);
for line in lines {
    writeln!(out, "{}", line)?;
}
out.flush()?;
```

**Example 3** (Ch. 12, "Reading Input as Raw Bytes"): Using `BufRead::read_until` to avoid UTF-8 validation overhead when processing ASCII or binary data.

# Relationships

## Builds Upon
- General Rust `std::io` traits (`Read`, `Write`, `BufRead`) -- assumed prerequisite

## Enables
- High-throughput CLI tools that produce large volumes of output
- Efficient log/data file processing pipelines

## Related
- **perf-iterators-and-bounds** -- iterator patterns for processing buffered input line-by-line
- **perf-general-tips** -- the general principle of avoiding unnecessary work applies to unbuffered I/O

## Contrasts With
- None explicitly stated in the source

# Common Errors

- **Error**: Using `println!` in a tight loop that produces thousands of lines of output.
  **Correction**: Lock stdout manually with `stdout().lock()` and use `writeln!` to avoid per-call lock acquisition.

- **Error**: Writing many small chunks to a file without buffering, causing one system call per write.
  **Correction**: Wrap the file handle in `BufWriter::new(file)` and call `flush()` explicitly when done.

- **Error**: Dropping a `BufWriter` without calling `flush()`, silently losing data if the final flush fails.
  **Correction**: Call `out.flush()?` explicitly to surface any errors from the final buffer flush.

# Common Confusions

- **Confusion**: Thinking Rust file I/O is buffered by default (as in many other languages).
  **Clarification**: Rust file I/O is explicitly unbuffered by default. You must opt in to buffering with `BufReader`/`BufWriter`.

- **Confusion**: Assuming the code change for buffered reading mirrors the trivial change for buffered writing.
  **Clarification**: Buffered writers implement the same `Write` trait as unbuffered writers (trivial code change). Buffered readers implement the `BufRead` trait instead of `Read`, which means structurally different code (e.g., gaining `read_line()` and `lines()` methods). This asymmetry is why forgetting to buffer is more common when writing.

- **Confusion**: Thinking reading into `String` is always the right approach for text processing.
  **Clarification**: Reading into `String` incurs UTF-8 validation on every read. For ASCII text or binary data, `BufRead::read_until` avoids this overhead.

# Source Reference

Chapter 12: I/O. Sections on Locking (stdout/stdin/stderr lock acquisition), Buffering (`BufReader`/`BufWriter`, `Write` vs `BufRead` trait asymmetry, explicit `flush`), Reading Lines from a File (cross-reference to heap allocations chapter), and Reading Input as Raw Bytes (`read_until`, `bstr`, `linereader` crates). Includes links to Rust compiler PR #93954 and dhat-rs PR #22 as buffering examples.

# Verification Notes

- Definition source: Directly from Ch. 12 prose, code examples, and inline commentary
- Key Properties: All 10 properties are explicitly stated or directly demonstrated in the source
- Confidence rationale: HIGH -- Ch. 12 is one of the most substantive chapters in this range, with clear before/after code examples and explicit explanations
- Uncertainties: The "Reading Lines from a File" section cross-references the heap allocations chapter (Ch. 7) without repeating its content
- Cross-reference status: perf-iterators-and-bounds and perf-general-tips are sibling cards from this extraction set
