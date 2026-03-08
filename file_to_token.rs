use rayon::prelude::*;
use std::fs;
use std::path::PathBuf;
use walkdir::WalkDir;
use tiktoken_rs::cl100k_base;
use anyhow::Result;

fn collect_files(dir: &str) -> Vec<PathBuf> {
    WalkDir::new(dir)
        .into_iter()
        .filter_map(|e| e.ok())
        .filter(|e| e.file_type().is_file())
        .map(|e| e.path().to_path_buf())
        .collect()
}

fn count_tokens(text: &str) -> usize {
    let bpe = cl100k_base().unwrap();
    let tokens = bpe.encode_with_special_tokens(text);
    tokens.len()
}

fn process_file(path: &PathBuf) -> Result<(String, usize)> {
    let content = fs::read_to_string(path)?;
    let tokens = count_tokens(&content);

    Ok((path.display().to_string(), tokens))
}

fn main() -> Result<()> {
    let dir = "./files"; // directory containing files

    let files = collect_files(dir);

    println!("Processing {} files in parallel...\n", files.len());

    let results: Vec<_> = files
        .par_iter()
        .map(|path| process_file(path))
        .collect();

    let mut total = 0;

    for res in results {
        match res {
            Ok((file, tokens)) => {
                println!("{} -> {} tokens", file, tokens);
                total += tokens;
            }
            Err(e) => println!("Error: {}", e),
        }
    }

    println!("\nTotal tokens: {}", total);

    Ok(())
}
