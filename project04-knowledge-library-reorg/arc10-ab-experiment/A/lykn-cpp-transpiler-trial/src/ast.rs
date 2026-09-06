#[derive(Debug, Clone, PartialEq, Eq)]
pub(crate) struct Program {
    pub(crate) statements: Vec<Stmt>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub(crate) enum Stmt {
    Let { name: String, value: Expr },
    Print(Expr),
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub(crate) enum Expr {
    Binary {
        op: BinaryOp,
        left: Box<Expr>,
        right: Box<Expr>,
    },
    Identifier(String),
    Integer(i32),
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(crate) enum BinaryOp {
    Add,
    Subtract,
    Multiply,
    Divide,
}

impl BinaryOp {
    pub(crate) fn from_lexeme(lexeme: &str) -> Option<Self> {
        match lexeme {
            "+" => Some(Self::Add),
            "-" => Some(Self::Subtract),
            "*" => Some(Self::Multiply),
            "/" => Some(Self::Divide),
            _ => None,
        }
    }

    pub(crate) fn cxx_operator(self) -> &'static str {
        match self {
            Self::Add => "+",
            Self::Subtract => "-",
            Self::Multiply => "*",
            Self::Divide => "/",
        }
    }
}
