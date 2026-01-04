use std::io::{self, Write};

/*
Starter template for Rust (stable)
Entrypoint: Run with `rustc starter.rs && ./starter`
Or with cargo: Create a new project with `cargo new myproject`, replace src/main.rs,
               then run with `cargo run`
*/

fn main() {
    /*
    Sample I/O:
      Input: (via stdin or args)
      Output: (via stdout)
    */

    // Read input
    print!("Enter your name: ");
    io::stdout().flush().unwrap();
    
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    
    let input = input.trim();

    // Process
    let result = format!("Hello, {}!", input);

    // Write output
    println!("{}", result);
}
