# LeetCode #12 — Integer to Roman

## Problem

Given an integer `num`, convert it to its Roman numeral representation.

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

Certain values use subtractive notation:

```text
4    → IV
9    → IX
40   → XL
90   → XC
400  → CD
900  → CM
```

### Examples

```text
Input: num = 3
Output: "III"
```

```text
Input: num = 58
Output: "LVIII"
```

```text
Input: num = 1994
Output: "MCMXCIV"
```

---

## Approach

The number is split into its thousands, hundreds, tens, and ones digits.

Each digit is converted independently using a lookup table.

For example:

```text
1994

1000 → 1 → M
 900 → 9 → CM
  90 → 9 → XC
   4 → 4 → IV
```

Result:

```text
MCMXCIV
```

Separate lookup tables are used for each decimal position:

```python
ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

thousands = ['', 'M', 'MM', 'MMM']
```

The digits are extracted using integer division and modulo:

```python
num // 1000
num % 1000
num // 100
num % 100
...
```

This avoids a large number of `if` statements for the special cases.

---

## Complexity

The number of decimal positions is fixed, so the amount of work does not depend on the size of `num`.

### Time Complexity

```text
O(1)
```

### Space Complexity

```text
O(1)
```

Only a fixed number of lookup tables and variables are used.

---

## Solution

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['', 'M', 'MM', 'MMM']

        roman = thousands[num // 1000]
        num = num % 1000

        roman += hundreds[num // 100]
        num = num % 100

        roman += tens[num // 10]
        num = num % 10

        roman += ones[num]

        return roman
```

---

## Key Idea

Roman numeral notation can be divided into four independent decimal positions:

```text
thousands | hundreds | tens | ones
```

Each position has only 10 possible values (`0`–`9`), so a lookup table is simpler and clearer than a large collection of conditional statements.

For example:

```text
1994
 ↓
1    9    9    4
 ↓    ↓    ↓    ↓
M    CM   XC   IV
 ↓
MCMXCIV
```
