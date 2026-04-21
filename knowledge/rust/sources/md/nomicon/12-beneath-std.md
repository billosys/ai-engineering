# Beneath `std`

This section documents features that are normally provided by the `std` crate and
that `#![no_std]` developers have to deal with (i.e. provide) to build
`#![no_std]` binary crates.

## Using `libc`

In order to build a `#[no_std]` executable we will need `libc` as a dependency.
We can specify this using our `Cargo.toml` file:

```toml
[dependencies]
libc = { version = "0.2.146", default-features = false }
```

Note that the default features have been disabled. This is a critical step -
**the default features of `libc` include the `std` crate and so must be
disabled.**

Alternatively, we can use the unstable `rustc_private` private feature together
with an `extern crate libc;` declaration as shown in the examples below. Note that
windows-msvc targets do not require a libc, and correspondingly there is no `libc`
crate in their sysroot. We do not need the `extern crate libc;` below, and having it
on a windows-msvc target would be a compile error.

## Writing an executable without `std`

We will probably need a nightly version of the compiler to produce
a `#![no_std]` executable because on many platforms, we have to provide the
`eh_personality` [lang item], which is unstable.

You will need to define a symbol for the entry point that is suitable for your target. For example, `main`, `_start`, `WinMain`, or whatever starting point is relevant for your target.
Additionally, you need to use the `#![no_main]` attribute to prevent the compiler from attempting to generate an entry point itself.

Additionally, it's required to define a [panic handler function](panic-handler.html).

```rust
#![feature(lang_items, core_intrinsics, rustc_private)]
#![allow(internal_features)]
#![no_std]
#![no_main]

// Necessary for `panic = "unwind"` builds on cfg(unix) platforms.
#![feature(panic_unwind)]
extern crate unwind;

// Pull in the system libc library for what crt0.o likely requires.
#[cfg(not(windows))]
extern crate libc;

use core::ffi::{c_char, c_int};
use core::panic::PanicInfo;

// Entry point for this program.
#[unsafe(no_mangle)] // ensure that this symbol is included in the output as `main`
extern "C" fn main(_argc: c_int, _argv: *const *const c_char) -> c_int {
    0
}

// These functions are used by the compiler, but not for an empty program like this.
// They are normally provided by `std`.
#[lang = "eh_personality"]
fn rust_eh_personality() {}
#[panic_handler]
fn panic_handler(_info: &PanicInfo) -> ! { core::intrinsics::abort() }
```

If you are working with a target that doesn't have binary releases of the
standard library available via rustup (this probably means you are building the
`core` crate yourself) and need compiler-rt intrinsics (i.e. you are probably
getting linker errors when building an executable:
``undefined reference to `__aeabi_memcpy'``), you need to manually link to the
[`compiler_builtins` crate] to get those intrinsics and solve the linker errors.

[`compiler_builtins` crate]: https://crates.io/crates/compiler_builtins
[lang item]: https://doc.rust-lang.org/nightly/unstable-book/language-features/lang-items.html


---

# #[panic_handler]

`#[panic_handler]` is used to define the behavior of `panic!` in `#![no_std]` applications.
The `#[panic_handler]` attribute must be applied to a function with signature `fn(&PanicInfo)
-> !` and such function must appear *once* in the dependency graph of a binary / dylib / cdylib
crate. The API of `PanicInfo` can be found in the [API docs].

[API docs]: ../core/panic/struct.PanicInfo.html

Given that `#![no_std]` applications have no *standard* output and that some `#![no_std]`
applications, e.g. embedded applications, need different panicking behaviors for development and for
release it can be helpful to have panic crates, crate that only contain a `#[panic_handler]`.
This way applications can easily swap the panicking behavior by simply linking to a different panic
crate.

Below is shown an example where an application has a different panicking behavior depending on
whether is compiled using the dev profile (`cargo build`) or using the release profile (`cargo build
--release`).

`panic-semihosting` crate -- log panic messages to the host stderr using semihosting:

<!-- ignore: simplified code -->
```rust,ignore
#![no_std]

use core::fmt::{Write, self};
use core::panic::PanicInfo;

struct HStderr {
    // ..
#     _0: (),
}
#
# impl HStderr {
#     fn new() -> HStderr { HStderr { _0: () } }
# }
#
# impl fmt::Write for HStderr {
#     fn write_str(&mut self, _: &str) -> fmt::Result { Ok(()) }
# }

#[panic_handler]
fn panic(info: &PanicInfo) -> ! {
    let mut host_stderr = HStderr::new();

    // logs "panicked at '$reason', src/main.rs:27:4" to the host stderr
    writeln!(host_stderr, "{}", info).ok();

    loop {}
}
```

`panic-halt` crate -- halt the thread on panic; messages are discarded:

<!-- ignore: simplified code -->
```rust,ignore
#![no_std]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
```

`app` crate:

<!-- ignore: requires the above crates -->
```rust,ignore
#![no_std]

// dev profile
#[cfg(debug_assertions)]
extern crate panic_semihosting;

// release profile
#[cfg(not(debug_assertions))]
extern crate panic_halt;

fn main() {
    // ..
}
```
