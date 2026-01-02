# Two Sum Challenge

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

## Solution Template (Python)

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two indices where nums[i] + nums[j] == target
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List containing two indices
    """
    # TODO: Implement your solution here
    pass


# Test cases
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All tests passed!")
```

## Hints
1. Try using a hash map to store the numbers you've seen
2. For each number, check if `target - number` exists in the hash map
3. Time complexity goal: O(n)
4. Space complexity goal: O(n)

## Solution Approach
The efficient solution uses a hash map to achieve O(n) time complexity:
1. Create a hash map to store number -> index
2. Iterate through the array
3. For each number, calculate complement = target - number
4. If complement exists in hash map, return [hash_map[complement], current_index]
5. Otherwise, add current number to hash map
