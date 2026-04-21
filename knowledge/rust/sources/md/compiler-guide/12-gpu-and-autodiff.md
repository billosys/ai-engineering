# std::offload

This module is under active development. Once upstream, it should allow Rust developers to run Rust code on GPUs.
We aim to develop a `rusty` GPU programming interface, which is safe, convenient and sufficiently fast by default.
This includes automatic data movement to and from the GPU, in a efficient way. We will (later)
also offer more advanced, possibly unsafe, interfaces which allow a higher degree of control.

The implementation is based on LLVM's "offload" project, which is already used by OpenMP to run Fortran or C++ code on GPUs.
While the project is under development, users will need to call other compilers like clang to finish the compilation process.

## High-level compilation design:
We use a single-source, two-pass compilation approach. 

First we compile all functions that should be offloaded for the device (e.g nvptx64, amdgcn-amd-amdhsa, intel in the future). Currently we require cumbersome `#cfg(target_os="")` annotations, but we intend to recognize those in the future based on our offload intrinsic. 
This first compilation currently does not leverage rustc's internal Query system, so it will always recompile your kernels at the moment. This should be easy to fix, but we prioritize features and runtime performance improvements at the moment. Please reach out if you want to implement it, though!

We then compile the code for the host (e.g. x86-64), where most of the offloading logic happens. On the host side, we generate calls to the openmp offload runtime, to inform it about the layout of the types (a simplified version of the autodiff TypeTrees). We also use the type system to figure out whether kernel arguments have to be moved only to the device (e.g. `&[f32;1024]`), from the device, or both (e.g. `&mut [f64]`). We then launch the kernel, after which we inform the runtime to end this environment and move data back (as far as needed).

The second pass for the host will load the kernel artifacts from the previous compilation. rustc in general may not "guess" or hardcode the build directory layout, and as such it must be told the path to the kernel artifacts in the second invocation. The logic for this could be integrated into cargo, but it also only requires a trivial cargo wrapper, which we could trivially provide via crates.io till we see larger adoption.

It might seem tempting to think about a single-source, single pass compilation approach. However, a lot of the rustc frontend (e.g. AST) will drop any dead code (e.g. code behind an inactive `cfg`). Getting the frontend to expand and lower code for two targets naively will result in multiple definitions of the same symbol (and other issues). Trying to teach the whole rustc middle and backend to be aware that any symbol now might contain two implementations is a large undertaking, and it is questionable why we should make the whole compiler more complex, if the alternative is a ~5 line cargo wrapper. We still control the full compilation pipeline and have both host and device code available, therefore there shouldn't be a runtime performance difference between the two approaches. 



---

# Installation

`std::offload` is partly available in nightly builds for users. For now, everyone however still needs to build rustc from source to use all features of it. 

## Build instructions

First you need to clone and configure the Rust repository:
```bash
git clone git@github.com:rust-lang/rust
cd rust
./configure --enable-llvm-link-shared --release-channel=nightly --enable-llvm-assertions --enable-llvm-offload --enable-llvm-enzyme --enable-clang --enable-lld --enable-option-checking --enable-ninja --disable-docs
```

Afterwards you can build rustc using:
```bash
./x build --stage 1 library
```

Afterwards rustc toolchain link will allow you to use it through cargo:
```
rustup toolchain link offload build/host/stage1
rustup toolchain install nightly # enables -Z unstable-options
```



## Build instruction for LLVM itself
```bash
git clone git@github.com:llvm/llvm-project
cd llvm-project
mkdir build
cd build
cmake -G Ninja ../llvm -DLLVM_TARGETS_TO_BUILD="host;AMDGPU;NVPTX" -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="clang;lld" -DLLVM_ENABLE_RUNTIMES="offload;openmp" -DLLVM_ENABLE_PLUGINS=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=.
ninja
ninja install
```
This gives you a working LLVM build.


## Testing
run
```
./x test --stage 1 tests/codegen-llvm/gpu_offload
```


---

# Usage

This feature is work-in-progress, and not ready for usage. The instructions here are for contributors, or people interested in following the latest progress.
We currently work on launching the following Rust kernel on the GPU. To follow along, copy it to a `src/lib.rs` file.

