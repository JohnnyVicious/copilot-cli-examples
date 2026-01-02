"""
File Operations - Skills for GitHub Copilot CLI
This file demonstrates file handling operations in Python.
"""

import json
import csv
from pathlib import Path


def read_text_file(filepath: str) -> str:
    """Read and return contents of a text file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def write_text_file(filepath: str, content: str) -> None:
    """Write content to a text file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)


def append_to_file(filepath: str, content: str) -> None:
    """Append content to a text file."""
    with open(filepath, 'a', encoding='utf-8') as file:
        file.write(content)


def read_lines(filepath: str) -> list[str]:
    """Read file and return list of lines."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()


def read_json(filepath: str) -> dict:
    """Read and parse a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(filepath: str, data: dict) -> None:
    """Write data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def read_csv(filepath: str) -> list[dict]:
    """Read a CSV file and return list of dictionaries."""
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(filepath: str, data: list[dict], fieldnames: list[str]) -> None:
    """Write data to a CSV file."""
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    return Path(filepath).exists()


def create_directory(dirpath: str) -> None:
    """Create a directory if it doesn't exist."""
    Path(dirpath).mkdir(parents=True, exist_ok=True)


def list_files(directory: str, pattern: str = "*") -> list[str]:
    """List all files in a directory matching the pattern."""
    path = Path(directory)
    return [str(f) for f in path.glob(pattern) if f.is_file()]


if __name__ == "__main__":
    # Example usage
    print("File Operations Examples")
    print("This module provides utilities for file handling")
    print("Import and use these functions in your projects")
