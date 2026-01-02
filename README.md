# GitHub Copilot CLI Examples

A comprehensive proof of concept repository demonstrating GitHub Copilot CLI capabilities through skills, coding challenges, and practical examples.

## 🎯 Purpose

This repository serves as a practical demonstration of how GitHub Copilot can assist developers with:
- Learning new programming concepts
- Solving coding challenges
- Building real-world applications
- Following best practices across multiple languages

## 📂 Repository Structure

```
copilot-cli-examples/
├── skills/              # Language-specific skills and patterns
│   ├── python/         # Python fundamentals, data structures, file I/O
│   ├── javascript/     # JS functions, async patterns
│   └── go/             # Go basics, concurrency patterns
├── challenges/          # Coding challenges by difficulty
│   ├── easy/           # Two Sum, Palindrome, Valid Parentheses
│   ├── medium/         # Longest Substring, Tree Traversal, Anagrams
│   └── hard/           # Merge K Lists, Word Ladder, Window Substring
├── examples/            # Complete runnable applications
│   ├── api_client.py   # REST API client implementation
│   └── web_scraper.py  # Web scraping with BeautifulSoup
├── docs/                # Comprehensive documentation
│   ├── GETTING_STARTED.md
│   └── BEST_PRACTICES.md
└── README.md           # This file
```

## 🚀 Quick Start

### Setup and Validation

**Automated Setup (Recommended):**
```bash
python setup.py
```

The `setup.py` script will:
- Check Python version (3.8+ required)
- Install Python dependencies (requests, beautifulsoup4)
- Verify repository structure
- Check for optional Node.js and Go installations

**Validate Everything Works:**
```bash
python validate.py
```

The `validate.py` script will:
- Test all Python skill examples
- Validate syntax of example applications
- Check all challenge files exist
- Verify documentation is complete

### Prerequisites

**Python examples:**
```bash
pip install requests beautifulsoup4
```

**JavaScript examples:**
```bash
node --version  # Ensure Node.js is installed
```

**Go examples:**
```bash
go version  # Ensure Go is installed
```

### Running Examples

**Python Skills:**
```bash
python skills/python/basic_functions.py
python skills/python/data_structures.py
```

**JavaScript Skills:**
```bash
node skills/javascript/basicFunctions.js
node skills/javascript/asyncPatterns.js
```

**Go Skills:**
```bash
go run skills/go/basic_functions.go
go run skills/go/concurrency.go
```

**Complete Examples:**
```bash
python examples/api_client.py
python examples/web_scraper.py
```

## 💡 What's Included

### Skills (Programming Fundamentals)

#### Python
- **basic_functions.py** - Essential functions: greet, sum, max, palindrome, fibonacci, factorial
- **data_structures.py** - Stack, Queue, LinkedList implementations with full methods
- **file_operations.py** - File I/O, JSON handling, CSV operations, directory management

#### JavaScript  
- **basicFunctions.js** - Array operations, string manipulation, functional programming patterns
- **asyncPatterns.js** - Promises, async/await, retry logic, parallel/sequential execution, batching

#### Go
- **basic_functions.go** - Type-safe functions, error handling, slice operations, unique values
- **concurrency.go** - Goroutines, channels, worker pools, pipelines, fan-out, rate limiting

### Challenges (Algorithmic Problem Solving)

#### Easy Level
1. **Two Sum** - Array + Hash Map (O(n) solution)
2. **Palindrome Number** - Number operations and validation
3. **Valid Parentheses** - Stack-based bracket matching

#### Medium Level
1. **Longest Substring Without Repeating Characters** - Sliding window technique
2. **Binary Tree Level Order Traversal** - BFS with queue
3. **Group Anagrams** - Hash maps with sorted keys

#### Hard Level
1. **Merge K Sorted Lists** - Min heap, divide and conquer
2. **Word Ladder** - BFS, shortest path in graph
3. **Minimum Window Substring** - Advanced sliding window

Each challenge includes:
- ✅ Problem description with examples
- ✅ Constraints and edge cases
- ✅ Solution template with test cases
- ✅ Multiple approaches and hints
- ✅ Time/space complexity analysis

### Examples (Real-World Applications)

#### API Client (`api_client.py`)
Complete REST API client demonstrating:
- HTTP methods (GET, POST, PUT, DELETE)
- Session management
- Error handling
- Practical usage with TodoAPIClient

