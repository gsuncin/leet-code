from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [2, 5, 7, 11, 15]

        # Sol 1 -> O(N)
        set_of_nums = set()
        for i in range(len(nums)):
            if target - nums[i] in set_of_nums:
                return [i, nums.index(target - nums[i])]
            set_of_nums.add(nums[i])
        
        # Sol 2 O(Nˆ2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]