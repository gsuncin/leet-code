from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[n] = nums[i]
                n+=1
        return len(nums)

            
    
sol = Solution()
sol.removeDuplicates([1,1,2])  # 2
sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])  # 5