```rust
#![feature(abi_gpu_kernel)]
#![feature(rustc_attrs)]
#![feature(core_intrinsics)]
#![no_std]

#[cfg(target_os = "linux")]
extern crate libc;
#[cfg(target_os = "linux")]
use libc::c_char;

#[cfg(target_os = "linux")]
use core::mem;

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}

#[cfg(target_os = "linux")]
#[unsafe(no_mangle)]
#[inline(never)]
fn main() {
    let array_c: *mut [f64; 256] =
        unsafe { libc::calloc(256, (mem::size_of::<f64>()) as libc::size_t) as *mut [f64; 256] };
    let output = c"The first element is zero %f\n";
    let output2 = c"The first element is NOT zero %f\n";
    let output3 = c"The second element is %f\n";
    unsafe {
        let val: *const c_char = if (*array_c)[0] < 0.1 {
            output.as_ptr()
        } else {
            output2.as_ptr()
        };
        libc::printf(val, (*array_c)[0]);
    }

    unsafe {
        kernel(array_c);
    }
    core::hint::black_box(&array_c);
    unsafe {
        let val: *const c_char = if (*array_c)[0] < 0.1 {
            output.as_ptr()
        } else {
            output2.as_ptr()
        };
        libc::printf(val, (*array_c)[0]);
        libc::printf(output3.as_ptr(), (*array_c)[1]);
    }
}

#[inline(never)]
unsafe fn kernel(x: *mut [f64; 256]) {
    core::intrinsics::offload(_kernel_1, [256, 1, 1], [32, 1, 1], (x,))
}

#[cfg(target_os = "linux")]
unsafe extern "C" {
    pub fn kernel_1(array_b: *mut [f64; 256]);
}

#[cfg(not(target_os = "linux"))]
#[unsafe(no_mangle)]
#[inline(never)]
#[rustc_offload_kernel]
pub extern "gpu-kernel" fn kernel_1(x: *mut [f64; 256]) {
    unsafe { (*x)[0] = 21.0 };
}
```

## Compile instructions
It is important to use a clang compiler build on the same llvm as rustc. Just calling clang without the full path will likely use your system clang, which probably will be incompatible. So either substitute clang/lld invocations below with absolute path, or set your `PATH` accordingly.

First we generate the device (gpu) code. Replace the target-cpu with the right code for your gpu.
```
RUSTFLAGS="-Ctarget-cpu=gfx90a --emit=llvm-bc,llvm-ir -Zoffload=Device -Csave-temps -Zunstable-options" cargo +offload build -Zunstable-options -r -v --target amdgcn-amd-amdhsa -Zbuild-std=core
```
You might afterwards need to copy your target/release/deps/<lib_name>.bc to lib.bc for now, before the next step.

Now we generate the host (cpu) code.
```
RUSTFLAGS="--emit=llvm-bc,llvm-ir -Csave-temps -Zoffload=Host=/p/lustre1/drehwald1/prog/offload/r/target/amdgcn-amd-amdhsa/release/deps/host.out -Zunstable-options" cargo +offload build -r
```
This call also does a lot of work and generates multiple intermediate files for llvm offload.
While we integrated most offload steps into rustc by now, one binary invocation still remains for now:

```
"clang-linker-wrapper" "--should-extract=gfx90a" "--device-compiler=amdgcn-amd-amdhsa=-g" "--device-compiler=amdgcn-amd-amdhsa=-save-temps=cwd" "--device-linker=amdgcn-amd-amdhsa=-lompdevice" "--host-triple=x86_64-unknown-linux-gnu" "--save-temps" "--linker-path=/ABSOlUTE_PATH_TO/rust/build/x86_64-unknown-linux-gnu/lld/bin/ld.lld" "--hash-style=gnu" "--eh-frame-hdr" "-m" "elf_x86_64" "-pie" "-dynamic-linker" "/lib64/ld-linux-x86-64.so.2" "-o" "bare" "/lib/../lib64/Scrt1.o" "/lib/../lib64/crti.o" "/ABSOLUTE_PATH_TO/crtbeginS.o" "-L/ABSOLUTE_PATH_TO/rust/build/x86_64-unknown-linux-gnu/llvm/bin/../lib/x86_64-unknown-linux-gnu" "-L/ABSOLUTE_PATH_TO/rust/build/x86_64-unknown-linux-gnu/llvm/lib/clang/21/lib/x86_64-unknown-linux-gnu" "-L/lib/../lib64" "-L/usr/lib64" "-L/lib" "-L/usr/lib" "target/<GPU_DIR>/release/host.o" "-lstdc++" "-lm" "-lomp" "-lomptarget" "-L/ABSOLUTE_PATH_TO/rust/build/x86_64-unknown-linux-gnu/llvm/lib" "-lgcc_s" "-lgcc" "-lpthread" "-lc" "-lgcc_s" "-lgcc" "/ABSOLUTE_PATH_TO/crtendS.o" "/lib/../lib64/crtn.o"
```

You can try to find the paths to those files on your system. However, I recommend to not fix the paths, but rather just re-generate them by copying a bare-mode openmp example and compiling it with your clang. By adding `-###` to your clang invocation, you can see the invidual steps.
It will show multiple steps, just look for the clang-linker-wrapper example. Make sure to still include the path to the `host.o` file, and not whatever tmp file you got when compiling your c++ example with the following call.
```
myclang++ -fuse-ld=lld -O3 -fopenmp  -fopenmp-offload-mandatory --offload-arch=gfx90a omp_bare.cpp -o main -###
```

In the final step, you can now run your binary

```
./main
The first element is zero 0.000000
The first element is NOT zero 21.000000
The second element is  0.000000
```

To receive more information about the memory transfer, you can enable info printing with
```
LIBOMPTARGET_INFO=-1  ./main
```


---

# Contributing

