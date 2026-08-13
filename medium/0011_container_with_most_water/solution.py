class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_volume = min(height[left], height[right])*(right-left)
        while left != right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_volume = max(max_volume, min(height[left], height[right])*(right-left))
        return max_volume