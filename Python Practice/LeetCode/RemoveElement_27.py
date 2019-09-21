class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i < len(nums):
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
            if j < i:
                break

        return j + 1