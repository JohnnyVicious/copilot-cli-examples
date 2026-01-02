# GitHub Copilot CLI Examples - Getting Started

## Overview
This repository contains a comprehensive collection of examples, skills, and coding challenges designed to demonstrate GitHub Copilot CLI capabilities. It serves as a proof of concept for how developers can leverage Copilot to assist with various programming tasks.

## What's Inside

### 📚 Skills (`/skills`)
Language-specific examples demonstrating fundamental programming concepts:

#### Python
- **basic_functions.py** - Common functions (greet, sum, max, palindromes, fibonacci, factorial)
- **data_structures.py** - Stack, Queue, and LinkedList implementations
- **file_operations.py** - File I/O, JSON, CSV operations

#### JavaScript
- **basicFunctions.js** - Array operations, string manipulation, functional programming
- **asyncPatterns.js** - Promises, async/await, retry logic, batching

#### Go
- **basic_functions.go** - Type-safe functions, error handling, slices
- **concurrency.go** - Goroutines, channels, worker pools, pipelines

### 🎯 Challenges (`/challenges`)
Coding challenges organized by difficulty level:

#### Easy
1. **Two Sum** - Array manipulation, hash maps
2. **Palindrome Number** - Number operations, string conversion
3. **Valid Parentheses** - Stack data structure

#### Medium
1. **Longest Substring** - Sliding window technique
2. **Binary Tree Traversal** - BFS, level order traversal
3. **Group Anagrams** - Hash maps, string sorting

#### Hard
1. **Merge K Sorted Lists** - Min heap, divide and conquer
2. **Word Ladder** - BFS, graph theory, shortest path
3. **Minimum Window Substring** - Sliding window optimization

### 💡 Examples (`/examples`)
Complete, runnable applications:
- **api_client.py** - REST API client with CRUD operations
- **web_scraper.py** - Web scraping with BeautifulSoup

## How to Use This Repository

### 1. Exploring Skills
Navigate to any skill file to see well-documented examples:

```bash
cd skills/python
python basic_functions.py
```

Each skill file:
- Contains multiple related functions
- Includes docstrings and type hints
- Has runnable test cases
- Demonstrates best practices

### 2. Solving Challenges
Each challenge includes:
- Problem description with examples
- Constraints and edge cases
- Solution template with test cases
- Hints and multiple approaches
- Time/space complexity analysis

To attempt a challenge:
1. Read the markdown file (e.g., `challenges/easy/two_sum.md`)
2. Implement the solution in the template
3. Run the test cases to verify

### 3. Learning from Examples
Complete examples show real-world patterns:

```bash
cd examples
python api_client.py
```

These demonstrate:
- Project structure
- Error handling
- Logging and debugging
- Documentation practices

## Using with GitHub Copilot CLI

### Getting Copilot Suggestions
When working on any file, Copilot can help you:

1. **Complete implementations** - Start typing a function and let Copilot suggest the body
2. **Generate test cases** - Ask for test cases for your functions
3. **Write documentation** - Request docstrings or comments
4. **Refactor code** - Ask for optimizations or alternative approaches

### Example Workflows

#### Learning a New Concept
```bash
# Open a skills file
code skills/python/data_structures.py

# Use Copilot to:
# - Explain how the Stack works
# - Suggest additional methods
# - Generate more test cases
```

#### Solving a Challenge
```bash
# Open a challenge
code challenges/medium/longest_substring.md

# Use Copilot to:
# - Implement the solution
# - Explain the algorithm
# - Optimize the solution
# - Generate edge case tests
```

#### Building a Project
```bash
# Use examples as starting points
code examples/api_client.py

# Use Copilot to:
# - Add authentication
# - Implement rate limiting
# - Add caching
# - Write integration tests
```

## Tips for Using Copilot

### Be Specific
❌ Bad: "write a function"
✅ Good: "write a Python function that reverses a string and handles unicode"

### Use Comments to Guide
```python
# Function to calculate fibonacci using dynamic programming
def fibonacci_dp(n: int) -> int:
    # Copilot will suggest optimized implementation
```

### Ask for Alternatives
```python
# Alternative approach using recursion
# Alternative approach using iteration
# Alternative approach with memoization
```

### Request Documentation
```python
def complex_function(param1, param2):
    # TODO: Add comprehensive docstring with examples
```

## Repository Structure

```
copilot-cli-examples/
├── skills/
│   ├── python/          # Python skills
│   ├── javascript/      # JavaScript skills
│   └── go/              # Go skills
├── challenges/
│   ├── easy/            # Beginner challenges
│   ├── medium/          # Intermediate challenges
│   └── hard/            # Advanced challenges
├── examples/            # Complete applications
├── docs/                # Documentation
└── README.md            # This file
```

## Prerequisites

### Python Examples
```bash
pip install requests beautifulsoup4
```

### JavaScript Examples
```bash
node skills/javascript/basicFunctions.js
```

### Go Examples
```bash
go run skills/go/basic_functions.go
```

## Contributing

This is a proof of concept repository. You can:
1. Add more skills in additional languages
2. Create new challenges
3. Build complete example applications
4. Improve documentation
5. Add tests and validation scripts

## Learning Path

### Beginner
1. Start with `skills/python/basic_functions.py`
2. Try `challenges/easy/two_sum.md`
3. Explore `examples/api_client.py`

### Intermediate
1. Study `skills/javascript/asyncPatterns.js`
2. Solve `challenges/medium/longest_substring.md`
3. Modify examples to add features

### Advanced
1. Learn `skills/go/concurrency.go`
2. Tackle `challenges/hard/merge_k_sorted_lists.md`
3. Build new examples from scratch

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Python Documentation](https://docs.python.org/)
- [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Go Documentation](https://go.dev/doc/)

## License

See LICENSE file for details.
