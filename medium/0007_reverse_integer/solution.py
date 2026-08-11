class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result

S = Solution()
print(S.reverse(123))
print(S.reverse(-123))
print(S.reverse(120))
print(S.reverse(1534236469))
