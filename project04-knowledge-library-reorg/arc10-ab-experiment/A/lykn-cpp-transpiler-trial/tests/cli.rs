use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::sync::atomic::{AtomicU64, Ordering};

const PRINT_LITERAL_CPP: &str =
    "#include <iostream>\n\nint main() {\n    std::cout << 42 << \"\\n\";\n    return 0;\n}\n";
const LET_LITERAL_CPP: &str = "#include <iostream>\n\nint main() {\n    int x{40};\n    std::cout << x << \"\\n\";\n    std::cout << 42 << \"\\n\";\n    return 0;\n}\n";
const ARITHMETIC_CPP: &str = "#include <iostream>\n\nint main() {\n    int x{40};\n    int y{(x + 2)};\n    std::cout << (y * 2) << \"\\n\";\n    return 0;\n}\n";
const FULL_TINY_SUBSET_CPP: &str = "#include <iostream>\n\nint main() {\n    int a{20};\n    int b{(a + 2)};\n    int c{(b - 5)};\n    int d{(c * (8 / 4))};\n    std::cout << (d + 1) << \"\\n\";\n    std::cout << ((b * c) / 3) << \"\\n\";\n    return 0;\n}\n";

static TEMP_FILE_COUNTER: AtomicU64 = AtomicU64::new(0);

#[test]
fn cli_valid_fixtures() {
    for (source, expected) in [
        ("print_literal.lyk", "print_literal.cpp"),
        ("let_literal_order.lyk", "let_literal_order.cpp"),
        ("arithmetic.lyk", "arithmetic.cpp"),
        ("full_tiny_subset.lyk", "full_tiny_subset.cpp"),
    ] {
        let source_path = fixture_path(["tests", "fixtures", "valid", source]);
        let expected_stdout =
            fs::read_to_string(fixture_path(["tests", "fixtures", "expected", expected]))
                .expect("expected C++ fixture should be readable");

        let output = run_transpiler(&source_path);

        assert!(
            output.status.success(),
            "expected {source} to succeed, stderr was: {}",
            String::from_utf8_lossy(&output.stderr)
        );
        assert_eq!(
            String::from_utf8(output.stdout).expect("stdout is UTF-8"),
            expected_stdout
        );
        assert!(output.stderr.is_empty());
    }
}

#[test]
fn cli_invalid_fixtures() {
    for (source, expected_stderr) in [
        (
            "unsupported_form.lyk",
            "error: unsupported form `bind` at byte 1",
        ),
        (
            "duplicate_binding.lyk",
            "error: duplicate binding `x` at byte 15",
        ),
        (
            "unsupported_operator.lyk",
            "error: unsupported arithmetic operator `%` at byte 8",
        ),
        (
            "extra_operand.lyk",
            "error: extra operand for arithmetic operator `+` at byte 8",
        ),
        (
            "invalid_identifier.lyk",
            "error: invalid identifier `bad-name` at byte 10",
        ),
        (
            "unknown_identifier.lyk",
            "error: unknown identifier `missing` at byte 7",
        ),
        (
            "before_bound_identifier.lyk",
            "error: unknown identifier `x` at byte 10",
        ),
        (
            "nested_missing_close.lyk",
            "error: unexpected end of input; expected `)`",
        ),
    ] {
        let source_path = fixture_path(["tests", "fixtures", "invalid", source]);
        let output = run_transpiler(&source_path);

        assert!(!output.status.success(), "expected {source} to fail");
        assert!(output.stdout.is_empty());

        let stderr = String::from_utf8(output.stderr).expect("stderr is UTF-8");
        assert!(
            stderr.contains(expected_stderr),
            "expected {source} stderr to contain {expected_stderr:?}, got {stderr:?}"
        );
    }
}

