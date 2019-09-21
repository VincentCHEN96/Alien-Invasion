class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = 46341    #int最大值的平方根
        while low <= high:
            middle = int((low + high) / 2)
            if middle ** 2 < x:
                low = middle + 1
            elif middle ** 2 > x:
                high = middle - 1
            else:
                return middle
        return low - 1