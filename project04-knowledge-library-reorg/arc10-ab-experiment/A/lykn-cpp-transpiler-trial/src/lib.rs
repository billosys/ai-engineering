mod ast;
mod codegen;
mod error;
mod parser;

use std::fs;
use std::path::Path;

pub use error::TranspileError;

/// Transpile one tiny Lykn-inspired source program to C++17.
///
/// # Errors
///
/// Returns [`TranspileError`] when the source is empty, malformed, or violates
/// this slice's integer, identifier, or binding-order policies.
pub fn transpile(source: &str) -> Result<String, TranspileError> {
    let program = parser::parse(source)?;
    Ok(codegen::generate(&program))
}

/// Read a source file and transpile it to C++17.
///
/// # Errors
///
/// Returns [`CliError::Io`] when the source file cannot be read and
/// [`CliError::Transpile`] when parsing or generation fails.
pub fn transpile_file(path: impl AsRef<Path>) -> Result<String, CliError> {
    let source = fs::read_to_string(path).map_err(CliError::Io)?;
    transpile(&source).map_err(CliError::Transpile)
}

#[derive(Debug)]
pub enum CliError {
    Io(std::io::Error),
    Transpile(TranspileError),
}

impl std::fmt::Display for CliError {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Io(error) => write!(formatter, "could not read source file: {error}"),
            Self::Transpile(error) => write!(formatter, "{error}"),
        }
    }
}

