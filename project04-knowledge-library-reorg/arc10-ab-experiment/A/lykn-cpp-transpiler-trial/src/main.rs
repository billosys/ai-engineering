use std::ffi::OsString;
use std::process::ExitCode;

use lykn_cpp_transpiler_trial::transpile_file;

fn main() -> ExitCode {
    let mut args = std::env::args_os();
    let program = args
        .next()
        .unwrap_or_else(|| OsString::from("lykn-cpp-transpiler-trial"));

    let Some(path) = args.next() else {
        eprintln!("usage: {} <source-file>", program.to_string_lossy());
        return ExitCode::from(2);
    };

    if args.next().is_some() {
        eprintln!("usage: {} <source-file>", program.to_string_lossy());
        return ExitCode::from(2);
    }

    match transpile_file(path) {
        Ok(output) => {
            print!("{output}");
            ExitCode::SUCCESS
        }
        Err(error) => {
            eprintln!("error: {error}");
            ExitCode::FAILURE
        }
    }
}
