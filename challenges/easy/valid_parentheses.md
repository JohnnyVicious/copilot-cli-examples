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

## Solution Template (Python)

```python
def is_valid_parentheses(s: str) -> bool:
    """
    Check if string has valid parentheses
    
    Args:
        s: String containing parentheses
    
    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == "__main__":
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("(]") == False
    assert is_valid_parentheses("([)]") == False
    assert is_valid_parentheses("{[]}") == True
    print("All tests passed!")
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
