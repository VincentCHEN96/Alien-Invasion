class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        # 重写nums，其元素代表包含第i个元素的最大子序和
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i-1] + nums[i]
        return max(nums)