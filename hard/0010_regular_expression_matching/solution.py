class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        caret_p = 0
        for ch in s:

            print(ch)
            print(f"caret_p: {caret_p}")
            if caret_p < len(p):
                print(f"p[caret_p]: {p[caret_p]}")
            if caret_p + 2 < len(p):
                print(f"p[caret_p+2]: {p[caret_p + 2]}")

            if caret_p + 1 < len(p) and p[caret_p + 1] == '*':
                if p[caret_p] == ch or p[caret_p] == '.':
                    print(f"compared character {ch} to {p[caret_p], caret_p} before asterix")
                    continue
                elif caret_p + 2 < len(p) and (ch == p[caret_p + 2] or p[caret_p + 2] == '.'):
                    print(f"compared character {ch} to {p[caret_p + 2], caret_p + 2} before asterix")
                    if caret_p + 3 < len(p) and p[caret_p + 3] == '*':
                        caret_p += 2
                    else:
                        caret_p += 3
                    continue
                else:
                    print('fail')
                    return False
            elif caret_p < len(p):
                if p[caret_p] == ch or p[caret_p] == '.':
                    print(f"compared character {ch} to {p[caret_p], caret_p}")
                    caret_p += 1
                    continue
                else:
                    print("lower fail")
                    return False
            else:
                return False
        return True

S = Solution()
print(S.isMatch('aa', 'a'))
print(S.isMatch('aa', 'a*'))
print(S.isMatch('ab', '.*'))
print(S.isMatch("mississippi", "mis*is*ip*."))
print(S.isMatch("ab", ".*c"))

