use lykn_cpp_transpiler::{CodegenError, ParseError, TranspileError, transpile_to_cpp};

const MISSING_TOP_LEVEL_CLOSE: &str =
    include_str!("../fixtures/invalid/missing_top_level_close_paren.lykn");
const MISSING_LET_EXPRESSION: &str =
    include_str!("../fixtures/invalid/missing_let_expression.lykn");
const MISSING_PRINT_EXPRESSION: &str =
    include_str!("../fixtures/invalid/missing_print_expression.lykn");
const TRAILING_NON_FORM_TOKEN: &str =
    include_str!("../fixtures/invalid/trailing_non_form_token.lykn");
const UNSUPPORTED_EXPRESSION_OPERATOR: &str =
    include_str!("../fixtures/invalid/unsupported_expression_operator.lykn");
const INTEGER_OVERFLOW: &str = include_str!("../fixtures/invalid/integer_overflow.lykn");
const RESERVED_DOUBLE_UNDERSCORE: &str =
    include_str!("../fixtures/invalid/reserved_double_underscore.lykn");
const RESERVED_UPPER_UNDERSCORE: &str =
    include_str!("../fixtures/invalid/reserved_upper_underscore.lykn");
const USE_BEFORE_BINDING_IN_LET: &str =
    include_str!("../fixtures/invalid/use_before_binding_in_let.lykn");

#[test]
fn diagnostic_matrix_covers_remaining_invalid_boundaries() {
    let cases = [
        MatrixCase {
            name: "missing top-level close parenthesis",
            source: MISSING_TOP_LEVEL_CLOSE,
            expected: ExpectedDiagnostic::UnexpectedEnd { expected: "`)`" },
        },
        MatrixCase {
            name: "missing let expression",
            source: MISSING_LET_EXPRESSION,
            expected: ExpectedDiagnostic::UnexpectedToken {
                expected: "expression",
                found_contains: "`)`",
            },
        },
        MatrixCase {
            name: "missing print expression",
            source: MISSING_PRINT_EXPRESSION,
            expected: ExpectedDiagnostic::UnexpectedToken {
                expected: "expression",
                found_contains: "`)`",
            },
        },
        MatrixCase {
            name: "trailing non-form token after valid statement",
            source: TRAILING_NON_FORM_TOKEN,
            expected: ExpectedDiagnostic::UnexpectedToken {
                expected: "`(`",
                found_contains: "`junk`",
            },
        },
        MatrixCase {
            name: "unsupported expression operator",
            source: UNSUPPORTED_EXPRESSION_OPERATOR,
            expected: ExpectedDiagnostic::UnsupportedForm { form: "%" },
        },
        MatrixCase {
            name: "integer overflow outside i32",
            source: INTEGER_OVERFLOW,
            expected: ExpectedDiagnostic::InvalidInteger {
                value_contains: "2147483648",
            },
        },
        MatrixCase {
            name: "reserved double-underscore identifier",
            source: RESERVED_DOUBLE_UNDERSCORE,
            expected: ExpectedDiagnostic::UnsafeIdentifier {
                name: "__reserved",
                reason: "reserved for C++",
            },
        },
        MatrixCase {
            name: "reserved underscore-uppercase identifier",
            source: RESERVED_UPPER_UNDERSCORE,
            expected: ExpectedDiagnostic::UnsafeIdentifier {
                name: "_Upper",
                reason: "reserved for C++",
            },
        },
        MatrixCase {
            name: "use before binding inside let initializer",
            source: USE_BEFORE_BINDING_IN_LET,
            expected: ExpectedDiagnostic::UnknownIdentifier { name: "x" },
        },
    ];

    for case in cases {
        let error = match transpile_to_cpp(case.source) {
            Ok(output) => panic!(
                "diagnostic matrix case unexpectedly passed: {}\n{output}",
                case.name
            ),
            Err(error) => error,
        };
        case.expected.assert_matches(case.name, error);
    }
}

struct MatrixCase {
    name: &'static str,
    source: &'static str,
    expected: ExpectedDiagnostic,
}

enum ExpectedDiagnostic {
    UnexpectedEnd {
        expected: &'static str,
    },
    UnexpectedToken {
        expected: &'static str,
        found_contains: &'static str,
    },
    UnsupportedForm {
        form: &'static str,
    },
    InvalidInteger {
        value_contains: &'static str,
    },
    UnsafeIdentifier {
        name: &'static str,
        reason: &'static str,
    },
    UnknownIdentifier {
        name: &'static str,
    },
}

impl ExpectedDiagnostic {
    fn assert_matches(&self, case_name: &str, error: TranspileError) {
        match (self, error) {
            (
                Self::UnexpectedEnd { expected },
                TranspileError::Parse(ParseError::UnexpectedEnd { expected: found }),
            ) => assert_eq!(found, *expected, "{case_name}"),
            (
                Self::UnexpectedToken {
                    expected,
                    found_contains,
                },
                TranspileError::Parse(ParseError::UnexpectedToken {
                    found,
                    expected: actual_expected,
                    ..
                }),
            ) => {
                assert_eq!(actual_expected, *expected, "{case_name}");
                assert!(
                    found.contains(found_contains),
                    "{case_name}: expected `{found}` to contain `{found_contains}`",
                );
            }
            (
                Self::UnsupportedForm { form },
                TranspileError::Parse(ParseError::UnsupportedForm {
                    form: actual_form, ..
                }),
            ) => assert_eq!(actual_form, *form, "{case_name}"),
            (
                Self::InvalidInteger { value_contains },
                TranspileError::Parse(ParseError::InvalidInteger { value, .. }),
            ) => assert!(
                value.contains(value_contains),
                "{case_name}: expected `{value}` to contain `{value_contains}`",
            ),
            (
                Self::UnsafeIdentifier { name, reason },
                TranspileError::Parse(ParseError::UnsafeIdentifier {
                    name: actual_name,
                    reason: actual_reason,
                    ..
                }),
            ) => {
                assert_eq!(actual_name, *name, "{case_name}");
                assert_eq!(actual_reason, *reason, "{case_name}");
            }
            (
                Self::UnknownIdentifier { name },
                TranspileError::Codegen(CodegenError::UnknownIdentifier { name: actual_name }),
            ) => assert_eq!(actual_name, *name, "{case_name}"),
            (_, error) => panic!("{case_name}: unexpected diagnostic: {error:?}"),
        }
    }
}
