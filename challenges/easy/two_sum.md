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

## Solution Templates (Python 3.11+, Go, Rust, PowerShell Core)

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Find two indices where nums[i] + nums[j] == target."""
    # TODO: Implement your solution here
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All tests passed!")
```

```go
package main

import "fmt"

func twoSum(nums []int, target int) []int {
    // TODO: Implement your solution here
    return []int{}
}

func main() {
    fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
```

```rust
fn two_sum(nums: &[i32], target: i32) -> Option<(usize, usize)> {
    // TODO: Implement your solution here
    None
}

fn main() {
    assert_eq!(two_sum(&[2, 7, 11, 15], 9), Some((0, 1)));
    assert_eq!(two_sum(&[3, 2, 4], 6), Some((1, 2)));
    assert_eq!(two_sum(&[3, 3], 6), Some((0, 1)));
    println!("All tests passed!");
}
```

```powershell
function Get-TwoSum {
    param(
        [int[]]$Nums,
        [int]$Target
    )
    # TODO: Implement your solution here
    return @()
}

# Test cases
$result1 = Get-TwoSum -Nums @(2, 7, 11, 15) -Target 9
if ($result1.Count -ne 2) { throw "Test failed: Expected array of length 2 but got $($result1.Count)" }
if (($result1[0] -ne 0) -or ($result1[1] -ne 1)) {
    throw "Test failed: Expected [0, 1] but got [$($result1 -join ', ')]"
}

$result2 = Get-TwoSum -Nums @(3, 2, 4) -Target 6
if ($result2.Count -ne 2) { throw "Test failed: Expected array of length 2 but got $($result2.Count)" }
if (($result2[0] -ne 1) -or ($result2[1] -ne 2)) {
    throw "Test failed: Expected [1, 2] but got [$($result2 -join ', ')]"
}

$result3 = Get-TwoSum -Nums @(3, 3) -Target 6
if ($result3.Count -ne 2) { throw "Test failed: Expected array of length 2 but got $($result3.Count)" }
if (($result3[0] -ne 0) -or ($result3[1] -ne 1)) {
    throw "Test failed: Expected [0, 1] but got [$($result3 -join ', ')]"
}

Write-Host "All tests passed!" -ForegroundColor Green
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
