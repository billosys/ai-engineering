#[derive(Debug, Clone, PartialEq, Eq)]
#[non_exhaustive]
pub enum TranspileError {
    EmptyInput,
    DuplicateBinding {
        name: String,
        first_position: usize,
        duplicate_position: usize,
    },
    InvalidIdentifier {
        name: String,
        position: usize,
    },
    UnexpectedEnd {
        expected: &'static str,
    },
    UnexpectedToken {
        expected: &'static str,
        found: String,
        position: usize,
    },
    UnsupportedOperator {
        operator: String,
        position: usize,
    },
    MissingOperand {
        operator: String,
        operator_position: usize,
        operand_index: u8,
    },
    ExtraOperand {
        operator: String,
        operator_position: usize,
        extra_position: usize,
    },
    UnsupportedForm {
        form: String,
        position: usize,
    },
    InvalidInteger {
        literal: String,
        position: usize,
    },
    UnknownIdentifier {
        name: String,
        position: usize,
    },
}

impl std::fmt::Display for TranspileError {
    fn fmt(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::EmptyInput => write!(formatter, "empty input"),
            Self::DuplicateBinding {
                name,
                first_position,
                duplicate_position,
            } => write!(
                formatter,
                "duplicate binding `{name}` at byte {duplicate_position}; first bound at byte {first_position}"
            ),
            Self::InvalidIdentifier { name, position } => write!(
                formatter,
                "invalid identifier `{name}` at byte {position}; identifiers must match [A-Za-z_][A-Za-z0-9_]*"
            ),
            Self::UnexpectedEnd { expected } => {
                write!(formatter, "unexpected end of input; expected {expected}")
            }
            Self::UnexpectedToken {
                expected,
                found,
                position,
            } => write!(
                formatter,
                "expected {expected} at byte {position}, found `{found}`"
            ),
            Self::UnsupportedOperator { operator, position } => write!(
                formatter,
                "unsupported arithmetic operator `{operator}` at byte {position}; supported operators are `+`, `-`, `*`, and `/`"
            ),
            Self::MissingOperand {
                operator,
                operator_position,
                operand_index,
            } => write!(
                formatter,
                "missing operand {operand_index} for arithmetic operator `{operator}` at byte {operator_position}"
            ),
            Self::ExtraOperand {
                operator,
                operator_position,
                extra_position,
            } => write!(
                formatter,
                "extra operand for arithmetic operator `{operator}` at byte {operator_position}; extra operand starts at byte {extra_position}"
            ),
            Self::UnsupportedForm { form, position } => write!(
                formatter,
                "unsupported form `{form}` at byte {position}; this slice only supports `let`, `print`, and binary arithmetic expressions with `+`, `-`, `*`, or `/`"
            ),
            Self::InvalidInteger { literal, position } => write!(
                formatter,
                "invalid integer literal `{literal}` at byte {position}; expected base-10 value in 0..=2147483647"
            ),
            Self::UnknownIdentifier { name, position } => write!(
                formatter,
                "unknown identifier `{name}` at byte {position}; identifiers must be bound before they are used"
            ),
        }
    }
}

impl std::error::Error for TranspileError {}
