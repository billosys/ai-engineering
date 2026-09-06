use std::collections::BTreeSet;

use crate::ast::{BinaryOperator, Expr, Program, Statement};
use crate::error::CodegenError;

pub(crate) fn generate_cpp(program: &Program) -> Result<String, CodegenError> {
    let mut output = String::from("#include <iostream>\n\nint main() {\n");
    let mut bindings = BTreeSet::new();

    for statement in &program.statements {
        match statement {
            Statement::Let { name, expr } => {
                if bindings.contains(name) {
                    return Err(CodegenError::DuplicateBinding { name: name.clone() });
                }
                let generated_expr = generate_expr(expr, &bindings)?;
                output.push_str("    const int ");
                output.push_str(name);
                output.push('{');
                output.push_str(&generated_expr);
                output.push_str("};\n");
                bindings.insert(name.clone());
            }
            Statement::Print { expr } => {
                let generated_expr = generate_expr(expr, &bindings)?;
                output.push_str("    std::cout << ");
                output.push_str(&generated_expr);
                output.push_str(" << \"\\n\";\n");
            }
        }
    }

    output.push_str("    return 0;\n}\n");
    Ok(output)
}

fn generate_expr(expr: &Expr, bindings: &BTreeSet<String>) -> Result<String, CodegenError> {
    match expr {
        Expr::Integer(value) => Ok(value.to_string()),
        Expr::Identifier(name) => {
            if bindings.contains(name) {
                Ok(name.clone())
            } else {
                Err(CodegenError::UnknownIdentifier { name: name.clone() })
            }
        }
        Expr::Binary {
            operator,
            left,
            right,
        } => {
            if *operator == BinaryOperator::Divide && matches!(right.as_ref(), Expr::Integer(0)) {
                return Err(CodegenError::DivisionByZero);
            }
            let left = generate_expr(left, bindings)?;
            let right = generate_expr(right, bindings)?;
            Ok(format!("({left} {} {right})", operator.as_cpp()))
        }
    }
}
