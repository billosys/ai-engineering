# Continuous Integration

It is recommended to run Clippy on CI with `-Dwarnings`, so that Clippy lints
prevent CI from passing. To enforce errors on warnings on all `cargo` commands
not just `cargo clippy`, you can set the env var `RUSTFLAGS="-Dwarnings"`.

We recommend to use Clippy from the same toolchain, that you use for compiling
your crate for maximum compatibility. E.g. if your crate is compiled with the
`stable` toolchain, you should also use `stable` Clippy.

> _Note:_ New Clippy lints are first added to the `nightly` toolchain. If you
> want to help with improving Clippy and have CI resources left, please consider
> adding a `nightly` Clippy check to your CI and report problems like false
> positives back to us. With that we can fix bugs early, before they can get to
> stable.

This chapter will give an overview on how to use Clippy on different popular CI
providers.


---

# GitHub Actions

GitHub hosted runners using the latest stable version of Rust have Clippy pre-installed.
It is as simple as running `cargo clippy` to run lints against the codebase.

```yml
on: push
name: Clippy check

# Make sure CI fails on all warnings, including Clippy lints
env:
  RUSTFLAGS: "-Dwarnings"

jobs:
  clippy_check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Run Clippy
        run: cargo clippy --all-targets --all-features
```


---

# GitLab CI

You can add Clippy to GitLab CI by using the latest stable [rust docker image](https://hub.docker.com/_/rust),
as it is shown in the `.gitlab-ci.yml` CI configuration file below,

```yml
# Make sure CI fails on all warnings, including Clippy lints
variables:
  RUSTFLAGS: "-Dwarnings"

clippy_check:
  image: rust:latest
  script:
    - rustup component add clippy
    - cargo clippy --all-targets --all-features
```


---

# Travis CI

You can add Clippy to Travis CI in the same way you use it locally:

```yml
language: rust
rust:
  - stable
  - beta
before_script:
  - rustup component add clippy
script:
  - cargo clippy
  # if you want the build job to fail when encountering warnings, use
  - cargo clippy -- -D warnings
  # in order to also check tests and non-default crate features, use
  - cargo clippy --all-targets --all-features -- -D warnings
  - cargo test
  # etc.
```
