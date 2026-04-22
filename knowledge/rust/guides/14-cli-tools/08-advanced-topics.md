# CLI Advanced Topics

Patterns for sophisticated command-line applications: signal handling, shell completions, cross-platform behavior, and stdin/stdout composition.

---

## CLI-43: Signal Handling and Graceful Shutdown

**Strength**: SHOULD

**Summary**: Intercept `SIGINT`/`SIGTERM` and drive a cancellation flag so long-running work can release resources before exit. Use `ctrlc` for the Ctrl-C common case, `signal-hook` for broader Unix signals.

```rust
// ❌ BAD: long loop with no interrupt support
fn process_all(items: &[Item]) -> Result<()> {
    for item in items {
        do_expensive_work(item)?; // Ctrl-C kills mid-write; temp files leak
    }
    Ok(())
}

// ✅ GOOD: Shared cancel flag checked in the hot loop
use std::sync::Arc;
use std::sync::atomic::{AtomicBool, Ordering};

fn process_all(items: &[Item]) -> anyhow::Result<()> {
    let cancel = Arc::new(AtomicBool::new(false));

    let flag = Arc::clone(&cancel);
    ctrlc::set_handler(move || {
        // Second Ctrl-C → die immediately
        if flag.swap(true, Ordering::SeqCst) {
            std::process::exit(130); // 128 + SIGINT
        }
        eprintln!("Interrupted — finishing current item, press Ctrl-C again to abort");
    })?;

    for item in items {
        if cancel.load(Ordering::SeqCst) {
            cleanup_partial_state()?;
            anyhow::bail!("cancelled by user");
        }
        do_expensive_work(item)?;
    }
    Ok(())
}
```

```rust
// ✅ GOOD: Channel-based with signal-hook + crossbeam for broader signals
use signal_hook::consts::{SIGINT, SIGTERM};
use signal_hook::iterator::Signals;
use std::thread;

fn install_shutdown(tx: crossbeam_channel::Sender<()>) -> anyhow::Result<()> {
    let mut signals = Signals::new([SIGINT, SIGTERM])?;
    thread::spawn(move || {
        for _ in signals.forever() {
            let _ = tx.send(());
        }
    });
    Ok(())
}

// In the main work loop:
// crossbeam_channel::select! {
//     recv(shutdown) -> _   => { cleanup(); break; }
//     recv(work_queue) -> w => { process(w?); }
// }
```

**Rationale**: The OS default on Ctrl-C is immediate termination. That is fine for `ls`, dangerous for anything that holds a network connection, a lock file, or partial output. The pattern is always the same: install a handler, flip an `AtomicBool` or emit on a channel, check at loop boundaries, and exit immediately on a second interrupt so a stuck cleanup can be escaped. Windows uses Console Handlers rather than POSIX signals; `ctrlc` abstracts the difference, `signal-hook` is Unix-only.

