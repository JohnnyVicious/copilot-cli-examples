# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

## Solution Template (Python)

```python
def length_of_longest_substring(s: str) -> int:
    """
    Find length of longest substring without repeating characters
    
    Args:
        s: Input string
    
    Returns:
        Length of longest substring without repeating characters
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("dvdf") == 3
    print("All tests passed!")
```

## Hints
1. Use the sliding window technique
2. Maintain a set or hash map of characters in current window
3. Move the right pointer to expand window
4. Move the left pointer when you find a duplicate
5. Track the maximum length seen

## Solution Approach - Sliding Window
1. Use two pointers (left and right) to represent a window
2. Use a hash map to store character positions
3. Expand the window by moving right pointer
4. When duplicate found, move left pointer past the previous occurrence
5. Update maximum length at each step

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is charset size

## Key Concepts
- Sliding Window
- Hash Map
- Two Pointers
