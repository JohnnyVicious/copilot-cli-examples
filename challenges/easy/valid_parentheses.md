# Valid Parentheses Challenge

## Problem Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([)]"
Output: false
```

**Example 5:**
```
Input: s = "{[]}"
Output: true
```

## Constraints
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

## Solution Templates (Python 3.11+, Go, Rust, PowerShell Core)

```python
def is_valid_parentheses(s: str) -> bool:
    """Check if string has valid parentheses."""
    # TODO: Implement your solution here
    return False


if __name__ == "__main__":
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([)]") is False
    assert is_valid_parentheses("{[]}") is True
    print("All tests passed!")
```

```go
package main

import "fmt"

func isValidParentheses(s string) bool {
    // TODO: Implement your solution here
    return false
}

func main() {
    fmt.Println(isValidParentheses("()"))
}
```

```rust
fn is_valid_parentheses(s: &str) -> bool {
    // TODO: Implement your solution here
    false
}

fn main() {
    assert!(is_valid_parentheses("()"));
    assert!(is_valid_parentheses("()[]{}"));
    assert!(!is_valid_parentheses("(]"));
    assert!(!is_valid_parentheses("([)]"));
    assert!(is_valid_parentheses("{[]}"));
    println!("All tests passed!");
}
```

```powershell
function Test-ValidParentheses {
    param([string]$Input)
    # TODO: Implement your solution here
}

Test-ValidParentheses -Input "()"
Test-ValidParentheses -Input "()[]{}"
Test-ValidParentheses -Input "(]"
Test-ValidParentheses -Input "([)]"
Test-ValidParentheses -Input "{[]}"
```

## Hints
1. Use a stack data structure
2. Push opening brackets onto the stack
3. For closing brackets, check if they match the top of the stack
4. At the end, the stack should be empty

## Solution Approach
1. Create an empty stack
2. Iterate through each character:
   - If opening bracket: push to stack
   - If closing bracket: check if it matches top of stack
     - If matches: pop from stack
     - If doesn't match: return False
3. After iteration, return True if stack is empty, False otherwise

Time Complexity: O(n)
Space Complexity: O(n)
