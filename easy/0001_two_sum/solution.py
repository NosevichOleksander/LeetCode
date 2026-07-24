class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, e in enumerate(nums):
            if target - e in seen:
                return [seen[target - e], i]

            seen[e] = i

if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))
    print(s.twoSum([3,3], 6))