#[test]
fn generated_cpp_examples_compile() {
    let Some(compiler) = first_available_cpp_compiler() else {
        eprintln!("skipping C++17 compile gate; no compiler was detected");
        return;
    };

    for example in ["arithmetic.cpp", "let_literal.cpp", "print_literal.cpp"] {
        let source_path = fixture_path(["examples", example]);
        let executable_path = temp_executable_path(example);

        let output = Command::new(&compiler)
            .args(["-std=c++17", "-Wall", "-Wextra", "-pedantic"])
            .arg(&source_path)
            .arg("-o")
            .arg(&executable_path)
            .output()
            .expect("C++ compiler process should run");

        fs::remove_file(&executable_path).ok();

        assert!(
            output.status.success(),
            "expected {example} to compile with {compiler}, stderr was: {}",
            String::from_utf8_lossy(&output.stderr)
        );
        assert!(output.stdout.is_empty());
    }
}

#[test]
fn generated_cpp_example_runs() {
    let Some(compiler) = first_available_cpp_compiler() else {
        eprintln!("skipping C++17 run gate; no compiler was detected");
        return;
    };

    let source_path = fixture_path(["examples", "arithmetic.cpp"]);
    let executable_path = temp_executable_path("arithmetic.cpp");

    let compile_output = Command::new(&compiler)
        .args(["-std=c++17", "-Wall", "-Wextra", "-pedantic"])
        .arg(&source_path)
        .arg("-o")
        .arg(&executable_path)
        .output()
        .expect("C++ compiler process should run");

    assert!(
        compile_output.status.success(),
        "expected arithmetic.cpp to compile with {compiler}, stderr was: {}",
        String::from_utf8_lossy(&compile_output.stderr)
    );

    let run_output = Command::new(&executable_path)
        .output()
        .expect("compiled C++ example should run");

    fs::remove_file(&executable_path).ok();

    assert!(
        run_output.status.success(),
        "expected compiled arithmetic example to exit successfully"
    );
    assert_eq!(
        String::from_utf8(run_output.stdout).expect("stdout is UTF-8"),
        "35\n124\n"
    );
    assert!(run_output.stderr.is_empty());
}

#[test]
fn cli_print_literal_writes_cpp_to_stdout() {
    let source_path = write_temp_source("cli_print_literal_writes_cpp_to_stdout", "(print 42)");

    let output = Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(&source_path)
        .output()
        .expect("CLI process should run");

    fs::remove_file(&source_path).expect("temporary source file should be removable");

    assert!(
        output.status.success(),
        "expected success, stderr was: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    assert_eq!(
        String::from_utf8(output.stdout).expect("stdout is UTF-8"),
        PRINT_LITERAL_CPP
    );
    assert!(output.stderr.is_empty());
}

#[test]
fn unsupported_input_writes_diagnostic_to_stderr() {
    let source_path = write_temp_source(
        "unsupported_input_writes_diagnostic_to_stderr",
        "(bind x 42)",
    );

    let output = Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(&source_path)
        .output()
        .expect("CLI process should run");

    fs::remove_file(&source_path).expect("temporary source file should be removable");

    assert!(!output.status.success());
    assert!(output.stdout.is_empty());

    let stderr = String::from_utf8(output.stderr).expect("stderr is UTF-8");
    assert!(stderr.contains("error: unsupported form `bind`"));
}

#[test]
fn cli_let_literal_writes_cpp_to_stdout() {
    let source_path = write_temp_source(
        "cli_let_literal_writes_cpp_to_stdout",
        "(let x 40)\n(print x)\n(print 42)",
    );

    let output = Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(&source_path)
        .output()
        .expect("CLI process should run");

    fs::remove_file(&source_path).expect("temporary source file should be removable");

    assert!(
        output.status.success(),
        "expected success, stderr was: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    assert_eq!(
        String::from_utf8(output.stdout).expect("stdout is UTF-8"),
        LET_LITERAL_CPP
    );
    assert!(output.stderr.is_empty());
}

#[test]
fn cli_semantic_error_exits_nonzero_without_stdout() {
    let source_path = write_temp_source(
        "cli_semantic_error_exits_nonzero_without_stdout",
        "(let x 1)\n(let x 2)",
    );

    let output = Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(&source_path)
        .output()
        .expect("CLI process should run");

    fs::remove_file(&source_path).expect("temporary source file should be removable");

    assert!(!output.status.success());
    assert!(output.stdout.is_empty());

    let stderr = String::from_utf8(output.stderr).expect("stderr is UTF-8");
    assert!(stderr.contains("error: duplicate binding `x`"));
}

