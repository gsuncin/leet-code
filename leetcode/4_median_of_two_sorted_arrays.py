"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #    [1, 3, 4, 5, 10], [2, 5, 6, 7]
        pass
        
        
        
        
        
        
        
        # merged = sorted(nums1 + nums2)
        # length = len(merged)
        # if length % 2 == 0:
        #     return (merged[length//2] + merged[length//2 - 1]) / 2
        # else:
        #     return merged[length//2]

sol = Solution()
sol.findMedianSortedArrays([1, 3, 4, 5, 10], [2, 5, 6, 7])