Contributions are always welcome. This project is experimental, so the documentation and code are likely incomplete. Please ask on [Zulip](https://rust-lang.zulipchat.com/#narrow/channel/422870-t-compiler.2Fgpgpu-backend) (preferred) or the Rust Community Discord for help if you get stuck or if our documentation is unclear.

We generally try to automate as much of the compilation process as possible for users. However, as a contributor it might sometimes be easier to directly rewrite and compile the LLVM-IR modules (.ll) to quickly iterate on changes, without needing to repeatedly recompile rustc. For people familiar with LLVM we therefore have the shell script below. Only when you are then happy with the IR changes you can work on updating rustc to generate the new, desired output.

```sh
set -e
# set -e to avoid continuing on errors, which would likely use stale artifacts
# inputs:
# lib.ll (host code) + host.out (device)

# You only need to run the first three commands once to generate lib.ll and host.out from your rust code.

# RUSTFLAGS="-Ctarget-cpu=gfx90a --emit=llvm-bc,llvm-ir -Zoffload=Device -Csave-temps -Zunstable-options" cargo +offload build -Zunstable-options -v --target amdgcn-amd-amdhsa -Zbuild-std=core -r
#
# RUSTFLAGS="--emit=llvm-bc,llvm-ir -Csave-temps -Zoffload=Host=/absolute/path/to/project/target/amdgcn-amd-amdhsa/release/deps/host.out -Zunstable-options" cargo +offload build -r
#
# cp target/release/deps/<project_name>.ll lib.ll

opt lib.ll -o lib.bc

"clang-21" "-cc1" "-triple" "x86_64-unknown-linux-gnu" "-S" "-save-temps=cwd" "-disable-free" "-clear-ast-before-backend" "-main-file-name" "lib.rs" "-mrelocation-model" "pic" "-pic-level" "2" "-pic-is-pie" "-mframe-pointer=all" "-fmath-errno" "-ffp-contract=on" "-fno-rounding-math" "-mconstructor-aliases" "-funwind-tables=2" "-target-cpu" "x86-64" "-tune-cpu" "generic" "-resource-dir" "/<path>/rust/build/x86_64-unknown-linux-gnu/llvm/lib/clang/21" "-ferror-limit" "19" "-fopenmp" "-fopenmp-offload-mandatory" "-fgnuc-version=4.2.1" "-fskip-odr-check-in-gmf" "-fembed-offload-object=host.out" "-fopenmp-targets=amdgcn-amd-amdhsa" "-faddrsig" "-D__GCC_HAVE_DWARF2_CFI_ASM=1" "-o" "host.s" "-x" "ir" "lib.bc"

"clang-21" "-cc1as" "-triple" "x86_64-unknown-linux-gnu" "-filetype" "obj" "-main-file-name" "lib.rs" "-target-cpu" "x86-64" "-mrelocation-model" "pic" "-o" "host.o" "host.s"

"/<path>/rust/build/x86_64-unknown-linux-gnu/llvm/bin/clang-linker-wrapper" "--should-extract=gfx90a" "--device-compiler=amdgcn-amd-amdhsa=-g" "--device-compiler=amdgcn-amd-amdhsa=-save-temps=cwd" "--device-linker=amdgcn-amd-amdhsa=-lompdevice" "--host-triple=x86_64-unknown-linux-gnu" "--save-temps" "--linker-path=/<path>/rust/build/x86_64-unknown-linux-gnu/lld/bin/ld.lld" "--hash-style=gnu" "--eh-frame-hdr" "-m" "elf_x86_64" "-pie" "-dynamic-linker" "/lib64/ld-linux-x86-64.so.2" "-o" "a.out" "/lib/../lib64/Scrt1.o" "/lib/../lib64/crti.o" "/opt/rh/gcc-toolset-12/root/usr/lib/gcc/x86_64-redhat-linux/12/crtbeginS.o" "-L/<path>/rust/build/x86_64-unknown-linux-gnu/llvm/bin/../lib/x86_64-unknown-linux-gnu" "-L/<path>/rust/build/x86_64-unknown-linux-gnu/llvm/lib/clang/21/lib/x86_64-unknown-linux-gnu" "-L/opt/rh/gcc-toolset-12/root/usr/lib/gcc/x86_64-redhat-linux/12" "-L/opt/rh/gcc-toolset-12/root/usr/lib/gcc/x86_64-redhat-linux/12/../../../../lib64" "-L/lib/../lib64" "-L/usr/lib64" "-L/lib" "-L/usr/lib" "host.o" "-lstdc++" "-lm" "-lomp" "-lomptarget" "-L/<path>/rust/build/x86_64-unknown-linux-gnu/llvm/lib" "-lgcc_s" "-lgcc" "-lpthread" "-lc" "-lgcc_s" "-lgcc" "/opt/rh/gcc-toolset-12/root/usr/lib/gcc/x86_64-redhat-linux/12/crtendS.o" "/lib/../lib64/crtn.o"

LIBOMPTARGET_INFO=-1 OFFLOAD_TRACK_ALLOCATION_TRACES=true ./a.out
```

Please update the `<path>` placeholders on the `clang-linker-wrapper` invocation. You will likely also need to adjust the library paths. See the linked usage section for details: [usage](usage.md#compile-instructions)


---

The `std::autodiff` module in Rust allows differentiable programming:

```rust
#![feature(autodiff)]
use std::autodiff::*;

// f(x) = x * x, f'(x) = 2.0 * x
// bar therefore returns (x * x, 2.0 * x)
#[autodiff_reverse(bar, Active, Active)]
fn foo(x: f32) -> f32 { x * x }

fn main() {
    assert_eq!(bar(3.0, 1.0), (9.0, 6.0));
    assert_eq!(bar(4.0, 1.0), (16.0, 8.0));
}
```

The detailed documentation for the `std::autodiff` module is available at [std::autodiff](https://doc.rust-lang.org/std/autodiff/index.html).

Differentiable programming is used in various fields like numerical computing, [solid mechanics][ratel], [computational chemistry][molpipx], [fluid dynamics][waterlily] or for Neural Network training via Backpropagation, [ODE solver][diffsol], [differentiable rendering][libigl], [quantum computing][catalyst], and climate simulations.

[ratel]: https://gitlab.com/micromorph/ratel
[molpipx]: https://arxiv.org/abs/2411.17011
[waterlily]: https://github.com/WaterLily-jl/WaterLily.jl
[diffsol]: https://github.com/martinjrobins/diffsol
[libigl]: https://github.com/alecjacobson/libigl-enzyme-example?tab=readme-ov-file#run
[catalyst]: https://github.com/PennyLaneAI/catalyst


---

# Installation

In the near future, `std::autodiff` should become available for users via rustup. As a rustc/enzyme/autodiff contributor however, you will still need to build rustc from source. 
For the meantime, you can download up-to-date builds to enable `std::autodiff` on your latest nightly toolchain, if you are using either of:  
**Linux**, with `x86_64-unknown-linux-gnu` or `aarch64-unknown-linux-gnu`  
**Windows**, with `x86_64-llvm-mingw` or `aarch64-llvm-mingw`  

You can also download slightly outdated builds for **Apple** (aarch64-apple), which should generally work for now. 

If you need any other platform, you can build rustc including autodiff from source. Please open an issue if you want to help enabling automatic builds for your prefered target.

## Installation guide

If you want to use `std::autodiff` and don't plan to contribute PR's to the project, then we recommend to just use your existing nightly installation and download the missing component. In the future, rustup will be able to do it for you.
For now, you'll have to manually download and copy it.

1) On our github repository, find the last merged PR: [`Repo`]
2) Scroll down to the lower end of the PR, where you'll find a rust-bors message saying `Test successful` with a `CI` link. 
3) Click on the `CI` link, and grep for your target. E.g. `dist-x86_64-linux` or `dist-aarch64-llvm-mingw` and click `Load summary`. 
4) Under the `CI artifacts` section, find the `enzyme-nightly` artifact, download, and unpack it.
5) Copy the artifact (libEnzyme-22.so for linux, libEnzyme-22.dylib for apple, etc.), which should be in a folder named `enzyme-preview`, to your rust toolchain directory. E.g. for linux: `cp  ~/Downloads/enzyme-nightly-x86_64-unknown-linux-gnu/enzyme-preview/lib/rustlib/x86_64-unknown-linux-gnu/lib/libEnzyme-22.so ~/.rustup/toolchains/nightly-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/lib`

