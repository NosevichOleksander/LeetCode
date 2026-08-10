# LeetCode #5 — Longest Palindromic Substring

## Problem

Given a string `s`, find the longest palindromic substring in `s`.

A **palindrome** is a string that reads the same forward and backward.

### Example

```text
Input: s = "babad"
Output: "bab"

Explanation:
"aba" is also a valid answer.
```

```text
Input: s = "cbbd"
Output: "bb"
```

---

## Approach

The solution uses the **Expand Around Center** technique.

Every palindrome has a center, so instead of checking every possible substring, we can consider each character as a potential center and expand outward while the characters on both sides are equal.

There are two possible types of centers:

### Odd-length palindrome

```text
  b a b
    ↑
  center
```

The center is a single character.

For each position:

```python
left = i
right = i
```

### Even-length palindrome

```text
  a b b a
    ↑ ↑
   center
```

The center is between two characters.

For each position:

```python
left = i
right = i + 1
```

The window is expanded while:

```python
left >= 0 and right < len(s) and s[left] == s[right]
```

When the characters stop matching or the boundaries of the string are reached, the current palindrome is complete.

The longest palindrome found during the process is stored.

---

## Complexity

There are `n` possible centers, and each center can expand up to `n` characters.

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

Only a few integer variables are used apart from the returned substring.

---

## Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0

        for i in range(len(s)):
            # Odd-length palindrome
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right

                left -= 1
                right += 1

            # Even-length palindrome
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right

                left -= 1
                right += 1

        return s[start:end + 1]
```

---

## Key Idea

Instead of generating every substring and checking whether it is a palindrome, we **start from the center of a potential palindrome and expand outward**.

This avoids repeatedly creating and reversing substrings and reduces the solution from roughly `O(n³)` to `O(n²)`.

The important observation is:

> A palindrome can be completely determined by its center.
