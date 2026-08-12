# LeetCode #9 — Palindrome Number

## Problem

Given an integer `x`, determine whether it is a palindrome.

A palindrome number reads the same forward and backward.

### Examples

```text
Input: x = 121
Output: true
````

```text
Input: x = -121
Output: false
```

```text
Input: x = 10
Output: false
```

---

## Approach

The solution reverses the digits of the number and compares the result with the original value.

The last digit is extracted using:

```python
temp % 10
```

It is then added to the reversed number:

```python
reverted = reverted * 10 + temp % 10
```

After extracting the digit, it is removed from the original number:

```python
temp //= 10
```

For example, for `12321`:

```text
12321 → 1232 → 123 → 12 → 1 → 0
```

The extracted digits are used to construct:

```text
0 → 1 → 12 → 123 → 1232 → 12321
```

Finally, the reversed number is compared with the original number.

Negative numbers automatically return `False`, because the loop only executes while `temp > 0`.

---

## Complexity

The number of iterations is proportional to the number of digits in `x`.

### Time Complexity

```text
O(log₁₀(n))
```

where `n` is the value of `x`.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are used.

---

## Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverted = 0

        while temp > 0:
            reverted = reverted * 10 + temp % 10
            temp //= 10

        return reverted == x
```

---

## Key Idea

Instead of converting the number into a string, reverse it mathematically using `%` and `//`.

The number is processed digit by digit:

```text
last digit = number % 10
remove digit = number // 10
```

The resulting reversed number is then compared with the original number.

If they are equal, the number is a palindrome.
