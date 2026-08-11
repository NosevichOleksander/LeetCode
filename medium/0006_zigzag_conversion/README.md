# LeetCode #6 — Zigzag Conversion

## Problem

Given a string `s` and an integer `numRows`, rearrange the characters of the string in a zigzag pattern across the specified number of rows and then read the rows from top to bottom.

### Example

```text
Input: s = "PAYPALISHIRING", numRows = 3

P   A   H   N
A P L S I I G
Y   I   R

Output: "PAHNAPLSIIGYIR"
```

If `numRows == 1`, the string does not change.

---

## Approach

The solution simulates movement through the rows instead of calculating the position of every character mathematically.

Two variables are used:

* `last` — current row;
* `diff` — current direction (`1` means moving down, `-1` means moving up).

Each character is added to the current row:

```python
temp[last].append(ch)
```

Then the current row is changed according to the direction:

```python
last += diff
```

When the top or bottom row is reached, the direction is reversed:

```python
if last == 0 or last == numRows - 1:
    diff = -diff
```

After all characters have been processed, the rows are joined together.

---

## Complexity

Every character is processed exactly once.

### Time Complexity

```text
O(n)
```

where `n` is the length of the input string.

### Space Complexity

```text
O(n)
```

The characters are stored in the row lists before constructing the result.

---

## Solution

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        temp = [[] for _ in range(numRows)]
        last = 0
        diff = 1

        for ch in s:
            temp[last].append(ch)

            last += diff

            if last == 0 or last == numRows - 1:
                diff = -diff

        return ''.join(''.join(row) for row in temp)
```

---

## Key Idea

Instead of trying to calculate the exact index of every character in the zigzag pattern, simulate the movement through the rows.

The direction changes whenever the current position reaches either end:

```text
↓
↓
↓
↑
↑
↑
↓
↓
↓
```

This produces a simple linear-time solution without explicitly constructing the two-dimensional zigzag.
