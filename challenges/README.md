# Coding Challenges

This directory contains algorithmic coding challenges organized by difficulty level.

## Structure

```
challenges/
├── easy/       # Beginner-friendly challenges
├── medium/     # Intermediate challenges
└── hard/       # Advanced challenges
```

## Challenge Format

Each challenge includes:
- **Problem Description** - Clear explanation of the task
- **Examples** - Input/output examples with explanations
- **Constraints** - Limitations and edge cases
- **Solution Templates** - Code skeletons with test cases for Python 3.11+, Go, Rust, and PowerShell Core
- **Hints** - Guidance without spoiling the solution
- **Approach** - Detailed solution strategy
- **Complexity Analysis** - Time and space complexity

## Easy Challenges

### 1. Two Sum
**File:** `easy/two_sum.md`  
**Topics:** Arrays, Hash Maps  
**Complexity:** O(n) time, O(n) space

Find two numbers in an array that add up to a target value.

### 2. Palindrome Number
**File:** `easy/palindrome_number.md`  
**Topics:** Math, String Manipulation  
**Complexity:** O(log n) time, O(1) space

Determine if an integer is a palindrome without converting to string.

### 3. Valid Parentheses
**File:** `easy/valid_parentheses.md`  
**Topics:** Stack, String  
**Complexity:** O(n) time, O(n) space

Check if brackets are properly matched and nested.

## Medium Challenges

### 1. Longest Substring Without Repeating Characters
**File:** `medium/longest_substring.md`  
**Topics:** Sliding Window, Hash Map  
**Complexity:** O(n) time, O(min(m,n)) space

Find the length of the longest substring without repeating characters.

### 2. Binary Tree Level Order Traversal
**File:** `medium/binary_tree_traversal.md`  
**Topics:** Trees, BFS, Queue  
**Complexity:** O(n) time, O(n) space

Traverse a binary tree level by level from left to right.

### 3. Group Anagrams
**File:** `medium/group_anagrams.md`  
**Topics:** Hash Map, String Sorting  
**Complexity:** O(n*k log k) time, O(n*k) space

Group strings that are anagrams of each other.

## Hard Challenges

### 1. Merge K Sorted Lists
**File:** `hard/merge_k_sorted_lists.md`  
**Topics:** Linked Lists, Heap, Divide and Conquer  
**Complexity:** O(N log k) time, O(k) space

Merge k sorted linked lists into one sorted list.

### 2. Word Ladder
**File:** `hard/word_ladder.md`  
**Topics:** BFS, Graph, Shortest Path  
**Complexity:** O(M²*N) time, O(M²*N) space

Find the length of the shortest transformation sequence from beginWord to endWord.

### 3. Minimum Window Substring
**File:** `hard/minimum_window_substring.md`  
**Topics:** Sliding Window, Hash Map  
**Complexity:** O(m+n) time, O(m+n) space

Find the minimum window substring containing all characters from a target string.

## How to Use These Challenges

### Step 1: Read the Challenge
Open the markdown file and read the problem description carefully.

```bash
cat challenges/easy/two_sum.md
```

### Step 2: Understand Examples
Study the provided examples to understand input/output format and edge cases.

### Step 3: Implement Solution
Choose your preferred language (Python 3.11+, Go, Rust, or PowerShell Core), copy the matching solution template, and implement your solution:

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    # Your implementation here
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Step 4: Test Your Solution
Run the provided test cases to verify correctness:

```python
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All tests passed!")
```

### Step 5: Analyze Complexity
Review the hints and complexity analysis to understand if your solution is optimal.

## Using GitHub Copilot

### Getting Help
When implementing solutions, use Copilot effectively:

```python
# Example: Ask Copilot for implementation
def length_of_longest_substring(s: str) -> int:
    """
    Find longest substring without repeating characters.
    Use sliding window with hash map to track character positions.
    """
    # Copilot will suggest implementation based on docstring
```

### Asking for Optimizations
```python
# TODO: Optimize this solution to O(n) time complexity
# Current solution is O(n²), need to use hash map
```

### Requesting Test Cases
```python
# TODO: Generate edge case tests for empty string, single character,
# all unique characters, all same characters
```

## Tips for Success

### 1. Start Simple
Begin with easy challenges to build confidence and understanding.

### 2. Think Before Coding
Spend time understanding the problem and planning your approach.

### 3. Consider Edge Cases
- Empty inputs
- Single element inputs
- Duplicate values
- Maximum/minimum constraints
- Special characters

### 4. Analyze Complexity
Always consider time and space complexity of your solution.

### 5. Try Multiple Approaches
Many problems have multiple solutions with different trade-offs.

### 6. Test Thoroughly
Run all provided test cases and create your own.

## Common Patterns

### Arrays & Hashing
- Two pointers
- Sliding window
- Hash maps for O(1) lookups
- Prefix sums

### Trees & Graphs
- Depth-first search (DFS)
- Breadth-first search (BFS)
- Level order traversal
- Tree/graph traversal patterns

### Linked Lists
- Two pointers (fast/slow)
- Reverse operations
- Merge operations
- Cycle detection

### Dynamic Programming
- Memoization
- Tabulation
- State machines
- Optimal substructure

### Strings
- Two pointers
- Sliding window
- Pattern matching
- Character counting

## Learning Path

### Week 1: Easy Challenges
- Day 1-2: Two Sum
- Day 3-4: Palindrome Number
- Day 5-7: Valid Parentheses

### Week 2: Medium Challenges
- Day 1-3: Longest Substring
- Day 4-5: Binary Tree Traversal
- Day 6-7: Group Anagrams

### Week 3+: Hard Challenges
- Days 1-4: Merge K Sorted Lists
- Days 5-8: Word Ladder
- Days 9+: Minimum Window Substring

## Additional Resources

- **LeetCode** - More practice problems
- **HackerRank** - Algorithm practice
- **Project Euler** - Mathematical challenges
- **Codeforces** - Competitive programming

## Contributing

To add a new challenge:

1. Create a markdown file in the appropriate difficulty directory
2. Follow the standard format with all sections
3. Include clear problem description
4. Provide solution template with test cases
5. Add hints and complexity analysis
6. Update this README with the new challenge

---

**Happy Coding!** 🚀

Remember: The goal is to learn and improve. Don't be discouraged if you don't solve a problem immediately. Use hints, learn from solutions, and try again!
