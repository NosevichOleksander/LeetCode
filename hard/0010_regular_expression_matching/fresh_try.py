class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sp = 0
        pp = 0
        backtracks = []
        while True:
            print(f"backtracks: {backtracks}")
            print(f"sp: {sp}, pp: {pp}")
            if pp+1 < len(p) and p[pp+1] == '*':
                if (sp, pp) not in backtracks:
                    backtracks.append((sp, pp))
                    pp += 2
                else:
                    sp += 1
                    pp += 1
            elif pp < len(p):
                if s[sp] == p[pp]:
                    sp += 1
                    pp += 1
                    continue
                else:
                    if backtracks and (sp, pp) in backtracks:
                        sp, pp = backtracks.pop()
                    else:
                        return False






S = Solution()
print(S.isMatch('aa', 'a'))
#print(S.isMatch('aab', 'c*a*b'))
#print(S.isMatch('ab', '.*'))
#print(S.isMatch("mississippi", "mis*is*ip*."))
#print(S.isMatch("ab", ".*c"))