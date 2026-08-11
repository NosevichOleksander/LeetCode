# LeetCode #7 — Reverse Integer

## Problem

Given a signed 32-bit integer `x`, return its digits reversed.

If the reversed integer is outside the signed 32-bit integer range:

```text
[-2³¹, 2³¹ - 1]
```

return `0`.

### Examples

```text
Input: x = 123
Output: 321
```

```text
Input: x = -123
Output: -321
```

```text
Input: x = 120
Output: 21
```

```text
Input: x = 1534236469
Output: 0
```

The last example overflows the 32-bit signed integer range after reversal.

---

## Approach

The number is reversed digit by digit.

The last digit can be obtained using:

```python
x % 10
```

After extracting the digit, it is removed from `x` using integer division:

```python
x //= 10
```

The extracted digit is appended to the result by shifting the existing digits one position to the left:

```python
result = result * 10 + digit
```

The process continues until all digits have been processed.

The sign of the original number is preserved.

Finally, the result is checked against the 32-bit signed integer limits.

---

## Complexity

Each digit is processed exactly once.

### Time Complexity

```text
O(log₁₀(n))
```

because the number of digits in `n` is proportional to `log₁₀(n)`.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are required.

---

## Solution

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
```

---

## Key Idea

Instead of converting the integer into a string and reversing it, process its digits mathematically.

For example:

```text
1234

1234 % 10 → 4
1234 // 10 → 123

123 % 10 → 3
123 // 10 → 12

12 % 10 → 2
12 // 10 → 1

1 % 10 → 1
1 // 10 → 0
```

The extracted digits are then accumulated into the reversed number:

```text
0 → 4 → 43 → 432 → 4321
```

The final step is checking whether the result fits into the required 32-bit signed integer range.
