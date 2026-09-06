#[derive(Debug, Clone, PartialEq, Eq)]
pub(crate) struct Program {
    pub(crate) statements: Vec<Statement>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub(crate) enum Statement {
    Let { name: String, expr: Expr },
    Print { expr: Expr },
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub(crate) enum Expr {
    Integer(i32),
    Identifier(String),
    Binary {
        operator: BinaryOperator,
        left: Box<Expr>,
        right: Box<Expr>,
    },
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(crate) enum BinaryOperator {
    Add,
    Subtract,
    Multiply,
    Divide,
}

impl BinaryOperator {
    pub(crate) fn from_atom(atom: &str) -> Option<Self> {
        match atom {
            "+" => Some(Self::Add),
            "-" => Some(Self::Subtract),
            "*" => Some(Self::Multiply),
            "/" => Some(Self::Divide),
            _ => None,
        }
    }

    pub(crate) fn as_cpp(self) -> &'static str {
        match self {
            Self::Add => "+",
            Self::Subtract => "-",
            Self::Multiply => "*",
            Self::Divide => "/",
        }
    }
}
