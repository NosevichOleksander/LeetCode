class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0

        for i in range(len(s)):
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right

                left -= 1
                right += 1

            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right

                left -= 1
                right += 1

        return s[start:end + 1]
s = Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbb'))
print(s.longestPalindrome('a'))
