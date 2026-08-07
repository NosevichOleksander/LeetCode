# LeetCode #3 — Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

### Example

```
Input: s = "abcabcbb"
Output: 3

Explanation:
The answer is "abc", with the length of 3.
```

```
Input: s = "bbbbb"
Output: 1

Explanation:
The answer is "b", with the length of 1.
```

```
Input: s = "pwwkew"
Output: 3

Explanation:
The answer is "wke", with the length of 3.
```

---

## Approach

The solution uses the **Sliding Window** technique.

Instead of checking every possible substring, we maintain a dynamic window that always contains only unique characters.

Two pointers are used:

* `left` — the left boundary of the current window
* `right` — the right boundary of the current window

A dictionary `seen` stores the last position where each character appeared.

When a repeated character is found:

1. Move the left boundary past the previous occurrence of this character.
2. Continue expanding the window.
3. Update the maximum window size.

### Example

For:

```
abcabcbb
```

The window changes like this:

```
[a]
[ab]
[abc]
[bca]
[cab]
[abc]
[cb]
[b]
```

The longest window contains 3 characters.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

Each character is processed at most twice:

* once when entering the window;
* once when the left pointer moves past it.

### Space Complexity

```
O(k)
```

where `k` is the number of unique characters stored in the dictionary.

---

## Solution

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        max_window = 0
        left = 0

        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left, seen[ch] + 1)

            seen[ch] = right

            max_window = max(max_window, right - left + 1)

        return max_window
```

---

## Key Idea

The main optimization is avoiding rebuilding substrings.

A brute-force approach creates every possible substring and checks it for duplicates, resulting in `O(n²)` or worse.

The sliding window approach keeps a valid substring at all times and only moves the boundaries when necessary, reducing the complexity to `O(n)`.
