//! Tiny Lykn-inspired S-expression to C++17 transpiler.

mod ast;
mod codegen;
mod parser;

pub mod error;

pub use error::{CodegenError, ParseError, TranspileError};

/// Transpile a tiny Lykn-inspired source program to one C++17 source file.
///
/// # Errors
///
/// Returns [`TranspileError::Parse`] when the source text is malformed or uses
/// unsupported syntax. Returns [`TranspileError::Codegen`] when the parsed AST
/// cannot be emitted as valid output in the supported C++ subset.
pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError> {
    let program = parser::parse_program(source).map_err(TranspileError::Parse)?;
    codegen::generate_cpp(&program).map_err(TranspileError::Codegen)
}
