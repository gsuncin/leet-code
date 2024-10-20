from typing import List


class Solution:
    def findDuplicated(self, nums: List[int]) -> int:
        set_nums = set()
        for n in range(len(nums)):
            if nums[n] in set_nums:
                return nums[n]
            set_nums.add(nums[n])
        return -1
sol = Solution()
print(sol.findDuplicated([1, 3, 4, 2]))
print(sol.findDuplicated([3, 1, 3, 4, 2]))
print(sol.findDuplicated([1, 1]))