class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        i = 0
        while i <= len(nums):
            if i < len(nums) and nums[i] < target:
                i += 1
            else:
                return i