**See also**:
- CLI-48: Piping and stdin/stdout integration
- [External: ctrlc](https://docs.rs/ctrlc), [signal-hook](https://docs.rs/signal-hook)

---

## CLI-44: Shell Completion Generation with `clap_complete`

**Strength**: CONSIDER

**Summary**: Generate bash/zsh/fish/PowerShell/elvish completions from a clap `Command` — either at build time (`generate_to` in `build.rs`), on demand via a hidden subcommand (`generate`), or dynamically through `CompleteEnv`.

```rust
// ✅ GOOD: On-demand generation via a subcommand
use clap::{Command, CommandFactory, Parser};
use clap_complete::{generate, Shell};
use std::io;

#[derive(Parser)]
#[command(name = "my-tool", version)]
struct Cli {
    /// Emit shell completions to stdout and exit.
    #[arg(long, value_enum, value_name = "SHELL")]
    completions: Option<Shell>,
    // ... other args ...
}

fn print_completions<G: clap_complete::Generator>(gen: G, cmd: &mut Command) {
    generate(gen, cmd, cmd.get_name().to_string(), &mut io::stdout());
}

fn main() {
    let cli = Cli::parse();
    if let Some(shell) = cli.completions {
        let mut cmd = Cli::command();
        print_completions(shell, &mut cmd);
        return;
    }
    // ... regular execution ...
}

// Users install with:
//   my-tool --completions bash > /usr/share/bash-completion/completions/my-tool
//   my-tool --completions zsh  > ~/.zfunc/_my-tool
```

```rust
// ✅ GOOD: Ahead-of-time generation in build.rs
// Cargo.toml:
// [build-dependencies]
// clap = { version = "4", features = ["derive"] }
// clap_complete = "4"

// build.rs
use clap_complete::{generate_to, Shell};
use std::env;

include!("src/cli.rs"); // exposes `fn build_cli() -> clap::Command`

fn main() -> std::io::Result<()> {
    let Some(outdir) = env::var_os("OUT_DIR") else { return Ok(()); };
    let mut cmd = build_cli();
    for &shell in &[Shell::Bash, Shell::Zsh, Shell::Fish, Shell::PowerShell] {
        generate_to(shell, &mut cmd, "my-tool", &outdir)?;
    }
    Ok(())
}
```

```rust
// ✅ GOOD: Dynamic completions via CompleteEnv (always in sync with binary)
use clap_complete::CompleteEnv;

fn cli() -> clap::Command { /* ... */ clap::Command::new("my-tool") }

fn main() {
    CompleteEnv::with_factory(cli).complete(); // must be first
    // ... rest of main ...
}
// User adds once to their shell rc:
//   source <(COMPLETE=bash my-tool)
```

```rust
// ✅ GOOD: Give clap enough info to drive path/value completions
use clap::{Arg, ArgAction, ValueHint};

Arg::new("input")
    .value_hint(ValueHint::FilePath)       // shell completes files here
    .action(ArgAction::Set);
```

**Rationale**: Completions turn a CLI from "memorize the flags" into "discoverable". `generate_to` in `build.rs` ships static scripts with your packaged binary — simple to install, can go stale on upgrade. Runtime `generate` behind a `--completions <shell>` flag lets the user produce the script for whichever shell they run today. `CompleteEnv` is the newest approach: completions are computed by running the binary itself, so they never drift from the CLI definition — but every completion request forks a process. Always set `ValueHint` on path/URL/host arguments so the generated scripts suggest files, hosts, and so on.

**See also**:
- CLI-14: Help text and documentation
- CLI-10: Subcommands with enums
- [External: clap_complete](https://docs.rs/clap_complete)

---

## CLI-45: Cross-Platform CLI Behavior

**Strength**: SHOULD

**Summary**: Avoid hard-coded Unix paths, shells, and separators. Use `std::path` join rather than string concatenation, gate OS-specific calls with `#[cfg(...)]`, and prefer crates (`directories`, `ctrlc`) that encapsulate the platform difference.

```rust
use std::path::{Path, PathBuf};

// ❌ BAD: hard-coded POSIX path and separator
fn default_config() -> PathBuf {
    PathBuf::from(format!("{}/.config/my-tool/config.toml", std::env::var("HOME").unwrap()))
}

// ✅ GOOD: join, and let `directories` resolve the platform
fn default_config() -> Option<PathBuf> {
    let dirs = directories::ProjectDirs::from("com", "MyOrg", "MyTool")?;
    Some(dirs.config_dir().join("config.toml"))
}

// ❌ BAD: spawn `sh` unconditionally
fn run_script(script: &str) -> std::io::Result<std::process::Output> {
    std::process::Command::new("sh").arg("-c").arg(script).output()
}

// ✅ GOOD: pick the right shell per platform
fn run_script(script: &str) -> std::io::Result<std::process::Output> {
    #[cfg(unix)]
    let (prog, flag) = ("sh", "-c");
    #[cfg(windows)]
    let (prog, flag) = ("cmd", "/C");
    std::process::Command::new(prog).arg(flag).arg(script).output()
}

// ✅ GOOD: gate permission-fiddling that only exists on Unix
#[cfg(unix)]
fn make_executable(path: &Path) -> std::io::Result<()> {
    use std::os::unix::fs::PermissionsExt;
    let mut perms = std::fs::metadata(path)?.permissions();
    perms.set_mode(perms.mode() | 0o111);
    std::fs::set_permissions(path, perms)
}

#[cfg(not(unix))]
fn make_executable(_path: &Path) -> std::io::Result<()> { Ok(()) }
```

**Rationale**: Users do not pick the platform you happened to develop on. Path separators differ (`/` vs `\`), `HOME` is `%USERPROFILE%` on Windows, file modes do not exist on Windows, and `sh` may not either. `PathBuf::join`, `cfg` attributes, and platform-aware crates (`directories`, `dunce`, `which`) turn each of these from a runtime bug report into a compile-time selection. Do this from day one — retrofitting cross-platform support later means auditing every `format!` that constructed a path.

**See also**:
- CLI-30: Configuration file locations
- CLI-33: XDG Base Directory specification
- CLI-41: Cross-compilation considerations

---

## CLI-46: Piping, Stdin, and Terminal Detection

**Strength**: SHOULD

**Summary**: Detect whether stdin/stdout are terminals or pipes and adapt. Accept `-` as a pseudo-path for stdin, emit plain machine-readable output when stdout is not a tty, and skip interactive prompts when stdin is not a tty.

```rust
use std::io::{self, BufRead, IsTerminal, Read, Write};
use std::fs::File;
use std::path::{Path, PathBuf};

// ✅ GOOD: `-` or no argument means stdin
fn open_input(path: Option<&Path>) -> io::Result<Box<dyn BufRead>> {
    match path {
        None => Ok(Box::new(io::stdin().lock())),
        Some(p) if p.as_os_str() == "-" => Ok(Box::new(io::stdin().lock())),
        Some(p) => Ok(Box::new(io::BufReader::new(File::open(p)?))),
    }
}

// ✅ GOOD: warn if stdin is interactive but we expected piped data
fn read_piped_input() -> io::Result<String> {
    if io::stdin().is_terminal() {
        eprintln!("note: reading from stdin — pipe data in or pass a file path");
    }
    let mut buf = String::new();
    io::stdin().lock().read_to_string(&mut buf)?;
    Ok(buf)
}

// ✅ GOOD: human table on a tty, line-delimited JSON on a pipe
fn emit(rows: &[Row]) -> io::Result<()> {
    let mut out = io::stdout().lock();
    if out.is_terminal() {
        for r in rows { writeln!(out, "{:<20} {:>8}", r.name, r.count)?; }
    } else {
        for r in rows { serde_json::to_writer(&mut out, r)?; writeln!(out)?; }
    }
    Ok(())
}

// ✅ GOOD: handle EPIPE silently when downstream closes the pipe
fn write_forever(data: &[u8]) {
    let mut out = io::stdout().lock();
    if let Err(e) = out.write_all(data) {
        if e.kind() == io::ErrorKind::BrokenPipe {
            std::process::exit(0); // `... | head` closed us — not an error
        }
    }
}
```

**Rationale**: Unix composition depends on this. A tool that dumps ANSI colors into a pipe corrupts the downstream parser. A tool that blocks on an interactive prompt inside a cron job hangs forever. A tool that panics on `BrokenPipe` when `my-tool | head -1` is run looks buggy. `std::io::IsTerminal` (stable since Rust 1.70) is the right detection primitive, `-` is the decades-old convention for "use stdin instead of a file", and `ErrorKind::BrokenPipe` should be treated as a clean exit, not an error.

**See also**:
- CLI-21: Human vs machine-readable output
- CLI-25: Confirmation prompts
- CLI-27: Stdout vs stderr usage

---

## Best Practices Summary

| Pattern | Strength | Key Takeaway |
|---------|----------|--------------|
| CLI-43 | SHOULD | Install a signal handler, flip an AtomicBool, check it in the hot loop |
| CLI-44 | CONSIDER | Ship completions via `clap_complete` — build-time, on-demand, or `CompleteEnv` |
| CLI-45 | SHOULD | `PathBuf::join` + `cfg` + platform crates; no hard-coded `/` or `HOME` |
| CLI-46 | SHOULD | `is_terminal()` drives format choice; accept `-` for stdin; treat `BrokenPipe` as clean exit |

## Related Guidelines

- CLI-21, CLI-26, CLI-27: Output discipline (in 04-output-and-ux.md)
- CLI-30, CLI-33: Platform-appropriate directory layout (in 05-configuration.md)
- CLI-41: Cross-compilation and release matrix (in 07-distribution.md)

## External References

- [ctrlc](https://docs.rs/ctrlc) — portable Ctrl-C handler
- [signal-hook](https://docs.rs/signal-hook) — full Unix signal support
- [clap_complete](https://docs.rs/clap_complete) — shell completion generation
- [directories](https://docs.rs/directories) — platform-native config/data/cache paths
- [`std::io::IsTerminal`](https://doc.rust-lang.org/std/io/trait.IsTerminal.html)
