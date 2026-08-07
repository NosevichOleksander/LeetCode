class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        max_window = 0
        left = 0

        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left, seen[ch] + 1)

            seen[ch] = right

            max_window = max(max_window, right - left + 1)

        return max_window

S = Solution()
print(S.lengthOfLongestSubstring('abcabcbb'))
print(S.lengthOfLongestSubstring('bbbbb'))
print(S.lengthOfLongestSubstring('pwwkew'))