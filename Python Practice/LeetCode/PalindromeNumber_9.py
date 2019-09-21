class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        for i in range(0, int(len(number) / 2 + 1)):
            if number[i] != number[-(i+1)]:
                return False

        return True