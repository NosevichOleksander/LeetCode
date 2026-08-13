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
                num += (romans[s[1]] - romans[s[0]])
                s = s[2:]

        return num