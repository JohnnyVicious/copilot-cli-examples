# Merge K Sorted Lists

## Problem Description
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Examples

**Example 1:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Example 2:**
```
Input: lists = []
Output: []
```

**Example 3:**
```
Input: lists = [[]]
Output: []
```

## Constraints
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

## Solution Template (Python)

```python
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists
    
    Args:
        lists: List of k sorted linked list heads
    
    Returns:
        Head of merged sorted linked list
    """
    # TODO: Implement your solution here
    pass


# Helper functions for testing
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    """Convert array to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    lists1 = [
        list_to_linkedlist([1, 4, 5]),
        list_to_linkedlist([1, 3, 4]),
        list_to_linkedlist([2, 6])
    ]
    result1 = merge_k_lists(lists1)
    assert linkedlist_to_list(result1) == [1, 1, 2, 3, 4, 4, 5, 6]
    
    lists2 = []
    result2 = merge_k_lists(lists2)
    assert linkedlist_to_list(result2) == []
    
    lists3 = [list_to_linkedlist([])]
    result3 = merge_k_lists(lists3)
    assert linkedlist_to_list(result3) == []
    
    print("All tests passed!")
```

## Hints
1. Use a min heap (priority queue) to efficiently get the smallest element
2. Insert the first node from each list into the heap
3. Extract minimum, add to result, and insert next node from same list
4. Alternative: Merge lists pairwise (divide and conquer)

## Solution Approaches

**Approach 1: Min Heap (Priority Queue)**
1. Create a min heap with first node from each list
2. While heap is not empty:
   - Extract minimum node
   - Add to result list
   - If extracted node has a next, add next to heap
3. Return merged list

Time Complexity: O(N log k) where N is total nodes, k is number of lists
Space Complexity: O(k) for the heap

**Approach 2: Divide and Conquer**
1. Pair up k lists and merge each pair
2. After first round, k lists are merged into k/2 lists
3. Repeat until only one list remains

Time Complexity: O(N log k)
Space Complexity: O(1) if not counting recursion stack

## Key Concepts
- Min Heap / Priority Queue
- Linked Lists
- Divide and Conquer
- Merge Sort Principles