Apple support was temporarily reverted, due to downstream breakages. If you want to download autodiff for apple, please look at the artifacts from this [`run`].

## Installation guide for Nix user.

This setup was recommended by a nix and autodiff user. It uses [`Overlay`]. Please verify for yourself if you are comfortable using that repository.
In that case you might use the following nix configuration to get a rustc that supports `std::autodiff`.
```nix
{
  enzymeLib = pkgs.fetchzip {
    url = "https://ci-artifacts.rust-lang.org/rustc-builds/ec818fda361ca216eb186f5cf45131bd9c776bb4/enzyme-nightly-x86_64-unknown-linux-gnu.tar.xz";
    sha256 = "sha256-Rnrop44vzS+qmYNaRoMNNMFyAc3YsMnwdNGYMXpZ5VY=";
  };
  
  rustToolchain = pkgs.symlinkJoin {
    name = "rust-with-enzyme";
    paths = [pkgs.rust-bin.nightly.latest.default];
    nativeBuildInputs = [pkgs.makeWrapper];
    postBuild = ''
      libdir=$out/lib/rustlib/x86_64-unknown-linux-gnu/lib
      cp ${enzymeLib}/enzyme-preview/lib/rustlib/x86_64-unknown-linux-gnu/lib/libEnzyme-22.so $libdir/
      wrapProgram $out/bin/rustc --add-flags "--sysroot $out"
    '';
  };
}
```

## Build instructions

First you need to clone and configure the Rust repository. Based on your preferences, you might also want to `--enable-clang` or `--enable-lld`.
```bash
git clone git@github.com:rust-lang/rust
cd rust
./configure --release-channel=nightly --enable-llvm-enzyme --enable-llvm-link-shared --enable-llvm-assertions --enable-ninja --enable-option-checking --disable-docs --set llvm.download-ci-llvm=false
```

Afterwards you can build rustc using:
```bash
./x build --stage 1 library
```

Afterwards rustc toolchain link will allow you to use it through cargo:
```
rustup toolchain link enzyme build/host/stage1
rustup toolchain install nightly # enables -Z unstable-options
```

You can then run our test cases:

