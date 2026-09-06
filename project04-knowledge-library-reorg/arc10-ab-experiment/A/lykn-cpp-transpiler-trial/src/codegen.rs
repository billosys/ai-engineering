use crate::ast::{Expr, Program, Stmt};

pub(crate) fn generate(program: &Program) -> String {
    let mut output = String::from("#include <iostream>\n\nint main() {\n");

    for statement in &program.statements {
        match statement {
            Stmt::Let { name, value } => {
                output.push_str("    int ");
                output.push_str(name);
                output.push('{');
                output.push_str(&generate_expr(value));
                output.push_str("};\n");
            }
            Stmt::Print(expr) => {
                output.push_str("    std::cout << ");
                output.push_str(&generate_expr(expr));
                output.push_str(" << \"\\n\";\n");
            }
        }
    }

    output.push_str("    return 0;\n}\n");
    output
}

fn generate_expr(expr: &Expr) -> String {
    match expr {
        Expr::Binary { op, left, right } => {
            format!(
                "({} {} {})",
                generate_expr(left),
                op.cxx_operator(),
                generate_expr(right)
            )
        }
        Expr::Identifier(name) => name.clone(),
        Expr::Integer(value) => value.to_string(),
    }
}
