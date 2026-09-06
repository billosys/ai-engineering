use std::process::Command;

use lykn_cpp_transpiler::{CodegenError, ParseError, TranspileError, transpile_to_cpp};

const HAPPY_SOURCE: &str = include_str!("../fixtures/valid/happy_path.lykn");
const HAPPY_CPP: &str = include_str!("../examples/generated/happy_path.cpp");
const ARITHMETIC_MIX_SOURCE: &str = include_str!("../fixtures/valid/arithmetic_mix.lykn");
const ARITHMETIC_MIX_CPP: &str = include_str!("../examples/generated/arithmetic_mix.cpp");
const MALFORMED_TOP_LEVEL: &str = include_str!("../fixtures/invalid/malformed_top_level.lykn");
const MALFORMED_EXPRESSION: &str = include_str!("../fixtures/invalid/malformed_expression.lykn");
const BINARY_TOO_FEW: &str = include_str!("../fixtures/invalid/binary_too_few_operands.lykn");
const BINARY_TOO_MANY: &str = include_str!("../fixtures/invalid/binary_too_many_operands.lykn");
const UNSUPPORTED_SOURCE: &str = include_str!("../fixtures/invalid/unsupported_form.lykn");
const DUPLICATE_BINDING: &str = include_str!("../fixtures/invalid/duplicate_binding.lykn");
const DIVISION_BY_ZERO: &str = include_str!("../fixtures/invalid/division_by_zero.lykn");
const CPP_RESERVED_WORD: &str = include_str!("../fixtures/invalid/cpp_reserved_word.lykn");
const HYPHENATED_IDENTIFIER: &str = include_str!("../fixtures/invalid/hyphenated_identifier.lykn");

#[test]
fn transpiles_valid_fixture_to_expected_cpp() {
    let generated = transpile_to_cpp(HAPPY_SOURCE);

    assert_eq!(generated.as_deref(), Ok(HAPPY_CPP));
}

#[test]
fn transpiles_additional_valid_fixture_to_expected_cpp() {
    let generated = transpile_to_cpp(ARITHMETIC_MIX_SOURCE);

    assert_eq!(generated.as_deref(), Ok(ARITHMETIC_MIX_CPP));
}

#[test]
fn malformed_top_level_returns_structured_diagnostic() {
    let error = transpile_to_cpp(MALFORMED_TOP_LEVEL);

    assert!(matches!(
        error,
        Err(TranspileError::Parse(ParseError::UnexpectedToken {
            expected: "`(`",
            ..
        }))
    ));
}

#[test]
fn malformed_expression_returns_structured_diagnostic() {
    let error = transpile_to_cpp(MALFORMED_EXPRESSION);

    assert!(matches!(
        error,
        Err(TranspileError::Parse(ParseError::UnexpectedToken {
            expected: "binary operator",
            ..
        }))
    ));
}

#[test]
fn binary_operator_rejects_too_few_operands() {
    let error = transpile_to_cpp(BINARY_TOO_FEW);

    assert!(matches!(
        error,
        Err(TranspileError::Parse(ParseError::BinaryOperatorArity {
            operator,
            expected: 2,
            found: 1,
            ..
        })) if operator == "+"
    ));
}

#[test]
fn binary_operator_rejects_too_many_operands() {
    let error = transpile_to_cpp(BINARY_TOO_MANY);

    assert!(matches!(
        error,
        Err(TranspileError::Parse(ParseError::BinaryOperatorArity {
            operator,
            expected: 2,
            found: 3,
            ..
        })) if operator == "+"
    ));
}

#[test]
fn unsupported_input_returns_structured_diagnostic() {
    let error = transpile_to_cpp(UNSUPPORTED_SOURCE);

    assert!(matches!(
        error,
        Err(TranspileError::Parse(ParseError::UnsupportedForm {
            form,
            ..
        })) if form == "wat"
    ));
}

#[test]
fn unknown_identifier_returns_codegen_diagnostic() {
    let error = transpile_to_cpp("(print missing)\n");

    assert!(matches!(
        error,
        Err(TranspileError::Codegen(CodegenError::UnknownIdentifier {
            name,
        })) if name == "missing"
    ));
}

#[test]
fn duplicate_binding_returns_codegen_diagnostic() {
    let error = transpile_to_cpp(DUPLICATE_BINDING);

    assert!(matches!(
        error,
        Err(TranspileError::Codegen(CodegenError::DuplicateBinding {
            name,
        })) if name == "x"
    ));
}

#[test]
fn direct_literal_division_by_zero_returns_codegen_diagnostic() {
    let error = transpile_to_cpp(DIVISION_BY_ZERO);

    assert!(matches!(
        error,
        Err(TranspileError::Codegen(CodegenError::DivisionByZero))
    ));
}

#[test]
fn cpp_reserved_word_identifier_is_rejected() {
    let error = transpile_to_cpp(CPP_RESERVED_WORD);

    assert!(matches!(
        error,
        Err(TranspileError::Parse(ParseError::UnsafeIdentifier {
            name,
            reason: "reserved for C++",
            ..
        })) if name == "class"
    ));
}

#[test]
fn hyphenated_identifier_is_rejected() {
    let error = transpile_to_cpp(HYPHENATED_IDENTIFIER);

    assert!(matches!(
        error,
        Err(TranspileError::Parse(ParseError::InvalidIdentifier {
            name,
            ..
        })) if name == "bad-name"
    ));
}

#[test]
fn cli_smoke_writes_cpp_to_stdout() {
    let binary = env!("CARGO_BIN_EXE_lykn-cpp-transpiler");
    let output = Command::new(binary)
        .arg("fixtures/valid/happy_path.lykn")
        .output()
        .unwrap_or_else(|error| panic!("failed to run CLI smoke test: {error}"));

    assert!(
        output.status.success(),
        "expected CLI success, stderr: {}",
        String::from_utf8_lossy(&output.stderr),
    );
    assert_eq!(String::from_utf8_lossy(&output.stdout), HAPPY_CPP);
    assert!(
        output.stderr.is_empty(),
        "expected no stderr, got: {}",
        String::from_utf8_lossy(&output.stderr),
    );
}

#[test]
fn cli_invalid_input_keeps_stdout_and_stderr_separate() {
    let binary = env!("CARGO_BIN_EXE_lykn-cpp-transpiler");
    let output = Command::new(binary)
        .arg("fixtures/invalid/division_by_zero.lykn")
        .output()
        .unwrap_or_else(|error| panic!("failed to run invalid CLI smoke test: {error}"));

    assert!(!output.status.success(), "expected CLI failure");
    assert!(
        output.stdout.is_empty(),
        "expected empty stdout, got: {}",
        String::from_utf8_lossy(&output.stdout),
    );
    assert!(
        String::from_utf8_lossy(&output.stderr)
            .contains("division by direct literal zero is not supported"),
        "expected division-by-zero diagnostic, got: {}",
        String::from_utf8_lossy(&output.stderr),
    );
}
