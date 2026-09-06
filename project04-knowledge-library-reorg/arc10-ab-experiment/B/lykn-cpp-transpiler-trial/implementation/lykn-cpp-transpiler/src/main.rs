use std::ffi::OsString;
use std::path::PathBuf;
use std::process::ExitCode;

fn main() -> ExitCode {
    match run(std::env::args_os().collect::<Vec<_>>()) {
        Ok(cpp) => {
            print!("{cpp}");
            ExitCode::SUCCESS
        }
        Err(CliError::Usage(message)) => {
            eprintln!("{message}");
            ExitCode::from(2)
        }
        Err(CliError::Read { path, source }) => {
            eprintln!("error: failed to read {}: {source}", path.display());
            ExitCode::FAILURE
        }
        Err(CliError::Transpile(error)) => {
            eprintln!("error: {error}");
            ExitCode::FAILURE
        }
    }
}

fn run(args: Vec<OsString>) -> Result<String, CliError> {
    let [program, input] = args.as_slice() else {
        return Err(CliError::Usage(String::from(
            "usage: lykn-cpp-transpiler <input.lykn>",
        )));
    };

    let path = PathBuf::from(input);
    let source = std::fs::read_to_string(&path).map_err(|source| CliError::Read {
        path: path.clone(),
        source,
    })?;

    let _program_name = program;
    lykn_cpp_transpiler::transpile_to_cpp(&source).map_err(CliError::Transpile)
}

#[derive(Debug)]
enum CliError {
    Usage(String),
    Read {
        path: PathBuf,
        source: std::io::Error,
    },
    Transpile(lykn_cpp_transpiler::TranspileError),
}