```bash
./x test --stage 1 tests/codegen-llvm/autodiff
./x test --stage 1 tests/pretty/autodiff
./x test --stage 1 tests/ui/autodiff
./x test --stage 1 tests/run-make/autodiff
./x test --stage 1 tests/ui/feature-gates/feature-gate-autodiff.rs
```

Autodiff is still experimental, so if you want to use it in your own projects, you will need to add `lto="fat"` to your Cargo.toml 
and use `RUSTFLAGS="-Zautodiff=Enable" cargo +enzyme` instead of `cargo` or `cargo +nightly`. 

## Compiler Explorer and dist builds

Our compiler explorer instance can be updated to a newer rustc in a similar way. First, prepare a docker instance.
```bash
docker run -it ubuntu:22.04
export CC=clang CXX=clang++
apt update
apt install wget vim python3 git curl libssl-dev pkg-config lld ninja-build cmake clang build-essential 
```
Then build rustc in a slightly altered way:
```bash
git clone https://github.com/rust-lang/rust
cd rust
./configure --release-channel=nightly --enable-llvm-enzyme --enable-llvm-link-shared --enable-llvm-assertions --enable-ninja --enable-option-checking --disable-docs --set llvm.download-ci-llvm=false
./x dist
```
We then copy the tarball to our host. The dockerid is the newest entry under `docker ps -a`.
```bash
docker cp <dockerid>:/rust/build/dist/rust-nightly-x86_64-unknown-linux-gnu.tar.gz rust-nightly-x86_64-unknown-linux-gnu.tar.gz
```
Afterwards we can create a new (pre-release) tag on the EnzymeAD/rust repository and make a PR against the EnzymeAD/enzyme-explorer repository to update the tag.
Remember to ping `tgymnich` on the PR to run his update script. Note: We should archive EnzymeAD/rust and update the instructions here. The explorer should soon
be able to get the rustc toolchain from the official rust servers.


## Build instruction for Enzyme itself

Following the Rust build instruction above will build LLVMEnzyme, LLDEnzyme, and ClangEnzyme along with the Rust compiler.
We recommend that approach, if you just want to use any of them and have no experience with cmake.
However, if you prefer to just build Enzyme without Rust, then these instructions might help.

```bash
git clone git@github.com:llvm/llvm-project
cd llvm-project
mkdir build
cd build
cmake -G Ninja ../llvm -DLLVM_TARGETS_TO_BUILD="host" -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="clang;lld" -DLLVM_ENABLE_RUNTIMES="openmp" -DLLVM_ENABLE_PLUGINS=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=.
ninja
ninja install
```
This gives you a working LLVM build, now we can continue with building Enzyme.
Leave the `llvm-project` folder, and execute the following commands:
```bash
git clone git@github.com:EnzymeAD/Enzyme
cd Enzyme/enzyme
mkdir build 
cd build 
cmake .. -G Ninja -DLLVM_DIR=<YourLocalPath>/llvm-project/build/lib/cmake/llvm/ -DLLVM_EXTERNAL_LIT=<YourLocalPath>/llvm-project/llvm/utils/lit/lit.py -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=YES -DBUILD_SHARED_LIBS=ON
ninja
```
This will build Enzyme, and you can find it in `Enzyme/enzyme/build/lib/<LLD/Clang/LLVM/lib>Enzyme.so`. (Endings might differ based on your OS).

[`Repo`]: https://github.com/rust-lang/rust/
[`run`]: https://github.com/rust-lang/rust/pull/153026#issuecomment-3950046599
[`Overlay`]: https://github.com/oxalica/rust-overlay


---

# Reporting backend crashes

If after a compilation failure you are greeted by a large amount of llvm-ir code, then our enzyme backend likely failed to compile your code. These cases are harder to debug, so your help is highly appreciated. Please also keep in mind that release builds are usually much more likely to work at the moment.

