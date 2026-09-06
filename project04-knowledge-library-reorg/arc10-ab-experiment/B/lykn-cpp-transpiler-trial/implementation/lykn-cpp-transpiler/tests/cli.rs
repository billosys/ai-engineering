use std::process::{Command, Output};

const HAPPY_CPP: &str = include_str!("../examples/generated/happy_path.cpp");
const ARITHMETIC_MIX_CPP: &str = include_str!("../examples/generated/arithmetic_mix.cpp");

#[test]
fn cli_writes_happy_path_cpp_to_stdout() {
    assert_cli_success("fixtures/valid/happy_path.lykn", HAPPY_CPP);
}

#[test]
fn cli_writes_additional_example_cpp_to_stdout() {
    assert_cli_success("fixtures/valid/arithmetic_mix.lykn", ARITHMETIC_MIX_CPP);
}

#[test]
fn cli_reports_transpile_diagnostics_to_stderr() {
    let output = run_cli(&["fixtures/invalid/use_before_binding_in_let.lykn"]);

    assert_eq!(output.status.code(), Some(1));
    assert!(
        output.stdout.is_empty(),
        "expected empty stdout, got: {}",
        String::from_utf8_lossy(&output.stdout),
    );
    assert!(
        String::from_utf8_lossy(&output.stderr).contains("unknown identifier `x`"),
        "expected unknown-identifier diagnostic, got: {}",
        String::from_utf8_lossy(&output.stderr),
    );
}

#[test]
fn cli_reports_usage_diagnostics_to_stderr() {
    let output = run_cli(&[]);

    assert_eq!(output.status.code(), Some(2));
    assert!(
        output.stdout.is_empty(),
        "expected empty stdout, got: {}",
        String::from_utf8_lossy(&output.stdout),
    );
    assert!(
        String::from_utf8_lossy(&output.stderr).contains("usage: lykn-cpp-transpiler <input.lykn>"),
        "expected usage diagnostic, got: {}",
        String::from_utf8_lossy(&output.stderr),
    );
}

fn assert_cli_success(path: &str, expected_stdout: &str) {
    let output = run_cli(&[path]);

    assert!(
        output.status.success(),
        "expected CLI success, stderr: {}",
        String::from_utf8_lossy(&output.stderr),
    );
    assert_eq!(String::from_utf8_lossy(&output.stdout), expected_stdout);
    assert!(
        output.stderr.is_empty(),
        "expected no stderr, got: {}",
        String::from_utf8_lossy(&output.stderr),
    );
}

fn run_cli(args: &[&str]) -> Output {
    Command::new(env!("CARGO_BIN_EXE_lykn-cpp-transpiler"))
        .args(args)
        .output()
        .unwrap_or_else(|error| panic!("failed to run CLI test: {error}"))
}
