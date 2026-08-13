class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['', 'M', 'MM', 'MMM']
        roman = thousands[num//1000]
        num = num%1000
        roman += hundreds[num//100]
        num = num%100
        roman += tens[num//10]
        num = num%10
        roman += ones[num]
        return roman
"""
Actual solution is so straightforward that i tried to overcomplicate and lost like an hour.
Gotta put first try into separate file for the giggles.
"""

S = Solution()
print(S.intToRoman(3))
print(S.intToRoman(58))
print(S.intToRoman(1994))

