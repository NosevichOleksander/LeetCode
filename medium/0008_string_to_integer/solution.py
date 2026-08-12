class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        caret = 0
        answ = 0
        while caret < len(s) and s[caret] == ' ':
            caret += 1
        if caret < len(s) and s[caret] in '-+':
            sign = -1 if s[caret] == '-' else 1
            caret += 1
        while caret < len(s) and s[caret] in '0123456789':
            answ = answ*10 + int(s[caret])
            caret += 1
        answ *= sign
        if answ < -2**31:
            answ = -2**31
        elif answ > 2**31 -1:
            answ = 2**31 - 1
        return answ

S = Solution()
print(S.myAtoi('42'))
print(S.myAtoi('   -42'))
print(S.myAtoi('4193 with words'))
print(S.myAtoi('words and 987'))
print(S.myAtoi('-91283472332'))