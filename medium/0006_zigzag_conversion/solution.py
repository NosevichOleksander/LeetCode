class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp = [[] for _ in range(numRows)]
        last = 0
        diff = 1
        for ch in s:
            temp[last].append(ch)
            last += diff
            if last == 0 or last == numRows - 1:
                diff = -diff
        return ''.join(''.join(row) for row in temp)
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        crypt = ''
        for row in range(numRows):
            if row == 0:
                crypt += s[0::(numRows * 2) - 2]
            elif row == numRows - 1:
                temp, sub = enumerate(list(s[row::(numRows * 2) - 2]))
                print(temp, sub)
                #temp = temp.insert((-i-1 for i in range(len(sub)-1)), )
                #crypt += sub
        return crypt

Gonna leave this unfinished first try just for the funsies, really got me scratching the head
"""
S = Solution()
print(S.convert('PAYPALISHIRING', 3))
print(S.convert('PAYPALISHIRING', 4))