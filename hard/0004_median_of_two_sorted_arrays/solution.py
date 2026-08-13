class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_len = len(nums1) + len(nums2)
        p1 = 0
        p2 = 0
        #while p1 + p2 < total_len//2-1:
        for _ in range(total_len//2):
            if nums1[p1] < nums2[p2]:
                if p1 != len(nums1)-1:
                    p1 += 1
                    flip = False
                else:
                    p2 += 1
                    flip = True
            else:
                if p2 != len(nums2)-1:
                    p2 += 1
                    flip = True
                else:
                    p1 += 1
                    flip = False
            if p1 + p2 > total_len//2-1:
                return nums1[p1-1] if flip==False else nums2[p2-1]
"""
Unfinished, too silly :c
"""