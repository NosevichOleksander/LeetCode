class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        while s or p:
            substring_pattern = ''
            for i in p:
                if i != '*' and i != '.':
                    substring_pattern += i
                elif i == '.':
                    break
                else:
                    substring_pattern = substring_pattern[:-1]
                    break
            print(f"substring_pattern: {substring_pattern}")
            if s.startswith(substring_pattern):
                s = s[len(substring_pattern):]
                p = p[len(substring_pattern):]
            print(f"s: {s}, p: {p}")
            while len(p) > 1 and p[0] == "." and p[1] != '*':
                s = s[1:]
                p = p[1:]
            if len(p) == 1 and p[0] == ".":
                s = s[1:]
                p = p[1:]
            if len(p) > 1 and p[1] == '*' and p[0] != ".":
                while p and s and p[-1] == s[-1]:
                    p = p[:-1]
                    s = s[:-1]
                s = s.lstrip(p[0])
                p = p[2:]
            elif len(p) > 1 and p[1] == '*' and p[0] == ".":
                sep = s.rfind(p[2::])
                print(sep)
                if sep == -1:
                    p = p[2::]
                    if len(p) > 1 and p[1] == '*' and p[0] != ".":
                        while p and s and p[-1] == s[-1]:
                            p = p[:-1]
                            s = s[:-1]
                        s = s.lstrip(p[0])
                        p = p[2:]
                        print(s , p)
                        if s == p:
                            return True
                    return False
                else:
                    return True
            else:
                if s == p:
                    return True
                print(s, p)
                print('ts pmo')
                return False
        return True

S = Solution()
#print(S.isMatch('aa', 'a'))
print(S.isMatch('aab', 'c*a*b'))
#print(S.isMatch('ab', '.*'))
#print(S.isMatch("mississippi", "mis*is*ip*."))
#print(S.isMatch("ab", ".*c"))