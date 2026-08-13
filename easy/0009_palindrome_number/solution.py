class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverted = 0
        while temp > 0:
            reverted = reverted*10 + temp%10
            temp = temp//10
        return reverted == x

S = Solution()
print(S.isPalindrome(121))
print(S.isPalindrome(-121))
print(S.isPalindrome(10))