The final goal here is to reproduce your bug in the enzyme [compiler explorer](https://enzyme.mit.edu/explorer/), in order to create a bug report in the [Enzyme](https://github.com/enzymead/enzyme/issues) repository.

We have an `autodiff` flag which you can pass to `rustflags` to help with this. it will print the whole llvm-ir module, along with some `__enzyme_fwddiff` or `__enzyme_autodiff` calls. A potential workflow on linux could look like:  

## Controlling llvm-ir generation

Before generating the llvm-ir, keep in mind two techniques that can help ensure the relevant rust code is visible for debugging:

- **`std::hint::black_box`**: wrap rust variables or expressions in `std::hint::black_box()` to prevent rust and llvm from optimizing them away. This is useful when you need to inspect or manually manipulate specific values in the llvm-ir.
- **`extern "rust"` or `extern "c"`**: if you want to see how a specific function declaration is lowered to llvm-ir, you can declare it as `extern "rust"` or `extern "c"`. You can also look for existing `__enzyme_autodiff` or similar declarations within the generated module for examples.

## 1) Generate an llvm-ir reproducer

```sh
RUSTFLAGS="-Z autodiff=Enable,PrintModBefore" cargo +enzyme build --release &> out.ll 
```

This also captures a few warnings and info messages above and below your module. open out.ll and remove every line above `; moduleid = <somehash>`. Now look at the end of the file and remove everything that's not part of llvm-ir, i.e. remove errors and warnings. The last line of your llvm-ir should now start with `!<somenumber> = `, i.e. `!40831 = !{i32 0, i32 1037508, i32 1037538, i32 1037559}` or `!43760 = !dilocation(line: 297, column: 5, scope: !43746)`.

The actual numbers will depend on your code.  

## 2) Check your llvm-ir reproducer

To confirm that your previous step worked, we will use llvm's `opt` tool. Find your path to the opt binary, with a path similar to `<some_dir>/rust/build/<x86/arm/...-target-triple>/ci-llvm/bin/opt`. If you build LLVM from source, you'll likely need to replace `ci-llvm` with `build`. Also find `llvmenzyme-21.<so/dll/dylib>` path, similar to `/rust/build/target-triple/enzyme/build/enzyme/llvmenzyme-21`. Please keep in mind that llvm frequently updates it's llvm backend, so the version number might be higher (20, 21, ...). Once you have both, run the following command:

```sh
<path/to/opt> out.ll -load-pass-plugin=/path/to/build/<target-triple>/stage1/lib/libEnzyme-21.so -passes="enzyme" -enzyme-strict-aliasing=0  -s
```
This command might fail for future versions or on your system, in which case you should replace libEnzyme-21.so with LLVMEnzyme-21.so. Look at the Enzyme docs for instructions on how to build it. You might need to also adjust how to build your LLVM version.

If the previous step succeeded, you are going to see the same error that you saw when compiling your rust code with cargo. 

If you fail to get the same error, please open an issue in the rust repository. If you succeed, congrats! the file is still huge, so let's automatically minimize it.

## 3) Minimize your llvm-ir reproducer

First find your `llvm-extract` binary, it's in the same folder as your opt binary. then run:

```sh
<path/to/llvm-extract> -s --func=<name> --recursive --rfunc="enzyme_autodiff*" --rfunc="enzyme_fwddiff*" --rfunc=<fnc_called_by_enzyme> out.ll -o mwe.ll 
```

This command creates `mwe.ll`, a minimal working example.

Please adjust the name passed with the last `--func` flag. You can either apply the `#[no_mangle]` attribute to the function you differentiate, then you can replace it with the rust name. otherwise you will need to look up the mangled function name. To do that, open `out.ll` and search for `__enzyme_fwddiff` or `__enzyme_autodiff`. the first string in that function call is the name of your function. example:

```llvm-ir 
define double @enzyme_opt_helper_0(ptr %0, i64 %1, double %2) {
  %4 = call double (...) @__enzyme_fwddiff(ptr @_zn2ad3_f217h3b3b1800bd39fde3e, metadata !"enzyme_const", ptr %0, metadata !"enzyme_const", i64 %1, metadata !"enzyme_dup", double %2, double %2)
  ret double %4
}
```

Here, `_zn2ad3_f217h3b3b1800bd39fde3e` is the correct name. make sure to not copy the leading `@`. redo step 2) by running the `opt` command again, but this time passing `mwe.ll` as the input file instead of `out.ll`. Check if this minimized example still reproduces the crash.

## 4) (Optional) Minimize your llvm-ir reproducer further.

After the previous step you should have an `mwe.ll` file with ~5k loc. let's try to get it down to 50. find your `llvm-reduce` binary next to `opt` and `llvm-extract`. Copy the first line of your error message, an example could be:

```sh
opt: /home/manuel/prog/rust/src/llvm-project/llvm/lib/ir/instructions.cpp:686: void llvm::callinst::init(llvm::functiontype*, llvm::value*, llvm::arrayref<llvm::value*>, llvm::arrayref<llvm::operandbundledeft<llvm::value*> >, const llvm::twine&): assertion `(args.size() == fty->getnumparams() || (fty->isvararg() && args.size() > fty->getnumparams())) && "calling a function with bad signature!"' failed.
```

If you just get a `segfault` there is no sensible error message and not much to do automatically, so continue to 5).  
otherwise, create a `script.sh` file containing

```sh
#!/bin/bash
<path/to/your/opt> $1 -load-pass-plugin=/path/to/llvmenzyme-19.so -passes="enzyme" \
    |& grep "/some/path.cpp:686: void llvm::callinst::init"
```

Experiment a bit with which error message you pass to grep. it should be long enough to make sure that the error is unique. However, for longer errors including `(` or `)` you will need to escape them correctly which can become annoying. Run

```sh 
<path/to/llvm-reduce> --test=script.sh mwe.ll 
```

If you see `input isn't interesting! verify interesting-ness test`, you got the error message in script.sh wrong, you need to make sure that grep matches your actual error. If all works out, you will see a lot of iterations, ending with a new `reduced.ll` file. Verify with `opt` that you still get the same error.

### Advanced debugging: manual llvm-ir investigation

Once you have a minimized reproducer (`mwe.ll` or `reduced.ll`), you can delve deeper:

- **manual editing:** try manually rewriting the llvm-ir. for certain issues, like those involving indirect calls, you might investigate enzyme-specific intrinsics like `__enzyme_virtualreverse`. Understanding how to use these might require consulting enzyme's documentation or source code.
- **enzyme test cases:** look for relevant test cases within the [enzyme repository](https://github.com/enzymead/enzyme/tree/main/enzyme/test) that might demonstrate the correct usage of features or intrinsics related to your problem.

## 5) Report your bug.

Afterwards, you should be able to copy and paste your `mwe.ll` (or `reduced.ll`) example into our [compiler explorer](https://enzyme.mit.edu/explorer/).

- Select `llvm ir` as language and `opt 20` as compiler.
- Replace the field to the right of your compiler with `-passes="enzyme"`, if it is not already set.
- Hopefully, you will see once again your now familiar error.
- Please use the share button to copy links to them.
- Please create an issue on [https://github.com/enzymead/enzyme/issues](https://github.com/enzymead/enzyme/issues) and share `mwe.ll` and (if you have it) `reduced.ll`, as well as links to the compiler explorer. Please feel free to also add your rust code or a link to it.

#### Documenting findings

some enzyme errors, like `"attempting to call an indirect active function whose runtime value is inactive"`, have historically caused confusion. If you investigate such an issue, even if you don't find a complete solution, please consider documenting your findings. If the insights are general to enzyme and not specific to its rust usage, contributing them to the main [enzyme documentation](https://github.com/enzymead/www) is often the best first step. You can also mention your findings in the relevant enzyme github issue or propose updates to these docs if appropriate. This helps prevent others from starting from scratch.

With a clear reproducer and documentation, hopefully an enzyme developer will be able to fix your bug. Once that happens, the enzyme submodule inside the rust compiler will be updated, which should allow you to differentiate your rust code. Thanks for helping us to improve rust-ad.

# Minimize rust code

Beyond having a minimal llvm-ir reproducer, it is also helpful to have a minimal rust reproducer without dependencies. This allows us to add it as a test case to ci once we fix it, which avoids regressions for the future.

There are a few solutions to help you with minimizing the rust reproducer. This is probably the most simple automated approach: [cargo-minimize](https://github.com/nilstrieb/cargo-minimize).

Otherwise we have various alternatives, including [`treereduce`](https://github.com/langston-barrett/treereduce), [`halfempty`](https://github.com/googleprojectzero/halfempty), or [`picireny`](https://github.com/renatahodovan/picireny), potentially also [`creduce`](https://github.com/csmith-project/creduce).


---

# Supported `RUSTFLAGS`

To support you while debugging or profiling, we have added support for an experimental `-Z autodiff` rustc flag (which can be passed to cargo via `RUSTFLAGS`), which allow changing the behaviour of Enzyme, without recompiling rustc. We currently support the following values for `autodiff`.

### Debug Flags

```text
PrintTA // Print TypeAnalysis information
PrintTAFn // Print TypeAnalysis information for a specific function
PrintAA // Print ActivityAnalysis information
Print // Print differentiated functions while they are being generated and optimized
PrintPerf // Print AD related Performance warnings
PrintModBefore // Print the whole LLVM-IR module directly before running AD
PrintModAfter // Print the whole LLVM-IR module after running AD, before optimizations
PrintModFinal // Print the whole LLVM-IR module after running optimizations and AD
LooseTypes // Risk incorrect derivatives instead of aborting when missing Type Info 
```

<div class="warning">

`LooseTypes` is often helpful to get rid of Enzyme errors stating `Can not deduce type of <X>` and to be able to run some code. But please keep in mind that this flag absolutely has the chance to cause incorrect gradients. Even worse, the gradients might be correct for certain input values, but not for others. So please create issues about such bugs and only use this flag temporarily while you wait for your bug to be fixed.

</div>

### Benchmark flags

For performance experiments and benchmarking we also support

```text
NoPostopt // We won't optimize the LLVM-IR Module after AD
RuntimeActivity // Enables the runtime activity feature from Enzyme 
Inline // Instructs Enzyme to maximize inlining as far as possible, beyond LLVM's default
```

You can combine multiple `autodiff` values using a comma as separator:

```bash
RUSTFLAGS="-Z autodiff=Enable,LooseTypes,PrintPerf" cargo +enzyme build
```

Using `-Zautodiff=Enable` will allow using autodiff and update your normal rustc compilation pipeline:

1. Run your selected compilation pipeline. If you selected a release build, we will disable vectorization and loop unrolling.
2. Differentiate your functions.
3. Run your selected compilation pipeline again on the whole module. This time we do not disable vectorization or loop unrolling.


---

# TypeTrees for Autodiff

## What are TypeTrees?
Memory layout descriptors for Enzyme. Tell Enzyme exactly how types are structured in memory so it can compute derivatives efficiently.

## Structure
```rust
TypeTree(Vec<Type>)

Type {
    offset: isize,  // byte offset (-1 = everywhere)
    size: usize,    // size in bytes
    kind: Kind,     // Float, Integer, Pointer, etc.
    child: TypeTree // nested structure
}
```

## Example: `fn compute(x: &f32, data: &[f32]) -> f32`

**Input 0: `x: &f32`**
```rust
TypeTree(vec![Type {
    offset: -1, size: 8, kind: Pointer,
    child: TypeTree(vec![Type {
        offset: 0, size: 4, kind: Float,  // Single value: use offset 0
        child: TypeTree::new()
    }])
}])
```

**Input 1: `data: &[f32]`**
```rust
TypeTree(vec![Type {
    offset: -1, size: 8, kind: Pointer,
    child: TypeTree(vec![Type {
        offset: -1, size: 4, kind: Float,  // -1 = all elements
        child: TypeTree::new()
    }])
}])
```

**Output: `f32`**
```rust
TypeTree(vec![Type {
    offset: 0, size: 4, kind: Float,  // Single scalar: use offset 0
    child: TypeTree::new()
}])
```

## Why Needed?
- Enzyme can't deduce complex type layouts from LLVM IR
- Prevents slow memory pattern analysis
- Enables correct derivative computation for nested structures
- Tells Enzyme which bytes are differentiable vs metadata

## What Enzyme Does With This Information:

Without TypeTrees:
```llvm
; Enzyme sees generic LLVM IR:
define float @distance(ptr %p1, ptr %p2) {
; Has to guess what these pointers point to
; Slow analysis of all memory operations
; May miss optimization opportunities
}
```

With TypeTrees:
```llvm
define "enzyme_type"="{[-1]:Float@float}" float @distance(
    ptr "enzyme_type"="{[-1]:Pointer, [-1,0]:Float@float}" %p1, 
    ptr "enzyme_type"="{[-1]:Pointer, [-1,0]:Float@float}" %p2
) {
; Enzyme knows exact type layout
; Can generate efficient derivative code directly
}
```

# TypeTrees - Offset and -1 Explained

## Type Structure

```rust
Type {
    offset: isize, // WHERE this type starts
    size: usize,   // HOW BIG this type is
    kind: Kind,    // WHAT KIND of data (Float, Int, Pointer)
    child: TypeTree // WHAT'S INSIDE (for pointers/containers)
}
```

## Offset Values

### Regular Offset (0, 4, 8, etc.)
**Specific byte position within a structure**

```rust
struct Point {
    x: f32, // offset 0, size 4
    y: f32, // offset 4, size 4
    id: i32, // offset 8, size 4
}
```

TypeTree for `&Point` (internal representation):
```rust
TypeTree(vec![
    Type { offset: 0, size: 4, kind: Float },   // x at byte 0
    Type { offset: 4, size: 4, kind: Float },   // y at byte 4
    Type { offset: 8, size: 4, kind: Integer }  // id at byte 8
])
```

Generates LLVM
```llvm
"enzyme_type"="{[-1]:Pointer, [-1,0]:Float@float, [-1,4]:Float@float, [-1,8]:Integer, [-1,9]:Integer, [-1,10]:Integer, [-1,11]:Integer}"
```

### Offset -1 (Special: "Everywhere")
**Means "this pattern repeats for ALL elements"**

#### Example 1: Direct Array `[f32; 100]` (no pointer indirection)
```rust
TypeTree(vec![Type {
    offset: -1, // ALL positions
    size: 4,    // each f32 is 4 bytes
    kind: Float, // every element is float
}])
```

Generates LLVM: `"enzyme_type"="{[-1]:Float@float}"`

#### Example 1b: Array Reference `&[f32; 100]` (with pointer indirection)  
```rust
TypeTree(vec![Type {
    offset: -1, size: 8, kind: Pointer,
    child: TypeTree(vec![Type {
        offset: -1, // ALL array elements
        size: 4,    // each f32 is 4 bytes
        kind: Float, // every element is float
    }])
}])
```

Generates LLVM: `"enzyme_type"="{[-1]:Pointer, [-1,-1]:Float@float}"`

Instead of listing 100 separate Types with offsets `0,4,8,12...396`

#### Example 2: Slice `&[i32]`
```rust
// Pointer to slice data
TypeTree(vec![Type {
    offset: -1, size: 8, kind: Pointer,
    child: TypeTree(vec![Type {
        offset: -1, // ALL slice elements
        size: 4,    // each i32 is 4 bytes
        kind: Integer
    }])
}])
```

Generates LLVM: `"enzyme_type"="{[-1]:Pointer, [-1,-1]:Integer}"`

#### Example 3: Mixed Structure
```rust
struct Container {
    header: i64,        // offset 0
    data: [f32; 1000],  // offset 8, but elements use -1
}
```

```rust
TypeTree(vec![
    Type { offset: 0, size: 8, kind: Integer }, // header
    Type { offset: 8, size: 4000, kind: Pointer,
        child: TypeTree(vec![Type {
            offset: -1, size: 4, kind: Float // ALL array elements
        }])
    }
])
```

## Key Distinction: Single Values vs Arrays

**Single Values** use offset `0` for precision:
- `&f32` has exactly one f32 value at offset 0
- More precise than using -1 ("everywhere")  
- Generates: `{[-1]:Pointer, [-1,0]:Float@float}`

**Arrays** use offset `-1` for efficiency:
- `&[f32; 100]` has the same pattern repeated 100 times
- Using -1 avoids listing 100 separate offsets
- Generates: `{[-1]:Pointer, [-1,-1]:Float@float}`