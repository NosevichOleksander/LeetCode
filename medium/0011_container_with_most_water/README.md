# LeetCode #11 — Container With Most Water

## Problem

Given an integer array `height` where each element represents the height of a vertical line, find two lines that together with the x-axis form a container containing the most water.

The amount of water is determined by:

```text
area = width × min(left_height, right_height)
````

### Examples

```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

```text
Input: height = [1,1]
Output: 1
```

---

## Approach

The solution uses two pointers:

* `left` starts at the beginning of the array.
* `right` starts at the end of the array.

The initial container has the maximum possible width.

For each pair of walls, the area is calculated using the height of the shorter wall:

```python
min(height[left], height[right]) * (right - left)
```

After calculating the area, the pointer corresponding to the shorter wall is moved inward.

If:

```python
height[left] < height[right]
```

the `left` pointer is moved.

Otherwise, the `right` pointer is moved.

The reason is that the shorter wall limits the container's height. Moving the taller wall would only decrease the width without giving the container a chance to become taller.

The maximum area found during the traversal is stored in `max_volume`.

---

## Complexity

Each pointer moves through the array at most once.

### Time Complexity

```text
O(n)
```

where `n` is the number of elements in `height`.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are used.

---

## Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_volume = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            max_volume = max(
                max_volume,
                min(height[left], height[right]) * (right - left)
            )

        return max_volume
```

---

## Key Idea

Instead of checking every possible pair of walls in `O(n²)`, use two pointers starting at opposite ends of the array.

The width is largest at the beginning, so moving the taller wall cannot improve the area while the shorter wall remains the limiting factor.

Therefore, always move the pointer at the shorter wall and look for a taller one.

This reduces the solution from:

```text
O(n²)
```

to:

```text
O(n)
```

