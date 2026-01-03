# Palindrome Number Challenge

## Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome is a number that reads the same backward as forward.

## Examples

**Example 1:**
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Constraints
- -2^31 <= x <= 2^31 - 1

## Solution Templates (Python 3.11+, Go, Rust, PowerShell Core)

```python
def is_palindrome(x: int) -> bool:
    """Check if an integer is a palindrome."""
    # TODO: Implement your solution here
    return False


if __name__ == "__main__":
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
    assert is_palindrome(0) is True
    print("All tests passed!")
```

```go
package main

import "fmt"

func isPalindrome(x int) bool {
    // TODO: Implement your solution here
    return false
}

func main() {
    fmt.Println(isPalindrome(121))
}
```

```rust
fn is_palindrome(x: i32) -> bool {
    // TODO: Implement your solution here
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[ignore] // Remove this attribute once you've implemented the function
    fn test_is_palindrome() {
        assert!(is_palindrome(121));
        assert!(!is_palindrome(-121));
        assert!(!is_palindrome(10));
        assert!(is_palindrome(0));
    }
}

fn main() {
    println!("Run tests with: cargo test");
    println!("Run ignored tests with: cargo test -- --ignored");
}
```

```powershell
function Test-PalindromeNumber {
    param([int]$Number)
    # TODO: Implement your solution here
}

Test-PalindromeNumber -Number 121
Test-PalindromeNumber -Number -121
Test-PalindromeNumber -Number 10
Test-PalindromeNumber -Number 0
```

## Hints
1. Negative numbers are never palindromes
2. Numbers ending in 0 (except 0 itself) are never palindromes
3. You could convert to string, but try without conversion for extra challenge
4. You can reverse half the number and compare

## Solution Approaches

**Approach 1: String Conversion (Simple)**
- Convert number to string
- Compare string with its reverse
- Time: O(n), Space: O(n)

**Approach 2: Mathematical (Optimal)**
- Reverse the second half of the number
- Compare with first half
- Time: O(log n), Space: O(1)
