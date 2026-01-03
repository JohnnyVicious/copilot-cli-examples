# Word Ladder

## Problem Description
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or 0 if no such sequence exists.

## Examples

**Example 1:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
```

**Example 2:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

## Constraints
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters
- beginWord != endWord
- All the words in wordList are unique

## Solution Templates (Python 3.11+, Go, Rust, PowerShell Core)

```python
from typing import List
from collections import deque


def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """Find shortest transformation sequence length."""
    # TODO: Implement your solution here
    return 0


if __name__ == "__main__":
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladder_length("a", "c", ["a", "b", "c"]) == 2
    print("All tests passed!")
```

```go
package main

import "fmt"

func ladderLength(beginWord string, endWord string, wordList []string) int {
    // TODO: Implement your solution here
    return 0
}

func main() {
    fmt.Println(ladderLength("hit", "cog", []string{"hot", "dot", "dog", "lot", "log", "cog"}))
}
```

```rust
fn ladder_length(begin_word: &str, end_word: &str, word_list: Vec<String>) -> usize {
    // TODO: Implement your solution here
    0
}

fn main() {
    let length = ladder_length(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"]
            .iter()
            .map(|s| s.to_string())
            .collect(),
    );
    println!("{length}");
}
```

```powershell
function Get-WordLadderLength {
    param(
        [string]$BeginWord,
        [string]$EndWord,
        [string[]]$WordList
    )
    # TODO: Implement your solution here
}

Get-WordLadderLength -BeginWord "hit" -EndWord "cog" -WordList @("hot","dot","dog","lot","log","cog")
```

## Hints
1. This is a shortest path problem - use BFS
2. Think of words as nodes in a graph
3. Two words are connected if they differ by exactly one letter
4. Use BFS from beginWord to find shortest path to endWord
5. Optimize by preprocessing words into groups by pattern

## Solution Approach - BFS with Preprocessing

**Step 1: Preprocessing**
Create a dictionary mapping word patterns to words:
- "h*t" -> ["hot", "hit"]
- "*ot" -> ["hot", "dot", "lot"]
- etc.

**Step 2: BFS**
1. If endWord not in wordList, return 0
2. Initialize queue with (beginWord, 1)
3. Keep track of visited words
4. For each word in queue:
   - Generate all patterns (change each letter to *)
   - Find all words matching each pattern
   - If word is endWord, return current length
   - Add unvisited words to queue with length + 1
5. If queue empty and endWord not found, return 0

Time Complexity: O(M^2 × N) where M is word length, N is number of words
Space Complexity: O(M^2 × N)

## Key Concepts
- Graph Theory
- Breadth-First Search (BFS)
- Shortest Path
- String Manipulation
- Pattern Matching
