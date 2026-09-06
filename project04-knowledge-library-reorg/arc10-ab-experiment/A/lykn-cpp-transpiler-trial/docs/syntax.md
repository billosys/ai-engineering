# Trial Syntax

This trial uses a deliberately tiny Lykn-inspired syntax. It keeps Lykn's
parenthesized surface form shape, but it does not try to be full Lykn.

## Slice 01

Slice 01 accepted exactly one source form, `(print 42)`, and generated a
complete C++17 program that writes the integer literal and a newline through
`std::cout`.

## Arc 01 Slice 02

Arc 01 Slice 02 accepts a small ordered program made of `(let ...)` and `(print ...)`
statements:

```lykn
(let x 40)
(print x)
(print 42)
```

The generated C++ preserves source statement order:

```cpp
#include <iostream>

int main() {
    int x{40};
    std::cout << x << "\n";
    std::cout << 42 << "\n";
    return 0;
}
```

`let` introduces one local `int` binding initialized from an integer literal.
`print` writes either an integer literal or an identifier that has already been
bound.

Integer literals are base-10 non-negative values in `0..=2147483647`. Negative
integer literals remain out of scope for this slice.

Identifiers must match `[A-Za-z_][A-Za-z0-9_]*`. The trial does not silently
rewrite identifiers.

Duplicate `let` bindings are rejected, and an identifier must be bound before
it can be printed.

## Fixtures And Examples

Audit orientation is documented in `docs/audit-readiness.md`.

Representative source fixtures live under `tests/fixtures/valid/` and
`tests/fixtures/invalid/`. Exact expected C++ outputs for accepted fixture
programs live under `tests/fixtures/expected/`.

Generated C++ examples live under `examples/`. The CLI integration tests use
the fixture tree for exact stdout and diagnostic checks, and compile generated
examples as C++17 when a local compiler is available.

## Arc 02 Final

Arc 02 final accepts the full tiny subset made of ordered `let` and `print`
statements, integer literals, already-bound identifiers, and recursive binary
arithmetic expressions. Expressions are valid in both `let` initializers and
`print` statements:

```lykn
(let a 20)
(let b (+ a 2))
(let c (- b 5))
(let d (* c (/ 8 4)))
(print (+ d 1))
(print (/ (* b c) 3))
```

The accepted arithmetic forms are binary prefix forms only:

```lykn
(+ left right)
(- left right)
(* left right)
(/ left right)
```

Each operand is another expression: an integer literal, a bound identifier, or
another binary arithmetic form.

Generated C++ uses deterministic parenthesized infix output:

```cpp
#include <iostream>

int main() {
    int a{20};
    int b{(a + 2)};
    int c{(b - 5)};
    int d{(c * (8 / 4))};
    std::cout << (d + 1) << "\n";
    std::cout << ((b * c) / 3) << "\n";
    return 0;
}
```

The binary arity is exact. A missing operand, an extra operand, and an
unsupported arithmetic operator are rejected with structured diagnostics. Empty
parenthesized expressions, missing closing parentheses in nested expressions,
extra operands after valid `print` or `let` expressions, invalid identifiers
inside arithmetic expressions, unknown identifiers, and identifiers used before
their binding are rejected before code generation.

Integer literals remain base-10 non-negative values in `0..=2147483647`.
Negative integer literals remain out of scope; use binary subtraction to
produce negative runtime values.

Arc 03 defers every broader language feature outside this final Arc 02 closure:
unary operators, variadic arithmetic, constant folding, expression evaluation,
overflow analysis beyond integer literal range checks, division-by-zero
analysis, strings, comments, functions, conditionals, loops, imports,
JavaScript behavior, source maps, and C++ build-system generation.

## Relationship To Lykn

This is related to real Lykn, but intentionally renamed for the experiment.
Lykn uses `bind` for immutable bindings and `console:log` for logging:

```lykn
(bind x 42)
(console:log x)
```

Prefix arithmetic is also part of the Lykn surface style and reserved for a
later slice of this trial:

```lykn
(+ x 2)
(let y (+ x 2))
```

Arc 02 final implements only the trial's binary integer arithmetic subset. It
still does not implement Lykn lisp-case-to-camelCase conversion, real Lykn
`bind`, real Lykn `console:log`, type annotations, strings, comments,
functions, conditionals, loops, imports, JavaScript behavior, source maps, or
C++ build-system generation.
