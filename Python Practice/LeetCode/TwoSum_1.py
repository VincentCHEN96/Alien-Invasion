class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        i = 0

        while i < len(nums):
            search = target - nums[i]   #待查找数（第二个加法因子）
            # 去重（避免重复利用数组中的相同元素）
            if search in nums[:i]:
                index = []
                index.append(i)
                index.append(nums[:i].index(search))
                return index
            elif search in nums[i+1:]:
                index = []
                index.append(i)
                index.append(nums[i+1:].index(search) + len(nums[:i]) + 1)  #后半部分计算下标要加上前半部分和去重元素
                return index
            i += 1

        return []   #找不到则返回空列表