#### Web Scraper (`web_scraper.py`)
Production-ready web scraper featuring:
- Rate limiting and respectful scraping
- BeautifulSoup parsing
- Link extraction
- Table data extraction
- Specialized article scraping

## 📖 Documentation

### [Getting Started Guide](docs/GETTING_STARTED.md)
- How to use each section
- Learning paths for different skill levels
- Using Copilot effectively with examples
- Tips and workflows

### [Best Practices](docs/BEST_PRACTICES.md)
- Writing code that works well with Copilot
- Language-specific conventions
- Testing strategies
- Security considerations
- Performance optimization
- Common design patterns

## 🎓 Learning Paths

### Beginner Path
1. Start with `skills/python/basic_functions.py`
2. Try solving `challenges/easy/two_sum.md`
3. Run `examples/api_client.py` and study the code
4. Modify examples to add simple features

### Intermediate Path
1. Explore `skills/javascript/asyncPatterns.js`
2. Solve `challenges/medium/longest_substring.md`
3. Study `examples/web_scraper.py`
4. Add error handling and logging to examples

### Advanced Path
1. Master `skills/go/concurrency.go`
2. Tackle `challenges/hard/merge_k_sorted_lists.md`
3. Build your own complete example
4. Implement advanced features like caching, monitoring

## 🤖 Using with GitHub Copilot

### Getting Suggestions
Copilot works best when you:
1. **Provide context** - Use descriptive names and comments
2. **Be specific** - Write clear function signatures
3. **Show patterns** - Give examples of what you want
4. **Iterate** - Refine suggestions to match your needs

### Example Workflow

```python
# 1. Write a clear function signature with docstring
def calculate_moving_average(data: list[float], window_size: int) -> list[float]:
    """
    Calculate moving average with specified window size.
    
    Args:
        data: List of numeric values
        window_size: Size of the moving window
    
    Returns:
        List of moving averages
    """
    # 2. Copilot will suggest implementation
    # 3. Review and adjust as needed
```

### Common Use Cases
- **Implementing algorithms** - Describe the algorithm in comments
- **Writing tests** - Copilot can generate comprehensive test cases
- **Documentation** - Request docstrings and README content
- **Refactoring** - Ask for cleaner or more efficient versions
- **Bug fixing** - Describe the issue and expected behavior

## 🛠️ Development

### Running Tests
Each skill and example file has embedded tests:

```bash
# Python
python skills/python/basic_functions.py
python examples/api_client.py

# JavaScript
node skills/javascript/basicFunctions.js

# Go
go run skills/go/basic_functions.go
```

### Adding New Content

#### New Skill
1. Create file in appropriate `skills/<language>/` directory
2. Include clear function signatures and docstrings
3. Add test cases in `if __name__ == "__main__"` block
4. Update this README

#### New Challenge
1. Create markdown file in `challenges/<difficulty>/`
2. Include problem statement, examples, constraints
3. Provide solution template with test cases
4. Add hints and complexity analysis

#### New Example
1. Create self-contained application in `examples/`
2. Include imports, main logic, and usage example
3. Add logging and error handling
4. Document in comments

## 📋 Challenge Solutions

The challenges are provided as templates for learning. To get the most value:
1. Read the problem description carefully
2. Try to implement the solution yourself first
3. Use Copilot to help when stuck
4. Run the test cases to verify
5. Compare with different approaches

## 🔒 Security Notes

When using these examples:
- ⚠️ Never commit real API keys or credentials
- ⚠️ Respect robots.txt when web scraping
- ⚠️ Use rate limiting for API calls
- ⚠️ Validate and sanitize all user inputs
- ⚠️ Use the examples as learning tools, not production code without review

## 🤝 Contributing

This is a proof of concept repository. Contributions welcome:
- Add skills in new languages (Rust, Java, C#, etc.)
- Create more coding challenges
- Build additional complete examples
- Improve documentation
- Add testing frameworks
- Create setup/validation scripts

## 📚 Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot CLI](https://githubnext.com/projects/copilot-cli)
- [Python Documentation](https://docs.python.org/)
- [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Go Documentation](https://go.dev/doc/)

## 📄 License

See [LICENSE](LICENSE) file for details.

## 💬 Feedback

This repository is designed to showcase GitHub Copilot capabilities. Your feedback helps improve the examples and documentation!

---

**Note:** This is a proof of concept and educational repository. All code examples are for demonstration and learning purposes. Review and test thoroughly before using in production environments.
