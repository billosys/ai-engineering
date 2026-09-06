use crate::ast::{BinaryOperator, Expr, Program, Statement};
use crate::error::ParseError;

#[derive(Debug, Clone, PartialEq, Eq)]
enum TokenKind {
    OpenParen,
    CloseParen,
    Atom(String),
}

#[derive(Debug, Clone, PartialEq, Eq)]
struct Token {
    kind: TokenKind,
    position: usize,
}

pub(crate) fn parse_program(source: &str) -> Result<Program, ParseError> {
    let tokens = lex(source);
    let mut parser = Parser { tokens, cursor: 0 };
    parser.parse_program()
}

fn lex(source: &str) -> Vec<Token> {
    let mut tokens = Vec::new();
    let mut chars = source.char_indices().peekable();

    while let Some((position, ch)) = chars.next() {
        match ch {
            '(' => tokens.push(Token {
                kind: TokenKind::OpenParen,
                position,
            }),
            ')' => tokens.push(Token {
                kind: TokenKind::CloseParen,
                position,
            }),
            ch if ch.is_whitespace() => {}
            _ => {
                let mut atom = String::from(ch);
                while let Some((_, next)) = chars.peek() {
                    if next.is_whitespace() || *next == '(' || *next == ')' {
                        break;
                    }
                    atom.push(*next);
                    let _ = chars.next();
                }
                tokens.push(Token {
                    kind: TokenKind::Atom(atom),
                    position,
                });
            }
        }
    }

    tokens
}

struct Parser {
    tokens: Vec<Token>,
    cursor: usize,
}

impl Parser {
    fn parse_program(&mut self) -> Result<Program, ParseError> {
        let mut statements = Vec::new();
        while self.peek().is_some() {
            statements.push(self.parse_statement()?);
        }
        Ok(Program { statements })
    }

    fn parse_statement(&mut self) -> Result<Statement, ParseError> {
        self.expect_open_paren()?;
        let (form, position) = self.expect_atom("statement form")?;

        let statement = match form.as_str() {
            "let" => {
                let (name, position) = self.expect_atom("binding name")?;
                validate_identifier(&name, position)?;
                let expr = self.parse_expr()?;
                Statement::Let { name, expr }
            }
            "print" => {
                let expr = self.parse_expr()?;
                Statement::Print { expr }
            }
            _ => return Err(ParseError::UnsupportedForm { position, form }),
        };

        self.expect_close_paren()?;
        Ok(statement)
    }

    fn parse_expr(&mut self) -> Result<Expr, ParseError> {
        match self.next() {
            Some(Token {
                kind: TokenKind::Atom(atom),
                position,
            }) => parse_atom_expr(atom, position),
            Some(Token {
                kind: TokenKind::OpenParen,
                ..
            }) => {
                let (operator, operator_atom, position) = self.parse_binary_operator()?;
                let operands = self.parse_binary_operands()?;
                let found = operands.len();
                if found != 2 {
                    return Err(ParseError::BinaryOperatorArity {
                        position,
                        operator: operator_atom,
                        expected: 2,
                        found,
                    });
                }

                let mut operands = operands.into_iter();
                let Some(left) = operands.next() else {
                    return Err(ParseError::BinaryOperatorArity {
                        position,
                        operator: operator_atom,
                        expected: 2,
                        found,
                    });
                };
                let Some(right) = operands.next() else {
                    return Err(ParseError::BinaryOperatorArity {
                        position,
                        operator: operator_atom,
                        expected: 2,
                        found,
                    });
                };

                Ok(Expr::Binary {
                    operator,
                    left: Box::new(left),
                    right: Box::new(right),
                })
            }
            Some(Token {
                kind: TokenKind::CloseParen,
                position,
            }) => Err(ParseError::UnexpectedToken {
                position,
                found: String::from("`)`"),
                expected: "expression",
            }),
            None => Err(ParseError::UnexpectedEnd {
                expected: "expression",
            }),
        }
    }

    fn parse_binary_operator(&mut self) -> Result<(BinaryOperator, String, usize), ParseError> {
        let (operator_atom, position) = self.expect_atom("binary operator")?;
        let Some(operator) = BinaryOperator::from_atom(&operator_atom) else {
            return Err(ParseError::UnsupportedForm {
                position,
                form: operator_atom,
            });
        };
        Ok((operator, operator_atom, position))
    }

    fn parse_binary_operands(&mut self) -> Result<Vec<Expr>, ParseError> {
        let mut operands = Vec::new();

        loop {
            match self.peek() {
                Some(Token {
                    kind: TokenKind::CloseParen,
                    ..
                }) => {
                    self.expect_close_paren()?;
                    return Ok(operands);
                }
                Some(_) => operands.push(self.parse_expr()?),
                None => return Err(ParseError::UnexpectedEnd { expected: "`)`" }),
            }
        }
    }

    fn expect_open_paren(&mut self) -> Result<(), ParseError> {
        match self.next() {
            Some(Token {
                kind: TokenKind::OpenParen,
                ..
            }) => Ok(()),
            Some(token) => Err(unexpected_token(token, "`(`")),
            None => Err(ParseError::UnexpectedEnd { expected: "`(`" }),
        }
    }

