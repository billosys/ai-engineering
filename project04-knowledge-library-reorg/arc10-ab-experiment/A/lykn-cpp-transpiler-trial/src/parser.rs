use crate::TranspileError;
use crate::ast::{BinaryOp, Expr, Program, Stmt};
use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq, Eq)]
enum TokenKind {
    LeftParen,
    RightParen,
    Atom(String),
}

#[derive(Debug, Clone, PartialEq, Eq)]
struct Token {
    kind: TokenKind,
    position: usize,
}

pub(crate) fn parse(source: &str) -> Result<Program, TranspileError> {
    let tokens = tokenize(source)?;
    let mut parser = Parser::new(tokens);
    parser.parse_program()
}

fn tokenize(source: &str) -> Result<Vec<Token>, TranspileError> {
    let mut tokens = Vec::new();
    let mut chars = source.char_indices().peekable();

    while let Some((position, character)) = chars.next() {
        match character {
            '(' => tokens.push(Token {
                kind: TokenKind::LeftParen,
                position,
            }),
            ')' => tokens.push(Token {
                kind: TokenKind::RightParen,
                position,
            }),
            character if character.is_whitespace() => {}
            _ => {
                let mut atom = String::from(character);

                while let Some((_, next)) = chars.peek() {
                    if next.is_whitespace() || *next == '(' || *next == ')' {
                        break;
                    }

                    atom.push(*next);
                    chars.next();
                }

                tokens.push(Token {
                    kind: TokenKind::Atom(atom),
                    position,
                });
            }
        }
    }

    if tokens.is_empty() {
        return Err(TranspileError::EmptyInput);
    }

    Ok(tokens)
}

struct Parser {
    tokens: Vec<Token>,
    cursor: usize,
    bindings: HashMap<String, usize>,
}

impl Parser {
    fn new(tokens: Vec<Token>) -> Self {
        Self {
            tokens,
            cursor: 0,
            bindings: HashMap::new(),
        }
    }

    fn parse_program(&mut self) -> Result<Program, TranspileError> {
        let mut statements = Vec::new();

        while !self.is_at_end() {
            statements.push(self.parse_statement()?);
        }

        Ok(Program { statements })
    }

    fn parse_statement(&mut self) -> Result<Stmt, TranspileError> {
        self.expect_left_paren()?;
        let (form, position) = self.expect_form_name()?;

        let statement = match form.as_str() {
            "let" => self.parse_let_statement(position)?,
            "print" => self.parse_print_statement()?,
            _ => {
                return Err(TranspileError::UnsupportedForm { form, position });
            }
        };

        self.expect_right_paren()?;
        Ok(statement)
    }

    fn parse_let_statement(&mut self, _form_position: usize) -> Result<Stmt, TranspileError> {
        let (name, position) = self.expect_atom("identifier")?;
        validate_identifier(&name, position)?;

        if let Some(first_position) = self.bindings.get(&name) {
            return Err(TranspileError::DuplicateBinding {
                name,
                first_position: *first_position,
                duplicate_position: position,
            });
        }

        let value = self.parse_expr()?;
        self.bindings.insert(name.clone(), position);

        Ok(Stmt::Let { name, value })
    }

    fn parse_print_statement(&mut self) -> Result<Stmt, TranspileError> {
        let expr = self.parse_expr()?;
        Ok(Stmt::Print(expr))
    }

    fn parse_expr(&mut self) -> Result<Expr, TranspileError> {
        match self.advance() {
            Some(Token {
                kind: TokenKind::LeftParen,
                ..
            }) => self.parse_arithmetic_expr(),
            Some(Token {
                kind: TokenKind::Atom(atom),
                position,
            }) => self.parse_atom_expr(&atom, position),
            Some(token) => Err(unexpected_token("expression", &token)),
            None => Err(TranspileError::UnexpectedEnd {
                expected: "expression",
            }),
        }
    }

    fn parse_arithmetic_expr(&mut self) -> Result<Expr, TranspileError> {
        let (operator, operator_position) = self.expect_atom("arithmetic operator")?;
        let op = BinaryOp::from_lexeme(&operator).ok_or_else(|| {
            TranspileError::UnsupportedOperator {
                operator: operator.clone(),
                position: operator_position,
            }
        })?;

        let left = self.parse_required_operand(&operator, operator_position, 1)?;
        let right = self.parse_required_operand(&operator, operator_position, 2)?;

        match self.peek() {
            Some(Token {
                kind: TokenKind::RightParen,
                ..
            }) => {
                self.advance();
                Ok(Expr::Binary {
                    op,
                    left: Box::new(left),
                    right: Box::new(right),
                })
            }
            Some(token) => Err(TranspileError::ExtraOperand {
                operator,
                operator_position,
                extra_position: token.position,
            }),
            None => Err(TranspileError::UnexpectedEnd { expected: "`)`" }),
        }
    }

