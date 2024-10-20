from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dp = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                k = j +1
                if k > len(nums)-1 or i == j:
                    continue
                elif k > len(nums) - 1:
                    break
                elif nums[i] + nums[j] + nums[k] == 0:
                    add = sorted([nums[i], nums[j], nums[k]])
                    if add in dp:
                        continue
                    dp.append(add)
        return dp
    
sol = Solution()
# print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([-2,0,1,1,2]))  # [[-2,0,2],[-2,1,1]]
