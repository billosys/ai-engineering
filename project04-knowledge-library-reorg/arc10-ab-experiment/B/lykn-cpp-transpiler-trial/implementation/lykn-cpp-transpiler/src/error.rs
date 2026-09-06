use std::error::Error;
use std::fmt;

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum TranspileError {
    Parse(ParseError),
    Codegen(CodegenError),
}

impl fmt::Display for TranspileError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::Parse(error) => write!(f, "{error}"),
            Self::Codegen(error) => write!(f, "{error}"),
        }
    }
}

impl Error for TranspileError {}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum ParseError {
    UnexpectedEnd {
        expected: &'static str,
    },
    UnexpectedToken {
        position: usize,
        found: String,
        expected: &'static str,
    },
    UnsupportedForm {
        position: usize,
        form: String,
    },
    BinaryOperatorArity {
        position: usize,
        operator: String,
        expected: usize,
        found: usize,
    },
    InvalidIdentifier {
        position: usize,
        name: String,
    },
    UnsafeIdentifier {
        position: usize,
        name: String,
        reason: &'static str,
    },
    InvalidInteger {
        position: usize,
        value: String,
    },
}

impl fmt::Display for ParseError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::UnexpectedEnd { expected } => {
                write!(
                    f,
                    "parse error: unexpected end of input, expected {expected}"
                )
            }
            Self::UnexpectedToken {
                position,
                found,
                expected,
            } => write!(
                f,
                "parse error at byte {position}: found {found}, expected {expected}",
            ),
            Self::UnsupportedForm { position, form } => {
                write!(
                    f,
                    "parse error at byte {position}: unsupported form `{form}`"
                )
            }
            Self::BinaryOperatorArity {
                position,
                operator,
                expected,
                found,
            } => write!(
                f,
                "parse error at byte {position}: binary operator `{operator}` expected {expected} operands, found {found}",
            ),
            Self::InvalidIdentifier { position, name } => write!(
                f,
                "parse error at byte {position}: invalid identifier `{name}`",
            ),
            Self::UnsafeIdentifier {
                position,
                name,
                reason,
            } => write!(
                f,
                "parse error at byte {position}: C++-unsafe identifier `{name}` ({reason})",
            ),
            Self::InvalidInteger { position, value } => {
                write!(
                    f,
                    "parse error at byte {position}: invalid integer `{value}`"
                )
            }
        }
    }
}

impl Error for ParseError {}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum CodegenError {
    DuplicateBinding { name: String },
    UnknownIdentifier { name: String },
    DivisionByZero,
}

impl fmt::Display for CodegenError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::DuplicateBinding { name } => {
                write!(f, "codegen error: duplicate binding `{name}`")
            }
            Self::UnknownIdentifier { name } => {
                write!(f, "codegen error: unknown identifier `{name}`")
            }
            Self::DivisionByZero => write!(
                f,
                "codegen error: division by direct literal zero is not supported"
            ),
        }
    }
}

impl Error for CodegenError {}