    fn parse_required_operand(
        &mut self,
        operator: &str,
        operator_position: usize,
        operand_index: u8,
    ) -> Result<Expr, TranspileError> {
        match self.peek() {
            Some(Token {
                kind: TokenKind::RightParen,
                ..
            })
            | None => Err(TranspileError::MissingOperand {
                operator: operator.to_string(),
                operator_position,
                operand_index,
            }),
            Some(_) => self.parse_expr(),
        }
    }

    fn expect_left_paren(&mut self) -> Result<(), TranspileError> {
        match self.advance() {
            Some(Token {
                kind: TokenKind::LeftParen,
                ..
            }) => Ok(()),
            Some(token) => Err(unexpected_token("`(`", &token)),
            None => Err(TranspileError::UnexpectedEnd { expected: "`(`" }),
        }
    }

    fn expect_form_name(&mut self) -> Result<(String, usize), TranspileError> {
        match self.advance() {
            Some(Token {
                kind: TokenKind::Atom(form),
                position,
            }) => Ok((form, position)),
            Some(token) => Err(unexpected_token("form name", &token)),
            None => Err(TranspileError::UnexpectedEnd {
                expected: "form name",
            }),
        }
    }

    fn parse_atom_expr(&self, atom: &str, position: usize) -> Result<Expr, TranspileError> {
        if atom.chars().next().is_some_and(|character| {
            character.is_ascii_digit() || character == '-' || character == '+'
        }) {
            return parse_integer(atom, position).map(Expr::Integer);
        }

        validate_identifier(atom, position)?;

        if !self.bindings.contains_key(atom) {
            return Err(TranspileError::UnknownIdentifier {
                name: atom.to_string(),
                position,
            });
        }

        Ok(Expr::Identifier(atom.to_string()))
    }

    fn expect_atom(&mut self, expected: &'static str) -> Result<(String, usize), TranspileError> {
        match self.advance() {
            Some(Token {
                kind: TokenKind::Atom(atom),
                position,
            }) => Ok((atom, position)),
            Some(token) => Err(unexpected_token(expected, &token)),
            None => Err(TranspileError::UnexpectedEnd { expected }),
        }
    }

    fn expect_right_paren(&mut self) -> Result<(), TranspileError> {
        match self.advance() {
            Some(Token {
                kind: TokenKind::RightParen,
                ..
            }) => Ok(()),
            Some(token) => Err(unexpected_token("`)`", &token)),
            None => Err(TranspileError::UnexpectedEnd { expected: "`)`" }),
        }
    }

    fn is_at_end(&self) -> bool {
        self.cursor >= self.tokens.len()
    }

    fn peek(&self) -> Option<&Token> {
        self.tokens.get(self.cursor)
    }

    fn advance(&mut self) -> Option<Token> {
        let token = self.tokens.get(self.cursor).cloned();
        self.cursor += usize::from(token.is_some());
        token
    }
}

fn parse_integer(atom: &str, position: usize) -> Result<i32, TranspileError> {
    if !is_integer_literal(atom) {
        return Err(TranspileError::InvalidInteger {
            literal: atom.to_string(),
            position,
        });
    }

    atom.parse::<i32>()
        .map_err(|_| TranspileError::InvalidInteger {
            literal: atom.to_string(),
            position,
        })
}

fn is_integer_literal(atom: &str) -> bool {
    !atom.is_empty() && atom.chars().all(|character| character.is_ascii_digit())
}

fn validate_identifier(name: &str, position: usize) -> Result<(), TranspileError> {
    let mut chars = name.chars();
    let Some(first) = chars.next() else {
        return Err(TranspileError::InvalidIdentifier {
            name: name.to_string(),
            position,
        });
    };

    if !(first.is_ascii_alphabetic() || first == '_') {
        return Err(TranspileError::InvalidIdentifier {
            name: name.to_string(),
            position,
        });
    }

    if !chars.all(|character| character.is_ascii_alphanumeric() || character == '_') {
        return Err(TranspileError::InvalidIdentifier {
            name: name.to_string(),
            position,
        });
    }

    Ok(())
}

fn unexpected_token(expected: &'static str, token: &Token) -> TranspileError {
    TranspileError::UnexpectedToken {
        expected,
        found: token_description(token),
        position: token.position,
    }
}

fn token_description(token: &Token) -> String {
    match &token.kind {
        TokenKind::LeftParen => "(".to_string(),
        TokenKind::RightParen => ")".to_string(),
        TokenKind::Atom(atom) => atom.clone(),
    }
}
