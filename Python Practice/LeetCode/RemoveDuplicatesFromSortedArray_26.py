class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i = 1   #结果数组元素计数器
        while i < len(set(nums)):
            j = 1
            while j < len(nums):
                if nums[j] != nums[j-1]:
                    nums[i] = nums[j]
                    i += 1
                j += 1
        return len(set(nums))