impl std::error::Error for CliError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            Self::Io(error) => Some(error),
            Self::Transpile(error) => Some(error),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const PRINT_LITERAL_CPP: &str =
        "#include <iostream>\n\nint main() {\n    std::cout << 42 << \"\\n\";\n    return 0;\n}\n";
    const LET_LITERAL_CPP: &str = "#include <iostream>\n\nint main() {\n    int x{40};\n    std::cout << x << \"\\n\";\n    std::cout << 42 << \"\\n\";\n    return 0;\n}\n";
    const ARITHMETIC_PRINT_CPP: &str = "#include <iostream>\n\nint main() {\n    std::cout << ((1 + 2) * 3) << \"\\n\";\n    return 0;\n}\n";
    const LET_ARITHMETIC_CPP: &str = "#include <iostream>\n\nint main() {\n    int x{40};\n    int y{(x + 2)};\n    std::cout << y << \"\\n\";\n    return 0;\n}\n";
    const ARITHMETIC_ORDER_CPP: &str = "#include <iostream>\n\nint main() {\n    int x{40};\n    int y{(x + 2)};\n    std::cout << (y * 2) << \"\\n\";\n    std::cout << (y / 4) << \"\\n\";\n    return 0;\n}\n";
    const FULL_TINY_SUBSET_CPP: &str = "#include <iostream>\n\nint main() {\n    int a{20};\n    int b{(a + 2)};\n    int c{(b - 5)};\n    int d{(c * (8 / 4))};\n    std::cout << (d + 1) << \"\\n\";\n    std::cout << ((b * c) / 3) << \"\\n\";\n    return 0;\n}\n";

    #[test]
    fn print_literal_transpiles_to_deterministic_cpp() {
        let output = transpile("(print 42)").expect("print literal should transpile");

        assert_eq!(output, PRINT_LITERAL_CPP);
    }

    #[test]
    fn let_literal_program_transpiles() {
        let output =
            transpile("(let x 40)\n(print x)\n(print 42)").expect("let program should transpile");

        assert_eq!(output, LET_LITERAL_CPP);
    }

    #[test]
    fn let_literal_codegen_order_preserves_source_order() {
        let output =
            transpile("(let x 40)\n(print x)\n(print 42)").expect("let program should transpile");

        let let_position = output.find("int x{40};").expect("let output should exist");
        let identifier_print_position = output
            .find("std::cout << x << \"\\n\";")
            .expect("identifier print should exist");
        let literal_print_position = output
            .find("std::cout << 42 << \"\\n\";")
            .expect("literal print should exist");
        let return_position = output.find("return 0;").expect("return should exist");

        assert!(let_position < identifier_print_position);
        assert!(identifier_print_position < literal_print_position);
        assert!(literal_print_position < return_position);
        assert_eq!(output, LET_LITERAL_CPP);
    }

    #[test]
    fn arithmetic_print_expression() {
        let output =
            transpile("(print (* (+ 1 2) 3))").expect("nested arithmetic should transpile");

        assert_eq!(output, ARITHMETIC_PRINT_CPP);
    }

    #[test]
    fn let_arithmetic_expression() {
        let output = transpile("(let x 40)\n(let y (+ x 2))\n(print y)")
            .expect("let expression should transpile");

        assert_eq!(output, LET_ARITHMETIC_CPP);
    }

    #[test]
    fn arithmetic_codegen_order() {
        let output = transpile("(let x 40)\n(let y (+ x 2))\n(print (* y 2))\n(print (/ y 4))")
            .expect("arithmetic program should transpile");

        assert_eq!(output, ARITHMETIC_ORDER_CPP);

        let x_position = output.find("int x{40};").expect("x binding should exist");
        let y_position = output
            .find("int y{(x + 2)};")
            .expect("y binding should exist");
        let multiply_position = output
            .find("std::cout << (y * 2) << \"\\n\";")
            .expect("multiply print should exist");
        let divide_position = output
            .find("std::cout << (y / 4) << \"\\n\";")
            .expect("divide print should exist");

        assert!(x_position < y_position);
        assert!(y_position < multiply_position);
        assert!(multiply_position < divide_position);
    }

    #[test]
    fn full_tiny_subset_program() {
        let output = transpile(
            "(let a 20)\n\
             (let b (+ a 2))\n\
             (let c (- b 5))\n\
             (let d (* c (/ 8 4)))\n\
             (print (+ d 1))\n\
             (print (/ (* b c) 3))",
        )
        .expect("full tiny subset program should transpile");

        assert_eq!(output, FULL_TINY_SUBSET_CPP);
    }

    #[test]
    fn integer_range_rejects_overflow_and_negative_literals() {
        let overflow =
            transpile("(let x 2147483648)").expect_err("overflowing i32 should be rejected");
        let negative = transpile("(print -1)").expect_err("negative literal is out of scope");

        assert_eq!(
            overflow,
            TranspileError::InvalidInteger {
                literal: "2147483648".to_string(),
                position: 7,
            }
        );
        assert_eq!(
            negative,
            TranspileError::InvalidInteger {
                literal: "-1".to_string(),
                position: 7,
            }
        );
    }

    #[test]
    fn identifier_policy_rejects_non_cpp_safe_names() {
        let error =
            transpile("(let bad-name 1)").expect_err("lisp-case conversion is out of scope");

        assert_eq!(
            error,
            TranspileError::InvalidIdentifier {
                name: "bad-name".to_string(),
                position: 5,
            }
        );
    }

    #[test]
    fn duplicate_binding_is_rejected() {
        let error = transpile("(let x 1)\n(let x 2)").expect_err("duplicate let should fail");

        assert_eq!(
            error,
            TranspileError::DuplicateBinding {
                name: "x".to_string(),
                first_position: 5,
                duplicate_position: 15,
            }
        );
    }

    #[test]
    fn unknown_identifier_is_rejected() {
        let unknown = transpile("(print missing)").expect_err("unknown identifier should fail");
        let before_bound = transpile("(print x)\n(let x 1)")
            .expect_err("identifier printed before binding should fail");

        assert_eq!(
            unknown,
            TranspileError::UnknownIdentifier {
                name: "missing".to_string(),
                position: 7,
            }
        );
        assert_eq!(
            before_bound,
            TranspileError::UnknownIdentifier {
                name: "x".to_string(),
                position: 7,
            }
        );
    }

    #[test]
    fn unknown_identifier_in_expression() {
        let unknown =
            transpile("(print (+ missing 1))").expect_err("nested unknown identifier should fail");
        let before_bound = transpile("(let y (+ x 2))\n(let x 1)")
            .expect_err("identifier in let initializer should be bound first");

        assert_eq!(
            unknown,
            TranspileError::UnknownIdentifier {
                name: "missing".to_string(),
                position: 10,
            }
        );
        assert_eq!(
            before_bound,
            TranspileError::UnknownIdentifier {
                name: "x".to_string(),
                position: 10,
            }
        );
    }

    #[test]
    fn malformed_expression_reports_structured_error() {
        let unsupported =
            transpile("(print (% 1 2))").expect_err("unsupported operator should fail");
        let missing = transpile("(print (+ 1))").expect_err("missing operand should fail");
        let extra = transpile("(print (+ 1 2 3))").expect_err("extra operand should fail");

        assert_eq!(
            unsupported,
            TranspileError::UnsupportedOperator {
                operator: "%".to_string(),
                position: 8,
            }
        );
        assert_eq!(
            missing,
            TranspileError::MissingOperand {
                operator: "+".to_string(),
                operator_position: 8,
                operand_index: 2,
            }
        );
        assert_eq!(
            extra,
            TranspileError::ExtraOperand {
                operator: "+".to_string(),
                operator_position: 8,
                extra_position: 14,
            }
        );
    }

    #[test]
    fn empty_expression_reports_structured_error() {
        let error = transpile("(print ())").expect_err("empty expression should fail");

        assert_eq!(
            error,
            TranspileError::UnexpectedToken {
                expected: "arithmetic operator",
                found: ")".to_string(),
                position: 8,
            }
        );
    }

    #[test]
    fn arithmetic_arity_matrix() {
        for (operator, source) in [
            ("+", "(print (+ 1))"),
            ("-", "(print (- 1))"),
            ("*", "(print (* 1))"),
            ("/", "(print (/ 1))"),
        ] {
            assert_eq!(
                transpile(source).expect_err("missing operand should fail"),
                TranspileError::MissingOperand {
                    operator: operator.to_string(),
                    operator_position: 8,
                    operand_index: 2,
                }
            );
        }

        for (operator, source) in [
            ("+", "(print (+ 1 2 3))"),
            ("-", "(print (- 1 2 3))"),
            ("*", "(print (* 1 2 3))"),
            ("/", "(print (/ 1 2 3))"),
        ] {
            assert_eq!(
                transpile(source).expect_err("extra operand should fail"),
                TranspileError::ExtraOperand {
                    operator: operator.to_string(),
                    operator_position: 8,
                    extra_position: 14,
                }
            );
        }
    }

    #[test]
    fn nested_expression_unexpected_end() {
        let error = transpile("(print (* (+ 1 2) 3)").expect_err("missing print close should fail");

        assert_eq!(error, TranspileError::UnexpectedEnd { expected: "`)`" });
    }

    #[test]
    fn unsupported_operator_matrix() {
        for (operator, position, source) in
            [("%", 8, "(print (% 1 2))"), ("mod", 8, "(print (mod 4 2))")]
        {
            assert_eq!(
                transpile(source).expect_err("unsupported operator should fail"),
                TranspileError::UnsupportedOperator {
                    operator: operator.to_string(),
                    position,
                }
            );
        }
    }

    #[test]
    fn statement_extra_operand_diagnostics() {
        let print_error = transpile("(print 1 2)").expect_err("extra print operand should fail");
        let let_error = transpile("(let x 1 2)").expect_err("extra let operand should fail");

        assert_eq!(
            print_error,
            TranspileError::UnexpectedToken {
                expected: "`)`",
                found: "2".to_string(),
                position: 9,
            }
        );
        assert_eq!(
            let_error,
            TranspileError::UnexpectedToken {
                expected: "`)`",
                found: "2".to_string(),
                position: 9,
            }
        );
    }

    #[test]
    fn invalid_identifier_in_expression() {
        let error =
            transpile("(print (+ bad-name 1))").expect_err("invalid nested identifier should fail");

        assert_eq!(
            error,
            TranspileError::InvalidIdentifier {
                name: "bad-name".to_string(),
                position: 10,
            }
        );
    }

    #[test]
    fn subtraction_expression_without_negative_literal() {
        let output = transpile("(print (- 1 2))").expect("binary subtraction should transpile");
        let negative = transpile("(print -1)").expect_err("negative literal remains out of scope");

        assert!(output.contains("std::cout << (1 - 2) << \"\\n\";"));
        assert_eq!(
            negative,
            TranspileError::InvalidInteger {
                literal: "-1".to_string(),
                position: 7,
            }
        );
    }

    #[test]
    fn unsupported_input_reports_structured_error() {
        let error = transpile("(bind x 42)").expect_err("real Lykn bind is out of scope");

        assert_eq!(
            error,
            TranspileError::UnsupportedForm {
                form: "bind".to_string(),
                position: 1,
            }
        );
        assert!(error.to_string().contains("unsupported form `bind`"));
    }
}
