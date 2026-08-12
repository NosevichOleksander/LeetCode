# LeetCode #8 — String to Integer (atoi)

## Problem

Implement the `myAtoi` function, which converts a string into a 32-bit signed integer.

The function should:

1. Ignore leading whitespace.
2. Determine the sign (`+` or `-`).
3. Read consecutive digits.
4. Stop reading at the first non-digit character.
5. Return the resulting integer.
6. Clamp the result to the 32-bit signed integer range:

```text
[-2³¹, 2³¹ - 1]
````

### Examples

```text
Input: s = "42"
Output: 42
```

```text
Input: s = "   -42"
Output: -42
```

```text
Input: s = "4193 with words"
Output: 4193
```

```text
Input: s = "words and 987"
Output: 0
```

```text
Input: s = "-91283472332"
Output: -2147483648
```

---

## Approach

The string is processed from left to right using an index `caret`.

First, leading spaces are skipped:

```python
while caret < len(s) and s[caret] == ' ':
    caret += 1
```

Then the sign is determined:

```python
if caret < len(s) and s[caret] in '-+':
    sign = -1 if s[caret] == '-' else 1
    caret += 1
```

The number is built digit by digit:

```python
answ = answ * 10 + int(s[caret])
```

For example:

```text
0 → 1 → 12 → 123 → 1234
```

The process stops when a non-digit character or the end of the string is reached.

Finally, the sign is applied and the result is clamped to the 32-bit signed integer range.

---

## Complexity

Each character is processed at most once.

### Time Complexity

```text
O(n)
```

where `n` is the length of the input string.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are used.

---

## Solution

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        caret = 0
        answ = 0

        # Skip leading spaces
        while caret < len(s) and s[caret] == ' ':
            caret += 1

        # Determine sign
        if caret < len(s) and s[caret] in '-+':
            sign = -1 if s[caret] == '-' else 1
            caret += 1

        # Read digits
        while caret < len(s) and s[caret] in '0123456789':
            answ = answ * 10 + int(s[caret])
            caret += 1

        answ *= sign

        # Clamp to 32-bit signed integer range
        if answ < -2**31:
            answ = -2**31
        elif answ > 2**31 - 1:
            answ = 2**31 - 1

        return answ
```

---

## Key Idea

Instead of converting the entire string directly into an integer, the number is constructed manually by processing each digit:

```text
result = result * 10 + digit
```

The input is traversed once, while leading spaces, an optional sign, consecutive digits, and integer overflow are handled separately.
