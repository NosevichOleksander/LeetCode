# LeetCode #13 — Roman to Integer

## Problem

Given a string containing a Roman numeral, convert it to an integer.

Roman numerals use the following symbols:

```text
I     = 1
V     = 5
X     = 10
L     = 50
C     = 100
D     = 500
M     = 1000
````

Some combinations use subtractive notation:

```text
IV   = 4
IX   = 9
XL   = 40
XC   = 90
CD   = 400
CM   = 900
```

### Examples

```text
Input: s = "III"
Output: 3
```

```text
Input: s = "LVIII"
Output: 58
```

```text
Input: s = "MCMXCIV"
Output: 1994
```

---

## Approach

The Roman numeral is processed from left to right.

For each character, its value is compared with the value of the next character.

If the current value is greater than or equal to the next value, it is added to the result:

```text
VI

V >= I
5 + 1 = 6
```

If the current value is smaller than the next value, the current value is part of a subtractive combination and the difference is added:

```text
IV

I < V
5 - 1 = 4
```

After processing a subtractive pair, both characters are skipped.

For example:

```text
MCMXCIV

M   → +1000
CM  → +900
XC  → +90
IV  → +4

Result = 1994
```

A dictionary is used to map Roman numeral characters to their integer values.

---

## Complexity

Each character is processed at most once.

### Time Complexity

```text
O(n)
```

where `n` is the length of the Roman numeral.

### Space Complexity

```text
O(1)
```

The dictionary contains a fixed number of Roman numeral symbols.

---

## Solution

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        num = 0

        while s:
            if (len(s) > 1 and romans[s[0]] >= romans[s[1]]) or len(s) == 1:
                num += romans[s[0]]
                s = s[1:]

            elif len(s) > 1 and romans[s[0]] < romans[s[1]]:
                num += romans[s[1]] - romans[s[0]]
                s = s[2:]

        return num
```

---

## Key Idea

The important rule is:

```text
current >= next → add current
current < next   → subtract current from next
```

This single comparison handles all subtractive Roman numeral combinations:

```text
IV   → 4
IX   → 9
XL   → 40
XC   → 90
CD   → 400
CM   → 900
```

Therefore, there is no need to explicitly check for each special combination.