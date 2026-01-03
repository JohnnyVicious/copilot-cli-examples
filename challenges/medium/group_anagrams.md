# Group Anagrams

## Problem Description
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

## Solution Templates (Python 3.11+, Go, Rust, PowerShell Core)

```python
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group anagrams together."""
    # TODO: Implement your solution here
    return []


if __name__ == "__main__":
    result1 = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result1_sorted = [sorted(group) for group in result1]
    expected1 = [sorted(group) for group in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]]
    assert sorted(result1_sorted) == sorted(expected1)
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed!")
```

```go
package main

import "fmt"

func groupAnagrams(strs []string) [][]string {
    // TODO: Implement your solution here
    return [][]string{}
}

func main() {
    fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
}
```

```rust
fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    // TODO: Implement your solution here
    Vec::new()
}

fn main() {
    let result = group_anagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
            .iter()
            .map(|s| s.to_string())
            .collect(),
    );
    println!("{result:?}");
}
```

```powershell
function Get-AnagramGroups {
    param([string[]]$Words)
    # TODO: Implement your solution here
}

Get-AnagramGroups -Words @("eat","tea","tan","ate","nat","bat")
```

## Hints
1. Anagrams have the same characters when sorted
2. Use sorted string as a key in hash map
3. Group strings with same sorted form together
4. Alternative: Use character count as key

## Solution Approaches

**Approach 1: Sorted String as Key**
1. Create a hash map
2. For each string, sort it and use as key
3. Add original string to the list for that key
4. Return all values from hash map

Time Complexity: O(n * k log k) where n is number of strings, k is max length
Space Complexity: O(n * k)

**Approach 2: Character Count as Key**
1. Create a hash map
2. For each string, count character frequencies
3. Use tuple of counts as key (since lists aren't hashable)
4. Add original string to the list for that key
5. Return all values from hash map

Time Complexity: O(n * k)
Space Complexity: O(n * k)

## Key Concepts
- Hash Maps / Dictionaries
- String Sorting
- Character Counting
- Anagrams
