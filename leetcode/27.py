class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                count += 1
                continue
            i += 1
        return len(nums)