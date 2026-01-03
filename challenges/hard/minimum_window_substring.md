# Minimum Window Substring

## Problem Description
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

## Examples

**Example 1:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Constraints
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters

## Solution Templates (Python 3.11+, Go, Rust, PowerShell Core)

```python
from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    """Find minimum window substring containing all characters from t."""
    # TODO: Implement your solution here
    return ""


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("ab", "b") == "b"
    print("All tests passed!")
```

```go
package main

import "fmt"

func minWindow(s string, t string) string {
    // TODO: Implement your solution here
    return ""
}

func main() {
    fmt.Println(minWindow("ADOBECODEBANC", "ABC"))
}
```

```rust
fn min_window(s: &str, t: &str) -> String {
    // TODO: Implement your solution here
    String::new()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[ignore] // Remove this attribute once you've implemented the function
    fn test_min_window() {
        assert_eq!(min_window("ADOBECODEBANC", "ABC"), "BANC");
    }
}

fn main() {
    println!("Run tests with: cargo test");
    println!("Run ignored tests with: cargo test -- --ignored");
}
```

```powershell
function Get-MinimumWindowSubstring {
    param(
        [string]$Source,
        [string]$Target
    )
    # TODO: Implement your solution here
    return ""
}

# Test cases
$result1 = Get-MinimumWindowSubstring -Source "ADOBECODEBANC" -Target "ABC"
if ($result1 -ne "BANC") { throw "Test failed: Expected 'BANC' but got '$result1'" }

$result2 = Get-MinimumWindowSubstring -Source "a" -Target "a"
if ($result2 -ne "a") { throw "Test failed: Expected 'a' but got '$result2'" }

$result3 = Get-MinimumWindowSubstring -Source "a" -Target "aa"
if ($result3 -ne "") { throw "Test failed: Expected '' but got '$result3'" }

$result4 = Get-MinimumWindowSubstring -Source "ab" -Target "b"
if ($result4 -ne "b") { throw "Test failed: Expected 'b' but got '$result4'" }

Write-Host "All tests passed!" -ForegroundColor Green
```

## Hints
1. Use sliding window technique with two pointers
2. Expand window by moving right pointer until all characters included
3. Contract window by moving left pointer while maintaining validity
4. Track character frequencies with hash maps
5. Keep track of minimum window seen

## Solution Approach - Sliding Window

**Step 1: Setup**
1. Create frequency map for characters in t
2. Initialize two pointers (left, right) at start
3. Track characters matched and required

**Step 2: Expand Window**
1. Move right pointer to expand window
2. Update window character count
3. Check if current character is needed

**Step 3: Contract Window**
1. When all characters matched, try to minimize window
2. Move left pointer while window still valid
3. Update minimum window if current is smaller

**Step 4: Continue**
1. Keep expanding and contracting
2. Return minimum window found

Time Complexity: O(m + n) where m = len(s), n = len(t)
Space Complexity: O(m + n) for hash maps

## Key Concepts
- Sliding Window
- Two Pointers
- Hash Maps
- String Manipulation
- Optimization Problems

## Edge Cases to Consider
- t longer than s
- No valid window exists
- Multiple valid windows of same length
- t contains duplicate characters
- Entire string s is the minimum window
