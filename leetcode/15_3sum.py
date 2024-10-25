"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

from typing import List


class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     arr = []
    #     if len(nums) < 3:
    #         return []
    #     for i in range(len(nums) - 2):
    #         j, k = len(nums) - 2, len(nums) - 1
    #         while i < j:
    #             triplet = sorted([nums[i], nums[j], nums[k]])
    #             if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and i != k:

    #                 if triplet not in arr:
    #                     arr.append(triplet)
    #             j -= 1
    #             k -= 1
    #     return arr
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    j += 1
                    if [nums[i], nums[j], nums[k]] not in arr:
                        arr.append([nums[i], nums[j], nums[k]])
        return arr
        arr = []
        if len(nums) < 3:
            return []
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                triplet = [nums[i], nums[j], nums[k]]
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    j += 1
                    if triplet not in arr:
                        arr.append(triplet)
        return arr


sol = Solution()
# sol.threeSum([-1, 0, 1, 2, -1, -4])  # [[-1,-1,2],[-1,0,1]]
# sol.threeSum([0, 1, 1])  # []
# sol.threeSum([0, 0, 0])  # [[0,0,0]]
print(sol.threeSum([-2, 0, 1, 1, 2]))  # [[-2,0,2],[-2,1,1]]
# print(sol.threeSum([-1, 0, 1, 0]))  # [[-1,0,1]]
