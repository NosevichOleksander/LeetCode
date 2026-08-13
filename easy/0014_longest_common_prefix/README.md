# LeetCode #14 — Longest Common Prefix

## Problem

Given an array of strings `strs`, find the longest common prefix shared by all strings.

If there is no common prefix, return an empty string.

### Examples

```text
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
````

```text
Input: strs = ["dog", "racecar", "car"]
Output: ""
```

---

## Approach

The strings are checked character by character using the same index.

For every position:

1. Take the character from the first string as the expected character.
2. Compare it with the character at the same position in every other string.
3. If any character differs, the common prefix has ended.
4. If any string is shorter than the current position, the common prefix has also ended.

For example:

```text
["flower", "flow", "flight"]

index 0:
f = f = f ✓

index 1:
l = l = l ✓

index 2:
o = o = o ✓

index 3:
w = w ≠ i ✗

Common prefix:
"fl"
```

The prefix is built one character at a time until a mismatch is found.

---

## Complexity

Let:

* `n` be the number of strings.
* `m` be the length of the shortest string.

In the worst case, every character of every string may need to be checked.

### Time Complexity

```text
O(n × m)
```

### Space Complexity

```text
O(m)
```

The resulting prefix can contain up to `m` characters.

---

## Solution

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''

        step = 0

        while True:
            curr = ''

            for string in strs:
                if curr == '' and step < len(string):
                    curr = string[step]

                if step < len(string) and curr != string[step]:
                    return pref
                elif step >= len(string):
                    return pref

            step += 1
            pref += curr
```

---

## Key Idea

The common prefix must contain the same character at every position in every string.

Therefore, instead of comparing entire strings, check them column by column:

```text
flower
flow
flight
^^^^
```

As soon as one column contains different characters, everything after that position cannot be part of the common prefix.

The search can therefore stop immediately at the first mismatch.
