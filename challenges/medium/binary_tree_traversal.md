# Binary Tree Level Order Traversal

## Problem Description
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: [[3],[9,20],[15,7]]
```

**Example 2:**
```
Input: root = [1]
Output: [[1]]
```

**Example 3:**
```
Input: root = []
Output: []
```

## Constraints
- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000

## Solution Template (Python)

```python
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Return level order traversal of binary tree
    
    Args:
        root: Root node of binary tree
    
    Returns:
        List of lists, each containing values at that level
    """
    # TODO: Implement your solution here
    pass


# Test helper
def build_tree(values: List) -> Optional[TreeNode]:
    """Build a tree from list representation"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    tree1 = build_tree([3, 9, 20, None, None, 15, 7])
    assert level_order_traversal(tree1) == [[3], [9, 20], [15, 7]]
    
    tree2 = build_tree([1])
    assert level_order_traversal(tree2) == [[1]]
    
    tree3 = build_tree([])
    assert level_order_traversal(tree3) == []
    
    print("All tests passed!")
```

## Hints
1. Use BFS (Breadth-First Search) with a queue
2. Process nodes level by level
3. Track the number of nodes at each level
4. Use a queue data structure (deque in Python)

## Solution Approach - BFS
1. If root is None, return empty list
2. Initialize queue with root node
3. While queue is not empty:
   - Get current level size
   - Create list for current level values
   - Process all nodes at current level
   - Add children to queue for next level
4. Return result

Time Complexity: O(n) - visit each node once
Space Complexity: O(n) - queue can hold up to n/2 nodes

## Key Concepts
- Binary Trees
- Breadth-First Search (BFS)
- Queue Data Structure
- Level Order Traversal