    fn expect_close_paren(&mut self) -> Result<(), ParseError> {
        match self.next() {
            Some(Token {
                kind: TokenKind::CloseParen,
                ..
            }) => Ok(()),
            Some(token) => Err(unexpected_token(token, "`)`")),
            None => Err(ParseError::UnexpectedEnd { expected: "`)`" }),
        }
    }

    fn expect_atom(&mut self, expected: &'static str) -> Result<(String, usize), ParseError> {
        match self.next() {
            Some(Token {
                kind: TokenKind::Atom(atom),
                position,
            }) => Ok((atom, position)),
            Some(token) => Err(unexpected_token(token, expected)),
            None => Err(ParseError::UnexpectedEnd { expected }),
        }
    }

    fn next(&mut self) -> Option<Token> {
        let token = self.tokens.get(self.cursor).cloned();
        self.cursor += usize::from(token.is_some());
        token
    }

    fn peek(&self) -> Option<&Token> {
        self.tokens.get(self.cursor)
    }
}

fn parse_atom_expr(atom: String, position: usize) -> Result<Expr, ParseError> {
    match atom.parse::<i32>() {
        Ok(value) => Ok(Expr::Integer(value)),
        Err(error) if looks_numeric(&atom) => Err(ParseError::InvalidInteger {
            position,
            value: if error.kind() == &std::num::IntErrorKind::PosOverflow {
                format!("{atom} (too large for int)")
            } else {
                atom
            },
        }),
        Err(_) => {
            validate_identifier(&atom, position)?;
            Ok(Expr::Identifier(atom))
        }
    }
}

fn looks_numeric(atom: &str) -> bool {
    atom.chars()
        .next()
        .is_some_and(|ch| ch.is_ascii_digit() || ch == '-')
}

fn validate_identifier(name: &str, position: usize) -> Result<(), ParseError> {
    let mut chars = name.chars();
    let Some(first) = chars.next() else {
        return Err(ParseError::InvalidIdentifier {
            position,
            name: name.to_owned(),
        });
    };
    if !(first.is_ascii_alphabetic() || first == '_')
        || !chars.all(|ch| ch.is_ascii_alphanumeric() || ch == '_')
    {
        return Err(ParseError::InvalidIdentifier {
            position,
            name: name.to_owned(),
        });
    }
    if is_cpp_reserved_identifier(name) {
        return Err(ParseError::UnsafeIdentifier {
            position,
            name: name.to_owned(),
            reason: "reserved for C++",
        });
    }
    Ok(())
}

fn is_cpp_reserved_identifier(name: &str) -> bool {
    is_cpp_keyword(name)
        || name.starts_with("__")
        || name
            .strip_prefix('_')
            .and_then(|tail| tail.chars().next())
            .is_some_and(|ch| ch.is_ascii_uppercase())
}

fn is_cpp_keyword(name: &str) -> bool {
    matches!(
        name,
        "alignas"
            | "alignof"
            | "and"
            | "and_eq"
            | "asm"
            | "auto"
            | "bitand"
            | "bitor"
            | "bool"
            | "break"
            | "case"
            | "catch"
            | "char"
            | "char16_t"
            | "char32_t"
            | "class"
            | "compl"
            | "const"
            | "constexpr"
            | "const_cast"
            | "continue"
            | "decltype"
            | "default"
            | "delete"
            | "do"
            | "double"
            | "dynamic_cast"
            | "else"
            | "enum"
            | "explicit"
            | "export"
            | "extern"
            | "false"
            | "float"
            | "for"
            | "friend"
            | "goto"
            | "if"
            | "inline"
            | "int"
            | "long"
            | "mutable"
            | "namespace"
            | "new"
            | "noexcept"
            | "not"
            | "not_eq"
            | "nullptr"
            | "operator"
            | "or"
            | "or_eq"
            | "private"
            | "protected"
            | "public"
            | "register"
            | "reinterpret_cast"
            | "return"
            | "short"
            | "signed"
            | "sizeof"
            | "static"
            | "static_assert"
            | "static_cast"
            | "struct"
            | "switch"
            | "template"
            | "this"
            | "thread_local"
            | "throw"
            | "true"
            | "try"
            | "typedef"
            | "typeid"
            | "typename"
            | "union"
            | "unsigned"
            | "using"
            | "virtual"
            | "void"
            | "volatile"
            | "wchar_t"
            | "while"
            | "xor"
            | "xor_eq"
    )
}

fn unexpected_token(token: Token, expected: &'static str) -> ParseError {
    ParseError::UnexpectedToken {
        position: token.position,
        found: describe_token(&token.kind),
        expected,
    }
}

fn describe_token(kind: &TokenKind) -> String {
    match kind {
        TokenKind::OpenParen => String::from("`(`"),
        TokenKind::CloseParen => String::from("`)`"),
        TokenKind::Atom(atom) => format!("`{atom}`"),
    }
}