#[test]
fn cli_arithmetic_expression_writes_cpp_to_stdout() {
    let source_path = write_temp_source(
        "cli_arithmetic_expression_writes_cpp_to_stdout",
        "(let x 40)\n(let y (+ x 2))\n(print (* y 2))",
    );

    let output = Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(&source_path)
        .output()
        .expect("CLI process should run");

    fs::remove_file(&source_path).expect("temporary source file should be removable");

    assert!(
        output.status.success(),
        "expected success, stderr was: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    assert_eq!(
        String::from_utf8(output.stdout).expect("stdout is UTF-8"),
        ARITHMETIC_CPP
    );
    assert!(output.stderr.is_empty());
}

#[test]
fn cli_full_tiny_subset_program_writes_cpp_to_stdout() {
    let source_path = write_temp_source(
        "cli_full_tiny_subset_program_writes_cpp_to_stdout",
        "(let a 20)\n\
         (let b (+ a 2))\n\
         (let c (- b 5))\n\
         (let d (* c (/ 8 4)))\n\
         (print (+ d 1))\n\
         (print (/ (* b c) 3))",
    );

    let output = Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(&source_path)
        .output()
        .expect("CLI process should run");

    fs::remove_file(&source_path).expect("temporary source file should be removable");

    assert!(
        output.status.success(),
        "expected success, stderr was: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    assert_eq!(
        String::from_utf8(output.stdout).expect("stdout is UTF-8"),
        FULL_TINY_SUBSET_CPP
    );
    assert!(output.stderr.is_empty());
}

#[test]
fn cli_expression_error_exits_nonzero_without_stdout() {
    assert_cli_error(
        "cli_expression_error_unsupported_operator",
        "(print (% 1 2))",
        "error: unsupported arithmetic operator `%`",
    );
    assert_cli_error(
        "cli_expression_error_extra_print_operand",
        "(print 1 2)",
        "error: expected `)` at byte 9, found `2`",
    );
}

fn assert_cli_error(test_name: &str, source: &str, expected_stderr: &str) {
    let source_path = write_temp_source(test_name, source);

    let output = Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(&source_path)
        .output()
        .expect("CLI process should run");

    fs::remove_file(&source_path).expect("temporary source file should be removable");

    assert!(!output.status.success());
    assert!(output.stdout.is_empty());

    let stderr = String::from_utf8(output.stderr).expect("stderr is UTF-8");
    assert!(stderr.contains(expected_stderr), "stderr was: {stderr}");
}

fn run_transpiler(source_path: &Path) -> std::process::Output {
    Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler-trial"))
        .arg(source_path)
        .output()
        .expect("CLI process should run")
}

fn fixture_path<const N: usize>(segments: [&str; N]) -> PathBuf {
    let mut path = PathBuf::from(env!("CARGO_MANIFEST_DIR"));

    for segment in segments {
        path.push(segment);
    }

    path
}

fn first_available_cpp_compiler() -> Option<String> {
    let cxx = std::env::var("CXX").ok().filter(|value| !value.is_empty());
    cxx.into_iter()
        .chain(["c++", "clang++", "g++"].map(str::to_string))
        .find(|candidate| compiler_works(candidate))
}

fn compiler_works(candidate: &str) -> bool {
    Command::new(candidate)
        .arg("--version")
        .output()
        .is_ok_and(|output| output.status.success())
}

fn temp_executable_path(example: &str) -> PathBuf {
    let sequence = TEMP_FILE_COUNTER.fetch_add(1, Ordering::Relaxed);
    std::env::temp_dir().join(format!(
        "lykn_cpp_transpiler_trial_{}_{}_{}",
        std::process::id(),
        example.replace('.', "_"),
        sequence
    ))
}

fn write_temp_source(test_name: &str, contents: &str) -> std::path::PathBuf {
    let sequence = TEMP_FILE_COUNTER.fetch_add(1, Ordering::Relaxed);
    let path = std::env::temp_dir().join(format!(
        "lykn_cpp_transpiler_trial_{}_{}_{}.lyk",
        std::process::id(),
        test_name,
        sequence
    ));

    fs::write(&path, contents).expect("temporary source file should be writable");
    path
}
